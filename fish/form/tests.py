from unittest.mock import patch
from django.test import TestCase
from django.utils import timezone
from .models import FormSubmission


class SubmissionTests(TestCase):
    def test_saves_metadata_without_password_or_file_log(self):
        before = timezone.now()
        with patch('logging.FileHandler.emit') as emit:
            response = self.client.post(
                '/', {'username': 'demo-user', 'password': 'private-password'},
                REMOTE_ADDR='192.0.2.1',
                HTTP_REFERER='https://example.org/login?password=private-password',
                HTTP_X_FORWARDED_FOR='198.51.100.1',
            )
        self.assertEqual(response.status_code, 302)
        entry = FormSubmission.objects.get()
        self.assertEqual(entry.username, 'demo-user')
        self.assertEqual(entry.ip_address, '192.0.2.1')
        self.assertEqual(entry.source, 'example.org')
        self.assertGreaterEqual(entry.submitted_at, before)
        self.assertNotIn('password', [f.name for f in entry._meta.fields])
        self.assertNotIn('private-password', str(entry.__dict__))
        emit.assert_not_called()

    def test_missing_or_invalid_metadata(self):
        for source in ('', 'https://[invalid'):
            self.client.post('/', HTTP_REFERER=source, REMOTE_ADDR='invalid')
        self.assertEqual(FormSubmission.objects.count(), 2)
        for entry in FormSubmission.objects.all():
            self.assertEqual(entry.source, '')
            self.assertIsNone(entry.ip_address)

    def test_get_does_not_create_submission(self):
        self.assertEqual(self.client.get('/').status_code, 200)
        self.assertFalse(FormSubmission.objects.exists())
