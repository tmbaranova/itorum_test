from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            request.user.made_an_order = True
            order.customer = request.user
            order.save()
            return redirect("posts:index")

        return render(request, 'new.html', {'form': form})

    form = OrderForm()
    return render(request, 'new.html', {'form': form})

