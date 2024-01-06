

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230913_0417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
