# Generated by Django 2.1.2 on 2019-02-27 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organ', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgunit',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='orgunit',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organ.OrgUnit', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='position',
            name='grade',
            field=models.CharField(choices=[('01', '员级'), ('02', '初级'), ('03', '中级'), ('04', '高级'), ('05', '专家')], default='01', max_length=2, verbose_name='position grade'),
        ),
        migrations.AlterField(
            model_name='position',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organ.Organization', verbose_name='organization'),
        ),
        migrations.AlterField(
            model_name='position',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='organ.Position', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='position',
            name='series',
            field=models.CharField(choices=[('A', '管理/行政类'), ('S', '营销/市场类'), ('T', '技术/研发类'), ('P', '生产/操作类')], default='A', max_length=1, verbose_name='position series'),
        ),
        migrations.AlterField(
            model_name='position',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organ.OrgUnit', verbose_name='org unit'),
        ),
    ]
