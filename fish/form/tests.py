from django.test import SimpleTestCase
from django.contrib.staticfiles import finders

class DemoTests(SimpleTestCase):
    def test_public_page_has_no_login_or_trackers(self):
        response = self.client.get("/")
        self.assertContains(response, "Демонстрация")
        html = response.content.decode()
        for forbidden in ("<form", 'type="password"', "ВолГУ", "mc.yandex.ru", "mail.ru"):
            self.assertNotIn(forbidden, html)

    def test_post_is_rejected_without_database_access(self):
        self.assertEqual(self.client.post("/", {"username": "test", "password": "test"}).status_code, 405)

    def test_old_admin_is_unavailable(self):
        self.assertEqual(self.client.get("/admin/").status_code, 404)

    def test_only_new_assets_are_published(self):
        self.assertTrue(finders.find("demo.css"))
        self.assertIsNone(finders.find("users.csv"))
