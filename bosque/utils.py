from urlparse import urljoin

from django.contrib.sites.models import Site


def make_absolute_url(path):
    """
    Make a absolute url from given path.
    Use Site framework to know the domain
    """
    site = Site.objects.get_current()

    protocol = 'http://'
    base_url = '{protocol}{site_url}'.format(
        protocol=protocol,
        site_url=site.domain
    )
    return urljoin(base_url, path)
