# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo888(models.Model):
#     _name = 'odoo888.odoo888'
#     _description = 'odoo888.odoo888'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api

class jugador(models.Model):
	_name = 'odoo888.jugador'
	_description = 'model persona'

	name = fields.Char('DNI',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	telefono = fields.Char(string='Teléfono',required=True)
