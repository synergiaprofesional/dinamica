# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class Cobro(models.Model):
    _inherit = 'prestamo.cobro'

    # cobrador_id = fields.Many2many(
    #     'prestamo.cobrador', string='Cobrador', required=True)

    cobrador_ids = fields.Many2many(
        'prestamo.cobrador', string='Cobrador', required=True)


    @api.multi
    def abrir_sesion(self):
        # for cobrador in self.cobrador_id:
        #     _logger.error(cobrador.name)
        
        sesion = self.env['prestamo.session'].sesion_actual(
            cobrador_id=self.env.user.cobrador_id.id)
        if sesion.id:
            self.sesion_id = sesion
            return
        _logger.error("abriendo sesion...")
        context = {
            'default_cobro_id': self.id,
            'default_cobrador_id': self.env.user.cobrador_id.id or False,
        }
        action = {
            'name': 'Abrir Sesión',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'prestamo.session',
            'target': 'current',
            'context': context,
        }
        return action

    @api.multi
    def reanudar_sesion(self):
        self.verificar_cobrador()
        cobrador_id = self.env.user.cobrador_id
        if not cobrador_id:
            raise exceptions.ValidationError(
                'El usuario actual no puede recaudar en este cobro')
        return cobrador_id.recaudar()

    @api.multi
    def get_sesion_actual(self):
        self.verificar_cobrador()
        context = {}
        if not self.sesion_id:
            context = {
                'default_cobro_id': self.id,
                'default_cobrador_id': self.env.user.cobrador_id.id or False,
            }
        return {
            'name': self.sesion_id.name,
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'prestamo.session',
            'res_id': self.sesion_id.id,
            'target': 'current',
            'context': context,
        }

    def verificar_cobrador(self):
        tiene_permiso = self.env.user.has_group(
            'base.group_system') or self.env.user.has_group('prestamo.grupo_cobrador_admin')
        _logger.error(tiene_permiso)    
        if not tiene_permiso:
            cobrador_id = self.env.user.cobrador_id
            if cobrador_id:
                if cobrador_id not in self.cobrador_id:
                    raise exceptions.ValidationError(
                        'Sr. %s usted no puede realizar la acción sobre este Cobro' % cobrador_id.name)
