from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm


@login_required
def image_create(request):
    if request.method == "POST":
        # form has been sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # data in the form is valid
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # assign the current user to the element
            new_image.user = request.user
            new_image.save()
            messages.success(request, "Image added successfully")
            # redirect to providing detailed information
            # about the newly created item
            return redirect(new_image.get_absolute_url())
    else:
        # compose a form with data,
        # provided by the bookmarklet with the GET method
        form = ImageCreateForm(data=request.GET)
    return render(
        request, "images/image/create.html", {"section": "images", "form": form}
    )
