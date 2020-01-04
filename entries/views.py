from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contract
from .forms import CommentForm
from users.models import Profile


class HomeView(LoginRequiredMixin, ListView):
	model = Contract
	template_name = 'entries/index.html'
	context_object_name = "blog_entries"
	ordering = ['-contract_date']
	paginate_by = 3

class HomeView1(ListView):
	model = Contract
	template_name = 'entries/base.html'
	context_object_name = "blog_entries"
	ordering = ['-contract_date']
	paginate_by = 3


class ContractView(LoginRequiredMixin, DetailView):
	model = Contract
	template_name = 'entries/contract_detail.html'

class UserDetailView(LoginRequiredMixin, DetailView):
	model = Profile
	template_name = 'entries/user-details.html'

class CreateContractView(LoginRequiredMixin, CreateView):
	model = Contract
	template_name = 'entries/create_contract.html'
	fields = ['contract_title', 'contract_details', 'contract_price', 'contract_deadline', 'contract_image1', 'contract_image2', 'contract_doc', 'contract_paymentVerification']

	def form_valid(self, form):
		form.instance.contract_creator = self.request.user
		return super().form_valid(form)

def add_comment_to_post(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.contract = contract
            comment.save()
            return redirect('contract-detail', pk=contract.pk)
    else:
        form = CommentForm()
    return render(request, 'entries/add_comment_to_post.html', {'form': form})