'''from django.forms import formset_factory
from django.shortcuts import render
from .forms import ProductForm, TargetSalesForm
from decimal import Decimal

def simulate_sales(request):
    # 商品数の取得（デフォルトは3）
    num_products = int(request.GET.get('num_products', 3))

    # フォームセットを作成
    ProductFormSet = formset_factory(ProductForm, extra=num_products)
    formset = ProductFormSet()

    # 目標売上のフォーム
    target_sales_form = TargetSalesForm()

    quantities = {}

    if request.method == 'POST':
        formset = ProductFormSet(request.POST)
        target_sales_form = TargetSalesForm(request.POST)

        if formset.is_valid() and target_sales_form.is_valid():
            # 目標売上を取得
            target_sales = Decimal(target_sales_form.cleaned_data['target_sales'])

            # 各商品の割合合計を計算
            total_ratio = sum(Decimal(form.cleaned_data['ratio']) for form in formset)

            # 各商品の販売個数を計算
            for form in formset:
                price = Decimal(form.cleaned_data['price'])
                ratio = Decimal(form.cleaned_data['ratio'])
                product_name = form.cleaned_data['name']

                sales_goal = (ratio / total_ratio) * target_sales
                quantity = sales_goal / price
                quantities[product_name] = round(quantity)

            return render(request, 'simulator/sales_result.html', {
                'quantities': quantities,
                'target_sales': target_sales,
            })

    return render(request, 'simulator/sales_form.html', {
        'formset': formset,
        'target_sales_form': target_sales_form,
        'num_products': num_products,
    })'''


from django.forms import formset_factory
from django.shortcuts import render
from .forms import ProductForm, TargetSalesForm
from decimal import Decimal

def simulate_sales(request):
    # 商品数の取得（デフォルトは3）
    num_products = int(request.GET.get('num_products', 3))

    # フォームセットを作成
    ProductFormSet = formset_factory(ProductForm, extra=num_products)
    
    # 初期値のフォームセット
    formset = ProductFormSet()
    target_sales_form = TargetSalesForm()

    quantities = {}

    if request.method == 'POST':
        # フォームセットの再作成
        formset = ProductFormSet(request.POST)
        target_sales_form = TargetSalesForm(request.POST)

        if formset.is_valid() and target_sales_form.is_valid():
            # 目標売上を取得
            target_sales = Decimal(target_sales_form.cleaned_data['target_sales'])

            # 各商品の割合合計を計算
            total_ratio = sum(Decimal(form.cleaned_data['ratio']) for form in formset)

            # 各商品の販売個数を計算
            for form in formset:
                price = Decimal(form.cleaned_data['price'])
                ratio = Decimal(form.cleaned_data['ratio'])
                product_name = form.cleaned_data['name']

                sales_goal = (ratio / total_ratio) * target_sales
                quantity = sales_goal / price
                quantities[product_name] = round(quantity)

            # 計算結果と共にフォームを再表示
            return render(request, 'simulator/sales_result.html', {
                'quantities': quantities,
                'target_sales': target_sales,
                'formset': formset,
                'target_sales_form': target_sales_form,
            })

    # POST以外のリクエスト時もフォームを表示
    return render(request, 'simulator/sales_form.html', {
        'formset': formset,
        'target_sales_form': target_sales_form,
        'num_products': num_products,
    })


