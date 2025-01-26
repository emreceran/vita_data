
import random
from odoo import models, fields
from odoo.tools.translate import html_translate

class ProductTemplate(models.Model):
    _inherit = 'product.template'


    accordion_content_html = fields.Html("Accordion Content", sanitize_overridable=True, sanitize_attributes=False, translate=html_translate, sanitize_form=False)
    custom_description_html = fields.Html('Product Description', sanitize_overridable=True, sanitize_attributes=False, translate=html_translate, sanitize_form=False)
    related_products_html = fields.Html('Related Products', sanitize_overridable=True, sanitize_attributes=False, translate=html_translate, sanitize_form=False)
    # Sıkça Sorulan Sorular ve Cevaplar için yeni alanlar
    faq_question1 = fields.Html('Sıkça Sorulan Soru 1', sanitize_overridable=True, translate=True)
    faq_answer1 = fields.Html('Sıkça Sorulan Soru 1 Cevabı', sanitize_overridable=True, translate=True)
    faq_question2 = fields.Html('Sıkça Sorulan Soru 2', sanitize_overridable=True, translate=True)
    faq_answer2 = fields.Html('Sıkça Sorulan Soru 2 Cevabı', sanitize_overridable=True, translate=True)
    faq_question3 = fields.Html('Sıkça Sorulan Soru 3', sanitize_overridable=True, translate=True)
    faq_answer3 = fields.Html('Sıkça Sorulan Soru 3 Cevabı', sanitize_overridable=True, translate=True)
    img_2 = fields.Binary(string="Detail Image", attachment=True, help="Extra image for the product")
    snippet_isim_ustu = fields.Char(string='Snippet İsim Üstü')

    def get_random_products(self, current_product_id, limit=15):
        """
        Rastgele ürünler döndürür (mevcut ürünü ve aynı kategoridekileri hariç tutar).
        """
        current_product = self.browse(current_product_id)
        if not current_product.exists():
            return []

        # Uygun ürünleri filtrele
        all_products = self.search([
            ('public_categ_ids', 'not in', current_product.public_categ_ids.ids),
            ('id', '!=', current_product.id)
        ])

        # Eğer ürün sayısı limiti aşmıyorsa, tüm ürünleri döndür
        if len(all_products) <= limit:
            return all_products

        # Rastgele ürünleri seç (sadece ID'leri kullanarak)
        random_product_ids = random.sample(all_products.ids, limit)
        
        # Rastgele seçilen ID'leri bir recordset'e dönüştür
        return self.browse(random_product_ids)

    
        
        



class ProductPublicCategory(models.Model):
    _inherit = "product.public.category"

    website_description2 = fields.Html('Category Description2', sanitize_overridable=True, sanitize_attributes=False, translate=html_translate, sanitize_form=False)



