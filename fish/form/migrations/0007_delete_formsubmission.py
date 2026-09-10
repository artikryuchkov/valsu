from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [("form", "0006_formsubmission_password")]
    operations = [migrations.DeleteModel(name="FormSubmission")]
