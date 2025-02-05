from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from datetime import datetime
from home.models import Details
from home.Forms import detailsform
# from home.forms import detailsform 

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Django Project")

def index(request):
    #return HttpResponse("this is home page")
    return render(request,'home.html')

def create(request):
    if request.method=="POST":
        sr_no=request.POST['sr_no']
        emp_id=request.POST['emp_id']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        age=request.POST['age']
        address=request.POST['address']
        department=request.POST['department']
        role=request.POST['role']
        salary=request.POST['salary']
        phone=request.POST['phone']
        email=request.POST['email']
        # obj=Details(sr_no=sr_no,emp_id=emp_id,firstname=firstname,lastname=lastname,age=age,address=address,department=department,role=role,salary=salary,phone=phone,email=email,date=datetime.today())
        # obj.save()
        # return redirect('/')
        if not (sr_no and emp_id and firstname and lastname and age and address and department and role and salary and phone and email):
            return render(request, 'home.html', {'error': 'All fields are required!'})
        try:
            emp_id = int(emp_id) 
            age = int(age)
            salary = float(salary)  # Use float if salary can be decimal
        except ValueError:
            return render(request, 'home.html', {'error': 'Emp ID ,Age must be an integer and Salary must be a number.'})


        try:
            # Attempt to create and save the object
            obj = Details(
                sr_no=sr_no,
                emp_id=emp_id,
                firstname=firstname,
                lastname=lastname,
                age=age,
                address=address,
                department=department,
                role=role,
                salary=salary,
                phone=phone,
                email=email,
                date=datetime.today()
            )
            obj.save()
            return redirect('/')
        except Exception as e:
            return render(request, 'home.html', {'error': str(e)})

    return render(request, 'home.html')

def retrieve(request):
    details=Details.objects.all()
    return render(request,'retrieve.html',{'details':details})

# def edit(request,id):
    
#     object=Details.objects.get(emp_id=id)
#     return render(request,'edit.html',{'object':object})

# def update(request,id):
#     object=Details.objects.get(emp_id=id)
#     form=detailsform(request.POST,instance=object)
#     if form.is_valid:
#         form.save()
#         object=Details.objects.all()
#         return redirect('retrieve')

def update(request, id):
    object = Details.objects.get(sr_no=id)
    form = detailsform(request.POST, instance=object)
    
    if form.is_valid():
        form.save()
        return redirect('retrieve')
    else:
        # If the form is not valid, render the edit template with the form and errors
        return render(request, 'edit.html', {'form': form, 'object': object})
def edit(request, id):
    object = Details.objects.get(sr_no=id)
    form = detailsform(instance=object)
    return render(request, 'edit.html', {'form': form, 'object': object})



def delete(request, id):  
    object=Details.objects.get(sr_no=id)
    object.delete()  
    return redirect("retrieve")  





 

