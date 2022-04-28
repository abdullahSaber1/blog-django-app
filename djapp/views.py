from django.shortcuts import render, redirect
from django.http import HttpResponse

from djapp.models import Student, Track

from .forms import StudentForm

# rest framework imports here

from .serializers import StudentSerializer, TrackSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# auth imports here
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserForm


# auth views here

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        register_form = UserForm()
        if request.method == 'POST':
            register_form = UserForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                username = register_form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('login')
        context = {'register_form': register_form}
        return render(request, 'djapp/register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            # name of Input fields in login.html
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))

                return redirect('home')
            else:
                messages.info(request, 'username or password is incorrect')
        context = {}
        return render(request, 'djapp/login.html', context)


def logout(request):
    logout(request)
    return redirect('login')


# rest Framework views here


@ api_view(['GET'])
def api_all_student(request):

    all_students = Student.objects.all()
    st_serializer = StudentSerializer(all_students, many=True)
    return Response(st_serializer.data)


@ api_view(['GET'])
def api_one_student(request, st_id):
    student = Student.objects.get(id=st_id)
    st_serializer = StudentSerializer(student, many=False)
    return Response(st_serializer.data)


@ api_view(['POST'])
def api_add_student(request):
    st_serilizer = StudentSerializer(data=request.data)
    if st_serilizer.is_valid():
        st_serilizer.save()
        return redirect('api-all')


@ api_view(['PUT'])
def api_edit_student(request, st_id):
    student = Student.objects.get(id=st_id)
    st_serializer = StudentSerializer(data=request.data, instance=student)
    if st_serializer.is_valid():
        st_serializer.save()
        return Response(st_serializer.data)

    return redirect('api-all')


@ api_view(['delete'])
def api_delete_student(request, st_id):
    student = Student.objects.get(id=st_id)
    student.delete()

    return Response('student is deleted ..')

    # Create your views here.


def home(request):
    all_student = Student.objects.all()
    context = {'student_list': all_student}
    return render(request, 'djapp/home.html', context)


def show(request, st_id):
    student = Student.objects.get(id=st_id)
    context = {'student': student}
    return render(request, 'djapp/show2.html', context)


def destroy(request, st_id):
    student = Student.objects.get(id=st_id)
    student.delete()

    return redirect('home')


def addStudent(request):
    studentForm = StudentForm()
    context = {'st_form': studentForm}

    if request.method == 'POST':
        studentForm = StudentForm(request.POST)

        if studentForm.is_valid():
            studentForm.save()
            return redirect('home')

    return render(request, 'djapp/addStudent.html', context)


def editStudent(request, st_id):
    student = Student.objects.get(id=st_id)
    st_form = StudentForm(instance=student)
    context = {'st_form': st_form}
    if request.method == 'POST':
        studentForm = StudentForm(request.POST, instance=student)

        if studentForm.is_valid():
            studentForm.save()
            return redirect('home')

    return render(request, 'djapp/addStudent.html', context)
