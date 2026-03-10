from typing import Any, Optional, Union


class QuotedKeyConfig:
    def __init__(self, id: str) -> None:
        self.id = id

    def to_dict(self) -> dict[str, Any]:
        return {'id': self.id}


class QuotedContentConfig:
    def __init__(self, conversation: str) -> None:
        self.conversation = conversation

    def to_dict(self) -> dict[str, Any]:
        return {'conversation': self.conversation}


class QuotedMessageConfig:
    def __init__(
        self,
        key: Union[dict[str, Any], QuotedKeyConfig],
        message: Union[dict[str, Any], QuotedContentConfig],
    ) -> None:
        self.key = key
        self.message = message

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {'key': self.key, 'message': self.message}

        if hasattr(payload['key'], 'to_dict'):
            payload['key'] = payload['key'].to_dict()

        if hasattr(payload['message'], 'to_dict'):
            payload['message'] = payload['message'].to_dict()

        return payload


class SendTextMessageConfig:
    def __init__(
        self,
        number: str,
        text: str,
        delay: Optional[int] = None,
        quoted: Optional[Union[dict[str, Any], QuotedMessageConfig]] = None,
        linkPreview: Optional[bool] = None,
        mentionsEveryOne: Optional[bool] = None,
        mentioned: Optional[list[str]] = None,
    ) -> None:
        self.__dict__['number'] = number
        self.__dict__['text'] = text

        for key, value in locals().items():
            if key in ('self', 'number', 'text'):
                continue
            if value is not None:
                self.__dict__[key] = value

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = dict(self.__dict__)

        if 'quoted' in payload and payload['quoted'] is not None:
            quoted = payload['quoted']
            if hasattr(quoted, 'to_dict'):
                payload['quoted'] = quoted.to_dict()

        return payload


class SendMediaUrlMessageConfig:
    def __init__(
        self,
        number: str,
        mediatype: str,
        media: str,
        mimetype: Optional[str] = None,
        caption: Optional[str] = None,
        fileName: Optional[str] = None,
    ) -> None:
        self.__dict__['number'] = number
        self.__dict__['mediatype'] = mediatype
        self.__dict__['media'] = media

        for key, value in locals().items():
            if key in ('self', 'number', 'mediatype', 'media'):
                continue
            if value is not None:
                self.__dict__[key] = value

    def to_dict(self) -> dict[str, Any]:
        return dict(self.__dict__)


class SendPtvMessageConfig:
    def __init__(
        self,
        number: str,
        video: str,
        delay: Optional[int] = None,
        quoted: Optional[Union[dict[str, Any], QuotedMessageConfig]] = None,
        mentionsEveryOne: Optional[bool] = None,
        mentioned: Optional[list[str]] = None,
    ) -> None:
        self.__dict__['number'] = number
        self.__dict__['video'] = video

        for key, value in locals().items():
            if key in ('self', 'number', 'video'):
                continue
            if value is not None:
                self.__dict__[key] = value

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = dict(self.__dict__)

        if 'quoted' in payload and payload['quoted'] is not None:
            quoted = payload['quoted']
            if hasattr(quoted, 'to_dict'):
                payload['quoted'] = quoted.to_dict()

        return payload


class SendNarratedAudioMessageConfig:
    def __init__(
        self,
        number: str,
        audio: str,
        delay: Optional[int] = None,
        quoted: Optional[Union[dict[str, Any], QuotedMessageConfig]] = None,
        mentionsEveryOne: Optional[bool] = None,
        mentioned: Optional[list[str]] = None,
        encoding: Optional[bool] = None,
    ) -> None:
        self.__dict__['number'] = number
        self.__dict__['audio'] = audio

        for key, value in locals().items():
            if key in ('self', 'number', 'audio'):
                continue
            if value is not None:
                self.__dict__[key] = value

    def to_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = dict(self.__dict__)

        if 'quoted' in payload and payload['quoted'] is not None:
            quoted = payload['quoted']
            if hasattr(quoted, 'to_dict'):
                payload['quoted'] = quoted.to_dict()

        return payload
