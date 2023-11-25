# Generated by Django 4.2.7 on 2023-11-25 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('name_unaccented', models.CharField(editable=False, max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('usuario_added', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='comente_sobres.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('curtidas', models.IntegerField(default=0)),
                ('id_topico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comente_sobres.topico')),
                ('id_usuario_added', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comente_sobres.usuario')),
            ],
        ),
    ]
