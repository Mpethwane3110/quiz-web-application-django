from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_quizmodel_totalques'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quesmodel',
            old_name='question',
            new_name='ques',
        ),
        migrations.DeleteModel(
            name='QuizModel',
        ),
    ]
