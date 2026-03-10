from unittest.mock import Mock

import pytest

from evolution_api_sdk.exception import EvolutionAuthenticationError, EvolutionNotFoundError, EvolutionAPIError
from evolution_api_sdk.service.instance import InstanceService


@pytest.fixture
def mock_client():
    return Mock()


@pytest.fixture
def instance_service(mock_client):
    return InstanceService(client=mock_client)


def test_fetch_instances_success(instance_service, mock_client):
    mock_client.get.return_value = [{'id': 1, 'name': 'Instance 1'}, {'id': 2, 'name': 'Instance 2'}]

    response = instance_service.fetch_instances()

    assert len(response) == 2
    assert response[0]['name'] == 'Instance 1'
    assert response[1]['name'] == 'Instance 2'

    mock_client.get.assert_called_once_with('instance/fetchInstances/', params=None)


def test_fetch_instances_authentication_error(instance_service, mock_client):
    mock_client.get.side_effect = EvolutionAuthenticationError('Falha na autenticação.')

    with pytest.raises(EvolutionAuthenticationError, match='Falha na autenticação.'):
        instance_service.fetch_instances()


def test_fetch_instances_not_found_error(instance_service, mock_client):
    mock_client.get.side_effect = EvolutionNotFoundError('Recurso não encontrado.')

    with pytest.raises(EvolutionNotFoundError, match='Recurso não encontrado.'):
        instance_service.fetch_instances()


def test_fetch_instances_api_error(instance_service, mock_client):
    mock_client.get.side_effect = EvolutionAPIError('Erro na requisição: 500 - Erro Interno do Servidor')

    with pytest.raises(EvolutionAPIError, match='Erro na requisição: 500 - Erro Interno do Servidor'):
        instance_service.fetch_instances()
