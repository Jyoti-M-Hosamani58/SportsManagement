# Generated by Django 3.0 on 2024-11-22 17:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('adhar', models.CharField(max_length=12, null=True)),
                ('parentName', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('place', models.CharField(max_length=500, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('uniformSize', models.CharField(max_length=15, null=True)),
                ('uniformColor', models.CharField(max_length=100, null=True)),
                ('package', models.CharField(max_length=100, null=True)),
                ('sessions', models.CharField(max_length=100, null=True)),
                ('totalAmount', models.CharField(max_length=100, null=True)),
                ('invoice_ID', models.CharField(max_length=100, null=True)),
                ('date', models.DateField()),
                ('blood_group', models.CharField(max_length=100, null=True)),
                ('payment', models.CharField(max_length=100, null=True)),
                ('balance', models.CharField(max_length=100, null=True)),
                ('batchtime', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('doj', models.CharField(max_length=100, null=True)),
                ('coachname', models.CharField(max_length=100, null=True)),
                ('coachType', models.CharField(max_length=100, null=True)),
                ('age', models.CharField(max_length=100, null=True)),
                ('dateOfBirth', models.CharField(max_length=20)),
                ('registration_fee', models.CharField(max_length=20)),
                ('paymentMode', models.CharField(max_length=20)),
                ('payment1', models.CharField(max_length=20)),
                ('accountholder', models.CharField(max_length=20)),
                ('accountnumber', models.CharField(max_length=20)),
                ('upiId', models.CharField(max_length=20)),
                ('transactionId', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coachname', models.CharField(max_length=100)),
                ('coachType', models.CharField(max_length=100)),
                ('current_date', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('sessions', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('batchtime', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Coach_allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=10)),
                ('batchtime', models.CharField(max_length=10)),
                ('coachname', models.CharField(max_length=10)),
                ('coachType', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Coach_Attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coachname', models.CharField(max_length=100)),
                ('coachType', models.CharField(max_length=100)),
                ('current_date', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='coachReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coachname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('coachType', models.CharField(max_length=100)),
                ('adhar', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('document', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comapny_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('other_details', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CricketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('stock', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('kit_name', models.CharField(max_length=255)),
                ('price_per_unit', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('totalCost', models.CharField(max_length=255)),
                ('updatedBalance', models.CharField(max_length=255)),
                ('receipt', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Duration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=100)),
                ('weekly_sessions', models.CharField(max_length=100)),
                ('payment', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('contact_no', models.CharField(max_length=20)),
                ('parent_name', models.CharField(max_length=100)),
                ('parent_mobile_no', models.CharField(max_length=20)),
                ('parent_email', models.EmailField(max_length=254)),
                ('parent_address', models.TextField()),
                ('weekly_sessions', models.CharField(max_length=1)),
                ('how_did_you_know', models.CharField(max_length=50)),
                ('other_details', models.TextField()),
                ('age', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Item_entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pieces', models.IntegerField()),
                ('purpose', models.CharField(max_length=100)),
                ('Purchase', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ItemPurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('price_per_unit', models.CharField(max_length=255)),
                ('total_cost', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='kit_distribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectCustomer', models.CharField(max_length=255)),
                ('admission_no', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('adhar', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('package', models.CharField(max_length=255)),
                ('sessions', models.CharField(max_length=255)),
                ('batchtime', models.CharField(max_length=255)),
                ('totalAmount', models.CharField(max_length=255)),
                ('balance', models.CharField(max_length=255)),
                ('brand_name', models.CharField(max_length=255)),
                ('kit_quantity', models.CharField(max_length=255)),
                ('kitTotalAmount', models.CharField(max_length=255)),
                ('itemname', models.CharField(max_length=255)),
                ('item_quantity', models.CharField(max_length=255)),
                ('itemTotalAmount', models.CharField(max_length=255)),
                ('finalAmount', models.CharField(max_length=255)),
                ('kit', models.CharField(max_length=255)),
                ('item', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('unit_price', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('receipt', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='KitItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('no_of_stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='KitPurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kit_name', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('price_per_unit', models.CharField(max_length=255)),
                ('total_cost', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('bill_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50, null=True)),
                ('utype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10, null=True)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('adhar', models.CharField(max_length=12, null=True)),
                ('parentName', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('place', models.CharField(max_length=500, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('uniformSize', models.CharField(max_length=15, null=True)),
                ('uniformColor', models.CharField(max_length=100, null=True)),
                ('package', models.CharField(max_length=100, null=True)),
                ('sessions', models.CharField(max_length=100, null=True)),
                ('totalAmount', models.CharField(max_length=100, null=True)),
                ('invoice_ID', models.CharField(max_length=100, null=True)),
                ('date', models.DateField()),
                ('blood_group', models.CharField(max_length=100, null=True)),
                ('payment', models.CharField(max_length=100, null=True)),
                ('balance', models.CharField(max_length=100, null=True)),
                ('batchtime', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('doj', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('admission_no', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('adhar', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('package', models.CharField(max_length=255)),
                ('sessions', models.CharField(max_length=255)),
                ('batchtime', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('price_per_unit', models.CharField(max_length=255)),
                ('updatedBalance', models.CharField(max_length=255)),
                ('totalCost', models.CharField(max_length=255)),
                ('receipt', models.CharField(max_length=255)),
                ('kit_name', models.CharField(max_length=255, null=True)),
                ('productname', models.CharField(max_length=255)),
                ('balance', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SportsKit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('price_per_unit', models.CharField(max_length=255)),
                ('total_cost', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StockAdjustment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kit_name', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
                ('price_per_unit', models.CharField(max_length=255)),
                ('total_cost', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Supliers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comapny_name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('phone_number', models.PositiveIntegerField()),
                ('email', models.DecimalField(decimal_places=2, max_digits=10)),
                ('other_details', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Userlogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchased_at', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports_app.KitItem')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('kit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sports_app.SportsKit')),
            ],
        ),
    ]
