# legacy dependency copied from here
# https://raw.githubusercontent.com/plone/plone.app.controlpanel/2.3.x/plone/app/controlpanel/widgets.py
# see link for details
from plone.app.form.widgets import MultiCheckBoxWidget


class MultiCheckBoxVocabularyWidget(MultiCheckBoxWidget):
    """ """

    def __init__(self, field, request):
        """Initialize the widget."""
        super(MultiCheckBoxVocabularyWidget, self).__init__(field,
            field.value_type.vocabulary, request)
