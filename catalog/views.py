from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Product
from .forms import ReviewForm
from . import forms
from django.views import View


class ProductListView(generic.ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        return context


class EditProductView(generic.UpdateView):
    template_name = "catalog/edit_product.html"
    form_class = forms.ProductForm
    success_url = "/catalog/"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(Product, id=product_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditProductView, self).form_valid(form=form)


class ProductDeleteView(generic.DeleteView):
    template_name = "catalog/confirm_product_delete.html"
    success_url = "/catalog/"

    def get_object(self, **kwargs):
        product_id = self.kwargs.get("id")
        return get_object_or_404(Product, id=product_id)


class AddReviewView(View):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        form = ReviewForm()
        return render(request, 'catalog/add_review.html', {'form': form, 'product': product})

    def post(self, request, id):
        product = get_object_or_404(Product, id=id)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('product_detail', id=product.id)
        return render(request, 'catalog/add_review.html', {'form': form, 'product': product})
