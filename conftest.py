import pytest
from utils.api_client import APIClient
from utils.config import API_BASE_URL, DEFAULT_HEADERS


@pytest.fixture(scope="session")
def api_client():
    """Fixture to initialize API Client"""
    return APIClient(API_BASE_URL)


@pytest.fixture(scope="session")
def default_headers():
    """Fixture for default headers"""
    return DEFAULT_HEADERS
