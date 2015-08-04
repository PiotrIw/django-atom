from django.utils.translation import ugettext_lazy as _
import django_filters


class CrispyFilterMixin(object):
    form_class = 'form-inline'

    @property
    def form(self):
        from crispy_forms.helper import FormHelper
        from crispy_forms.layout import Submit
        self._form = super(CrispyFilterMixin, self).form
        self._form.helper = FormHelper(self._form)
        if self.form_class:
            self._form.helper.form_class = 'form-inline'
        self._form.helper.form_method = 'get'
        self._form.helper.layout.append(Submit('filter', _('Filter')))
        return self._form


class AutocompleteChoiceFilter(django_filters.ModelChoiceFilter):
    def __init__(self, autocomplete_name, *args, **kwargs):
        from autocomplete_light.registry import registry
        from autocomplete_light import ChoiceWidget
        autocomplete = registry.get_autocomplete_from_arg(autocomplete_name)
        kwargs['queryset'] = autocomplete.choices
        kwargs['widget'] = ChoiceWidget(autocomplete)
        super(AutocompleteChoiceFilter, self).__init__(*args, **kwargs)
