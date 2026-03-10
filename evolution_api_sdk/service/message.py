from typing import Any, Union

from evolution_api_sdk.models.message import (
    SendMediaUrlMessageConfig,
    SendNarratedAudioMessageConfig,
    SendPtvMessageConfig,
    SendTextMessageConfig,
)


class MessageService:
    def __init__(self, client) -> None:
        self.client = client

    def send_text(self, instance_name: str, payload: Union[SendTextMessageConfig, dict[str, Any]]) -> Any:
        if isinstance(payload, SendTextMessageConfig):
            data = payload.to_dict()
        else:
            data = payload

        return self.client.post(f'message/sendText/{instance_name}', data=data)

    def send_media_url(self, instance_name: str, payload: Union[SendMediaUrlMessageConfig, dict[str, Any]]) -> Any:
        if isinstance(payload, SendMediaUrlMessageConfig):
            data = payload.to_dict()
        else:
            data = payload

        return self.client.post(f'message/sendMedia/{instance_name}', data=data)

    def send_ptv(self, instance_name: str, payload: Union[SendPtvMessageConfig, dict[str, Any]]) -> Any:
        if isinstance(payload, SendPtvMessageConfig):
            data = payload.to_dict()
        else:
            data = payload

        return self.client.post(f'message/sendPtv/{instance_name}', data=data)

    def send_narrated_audio(
        self, instance_name: str, payload: Union[SendNarratedAudioMessageConfig, dict[str, Any]]
    ) -> Any:
        if isinstance(payload, SendNarratedAudioMessageConfig):
            data = payload.to_dict()
        else:
            data = payload

        return self.client.post(f'message/sendWhatsAppAudio/{instance_name}', data=data)
