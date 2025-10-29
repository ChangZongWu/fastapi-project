from app import schemas
from jose import jwt
from app.config import settings
import pytest
# def test_root(client):
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json().get("message") == "Hello World from FastAPI!"

def test_create_user(client):
    res = client.post("/users/", json={"email": "hello@gmail.com", "password": "password123"})
    user = schemas.UserOut(**res.json())
    assert res.status_code == 201
    assert user.email == "hello@gmail.com"

def test_login_user(test_user,client):
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id: str = payload.get("user_id")
    assert id == test_user['id']
    assert res.status_code == 200
    assert login_res.token_type == "bearer"

@pytest.mark.parametrize("email, password, status_code", [
    ("hello@email.com", "wrongpassword", 403),
    ("wrong@email.com", "password123", 403),
    ("wrong@email.com", "wrongpassword", 403),
    (None, "password123", 403),
    ("hello@email.com", None, 403)
])
def test_incorrect_login(email, password, status_code, client):
    res = client.post("/login", data={"username": email, "password": password})
    assert res.status_code == status_code

