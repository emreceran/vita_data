# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class vita_data(models.Model):
#     _name = 'vita_data.vita_data'
#     _description = 'vita_data.vita_data'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

