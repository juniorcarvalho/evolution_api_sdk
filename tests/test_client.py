import pytest
from unittest.mock import patch, Mock
from evolution_api_sdk.client import EvolutionClient
from evolution_api_sdk.exception import EvolutionAuthenticationError, EvolutionNotFoundError, EvolutionAPIError


@pytest.fixture
def client():
    return EvolutionClient(base_url="http://fakeapi.com", api_token="fake_token")


@patch('evolution_api_sdk.client.requests.get')
def test_get_success(mock_get, client):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.ok = True
    mock_response.json.return_value = {'key': 'value'}
    mock_get.return_value = mock_response

    response = client.get('endpoint')

    assert response == {'key': 'value'}
    mock_get.assert_called_once_with(
        'http://fakeapi.com/endpoint',
        headers={'apikey': 'fake_token', 'Content-Type': 'application/json'},
        params=None,
        verify=False
    )


@patch('evolution_api_sdk.client.requests.get')
def test_get_authentication_error(mock_get, client):
    mock_response = Mock()
    mock_response.status_code = 401
    mock_response.ok = False
    mock_get.return_value = mock_response

    with pytest.raises(EvolutionAuthenticationError, match="Falha na autenticação."):
        client.get('endpoint')


@patch('evolution_api_sdk.client.requests.get')
def test_get_not_found_error(mock_get, client):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.ok = False
    mock_get.return_value = mock_response

    with pytest.raises(EvolutionNotFoundError, match="Recurso não encontrado."):
        client.get('endpoint')


@patch('evolution_api_sdk.client.requests.get')
def test_get_api_error(mock_get, client):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.ok = False
    mock_response.text = "Erro Interno do Servidor"
    mock_get.return_value = mock_response
    with pytest.raises(EvolutionAPIError):
        client.get('endpoint')


@patch('evolution_api_sdk.client.requests.get')
def test_get_non_json_response(mock_get, client):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.ok = True
    mock_response.json.side_effect = ValueError()
    mock_response.content = b'Non-JSON content'
    mock_get.return_value = mock_response

    response = client.get('endpoint')

    assert response == b'Non-JSON content'
