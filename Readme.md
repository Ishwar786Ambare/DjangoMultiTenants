## django milti tenent

* resources

* `https://hygull.github.io/try-django-tenant-schemas/`
* `https://hygull.github.io/try-django-tenant-schemas/`
# 
### for create superuser IMP
* `./manage.py tenant_command createsuperuser --schema=tenant1`
* or
* `./manage.py tenant_command -s=customer1 createsuperuser`


#### Other permutations of the same command gives similar results:

`python manage.py tenant_command loaddata -s SCHEMA_NAME data.json`

`python manage.py tenant_command loaddata --schema=SCHEMA_NAME data.json`

`python manage.py tenant_command -s SCHEMA_NAME loaddata data.json`


`https://github.com/bernardopires/django-tenant-schemas/issues/618`
