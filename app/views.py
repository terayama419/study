# app/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from .forms import MemoForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import SignUpForm

class MemoCreateView(LoginRequiredMixin, View):
# django.views.generic    
#     model = Memo
#     fields = ['title', 'content']
#     template_name = 'app/memo_form.html'
#     success_url = '/memo/'
    def get(self, request):
        form = MemoForm()
        return render(request, 'app/memo_form.html', {'form': form})

    def post(self, request):
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            # ログインユーザーをセット
            memo.user = request.user        
            form.save()
            return redirect('memo_list')

        # バリデーションエラー時
        return render(request, 'app/memo_form.html', {'form': form})

class MemoListView(LoginRequiredMixin, View):
    def get(self, request):
        keyword = request.GET.get('q', '')
        page_number = request.GET.get('page', 1)

        memos = Memo.objects.filter(user=request.user)

        # AND 検索部分
        if keyword:
            words = keyword.split()
            for word in words:
                memos = memos.filter(
                    Q(title__icontains=word) |
                    Q(content__icontains=word)
                )

        memos  = memos.order_by('-created_at')

        paginator = Paginator(memos, 5)
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'app/memo_list.html',
            {
                'page_obj': page_obj,
                'keyword': keyword,
            }
        )

class MemoUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        # 対象のメモ取得（本人のものだけ）
        memo = get_object_or_404(Memo, pk=pk, user=request.user)
        form = MemoForm(instance=memo)
        return render(request, 'app/memo_form.html', {'form': form})

    def post(self, request, pk):
        # pk=id, テーブルからデータを取得する
        memo = get_object_or_404(Memo, pk=pk, user=request.user)
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('memo_list')

        # バリデーションエラー時
        return render(request, 'app/memo_form.html', {'form': form})

class MemoDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        memo = get_object_or_404(Memo, pk=pk, user=request.user)
        memo.delete()
        return redirect('memo_list')

    # memo = get_object_or_404(Memo, pk=pk)

    # if request.method == 'POST':
    #     memo.delete()
    #     return redirect('memo_list')

    # return render(request, 'app/memo_confirm_delete.html', {'memo': memo})

class SignUpView(View):

    def get(self, request):
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            login(request, user)  # ← 自動ログイン
            return redirect('memo_list')

        return render(request, 'registration/signup.html', {'form': form})