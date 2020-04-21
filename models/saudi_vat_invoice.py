# -*- coding: utf-8 -*-
# Copyright (C) 2017-Today  Technaureus Info Solutions(<http://technaureus.com/>).
from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    date_issue = fields.Date(string="Date of Issue")
    date_supply = fields.Date(string="Date of Supply")

    def net_amount_to_words(self, amount):
        return self.currency_id.amount_to_text(amount)
