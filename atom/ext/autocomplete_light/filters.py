import django_filters
from dal import autocomplete


class AutocompleteChoiceFilter(django_filters.ModelChoiceFilter):
    def __init__(self, autocomplete_name, *args, **kwargs):
        autocomplete = autocomplete.registry.get_autocomplete_from_name(autocomplete_name)
        kwargs['queryset'] = autocomplete.queryset
        kwargs['widget'] = autocomplete.widget
        super(AutocompleteChoiceFilter, self).__init__(*args, **kwargs)
