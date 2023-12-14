from import_export import resources
from currency.models import Rate


class RateResources(resources.ModelResource):

    class Meta:
        model = Rate
