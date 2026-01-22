import requests
from requests_toolbelt import MultipartEncoder

from evolution_api_sdk.exception import EvolutionAuthenticationError, EvolutionNotFoundError, EvolutionAPIError
from evolution_api_sdk.service.instance import InstanceService


class EvolutionClient:
    error: bool = False

    def __init__(self, base_url: str, api_token: str):
        self.base_url = base_url.rstrip('/')
        self.api_token = api_token
        self.instance = InstanceService(self)

    def _get_headers(self):
        return {
            'apikey': self.api_token,
            'Content-Type': 'application/json'
        }

    def _get_full_url(self, endpoint):
        return f'{self.base_url}/{endpoint}'

    def _handle_response(self, response):
        if response.status_code == 401:
            self.error = True
            raise EvolutionAuthenticationError('Falha na autenticação.')
        elif response.status_code == 404:
            self.error = True
            raise EvolutionNotFoundError('Recurso não encontrado.')
        elif response.status_code == 400 or response.status_code == 403:
            self.error = True
            try:
                error_detail = f' - {response.json()}'
            except:
                error_detail = f' - {response.text}'
            self.error = True
            raise EvolutionAPIError(f'Erro na requisição: {response.status_code}{error_detail}')
        elif response.ok:
            try:
                return response.json()
            except ValueError:
                return response.content
        else:
            try:
                error_detail = f' - {response.json()}'
            except:
                error_detail = f' - {response.text}'
            self.error = True
            raise EvolutionAPIError(f'Erro na requisição: {response.status_code}{error_detail}')

    def get(self, endpoint: str, params = None):
        """Faz uma requisição GET."""
        url = self._get_full_url(endpoint)
        response = requests.get(url, headers=self._get_headers(), params=params, verify=False)
        return self._handle_response(response)

    def delete(self, endpoint: str):
        """faz uma requisição DELETE."""
        url = self._get_full_url(endpoint)
        response = requests.delete(url, headers=self._get_headers())
        return self._handle_response(response)

    def post(self, endpoint: str, data: dict = None, files: dict = None):
        url = f'{self.base_url}/{endpoint}'
        headers = self._get_headers()

        if files:
            # Remove o Content-Type do header quando enviando arquivos
            if 'Content-Type' in headers:
                del headers['Content-Type']

            # Prepara os campos do multipart
            fields = {}

            # Adiciona os campos do data
            for key, value in data.items():
                fields[key] = str(value) if not isinstance(value, (int, float)) else (None, str(value), 'text/plain')

            # Adiciona o arquivo
            file_tuple = files['file']
            fields['file'] = (file_tuple[0], file_tuple[1], file_tuple[2])

            # Cria o multipart encoder
            multipart = MultipartEncoder(fields=fields)
            headers['Content-Type'] = multipart.content_type

            response = requests.post(
                url,
                headers=headers,
                data=multipart
            )
        else:
            response = requests.post(
                url,
                headers=headers,
                json=data
            )

        return response.json()

    def put(self, endpoint, data=None):
        """Faz uma requisição PUT."""
        url = self._get_full_url(endpoint)
        response = requests.put(url, headers=self.headers, json=data)
        return self._handle_response(response)
