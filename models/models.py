# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Feriados(models.Model):
	_name = 'feriados.feriados'

	name = fields.Char()
	dia_ids = fields.One2many('feriados.feriados.dia', 'feriado_id', 'Feriados')
	dia_count = fields.Integer('Cantidad de feriados', compute='_compute_feriados')
	company_id = fields.Many2one('res.company', 'Empresa', required=False, default=lambda self: self.env['res.company']._company_default_get('feriados.feriados'))

	@api.one
	def _compute_feriados(self):
		self.dia_count = len(self.dia_ids)

	@api.one
	def es_feriado(self, fecha):
		ret = False
		for dia_id in self.dia_ids:
			if fecha == dia_id.date:
				ret = True
				break
		return ret

class FeriadosDia(models.Model):
	_name = 'feriados.feriados.dia'
	
	_order = 'date asc'
	feriado_id = fields.Many2one('feriados.feriados', "Lista", ondelete="cascade")
	date = fields.Date('Dia')
	company_id = fields.Many2one('res.company', 'Empresa', required=False, default=lambda self: self.env['res.company']._company_default_get('feriados.feriados.dia'))
