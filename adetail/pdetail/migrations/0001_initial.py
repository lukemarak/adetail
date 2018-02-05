# Generated by Django 2.0 on 2018-02-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processor', models.CharField(blank=True, help_text='e.g.i3-3220@3.2', max_length=20)),
                ('ram', models.CharField(blank=True, help_text='e.g.4GBDDR3x1', max_length=50)),
                ('hdd', models.CharField(blank=True, help_text='e.g. 1TBx1, 1TBx2', max_length=100)),
                ('smps', models.CharField(blank=True, help_text='e.g.FSP400W', max_length=50)),
                ('graphics', models.CharField(blank=True, help_text='e.g.2GBDDR3Graphic', max_length=50)),
                ('soundcard', models.CharField(blank=True, help_text='1xSoundCard', max_length=50)),
                ('rs232', models.CharField(blank=True, help_text='e.g.2xRS232', max_length=10)),
                ('parallel', models.CharField(blank=True, help_text='1xPP', max_length=10)),
                ('lan', models.CharField(blank=True, help_text='e.g.1xDualPort', max_length=50)),
                ('hddbay', models.CharField(blank=True, help_text='1xRemovalHddBay', max_length=50)),
                ('wipicard', models.CharField(blank=True, help_text='1xWipiCard', max_length=20)),
                ('systemos', models.CharField(blank=True, help_text='Win-7pro.x32_64', max_length=50)),
                ('others', models.CharField(blank=True, help_text='extra', max_length=100)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['processor', 'ram', 'hdd', 'smps', 'graphics', 'soundcard', 'rs232', 'parallel', 'lan', 'hddbay', 'wipicard', 'systemos', 'others'],
                'verbose_name_plural': 'configurations',
                'verbose_name': 'configuration',
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=50)),
                ('chasis', models.CharField(choices=[('510', 'IPC-510'), ('610', 'IPC-610'), ('A4000', 'ACP-4000'), ('A4320', 'ACP-4320'), ('A2010', 'ACP-2010'), ('A4340', 'ACP-4340'), ('A4360', 'ACP-4360')], max_length=50)),
                ('chasis_serial', models.CharField(max_length=50)),
                ('motherboard', models.CharField(choices=[('I701', 'AIMB-701'), ('I767', 'AIMB-767'), ('I769', 'AIMB-769'), ('I780', 'AIMB-780'), ('I781', 'AIMB-781'), ('I782', 'AIMB-782'), ('I785', 'AIMB-785'), ('I784', 'AIMB-784'), ('S584', 'ASMB-584'), ('S784', 'ASMB-784'), ('S785', 'ASMB-785'), ('S781', 'ASMB-781'), ('S782', 'ASMB-782')], max_length=50)),
                ('board_serial', models.CharField(max_length=50)),
                ('smps', models.CharField(blank=True, max_length=50)),
                ('ram', models.CharField(blank=True, max_length=20)),
                ('hdd', models.CharField(blank=True, max_length=20)),
                ('productkey', models.CharField(blank=True, max_length=100)),
                ('others', models.TextField(blank=True)),
                ('assembled_by', models.CharField(blank=True, max_length=50)),
                ('assembled_on', models.DateTimeField(auto_now_add=True)),
                ('configuration', models.ForeignKey(on_delete='models.cascade', related_name='detail', to='pdetail.Configuration')),
            ],
            options={
                'ordering': ('assembled_on',),
            },
        ),
    ]
