from odoo import api, fields, models, _

class RestePartner(models.Model):
    _inherit = 'res.partner'
    @api.multi
    #@api.one
    def _compute_credit(self):
    	for rec in self:
    		rec.credite = -rec.credit
  
    @api.multi
    #@api.one
    def _compute_debit(self):
    	for rec in self:
    		rec.debite = -rec.debit
    credite = fields.Monetary(string='Balance Client', help="Balance client.", compute='_compute_credit')
    debite = fields.Monetary(string='Balance Fournisseur', help="Balance Fournisseur.", compute='_compute_debit')
    
    def do_nothing(self):
    	print("hello")