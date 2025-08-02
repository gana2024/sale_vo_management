from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError
from datetime import datetime, date

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_vo = fields.Boolean(string="Is VO", default=False,readonly=True)
    related_so_id = fields.Many2one('sale.order', string="Related Sale Order")
    vo_ids = fields.One2many('sale.order', 'related_so_id', string="Variation Orders")
    opportunity_id = fields.Many2one('crm.lead', string='Opportunity')

    def action_open_related_so(self):
        self.ensure_one()
        if not self.related_so_id:
            raise UserError(_("This VO has no related parent Sale Order."))
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',
            'res_id': self.related_so_id.id,
            'view_mode': 'form',
            'target': 'current',
        }

    def action_create_vo(self):
        self.ensure_one()
        if self.is_vo or self.state in ['draft', 'cancel']:
            raise UserError(_("You can only create VO from confirmed non-VO orders."))

        context = {
            'default_is_vo': True,
            'default_related_so_id': self.id,
        }

        if self.tag_ids:
            context['default_tag_ids'] = [(6, 0, self.tag_ids.ids)]

        if self.opportunity_id:
            context['default_opportunity_id'] = self.opportunity_id.id

        if self.project_id:
            context['default_project_id'] = self.project_id.id

        return {
            'type': 'ir.actions.act_window',
            'name': 'Create VO',
            'res_model': 'sale.order',
            'view_mode': 'form',
            'target': 'current',
            'context': context,
        }




