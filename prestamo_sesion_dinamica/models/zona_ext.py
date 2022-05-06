# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class Zona(models.Model):
    _inherit = 'prestamo.zona'

    barrios = fields.One2many('prestamo.barrio', 'zona_id', 'Barrios')


class Barrio(models.Model):
    _inherit = 'prestamo.barrio'

    zona_id = fields.Many2one('prestamo.zona', 'Zona',required=True)


class Cliente(models.Model):
    _inherit = 'prestamo.cliente'

    @api.multi
    @api.onchange('barrio_id')
    def actualizar_zona(self):
        _logger.error('Actualizando zona...')
        for cliente in self:
            if cliente.barrio_id:
                cliente.zona_id = cliente.barrio_id.zona_id
            else:
                cliente.zona_id = False
