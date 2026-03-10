import json
import threading
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any

import pytest


@dataclass
class EvolutionAPIMockServer:
    base_url: str
    created_instances: dict[str, dict[str, Any]] = field(default_factory=dict)
    deleted_instances: list[str] = field(default_factory=list)


@pytest.fixture
def evolution_api_mock_server() -> EvolutionAPIMockServer:
    state = EvolutionAPIMockServer(base_url='')

    class Handler(BaseHTTPRequestHandler):
        def _write_json(self, status_code: int, payload: dict[str, Any]) -> None:
            body = json.dumps(payload).encode('utf-8')
            self.send_response(status_code)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _read_json_body(self) -> dict[str, Any]:
            content_length = int(self.headers.get('Content-Length', '0'))
            if content_length == 0:
                return {}

            raw_body = self.rfile.read(content_length)
            if not raw_body:
                return {}

            return json.loads(raw_body.decode('utf-8'))

        def do_POST(self) -> None:  # noqa: N802
            if self.path != '/instance/create':
                self._write_json(404, {'error': 'not found'})
                return

            payload = self._read_json_body()
            instance_name = payload.get('instanceName')

            if not instance_name:
                self._write_json(400, {'error': 'instanceName is required'})
                return

            state.created_instances[instance_name] = payload
            self._write_json(
                200,
                {
                    'instance': payload,
                    'hash': f'mock-hash-{instance_name}',
                    'qrcode': 'mock-qrcode',
                },
            )

        def do_DELETE(self) -> None:  # noqa: N802
            prefix = '/instance/delete/'
            if not self.path.startswith(prefix):
                self._write_json(404, {'error': 'not found'})
                return

            instance_name = self.path[len(prefix) :]
            state.deleted_instances.append(instance_name)
            state.created_instances.pop(instance_name, None)

            self._write_json(
                200,
                {
                    'status': 'deleted',
                    'instanceName': instance_name,
                },
            )

        def log_message(self, format: str, *args: Any) -> None:
            return

    server = HTTPServer(('127.0.0.1', 0), Handler)
    host, port = server.server_address
    state.base_url = f'http://{host}:{port}'

    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        yield state
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
