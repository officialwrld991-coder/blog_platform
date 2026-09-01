from uuid import uuid4
from app.models.blogger import Blogger

def test_that_i_can_create_a_blogger_account(client):
    response = client.post(
        "/bloggers",
        json={
            "username": "colly",
            "email": "colly@gmail.com",
            "password": "wes123",
        }
    )
    assert response.status_code == 201
    data = response.json()

    assert data["username"] == "colly"
    assert data["email"] == "colly@gmail.com"
def test_that_i_can_find_a_blogger_by_id(client, db_session):
    blogger = Blogger(
        username="colly",
        email="colly@gmail.com",
        password="wes123"
    )

    db_session.add(blogger)
    db_session.commit()
    db_session.refresh(blogger)

    response = client.get(f"/bloggers/{blogger.id}")

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == "colly"
    assert data["email"] == "colly@gmail.com"

def test_that_i_get_404_when_blogger_does_not_exist(client):
    blogger_id = uuid4()

    response = client.get(f"/bloggers/{blogger_id}")

    assert response.status_code == 404

def test_that_i_can_find_a_blogger_by_username(client, db_session):
    blogger = Blogger(
        username="collete",
        email="colly@gmail.com",
        password="wes123"
    )
    db_session.add(blogger)
    db_session.commit()
    db_session.refresh(blogger)
    response = client.get("/bloggers/username/collete")

    assert response.status_code == 200
    assert response.json()["username"] == "collete"
    assert response.json()["email"] == "colly@gmail.com"

def test_that_i_get_404_when_username_does_not_exist(client):
    response = client.get("/bloggers/username/unknown")

    assert response.status_code == 404

def test_that_i_can_find_a_blogger_by_email(client, db_session):
    blogger = Blogger(
        username="collete",
        email="colly@gmail.com",
        password="wes123"
    )

    db_session.add(blogger)
    db_session.commit()
    db_session.refresh(blogger)

    response = client.get("/bloggers/email/colly@gmail.com")

    assert response.status_code == 200
    assert response.json()["username"] == "collete"
    assert response.json()["email"] == "colly@gmail.com"

def test_that_i_get_404_when_email_does_not_exist(client):
    response = client.get("/bloggers/email/unknown@gmail.com")

    assert response.status_code == 404

def test_that_i_can_find_all_bloggers(client, db_session):
    blogger1 = Blogger(
        username="colly",
        email="colly@gmail.com",
        password="wes123"
    )

    blogger2 = Blogger(
        username="john",
        email="john@gmail.com",
        password="abc123"
    )

    db_session.add(blogger1)
    db_session.add(blogger2)
    db_session.commit()

    response = client.get("/bloggers")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2
    assert data[0]["username"] == "colly"
    assert data[1]["username"] == "john"

def test_that_i_get_an_empty_list_when_no_bloggers_exist(client):
    response = client.get("/bloggers")

    assert response.status_code == 200
    assert response.json() == []

def test_that_i_can_update_a_blogger(client, db_session):
    blogger = Blogger(
        username="colly",
        email="colly@gmail.com",
        password="wes123"
    )

    db_session.add(blogger)
    db_session.commit()
    db_session.refresh(blogger)

    response = client.put(
        f"/bloggers/{blogger.id}",
        json={
            "username": "collete",
            "email": "collete@gmail.com",
            "password": "newpassword"
        }
    )
    print(response.json())

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == "collete"
    assert data["email"] == "collete@gmail.com"