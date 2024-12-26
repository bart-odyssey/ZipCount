import pytest
import duckdb

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@pytest.mark.parametrize("postal_code, count", [
    ('4433AH', 16),
    ('4438AK', 20),
    ('3000', 0)
])
def test_count_addresses_paramtric(postal_code, count):
    response = client.get("/addresses/count/"+ postal_code)
    assert response.status_code == 200
    assert response.json() == {'count': count, 'post_code': postal_code}

