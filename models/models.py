# -*- coding: utf-8 -*-


from odoo import models, fields
from odoo.tools.translate import html_translate

class ProductTemplate(models.Model):
    _inherit = 'product.template'


    accordion_content_html = fields.Html("Accordion Content", sanitize_overridable=True, sanitize_attributes=False, translate=html_translate, sanitize_form=False)
    custom_description_html = fields.Html('Product Description', sanitize_overridable=True, sanitize_attributes=False, translate=html_translate, sanitize_form=False)
    related_products_html = fields.Html('Related Products', sanitize_overridable=True, sanitize_attributes=False, translate=html_translate, sanitize_form=False)



class ProductPublicCategory(models.Model):
    _inherit = "product.public.category"



    website_description2 = fields.Html('Category Description2', sanitize_overridable=True, sanitize_attributes=False, translate=html_translate, sanitize_form=False)
