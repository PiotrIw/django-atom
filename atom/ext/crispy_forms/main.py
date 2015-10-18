from __future__ import absolute_import
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Reset, Submit
from django.forms.models import BaseInlineFormSet
from django.forms import BaseFormSet
from django.utils.translation import ugettext_lazy as _


class FormsetHelper(FormHelper):
    form_tag = False


class TableFormSetHelper(FormsetHelper):
    template = 'bootstrap/table_inline_formset.html'


class TableFormSetMixin(object):
    def __init__(self, *args, **kwargs):
        super(InlineTableFormSet, self).__init__(*args, **kwargs)
        self.helper = TableFormSetHelper()


class InlineTableFormSet(TableFormSetMixin, BaseInlineFormSet):
    pass


class TableFormSet(TableFormSetMixin, BaseFormSet):
    pass


class HelperMixin(object):
    form_helper_cls = FormHelper

    def __init__(self, *args, **kwargs):
        super(HelperMixin, self).__init__(*args, **kwargs)
        self.helper = getattr(self, 'helper', self.form_helper_cls(self))


class SingleButtonMixin(HelperMixin):
    form_helper_cls = FormHelper

    @property
    def action_text(self):
        return _('Update') if hasattr(self, 'instance') and self.instance.pk else _('Save')

    def __init__(self, *args, **kwargs):
        super(SingleButtonMixin, self).__init__(*args, **kwargs)
        self.helper.add_input(Submit('action', self.action_text, css_class="btn-primary"))


class SaveButtonMixin(SingleButtonMixin):

    def __init__(self, *args, **kwargs):
        super(SaveButtonMixin, self).__init__(*args, **kwargs)
        self.helper.add_input(Reset('reset', _('Reset!')))


class FormHorizontalMixin(HelperMixin):

    def __init__(self, *args, **kwargs):
        super(FormHorizontalMixin, self).__init__(*args, **kwargs)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
