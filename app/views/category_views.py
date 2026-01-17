from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from app.forms import CategoryForm

class CategoryCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'app/category_form.html', {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():    
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('memo_list')

        # バリデーションエラー時
        return render(request, 'app/category_form.html', {'form': form})

