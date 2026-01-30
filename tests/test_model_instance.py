import pytest


from evolution_api_sdk.models import InstanceConfig, WebhookConfig, PresenceConfig, PresenceStatus


def test_instance_config_includes_only_instanceName_when_all_optional_none():
    cfg = InstanceConfig(instanceName="inst1")
    assert cfg.to_dict() == {"instanceName": "inst1"}


def test_instance_config_includes_only_non_none_fields():
    cfg = InstanceConfig(
        instanceName="inst1",
        integration="WHATSAPP-BAILEYS",
        qrcode=True,
        rejectCall=False,
        msgCall="nao ligo",
        token=None,
    )

    payload = cfg.to_dict()

    assert payload["instanceName"] == "inst1"
    assert payload["integration"] == "WHATSAPP-BAILEYS"
    assert payload["qrcode"] is True
    assert payload["rejectCall"] is False
    assert payload["msgCall"] == "nao ligo"
    assert "token" not in payload


def test_instance_config_webhook_as_dict_pass_through():
    webhook_dict = {
        "url": "https://example.com/hook",
        "byEvents": False,
        "base64": True,
        "headers": {"Content-Type": "application/json"},
        "events": ["QRCODE_UPDATED"],
    }

    cfg = InstanceConfig(instanceName="inst1", webhook=webhook_dict)

    payload = cfg.to_dict()
    assert payload["instanceName"] == "inst1"
    assert payload["webhook"] == webhook_dict


def test_instance_config_webhook_as_object_is_converted_to_dict():
    webhook = WebhookConfig(
        url="https://example.com/hook",
        byEvents=False,
        base64=True,
        headers={"Content-Type": "application/json"},
        events=["APPLICATION_STARTUP", "QRCODE_UPDATED"],
    )

    cfg = InstanceConfig(instanceName="inst1", webhook=webhook)
    payload = cfg.to_dict()

    assert payload["webhook"] == {
        "url": "https://example.com/hook",
        "byEvents": False,
        "base64": True,
        "headers": {"Content-Type": "application/json"},
        "events": ["APPLICATION_STARTUP", "QRCODE_UPDATED"],
    }


def test_webhook_config_only_includes_url_when_all_optional_none():
    webhook = WebhookConfig(url="https://example.com/hook")
    assert webhook.to_dict() == {"url": "https://example.com/hook"}


def test_webhook_config_omits_events_when_none():
    webhook = WebhookConfig(
        url="https://example.com/hook",
        byEvents=True,
        base64=False,
        headers={"Authorization": "Bearer TOKEN"},
        events=None, 
    )
    d = webhook.to_dict()

    assert d["url"] == "https://example.com/hook"
    assert d["byEvents"] is True
    assert d["base64"] is False
    assert d["headers"] == {"Authorization": "Bearer TOKEN"}
    assert "events" not in d


def test_webhook_config_includes_events_when_empty_list_provided():
    webhook = WebhookConfig(
        url="https://example.com/hook",
        events=[],
    )
    d = webhook.to_dict()
    assert d["url"] == "https://example.com/hook"
    assert d["events"] == []


def test_instance_config_webhook_none_is_omitted():
    cfg = InstanceConfig(instanceName="inst1", webhook=None)
    assert cfg.to_dict() == {"instanceName": "inst1"}


def test_presence_config_uses_enum_value_available():
    presence = PresenceConfig(PresenceStatus.AVAILABLE)
    assert presence.presence == "available"


def test_presence_config_uses_enum_value_unavailable():
    presence = PresenceConfig(PresenceStatus.UNAVAILABLE)
    assert presence.presence == "unavailable"
