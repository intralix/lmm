# -*- coding: utf-8 -*-
from . import models
from . import wizard
from odoo import _


def pre_init_check(cr):
    from odoo.service import common
    from odoo.exceptions import UserError
    version_info = common.exp_version()
    server_serie = version_info.get('server_serie')
    if server_serie != '15.0':
        raise UserError(_('This module support Odoo series 15.0, found %s.') %
                      server_serie)
    return True
