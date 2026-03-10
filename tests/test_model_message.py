from evolution_api_sdk.models import (
    QuotedContentConfig,
    QuotedKeyConfig,
    QuotedMessageConfig,
    SendMediaUrlMessageConfig,
    SendNarratedAudioMessageConfig,
    SendPtvMessageConfig,
    SendTextMessageConfig,
)


def test_send_text_config_includes_required_fields():
    config = SendTextMessageConfig(number='5511999999999@s.whatsapp.net', text='teste de envio')

    assert config.to_dict() == {
        'number': '5511999999999@s.whatsapp.net',
        'text': 'teste de envio',
    }


def test_send_text_config_omits_optional_none_fields():
    config = SendTextMessageConfig(number='5511999999999@s.whatsapp.net', text='teste de envio')

    payload = config.to_dict()

    assert payload['number'] == '5511999999999@s.whatsapp.net'
    assert payload['text'] == 'teste de envio'
    assert 'delay' not in payload
    assert 'quoted' not in payload
    assert 'linkPreview' not in payload
    assert 'mentionsEveryOne' not in payload
    assert 'mentioned' not in payload


def test_send_text_config_keeps_false_boolean_fields():
    config = SendTextMessageConfig(
        number='5511999999999@s.whatsapp.net',
        text='teste de envio',
        linkPreview=False,
        mentionsEveryOne=False,
    )

    payload = config.to_dict()

    assert payload['linkPreview'] is False
    assert payload['mentionsEveryOne'] is False


def test_send_text_config_with_mentioned_list():
    config = SendTextMessageConfig(
        number='5511999999999@s.whatsapp.net',
        text='teste de envio',
        mentioned=['5511999999999@s.whatsapp.net'],
    )

    assert config.to_dict()['mentioned'] == ['5511999999999@s.whatsapp.net']


def test_send_text_config_with_quoted_object():
    quoted = QuotedMessageConfig(
        key=QuotedKeyConfig(id='MESSAGE_ID'),
        message=QuotedContentConfig(conversation='CONTENT_MESSAGE'),
    )
    config = SendTextMessageConfig(number='5511999999999@s.whatsapp.net', text='teste de envio', quoted=quoted)

    assert config.to_dict()['quoted'] == {
        'key': {'id': 'MESSAGE_ID'},
        'message': {'conversation': 'CONTENT_MESSAGE'},
    }


def test_send_text_config_with_quoted_dict_pass_through():
    quoted = {
        'key': {'id': 'MESSAGE_ID'},
        'message': {'conversation': 'CONTENT_MESSAGE'},
    }
    config = SendTextMessageConfig(number='5511999999999@s.whatsapp.net', text='teste de envio', quoted=quoted)

    assert config.to_dict()['quoted'] == quoted


def test_send_media_url_config_includes_required_fields():
    config = SendMediaUrlMessageConfig(
        number='5511999999999',
        mediatype='image',
        media='https://s3.amazonaws.com/bucket/image.png',
    )

    assert config.to_dict() == {
        'number': '5511999999999',
        'mediatype': 'image',
        'media': 'https://s3.amazonaws.com/bucket/image.png',
    }


def test_send_media_url_config_omits_optional_none_fields():
    config = SendMediaUrlMessageConfig(
        number='5511999999999',
        mediatype='image',
        media='https://s3.amazonaws.com/bucket/image.png',
    )

    payload = config.to_dict()

    assert payload['number'] == '5511999999999'
    assert payload['mediatype'] == 'image'
    assert payload['media'] == 'https://s3.amazonaws.com/bucket/image.png'
    assert 'mimetype' not in payload
    assert 'caption' not in payload
    assert 'fileName' not in payload


def test_send_media_url_config_includes_optional_fields():
    config = SendMediaUrlMessageConfig(
        number='5511999999999',
        mediatype='image',
        media='https://s3.amazonaws.com/bucket/image.png',
        mimetype='image/png',
        caption='Teste de caption',
        fileName='Imagem.png',
    )

    assert config.to_dict() == {
        'number': '5511999999999',
        'mediatype': 'image',
        'media': 'https://s3.amazonaws.com/bucket/image.png',
        'mimetype': 'image/png',
        'caption': 'Teste de caption',
        'fileName': 'Imagem.png',
    }


def test_send_ptv_config_includes_required_fields():
    config = SendPtvMessageConfig(number='5511999999999', video='https://evolution-api.com/files/video.mp4')

    assert config.to_dict() == {
        'number': '5511999999999',
        'video': 'https://evolution-api.com/files/video.mp4',
    }


