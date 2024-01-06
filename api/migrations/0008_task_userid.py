

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='userId',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
