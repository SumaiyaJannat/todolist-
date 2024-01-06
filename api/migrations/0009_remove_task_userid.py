
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0008_task_userid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="userId",
        ),
    ]
