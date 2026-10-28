from django.db import migrations

def create_initial_products(apps, schema_editor):
    Product = apps.get_model('api', 'Product')
    products = [
        {'name': 'TV', 'price': 5000, 'quantity': 10},
        {'name': 'Notebook', 'price': 30000, 'quantity': 5},
        {'name': 'Mouse', 'price': 500, 'quantity': 20}
    ]
    for p in products:
        Product.objects.get_or_create(name=p['name'], defaults=p)

def remove_initial_products(apps, schema_editor):
    Product = apps.get_model('api', 'Product')
    Product.objects.filter(name__in=['TV', 'Notebook', 'Mouse']).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_products, remove_initial_products),
    ]
