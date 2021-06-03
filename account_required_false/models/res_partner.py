# -*- coding: utf-8 -*-
from odoo import models,api,fields
from odoo.exceptions import ValidationError


class res_partner(models.Model):
    _inherit = 'res.partner'

    property_account_receivable_id = fields.Many2one(required=False)
    property_account_payable_id = fields.Many2one(required=False)
