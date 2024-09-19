from django.shortcuts import render


def product_page(request):
    """
    Представление страницы продуктов.
    """
    return render(request, 'product_page.html')
