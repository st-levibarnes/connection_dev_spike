# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class connection_dev_spike(models.Model):
#     _name = 'connection_dev_spike.connection_dev_spike'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
class connection_binding(models.Model):
    _name = 'connection_dev_spike.connection_binding'

    name = fields.Char()
    server = fields.Char()
    userName = fields.Char()
    password = fields.Char()
    database = fields.Char()