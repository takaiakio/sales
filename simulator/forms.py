from django import forms

class TargetSalesForm(forms.Form):
    target_sales = forms.DecimalField(label="目標売上", min_value=0)

class ProductForm(forms.Form):
    name = forms.CharField(label="商品名", max_length=100)
    price = forms.DecimalField(label="価格", min_value=0)
    ratio = forms.DecimalField(label="販売比率", min_value=0)


