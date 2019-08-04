from django.conf import settings

from confapp import conf
from pyforms.basewidget import segment
from pyforms.controls import ControlCheckBox
from pyforms_web.web.middleware import PyFormsMiddleware
from pyforms_web.widgets.django import ModelAdminWidget

from finance.models import CostCenter

from .financeproject_list import FinanceProjectListApp


class CostCenterListApp(ModelAdminWidget):

    TITLE = 'Cost Centers'
    UID = 'cost-centers'

    MODEL = CostCenter

    LIST_DISPLAY = ['costcenter_code', 'costcenter_name', 'start_date', 'end_date']

    LIST_FILTER = ['group', 'financeproject__financeproject_code']

    SEARCH_FIELDS = ['costcenter_name__icontains', 'costcenter_code__icontains']

    INLINES = [FinanceProjectListApp]

    FIELDSETS = [
        segment(
            'costcenter_name',
            ('costcenter_code', 'start_date', 'end_date'),
            'group',
        ),
        ' ',
        'FinanceProjectListApp',
        ' ',
    ]

    # ORQUESTRA CONFIGURATION
    # =========================================================================
    ORQUESTRA_MENU = 'left>FinancesDashboardWidget'
    ORQUESTRA_MENU_ORDER = 10
    ORQUESTRA_MENU_ICON = 'boxes'
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    # =========================================================================

    AUTHORIZED_GROUPS = ['superuser', settings.PROFILE_LAB_ADMIN]

    def __init__(self, *args, **kwargs):

        self._active = ControlCheckBox(
            'Active',
            default=True,
            label_visible=False,
            changed_event=self.populate_list,
            # field_style='text-align:right;',  # FIXME breaks form
        )

        super().__init__(*args, **kwargs)

        # Edit filter label
        self._list.custom_filter_labels = {
            'financeproject__financeproject_code': 'Project Code',
        }

    def get_toolbar_buttons(self, has_add_permission=False):
        return tuple(
            (['_add_btn'] if has_add_permission else []) + [
                '_active',
            ]
        )

    def get_queryset(self, request, qs):

        if self._active.value:
            qs = qs.active()

        return qs

    def has_remove_permissions(self, obj):
        """Only superusers may delete these objects."""
        user = PyFormsMiddleware.user()
        return user.is_superuser
