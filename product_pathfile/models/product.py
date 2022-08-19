from odoo import models, fields


class Product(models.Model):
    _inherit = "product.product"

    # new fields
    # path to different file formats
    pathfile_pdf = fields.Char(
        string="Path to PDF",
        )
    pathfile_dwg = fields.Char(
        string="Path to DWG",
        )
    pathfile_stp = fields.Char(
        string="Path to STP",
        )
