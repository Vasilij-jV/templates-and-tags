from django.shortcuts import render, get_object_or_404, redirect
from .models import Variables, Page
from .forms import PageForm
from .templatetags.blog_tags import random_color


def list_variables(request):
    variables = Variables.objects.all()
    return render(request, 'main/list_variables.html', {'variables': variables})


def list_pages(request):
    pages = Page.objects.all()
    if request.method == 'POST':
        create_page = PageForm(request.POST)
        if create_page.is_valid():
            new_page = create_page.save(commit=False)
            new_page.save()
            return redirect('pagemanagement:list_pages')
    else:
        create_page = PageForm()

    return render(request, 'main/list_pages.html', {'pages': pages, 'create_page': create_page})


def edit_page(request, page):
    page = get_object_or_404(Page, slug=page)
    if request.method == 'POST' and 'edit' in request.POST:
        edit_form = PageForm(request.POST, instance=page)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('pagemanagement:one_page', page=page)
    else:
        edit_form = PageForm(instance=page)

    if request.method == 'POST' and 'delete' in request.POST:
        page.delete()
        return redirect('pagemanagement:list_pages')

    return render(request, 'main/one_page.html', {'page': page, 'edit_form': edit_form})


def random_color_view(request):
    list_colors = random_color()
    print(list_colors)
    context = {
        'random_color': list_colors,
    }
    return render(request, 'main/random_color_template.html', context)

