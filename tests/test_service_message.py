from unittest.mock import Mock

import pytest

from evolution_api_sdk.exception import EvolutionAPIError, EvolutionAuthenticationError, EvolutionNotFoundError
from evolution_api_sdk.models import (
    SendMediaUrlMessageConfig,
    SendNarratedAudioMessageConfig,
    SendPtvMessageConfig,
    SendTextMessageConfig,
)
from evolution_api_sdk.service.message import MessageService


@pytest.fixture
def mock_client():
    return Mock()


@pytest.fixture
def message_service(mock_client):
    return MessageService(client=mock_client)


def test_send_text_success_with_model_payload(message_service, mock_client):
    mock_client.post.return_value = {'status': 'success'}
    payload = SendTextMessageConfig(number='5511999999999@s.whatsapp.net', text='teste de envio')

    response = message_service.send_text('inst1', payload)

    assert response == {'status': 'success'}
    mock_client.post.assert_called_once_with(
        'message/sendText/inst1',
        data={'number': '5511999999999@s.whatsapp.net', 'text': 'teste de envio'},
    )


def test_send_text_success_with_dict_payload(message_service, mock_client):
    mock_client.post.return_value = {'status': 'success'}
    payload = {'number': '5511999999999@s.whatsapp.net', 'text': 'teste de envio'}

    response = message_service.send_text('inst1', payload)

    assert response == {'status': 'success'}
    mock_client.post.assert_called_once_with('message/sendText/inst1', data=payload)


def test_send_text_propagates_authentication_error(message_service, mock_client):
    mock_client.post.side_effect = EvolutionAuthenticationError('Falha na autenticação.')

    with pytest.raises(EvolutionAuthenticationError, match='Falha na autenticação.'):
        message_service.send_text('inst1', {'number': '5511999999999@s.whatsapp.net', 'text': 'teste de envio'})


def test_send_text_propagates_not_found_error(message_service, mock_client):
    mock_client.post.side_effect = EvolutionNotFoundError('Recurso não encontrado.')

    with pytest.raises(EvolutionNotFoundError, match='Recurso não encontrado.'):
        message_service.send_text('inst1', {'number': '5511999999999@s.whatsapp.net', 'text': 'teste de envio'})


def test_send_text_propagates_api_error(message_service, mock_client):
    mock_client.post.side_effect = EvolutionAPIError('Erro na requisição: 500 - Erro Interno do Servidor')

    with pytest.raises(EvolutionAPIError, match='Erro na requisição: 500 - Erro Interno do Servidor'):
        message_service.send_text('inst1', {'number': '5511999999999@s.whatsapp.net', 'text': 'teste de envio'})


def test_send_media_url_success_with_model_payload(message_service, mock_client):
    mock_client.post.return_value = {'status': 'success'}
    payload = SendMediaUrlMessageConfig(
        number='5511999999999',
        mediatype='image',
        media='https://s3.amazonaws.com/bucket/image.png',
        mimetype='image/png',
        caption='Teste de caption',
        fileName='Imagem.png',
    )

    response = message_service.send_media_url('inst1', payload)

    assert response == {'status': 'success'}
    mock_client.post.assert_called_once_with(
        'message/sendMedia/inst1',
        data={
            'number': '5511999999999',
            'mediatype': 'image',
            'media': 'https://s3.amazonaws.com/bucket/image.png',
            'mimetype': 'image/png',
            'caption': 'Teste de caption',
            'fileName': 'Imagem.png',
        },
    )


def test_send_media_url_success_with_dict_payload(message_service, mock_client):
    mock_client.post.return_value = {'status': 'success'}
    payload = {
        'number': '5511999999999',
        'mediatype': 'image',
        'media': 'https://s3.amazonaws.com/bucket/image.png',
    }

    response = message_service.send_media_url('inst1', payload)

    assert response == {'status': 'success'}
    mock_client.post.assert_called_once_with('message/sendMedia/inst1', data=payload)


def test_send_media_url_propagates_authentication_error(message_service, mock_client):
    mock_client.post.side_effect = EvolutionAuthenticationError('Falha na autenticação.')

    with pytest.raises(EvolutionAuthenticationError, match='Falha na autenticação.'):
        message_service.send_media_url(
            'inst1',
            {'number': '5511999999999', 'mediatype': 'image', 'media': 'https://s3.amazonaws.com/bucket/image.png'},
        )


def test_send_media_url_propagates_not_found_error(message_service, mock_client):
    mock_client.post.side_effect = EvolutionNotFoundError('Recurso não encontrado.')

    with pytest.raises(EvolutionNotFoundError, match='Recurso não encontrado.'):
        message_service.send_media_url(
            'inst1',
            {'number': '5511999999999', 'mediatype': 'image', 'media': 'https://s3.amazonaws.com/bucket/image.png'},
        )


def test_send_media_url_propagates_api_error(message_service, mock_client):
    mock_client.post.side_effect = EvolutionAPIError('Erro na requisição: 500 - Erro Interno do Servidor')

    with pytest.raises(EvolutionAPIError, match='Erro na requisição: 500 - Erro Interno do Servidor'):
        message_service.send_media_url(
            'inst1',
            {'number': '5511999999999', 'mediatype': 'image', 'media': 'https://s3.amazonaws.com/bucket/image.png'},
        )


