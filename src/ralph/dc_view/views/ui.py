# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from ralph.admin.mixins import RalphTemplateView
from ralph.data_center.models.physical import DataCenter


class DataCenterView(RalphTemplateView):

    template_name = 'dc_view/data_center_view.html'

    def get_context_data(self, **kwargs):
        context = super(DataCenterView, self).get_context_data(**kwargs)
        context['data_centers'] = DataCenter.objects.all()
        context['site_header'] = "Ralph 3"
        return context
