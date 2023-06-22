from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..helpers import check_membership

from ..models.course import Course


@login_required(login_url='login')
def AccountCoursesView(request):
    user = request.user
    isMember = check_membership(user)
    courses = Course.objects.filter(instructor__app_user=user)


    context = {
        'user':user,
        'isMember':isMember,
        'courses':courses,
    }

    return render(request, "pages/account-courses.html", context)
