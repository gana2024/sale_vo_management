##############################################################################
#    Copyright (c) 2024 CDS Solutions SRL. (http://cds-solutions.co)
#    Maintainer: Eng.Ramadan Khalil (<info@cdsegypt.com>)
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
##############################################################################
from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    vo_count = fields.Integer(string="VO Count", compute='_compute_vo_count')

    def _compute_vo_count(self):
        for lead in self:
            related_sos = self.env['sale.order'].search([('opportunity_id', '=', lead.id)])
            vos_count = self.env['sale.order'].search_count([
                ('is_vo', '=', True),
                ('related_so_id', 'in', related_sos.ids)
            ])
            lead.vo_count = vos_count

    def action_view_vos(self):
        self.ensure_one()
        related_sos = self.env['sale.order'].search([('opportunity_id', '=', self.id)])
        vos = self.env['sale.order'].search([
            ('is_vo', '=', True),
            ('related_so_id', 'in', related_sos.ids)
        ])
        return {
            'type': 'ir.actions.act_window',
            'name': 'VOs',
            'res_model': 'sale.order',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', vos.ids)],
            'target': 'current',
        }
