from enum import Enum

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
            syncFullHistory: bool = None
    ):
        self.__dict__['instanceName'] = instanceName

        for key, value in locals().items():
            if key != 'self' and key != 'instanceName' and value is not None:
                self.__dict__[key] = value


class PresenceStatus(Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"

class PresenceConfig:
    def __init__(self, presence: PresenceStatus):
        self.presence = presence.value