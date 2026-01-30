from enum import Enum
from typing import Optional, Dict, Any, Union, List

class InstanceConfig:
    def __init__(
            self,
            instanceName: str,
            integration: str = None,
            businessId: str = None,
            token: str = None,
            number: str = None,
            qrcode: bool = None,
            rejectCall: bool = None,
            msgCall: str = None,
            groupsIgnore: bool = None,
            alwaysOnline: bool = None,
            readMessages: bool = None,
            readStatus: bool = None,
            syncFullHistory: bool = None,
            webhook: Optional[Union[Dict[str, Any], "WebhookConfig"]] = None,
        ):
        self.__dict__['instanceName'] = instanceName

        for key, value in locals().items():
            if key in ("self", "instanceName"):
                continue
            if value is not None:
                self.__dict__[key] = value

    def to_dict(self) -> Dict[str, Any]:
        payload: Dict[str, Any] = dict(self.__dict__)

        if "webhook" in payload and payload["webhook"] is not None:
            wh = payload["webhook"]
            if hasattr(wh, "to_dict"):
                payload["webhook"] = wh.to_dict()

        return payload                


class WebhookConfig:
    def __init__(
        self,
        url: str,
        byEvents: Optional[bool] = None,
        base64: Optional[bool] = None,
        headers: Optional[Dict[str, str]] = None,
        events: Optional[List[str]] = None,
    ):
        self.url = url
        if byEvents is not None:
            self.byEvents = byEvents
        if base64 is not None:
            self.base64 = base64
        if headers is not None:
            self.headers = headers
        if events is not None:
            self.events = events

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {"url": self.url}
        if hasattr(self, "byEvents"):
            d["byEvents"] = self.byEvents
        if hasattr(self, "base64"):
            d["base64"] = self.base64
        if hasattr(self, "headers"):
            d["headers"] = self.headers
        if hasattr(self, "events"):
            d["events"] = self.events
        return d



class PresenceStatus(Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"

class PresenceConfig:
    def __init__(self, presence: PresenceStatus):
        self.presence = presence.value