def test_send_ptv_config_omits_optional_none_fields():
    config = SendPtvMessageConfig(number='5511999999999', video='https://evolution-api.com/files/video.mp4')

    payload = config.to_dict()

    assert payload['number'] == '5511999999999'
    assert payload['video'] == 'https://evolution-api.com/files/video.mp4'
    assert 'delay' not in payload
    assert 'quoted' not in payload
    assert 'mentionsEveryOne' not in payload
    assert 'mentioned' not in payload


def test_send_ptv_config_keeps_false_boolean_fields():
    config = SendPtvMessageConfig(
        number='5511999999999',
        video='https://evolution-api.com/files/video.mp4',
        mentionsEveryOne=False,
    )

    payload = config.to_dict()

    assert payload['mentionsEveryOne'] is False


def test_send_ptv_config_with_mentioned_list():
    config = SendPtvMessageConfig(
        number='5511999999999',
        video='https://evolution-api.com/files/video.mp4',
        mentioned=['5511999999999'],
    )

    assert config.to_dict()['mentioned'] == ['5511999999999']


def test_send_ptv_config_with_quoted_object():
    quoted = QuotedMessageConfig(
        key=QuotedKeyConfig(id='MESSAGE_ID'),
        message=QuotedContentConfig(conversation='CONTENT_MESSAGE'),
    )
    config = SendPtvMessageConfig(
        number='5511999999999', video='https://evolution-api.com/files/video.mp4', quoted=quoted
    )

    assert config.to_dict()['quoted'] == {
        'key': {'id': 'MESSAGE_ID'},
        'message': {'conversation': 'CONTENT_MESSAGE'},
    }


def test_send_ptv_config_with_quoted_dict_pass_through():
    quoted = {
        'key': {'id': 'MESSAGE_ID'},
        'message': {'conversation': 'CONTENT_MESSAGE'},
    }
    config = SendPtvMessageConfig(
        number='5511999999999', video='https://evolution-api.com/files/video.mp4', quoted=quoted
    )

    assert config.to_dict()['quoted'] == quoted


def test_send_narrated_audio_config_includes_required_fields():
    config = SendNarratedAudioMessageConfig(
        number='5511999999999',
        audio='https://evolution-api.com/files/narratedaudio.mp3',
    )

    assert config.to_dict() == {
        'number': '5511999999999',
        'audio': 'https://evolution-api.com/files/narratedaudio.mp3',
    }


def test_send_narrated_audio_config_omits_optional_none_fields():
    config = SendNarratedAudioMessageConfig(
        number='5511999999999',
        audio='https://evolution-api.com/files/narratedaudio.mp3',
    )

    payload = config.to_dict()

    assert payload['number'] == '5511999999999'
    assert payload['audio'] == 'https://evolution-api.com/files/narratedaudio.mp3'
    assert 'delay' not in payload
    assert 'quoted' not in payload
    assert 'mentionsEveryOne' not in payload
    assert 'mentioned' not in payload
    assert 'encoding' not in payload


def test_send_narrated_audio_config_keeps_false_boolean_fields():
    config = SendNarratedAudioMessageConfig(
        number='5511999999999',
        audio='https://evolution-api.com/files/narratedaudio.mp3',
        mentionsEveryOne=False,
        encoding=False,
    )

    payload = config.to_dict()

    assert payload['mentionsEveryOne'] is False
    assert payload['encoding'] is False


def test_send_narrated_audio_config_with_mentioned_list():
    config = SendNarratedAudioMessageConfig(
        number='5511999999999',
        audio='https://evolution-api.com/files/narratedaudio.mp3',
        mentioned=['5511999999999'],
    )

    assert config.to_dict()['mentioned'] == ['5511999999999']


def test_send_narrated_audio_config_with_quoted_object():
    quoted = QuotedMessageConfig(
        key=QuotedKeyConfig(id='MESSAGE_ID'),
        message=QuotedContentConfig(conversation='CONTENT_MESSAGE'),
    )
    config = SendNarratedAudioMessageConfig(
        number='5511999999999',
        audio='https://evolution-api.com/files/narratedaudio.mp3',
        quoted=quoted,
    )

    assert config.to_dict()['quoted'] == {
        'key': {'id': 'MESSAGE_ID'},
        'message': {'conversation': 'CONTENT_MESSAGE'},
    }


def test_send_narrated_audio_config_with_quoted_dict_pass_through():
    quoted = {
        'key': {'id': 'MESSAGE_ID'},
        'message': {'conversation': 'CONTENT_MESSAGE'},
    }
    config = SendNarratedAudioMessageConfig(
        number='5511999999999',
        audio='https://evolution-api.com/files/narratedaudio.mp3',
        quoted=quoted,
    )

    assert config.to_dict()['quoted'] == quoted
