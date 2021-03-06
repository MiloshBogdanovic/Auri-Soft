# Generated by Django 3.2.6 on 2021-12-27 10:10

from django.db import migrations, models
import django.db.models.deletion
import internationalflavor.vat_number.models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataDesignerIndividual',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=120)),
                ('dob', models.DateField()),
                ('birthplace', models.CharField(max_length=30)),
                ('birthplace_county', models.CharField(max_length=30)),
                ('residence_city', models.CharField(max_length=50)),
                ('residence_province', models.CharField(max_length=50)),
                ('residence_cap', models.IntegerField()),
                ('activity_street', models.CharField(max_length=50)),
                ('activity_municipality', models.CharField(max_length=50)),
                ('activity_province', models.CharField(max_length=50)),
                ('activity_cap', models.IntegerField()),
                ('residence_street', models.CharField(max_length=50)),
                ('board_order_registration', models.CharField(max_length=50)),
                ('province_college', models.CharField(max_length=40)),
                ('number_of_reg_order_college', models.IntegerField()),
                ('vat_number', internationalflavor.vat_number.models.VATNumberField(countries=['IT'])),
                ('fiscal_code', models.CharField(max_length=40)),
                ('phone_number', phone_field.models.PhoneField(max_length=31)),
                ('security_case_technician', models.CharField(choices=[('4%', '4%'), ('4%', '5%')], max_length=5)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DataDesignerLegal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('municipal_reg_office', models.CharField(max_length=20)),
                ('province_reg_office', models.CharField(max_length=20)),
                ('cap_reg_office', models.CharField(max_length=20)),
                ('street_reg_office', models.CharField(max_length=100)),
                ('province_of_inscription_enterprises_register', models.CharField(max_length=20)),
                ('number_of_inscription_enterprises_register', models.CharField(max_length=50)),
                ('rep_name', models.CharField(max_length=100)),
                ('rep_dob', models.DateField()),
                ('rep_dob_municipality', models.CharField(max_length=50)),
                ('rep_dob_province', models.CharField(max_length=50)),
                ('rep_residence_municipality', models.CharField(max_length=100)),
                ('rep_residence_province', models.CharField(max_length=100)),
                ('rep_residence_zip', models.CharField(max_length=30)),
                ('rep_street', models.CharField(max_length=100)),
                ('rep_fiscal_code', models.CharField(max_length=50)),
                ('rep_phone_number', models.IntegerField()),
                ('ss_fund', models.IntegerField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DataDirectorWorksIndividual',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=120)),
                ('dob', models.DateField()),
                ('birthplace', models.CharField(max_length=30)),
                ('birthplace_county', models.CharField(max_length=30)),
                ('residence_city', models.CharField(max_length=50)),
                ('residence_province', models.CharField(max_length=50)),
                ('residence_cap', models.IntegerField()),
                ('activity_street', models.CharField(max_length=50)),
                ('activity_municipality', models.CharField(max_length=50)),
                ('activity_province', models.CharField(max_length=50)),
                ('activity_cap', models.IntegerField()),
                ('residence_street', models.CharField(max_length=50)),
                ('board_order_registration', models.CharField(max_length=50)),
                ('province_college', models.CharField(max_length=40)),
                ('number_of_reg_order_college', models.IntegerField()),
                ('vat_number', internationalflavor.vat_number.models.VATNumberField(countries=['IT'])),
                ('fiscal_code', models.CharField(max_length=40)),
                ('phone_number', phone_field.models.PhoneField(max_length=31)),
                ('security_case_technician', models.CharField(choices=[('4%', '4%'), ('4%', '5%')], max_length=5)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DataDirectorWorksLegal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('municipal_reg_office', models.CharField(max_length=20)),
                ('province_reg_office', models.CharField(max_length=20)),
                ('cap_reg_office', models.CharField(max_length=20)),
                ('street_reg_office', models.CharField(max_length=100)),
                ('province_of_inscription_enterprises_register', models.CharField(max_length=20)),
                ('number_of_inscription_enterprises_register', models.CharField(max_length=50)),
                ('rep_name', models.CharField(max_length=100)),
                ('rep_dob', models.DateField()),
                ('rep_dob_municipality', models.CharField(max_length=50)),
                ('rep_dob_province', models.CharField(max_length=50)),
                ('rep_residence_municipality', models.CharField(max_length=100)),
                ('rep_residence_province', models.CharField(max_length=100)),
                ('rep_residence_zip', models.CharField(max_length=30)),
                ('rep_street', models.CharField(max_length=100)),
                ('rep_fiscal_code', models.CharField(max_length=50)),
                ('rep_phone_number', models.IntegerField()),
                ('ss_fund', models.IntegerField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DataEnergyExpertIndividual',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=120)),
                ('dob', models.DateField()),
                ('birthplace', models.CharField(max_length=30)),
                ('birthplace_county', models.CharField(max_length=30)),
                ('residence_city', models.CharField(max_length=50)),
                ('residence_province', models.CharField(max_length=50)),
                ('residence_cap', models.IntegerField()),
                ('activity_street', models.CharField(max_length=50)),
                ('activity_municipality', models.CharField(max_length=50)),
                ('activity_province', models.CharField(max_length=50)),
                ('activity_cap', models.IntegerField()),
                ('residence_street', models.CharField(max_length=50)),
                ('board_order_registration', models.CharField(max_length=50)),
                ('province_college', models.CharField(max_length=40)),
                ('number_of_reg_order_college', models.IntegerField()),
                ('vat_number', internationalflavor.vat_number.models.VATNumberField(countries=['IT'])),
                ('fiscal_code', models.CharField(max_length=40)),
                ('phone_number', phone_field.models.PhoneField(max_length=31)),
                ('security_case_technician', models.CharField(choices=[('4%', '4%'), ('4%', '5%')], max_length=5)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DataEnergyExpertLegal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('municipal_reg_office', models.CharField(max_length=20)),
                ('province_reg_office', models.CharField(max_length=20)),
                ('cap_reg_office', models.CharField(max_length=20)),
                ('street_reg_office', models.CharField(max_length=100)),
                ('province_of_inscription_enterprises_register', models.CharField(max_length=20)),
                ('number_of_inscription_enterprises_register', models.CharField(max_length=50)),
                ('rep_name', models.CharField(max_length=100)),
                ('rep_dob', models.DateField()),
                ('rep_dob_municipality', models.CharField(max_length=50)),
                ('rep_dob_province', models.CharField(max_length=50)),
                ('rep_residence_municipality', models.CharField(max_length=100)),
                ('rep_residence_province', models.CharField(max_length=100)),
                ('rep_residence_zip', models.CharField(max_length=30)),
                ('rep_street', models.CharField(max_length=100)),
                ('rep_fiscal_code', models.CharField(max_length=50)),
                ('rep_phone_number', models.IntegerField()),
                ('ss_fund', models.IntegerField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DataResponsibleForWorksIndividual',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=120)),
                ('dob', models.DateField()),
                ('birthplace', models.CharField(max_length=30)),
                ('birthplace_county', models.CharField(max_length=30)),
                ('residence_city', models.CharField(max_length=50)),
                ('residence_province', models.CharField(max_length=50)),
                ('residence_cap', models.IntegerField()),
                ('activity_street', models.CharField(max_length=50)),
                ('activity_municipality', models.CharField(max_length=50)),
                ('activity_province', models.CharField(max_length=50)),
                ('activity_cap', models.IntegerField()),
                ('residence_street', models.CharField(max_length=50)),
                ('board_order_registration', models.CharField(max_length=50)),
                ('province_college', models.CharField(max_length=40)),
                ('number_of_reg_order_college', models.IntegerField()),
                ('vat_number', internationalflavor.vat_number.models.VATNumberField(countries=['IT'])),
                ('fiscal_code', models.CharField(max_length=40)),
                ('phone_number', phone_field.models.PhoneField(max_length=31)),
                ('security_case_technician', models.CharField(choices=[('4%', '4%'), ('4%', '5%')], max_length=5)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DataResponsibleForWorksLegal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('municipal_reg_office', models.CharField(max_length=20)),
                ('province_reg_office', models.CharField(max_length=20)),
                ('cap_reg_office', models.CharField(max_length=20)),
                ('street_reg_office', models.CharField(max_length=100)),
                ('province_of_inscription_enterprises_register', models.CharField(max_length=20)),
                ('number_of_inscription_enterprises_register', models.CharField(max_length=50)),
                ('rep_name', models.CharField(max_length=100)),
                ('rep_dob', models.DateField()),
                ('rep_dob_municipality', models.CharField(max_length=50)),
                ('rep_dob_province', models.CharField(max_length=50)),
                ('rep_residence_municipality', models.CharField(max_length=100)),
                ('rep_residence_province', models.CharField(max_length=100)),
                ('rep_residence_zip', models.CharField(max_length=30)),
                ('rep_street', models.CharField(max_length=100)),
                ('rep_fiscal_code', models.CharField(max_length=50)),
                ('rep_phone_number', models.IntegerField()),
                ('ss_fund', models.IntegerField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DataSecurityCoordinatorExecutionIndividual',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=120)),
                ('dob', models.DateField()),
                ('birthplace', models.CharField(max_length=30)),
                ('birthplace_county', models.CharField(max_length=30)),
                ('residence_city', models.CharField(max_length=50)),
                ('residence_province', models.CharField(max_length=50)),
                ('residence_cap', models.IntegerField()),
                ('activity_street', models.CharField(max_length=50)),
                ('activity_municipality', models.CharField(max_length=50)),
                ('activity_province', models.CharField(max_length=50)),
                ('activity_cap', models.IntegerField()),
                ('residence_street', models.CharField(max_length=50)),
                ('board_order_registration', models.CharField(max_length=50)),
                ('province_college', models.CharField(max_length=40)),
                ('number_of_reg_order_college', models.IntegerField()),
                ('vat_number', internationalflavor.vat_number.models.VATNumberField(countries=['IT'])),
                ('fiscal_code', models.CharField(max_length=40)),
                ('phone_number', phone_field.models.PhoneField(max_length=31)),
                ('security_case_technician', models.CharField(choices=[('4%', '4%'), ('4%', '5%')], max_length=5)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DataSecurityCoordinatorExecutionLegal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('municipal_reg_office', models.CharField(max_length=20)),
                ('province_reg_office', models.CharField(max_length=20)),
                ('cap_reg_office', models.CharField(max_length=20)),
                ('street_reg_office', models.CharField(max_length=100)),
                ('province_of_inscription_enterprises_register', models.CharField(max_length=20)),
                ('number_of_inscription_enterprises_register', models.CharField(max_length=50)),
                ('rep_name', models.CharField(max_length=100)),
                ('rep_dob', models.DateField()),
                ('rep_dob_municipality', models.CharField(max_length=50)),
                ('rep_dob_province', models.CharField(max_length=50)),
                ('rep_residence_municipality', models.CharField(max_length=100)),
                ('rep_residence_province', models.CharField(max_length=100)),
                ('rep_residence_zip', models.CharField(max_length=30)),
                ('rep_street', models.CharField(max_length=100)),
                ('rep_fiscal_code', models.CharField(max_length=50)),
                ('rep_phone_number', models.IntegerField()),
                ('ss_fund', models.IntegerField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DataSecurityCoordinatorIndividual',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=120)),
                ('dob', models.DateField()),
                ('birthplace', models.CharField(max_length=30)),
                ('birthplace_county', models.CharField(max_length=30)),
                ('residence_city', models.CharField(max_length=50)),
                ('residence_province', models.CharField(max_length=50)),
                ('residence_cap', models.IntegerField()),
                ('activity_street', models.CharField(max_length=50)),
                ('activity_municipality', models.CharField(max_length=50)),
                ('activity_province', models.CharField(max_length=50)),
                ('activity_cap', models.IntegerField()),
                ('residence_street', models.CharField(max_length=50)),
                ('board_order_registration', models.CharField(max_length=50)),
                ('province_college', models.CharField(max_length=40)),
                ('number_of_reg_order_college', models.IntegerField()),
                ('vat_number', internationalflavor.vat_number.models.VATNumberField(countries=['IT'])),
                ('fiscal_code', models.CharField(max_length=40)),
                ('phone_number', phone_field.models.PhoneField(max_length=31)),
                ('security_case_technician', models.CharField(choices=[('4%', '4%'), ('4%', '5%')], max_length=5)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DataSecurityCoordinatorLegal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('municipal_reg_office', models.CharField(max_length=20)),
                ('province_reg_office', models.CharField(max_length=20)),
                ('cap_reg_office', models.CharField(max_length=20)),
                ('street_reg_office', models.CharField(max_length=100)),
                ('province_of_inscription_enterprises_register', models.CharField(max_length=20)),
                ('number_of_inscription_enterprises_register', models.CharField(max_length=50)),
                ('rep_name', models.CharField(max_length=100)),
                ('rep_dob', models.DateField()),
                ('rep_dob_municipality', models.CharField(max_length=50)),
                ('rep_dob_province', models.CharField(max_length=50)),
                ('rep_residence_municipality', models.CharField(max_length=100)),
                ('rep_residence_province', models.CharField(max_length=100)),
                ('rep_residence_zip', models.CharField(max_length=30)),
                ('rep_street', models.CharField(max_length=100)),
                ('rep_fiscal_code', models.CharField(max_length=50)),
                ('rep_phone_number', models.IntegerField()),
                ('ss_fund', models.IntegerField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DataThermoTechnicalIndividual',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=120)),
                ('dob', models.DateField()),
                ('birthplace', models.CharField(max_length=30)),
                ('birthplace_county', models.CharField(max_length=30)),
                ('residence_city', models.CharField(max_length=50)),
                ('residence_province', models.CharField(max_length=50)),
                ('residence_cap', models.IntegerField()),
                ('activity_street', models.CharField(max_length=50)),
                ('activity_municipality', models.CharField(max_length=50)),
                ('activity_province', models.CharField(max_length=50)),
                ('activity_cap', models.IntegerField()),
                ('residence_street', models.CharField(max_length=50)),
                ('board_order_registration', models.CharField(max_length=50)),
                ('province_college', models.CharField(max_length=40)),
                ('number_of_reg_order_college', models.IntegerField()),
                ('vat_number', internationalflavor.vat_number.models.VATNumberField(countries=['IT'])),
                ('fiscal_code', models.CharField(max_length=40)),
                ('phone_number', phone_field.models.PhoneField(max_length=31)),
                ('security_case_technician', models.CharField(choices=[('4%', '4%'), ('4%', '5%')], max_length=5)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DataThermoTechnicalLegal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50)),
                ('municipal_reg_office', models.CharField(max_length=20)),
                ('province_reg_office', models.CharField(max_length=20)),
                ('cap_reg_office', models.CharField(max_length=20)),
                ('street_reg_office', models.CharField(max_length=100)),
                ('province_of_inscription_enterprises_register', models.CharField(max_length=20)),
                ('number_of_inscription_enterprises_register', models.CharField(max_length=50)),
                ('rep_name', models.CharField(max_length=100)),
                ('rep_dob', models.DateField()),
                ('rep_dob_municipality', models.CharField(max_length=50)),
                ('rep_dob_province', models.CharField(max_length=50)),
                ('rep_residence_municipality', models.CharField(max_length=100)),
                ('rep_residence_province', models.CharField(max_length=100)),
                ('rep_residence_zip', models.CharField(max_length=30)),
                ('rep_street', models.CharField(max_length=100)),
                ('rep_fiscal_code', models.CharField(max_length=50)),
                ('rep_phone_number', models.IntegerField()),
                ('ss_fund', models.IntegerField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Prof_table',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('designer_individual', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disgner_individual', to='professionals.datadesignerindividual')),
                ('designer_legal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disgner_legal', to='professionals.datadesignerlegal')),
                ('director_works_individual', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='direktor_individual', to='professionals.datadirectorworksindividual')),
                ('director_works_legal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='direktor_legal', to='professionals.datadirectorworkslegal')),
                ('energy_expert_individual', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dividual', to='professionals.dataenergyexpertindividual')),
                ('energy_expert_legal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='energy_legal', to='professionals.dataenergyexpertlegal')),
                ('resp_work_individual', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resposible_for_work_ind', to='professionals.dataresponsibleforworksindividual')),
                ('resp_work_legal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resposible_for_work_leg', to='professionals.dataresponsibleforworkslegal')),
                ('security_exe_individual', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sec_exe_individual', to='professionals.datasecuritycoordinatorexecutionindividual')),
                ('security_exe_legal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sec_exe_legal', to='professionals.datasecuritycoordinatorexecutionlegal')),
                ('security_plan_individual', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secutiy_individual', to='professionals.datasecuritycoordinatorindividual')),
                ('security_plan_legal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='security_individual', to='professionals.datasecuritycoordinatorlegal')),
                ('thermotechnical_individual', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='professionals.datathermotechnicalindividual')),
                ('thermotechnical_legal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='professionals.datathermotechnicallegal')),
            ],
            options={
                'verbose_name': 'Proifessionals Table List',
            },
        ),
    ]
