import logging

from django.conf import settings

logger = logging.getLogger(__name__)

def tenant_db_from_request(request):
        # Get the domain name from below 
        # current_site = request.META['HTTP_HOST']

        # Since this is a test project, no domain is associated, so the
        # attached tenant it's url. Uncomment the below two lines to 
        # remove this logic
        current_site = request.get_full_path()
        if 'api' in current_site:
                current_site = current_site.split('/')[2]
        elif 'test' in current_site:
                current_site = current_site.split('/')[3]
        logger.info(current_site)


        database = 'default'
        for key,value in settings.TENANTS_WITH_DB_NAME.items():
                if(current_site in key):
                        database = settings.TENANTS_WITH_DB_NAME[key]
                        break
        return database