def test_send_ptv_success_with_model_payload(message_service, mock_client):
    mock_client.post.return_value = {'status': 'success'}
    payload = SendPtvMessageConfig(
        number='5511999999999',
        video='https://evolution-api.com/files/video.mp4',
        delay=1200,
        mentionsEveryOne=False,
        mentioned=['5511999999999'],
    )

    response = message_service.send_ptv('inst1', payload)

    assert response == {'status': 'success'}
    mock_client.post.assert_called_once_with(
        'message/sendPtv/inst1',
        data={
            'number': '5511999999999',
            'video': 'https://evolution-api.com/files/video.mp4',
            'delay': 1200,
            'mentionsEveryOne': False,
            'mentioned': ['5511999999999'],
        },
    )


def test_send_ptv_success_with_dict_payload(message_service, mock_client):
    mock_client.post.return_value = {'status': 'success'}
    payload = {
        'number': '5511999999999',
        'video': 'https://evolution-api.com/files/video.mp4',
    }

    response = message_service.send_ptv('inst1', payload)

    assert response == {'status': 'success'}
    mock_client.post.assert_called_once_with('message/sendPtv/inst1', data=payload)


def test_send_ptv_propagates_authentication_error(message_service, mock_client):
    mock_client.post.side_effect = EvolutionAuthenticationError('Falha na autenticação.')

    with pytest.raises(EvolutionAuthenticationError, match='Falha na autenticação.'):
        message_service.send_ptv(
            'inst1', {'number': '5511999999999', 'video': 'https://evolution-api.com/files/video.mp4'}
        )


def test_send_ptv_propagates_not_found_error(message_service, mock_client):
    mock_client.post.side_effect = EvolutionNotFoundError('Recurso não encontrado.')

    with pytest.raises(EvolutionNotFoundError, match='Recurso não encontrado.'):
        message_service.send_ptv(
            'inst1', {'number': '5511999999999', 'video': 'https://evolution-api.com/files/video.mp4'}
        )


def test_send_ptv_propagates_api_error(message_service, mock_client):
    mock_client.post.side_effect = EvolutionAPIError('Erro na requisição: 500 - Erro Interno do Servidor')

    with pytest.raises(EvolutionAPIError, match='Erro na requisição: 500 - Erro Interno do Servidor'):
        message_service.send_ptv(
            'inst1', {'number': '5511999999999', 'video': 'https://evolution-api.com/files/video.mp4'}
        )


def test_send_narrated_audio_success_with_model_payload(message_service, mock_client):
    mock_client.post.return_value = {'status': 'success'}
    payload = SendNarratedAudioMessageConfig(
        number='5511999999999',
        audio='https://evolution-api.com/files/narratedaudio.mp3',
        delay=1200,
        mentionsEveryOne=False,
        mentioned=['5511999999999'],
        encoding=True,
    )

    response = message_service.send_narrated_audio('inst1', payload)

    assert response == {'status': 'success'}
    mock_client.post.assert_called_once_with(
        'message/sendWhatsAppAudio/inst1',
        data={
            'number': '5511999999999',
            'audio': 'https://evolution-api.com/files/narratedaudio.mp3',
            'delay': 1200,
            'mentionsEveryOne': False,
            'mentioned': ['5511999999999'],
            'encoding': True,
        },
    )


def test_send_narrated_audio_success_with_dict_payload(message_service, mock_client):
    mock_client.post.return_value = {'status': 'success'}
    payload = {
        'number': '5511999999999',
        'audio': 'https://evolution-api.com/files/narratedaudio.mp3',
    }

    response = message_service.send_narrated_audio('inst1', payload)

    assert response == {'status': 'success'}
    mock_client.post.assert_called_once_with('message/sendWhatsAppAudio/inst1', data=payload)


def test_send_narrated_audio_propagates_authentication_error(message_service, mock_client):
    mock_client.post.side_effect = EvolutionAuthenticationError('Falha na autenticação.')

    with pytest.raises(EvolutionAuthenticationError, match='Falha na autenticação.'):
        message_service.send_narrated_audio(
            'inst1', {'number': '5511999999999', 'audio': 'https://evolution-api.com/files/narratedaudio.mp3'}
        )


def test_send_narrated_audio_propagates_not_found_error(message_service, mock_client):
    mock_client.post.side_effect = EvolutionNotFoundError('Recurso não encontrado.')

    with pytest.raises(EvolutionNotFoundError, match='Recurso não encontrado.'):
        message_service.send_narrated_audio(
            'inst1', {'number': '5511999999999', 'audio': 'https://evolution-api.com/files/narratedaudio.mp3'}
        )


def test_send_narrated_audio_propagates_api_error(message_service, mock_client):
    mock_client.post.side_effect = EvolutionAPIError('Erro na requisição: 500 - Erro Interno do Servidor')

    with pytest.raises(EvolutionAPIError, match='Erro na requisição: 500 - Erro Interno do Servidor'):
        message_service.send_narrated_audio(
            'inst1', {'number': '5511999999999', 'audio': 'https://evolution-api.com/files/narratedaudio.mp3'}
        )
