import json

from project import db
from project.api.models import User
from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """Tests for the Users Service."""

    def test_users_ping(self):
        """Ensure the /ping route behaves correctly."""
        with self.client:
            response = self.client.get("/users/ping")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn("pong!", data["message"])
            self.assertIn("success", data["status"])

    def test_add_user(self):
        """Ensure a new user can be added to the database."""
        with self.client:
            user = User(username="test", email="test@test.com")
            db.session.add(user)
            db.session.commit()
            response = self.client.get("/users")
            data = json.loads(response.data.decode())["data"]
            self.assertEqual(response.status_code, 200)
            self.assertTrue(data["users"][0]["active"])
            self.assertFalse(data["users"][0]["admin"])
            self.assertEqual(data["users"][0]["email"], "test@test.com")
            self.assertEqual(data["users"][0]["username"], "test")
            self.assertEqual(data["users"][0]["id"], 1)
