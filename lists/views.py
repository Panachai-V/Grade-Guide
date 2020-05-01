from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import GPA,Term


from lists.models import Userinfo

# เรียกไฟล์ home.html เพื่อทำการ render
def home_page(request):
    return render(request, 'home.html')

# เรียกไฟล์ picFlow.html เพื่อทำการ render โดยหน้า picFlow จะเป็นหน้ารูปของแผนผังวิชาต่างๆ
def pic_flow(request):
    return render(request, 'picFlow.html')

# เรียกไฟล์ about.html เพื่อทำการ render
def about(request):
    return render(request, 'about.html')

# เรียกไฟล์ help.html เพื่อทำการ render
def help(request):
    return render(request, 'help.html')

# ส่งจำนวนสมาชิกทั้งหมดเพื่อทำการ render
def user_count(request):

    # นับจำนวน user ทั้งหมดเพื่อดูว่าเว็บของเราเป็นทีนิยมขนาดไหน
    count = User.objects.count()
    return render(request, 'index.html', {
        'count': count
    })

# สมัครสมาชิกโดยการใช้ฟอร์มของ Django ที่มีมาให้
def sign_up(request):
    # เมือมีการมีการ POST
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # จะทำการเช็คว่ามี user นี้หรือยัง
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            Userinfo.objects.create(name=username)
            user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            dataGPA = GPA.objects.all()
            # เมื่อไม่มีข้อมูล GPA
            if len(dataGPA) == 0:
                # จะทำการสร้้างออบเจ็ค gpa ในแต่ละเทอมขึ้นมาเท่ากับ 0
                GPA.objects.create(GPA_1=0, GPA_2=0, GPA_3=0, GPA_4=0, GPA_5=0, GPA_6=0, GPA_7=0, GPA_8=0, )
            return redirect('home')
    # จะทำการใช้ UserCreationForm() โดยอัตโนมัติ เมื่อเข้าหน้า sign up
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

# ส่วนของหน้า grade calculator จะบันทึกเกรดโดยแก้ไขเกรด
def cal_grade(request):

    none_input_text = 'Plese check your infromation before saving.'
    check_input =float(request.POST.get('subject1Unit')) + float(request.POST.get('subject1Grade'))+\
                 float(request.POST.get('subject2Unit')) + float(request.POST.get('subject2Grade'))+\
                 float(request.POST.get('subject3Unit')) + float(request.POST.get('subject3Grade'))+\
                 float(request.POST.get('subject4Unit')) + float(request.POST.get('subject4Grade'))+\
                 float(request.POST.get('subject5Unit')) + float(request.POST.get('subject5Grade'))+\
                 float(request.POST.get('subject6Unit')) + float(request.POST.get('subject6Grade'))+\
                 float(request.POST.get('subject7Unit')) + float(request.POST.get('subject7Grade'))+\
                 float(request.POST.get('subject8Unit')) + float(request.POST.get('subject8Grade'))+\
                 float(request.POST.get('subject9Unit')) + float(request.POST.get('subject9Grade'))
    if len(Term.objects.all()) <= 100:
        # ถ้าผู้ใช้เลือกเทอมที่ 1
        if request.POST.get('subjectTerm') == '1':
            # ถ้าไม่ได้กรอกข้อมูลอะไรไปเลยจะแสดงผลเป็นคำว่า 'Plese check your infromation before saving.'
            if check_input == 0.0:
                return render(request, 'home.html', {'notinput': none_input_text})
            # คำนวณ GPA
            multi_subject_1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            multi_subject_2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            multi_subject_3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            multi_subject_4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            multi_subject_5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            multi_subject_6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            multi_subject_7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            multi_subject_8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            multi_subject_9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            sum_unit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit'))
            sum_multi_subject = multi_subject_1 + multi_subject_2 + multi_subject_3 + multi_subject_4 + multi_subject_5 + multi_subject_6 + multi_subject_7 + multi_subject_8 + multi_subject_9
            gpa = sum_multi_subject / sum_unit
            gpa_result = '%.2f' %gpa
            # บันทึกเกรด
            # บันทึกเกรด
            if len(Term.objects.filter(term="1")) == 0 :
                GPA.objects.update(GPA_1=gpa_result)
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject1name'],
                                    unit=request.POST['subject1Unit'], Grade=request.POST['subject1Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject2name'],
                                    unit=request.POST['subject2Unit'], Grade=request.POST['subject2Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject3name'],
                                    unit=request.POST['subject3Unit'], Grade=request.POST['subject3Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject4name'],
                                    unit=request.POST['subject4Unit'], Grade=request.POST['subject4Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject5name'],
                                    unit=request.POST['subject5Unit'], Grade=request.POST['subject5Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject6name'],
                                    unit=request.POST['subject6Unit'], Grade=request.POST['subject6Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject7name'],
                                    unit=request.POST['subject7Unit'], Grade=request.POST['subject7Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject8name'],
                                    unit=request.POST['subject8Unit'], Grade=request.POST['subject8Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject9name'],
                                    unit=request.POST['subject9Unit'], Grade=request.POST['subject9Grade'])
                return render(request, 'home.html',{'result':gpa_result})
            # แก้ไขเกรด
            else:
                Term.objects.filter(term="1").all().delete()
                GPA.objects.update(GPA_1=gpa_result)
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject1name'],
                                    unit=request.POST['subject1Unit'], Grade=request.POST['subject1Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject2name'],
                                    unit=request.POST['subject2Unit'], Grade=request.POST['subject2Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject3name'],
                                    unit=request.POST['subject3Unit'], Grade=request.POST['subject3Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject4name'],
                                    unit=request.POST['subject4Unit'], Grade=request.POST['subject4Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject5name'],
                                    unit=request.POST['subject5Unit'], Grade=request.POST['subject5Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject6name'],
                                    unit=request.POST['subject6Unit'], Grade=request.POST['subject6Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject7name'],
                                    unit=request.POST['subject7Unit'], Grade=request.POST['subject7Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject8name'],
                                    unit=request.POST['subject8Unit'], Grade=request.POST['subject8Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject9name'],
                                    unit=request.POST['subject9Unit'], Grade=request.POST['subject9Grade'])
                return render(request, 'home.html',{'result':gpa_result})

        # ถ้าผู้ใช้เลือกเทอมที่ 2
        if request.POST.get('subjectTerm') == '2':
            # ถ้าไม่ได้กรอกข้อมูลอะไรไปเลยจะแสดงผลเป็นคำว่า 'Plese check your infromation before saving.'
            if check_input == 0.0:
                return render(request, 'home.html', {'notinput': none_input_text})
            # คำนวณ GPA
            multi_subject_1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            multi_subject_2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            multi_subject_3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            multi_subject_4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            multi_subject_5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            multi_subject_6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            multi_subject_7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            multi_subject_8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            multi_subject_9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            sum_unit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit'))
            sum_multi_subject = multi_subject_1 + multi_subject_2 + multi_subject_3 + multi_subject_4 + multi_subject_5 + multi_subject_6 + multi_subject_7 + multi_subject_8 + multi_subject_9
            gpa = sum_multi_subject / sum_unit
            gpa_result = '%.2f' %gpa
            # บันทึกเกรด
            if len(Term.objects.filter(term="2")) == 0 :
                GPA.objects.update(GPA_2=gpa_result)
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject1name'],
                                    unit=request.POST['subject1Unit'], Grade=request.POST['subject1Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject2name'],
                                    unit=request.POST['subject2Unit'], Grade=request.POST['subject2Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject3name'],
                                    unit=request.POST['subject3Unit'], Grade=request.POST['subject3Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject4name'],
                                    unit=request.POST['subject4Unit'], Grade=request.POST['subject4Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject5name'],
                                    unit=request.POST['subject5Unit'], Grade=request.POST['subject5Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject6name'],
                                    unit=request.POST['subject6Unit'], Grade=request.POST['subject6Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject7name'],
                                    unit=request.POST['subject7Unit'], Grade=request.POST['subject7Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject8name'],
                                    unit=request.POST['subject8Unit'], Grade=request.POST['subject8Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject9name'],
                                    unit=request.POST['subject9Unit'], Grade=request.POST['subject9Grade'])
                return render(request, 'home.html',{'result':gpa_result})
            # แก้ไขเกรด
            else:
                Term.objects.filter(term="2").all().delete()
                GPA.objects.update(GPA_2=gpa_result)
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject1name'],
                                    unit=request.POST['subject1Unit'], Grade=request.POST['subject1Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject2name'],
                                    unit=request.POST['subject2Unit'], Grade=request.POST['subject2Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject3name'],
                                    unit=request.POST['subject3Unit'], Grade=request.POST['subject3Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject4name'],
                                    unit=request.POST['subject4Unit'], Grade=request.POST['subject4Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject5name'],
                                    unit=request.POST['subject5Unit'], Grade=request.POST['subject5Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject6name'],
                                    unit=request.POST['subject6Unit'], Grade=request.POST['subject6Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject7name'],
                                    unit=request.POST['subject7Unit'], Grade=request.POST['subject7Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject8name'],
                                    unit=request.POST['subject8Unit'], Grade=request.POST['subject8Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject9name'],
                                    unit=request.POST['subject9Unit'], Grade=request.POST['subject9Grade'])
                return render(request, 'home.html',{'result':gpa_result})

        # ถ้าผู้ใช้เลือกเทอมที่ 3
        if request.POST.get('subjectTerm') == '3':
            # ถ้าไม่ได้กรอกข้อมูลอะไรไปเลยจะแสดงผลเป็นคำว่า 'Plese check your infromation before saving.'
            if check_input == 0.0:
                return render(request, 'home.html', {'notinput': none_input_text})
            # คำนวณ GPA
            multi_subject_1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            multi_subject_2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            multi_subject_3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            multi_subject_4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            multi_subject_5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            multi_subject_6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            multi_subject_7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            multi_subject_8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            multi_subject_9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            sum_unit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit'))
            sum_multi_subject = multi_subject_1 + multi_subject_2 + multi_subject_3 + multi_subject_4 + multi_subject_5 + multi_subject_6 + multi_subject_7 + multi_subject_8 +multi_subject_9
            gpa = sum_multi_subject / sum_unit
            gpa_result = '%.2f' %gpa
            # บันทึกเกรด
            if len(Term.objects.filter(term="3")) == 0 :
                GPA.objects.update(GPA_3=gpa_result)
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject1name'],
                                    unit=request.POST['subject1Unit'], Grade=request.POST['subject1Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject2name'],
                                    unit=request.POST['subject2Unit'], Grade=request.POST['subject2Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject3name'],
                                    unit=request.POST['subject3Unit'], Grade=request.POST['subject3Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject4name'],
                                    unit=request.POST['subject4Unit'], Grade=request.POST['subject4Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject5name'],
                                    unit=request.POST['subject5Unit'], Grade=request.POST['subject5Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject6name'],
                                    unit=request.POST['subject6Unit'], Grade=request.POST['subject6Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject7name'],
                                    unit=request.POST['subject7Unit'], Grade=request.POST['subject7Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject8name'],
                                    unit=request.POST['subject8Unit'], Grade=request.POST['subject8Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject9name'],
                                    unit=request.POST['subject9Unit'], Grade=request.POST['subject9Grade'])
                return render(request, 'home.html',{'result':gpa_result})
            # แก้ไขเกรด
            else:
                Term.objects.filter(term="3").all().delete()
                GPA.objects.update(GPA_3=gpa_result)
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject1name'],
                                    unit=request.POST['subject1Unit'], Grade=request.POST['subject1Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject2name'],
                                    unit=request.POST['subject2Unit'], Grade=request.POST['subject2Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject3name'],
                                    unit=request.POST['subject3Unit'], Grade=request.POST['subject3Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject4name'],
                                    unit=request.POST['subject4Unit'], Grade=request.POST['subject4Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject5name'],
                                    unit=request.POST['subject5Unit'], Grade=request.POST['subject5Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject6name'],
                                    unit=request.POST['subject6Unit'], Grade=request.POST['subject6Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject7name'],
                                    unit=request.POST['subject7Unit'], Grade=request.POST['subject7Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject8name'],
                                    unit=request.POST['subject8Unit'], Grade=request.POST['subject8Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject9name'],
                                    unit=request.POST['subject9Unit'], Grade=request.POST['subject9Grade'])
                return render(request, 'home.html',{'result':gpa_result})

        # ถ้าผู้ใช้เลือกเทอมที่ 4
        if request.POST.get('subjectTerm') == '4':
            # ถ้าไม่ได้กรอกข้อมูลอะไรไปเลยจะแสดงผลเป็นคำว่า 'Plese check your infromation before saving.'
            if check_input == 0.0:
                return render(request, 'home.html', {'notinput': none_input_text})
            # คำนวณ GPA
            multi_subject_1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            multi_subject_2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            multi_subject_3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            multi_subject_4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            multi_subject_5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            multi_subject_6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            multi_subject_7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            multi_subject_8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            multi_subject_9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))
            sum_unit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit'))
            sum_multi_subject = multi_subject_1 + multi_subject_2 + multi_subject_3 + multi_subject_4 + multi_subject_5 + multi_subject_6 + multi_subject_7 + multi_subject_8 +multi_subject_9
            gpa = sum_multi_subject / sum_unit
            gpa_result = '%.2f' %gpa
            # บันทึกเกรด
            if len(Term.objects.filter(term="4")) == 0 :
                GPA.objects.update(GPA_4=gpa_result)
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject1name'],
                                    unit=request.POST['subject1Unit'], Grade=request.POST['subject1Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject2name'],
                                    unit=request.POST['subject2Unit'], Grade=request.POST['subject2Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject3name'],
                                    unit=request.POST['subject3Unit'], Grade=request.POST['subject3Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject4name'],
                                    unit=request.POST['subject4Unit'], Grade=request.POST['subject4Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject5name'],
                                    unit=request.POST['subject5Unit'], Grade=request.POST['subject5Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject6name'],
                                    unit=request.POST['subject6Unit'], Grade=request.POST['subject6Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject7name'],
                                    unit=request.POST['subject7Unit'], Grade=request.POST['subject7Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject8name'],
                                    unit=request.POST['subject8Unit'], Grade=request.POST['subject8Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject9name'],
                                    unit=request.POST['subject9Unit'], Grade=request.POST['subject9Grade'])
                return render(request, 'home.html',{'result':gpa_result})
            # แก้ไขเกรด
            else:
                Term.objects.filter(term="4").all().delete()
                GPA.objects.update(GPA_4=gpa_result)
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject1name'],
                                    unit=request.POST['subject1Unit'], Grade=request.POST['subject1Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject2name'],
                                    unit=request.POST['subject2Unit'], Grade=request.POST['subject2Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject3name'],
                                    unit=request.POST['subject3Unit'], Grade=request.POST['subject3Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject4name'],
                                    unit=request.POST['subject4Unit'], Grade=request.POST['subject4Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject5name'],
                                    unit=request.POST['subject5Unit'], Grade=request.POST['subject5Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject6name'],
                                    unit=request.POST['subject6Unit'], Grade=request.POST['subject6Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject7name'],
                                    unit=request.POST['subject7Unit'], Grade=request.POST['subject7Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject8name'],
                                    unit=request.POST['subject8Unit'], Grade=request.POST['subject8Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject9name'],
                                    unit=request.POST['subject9Unit'], Grade=request.POST['subject9Grade'])
                return render(request, 'home.html',{'result':gpa_result})

        # ถ้าผู้ใช้เลือกเทอมที่ 5
        if request.POST.get('subjectTerm') == '5':
            # ถ้าไม่ได้กรอกข้อมูลอะไรไปเลยจะแสดงผลเป็นคำว่า 'Plese check your infromation before saving.'
            if check_input == 0.0:
                return render(request, 'home.html', {'notinput': none_input_text})
            # คำนวณ GPA
            multi_subject_1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            multi_subject_2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            multi_subject_3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            multi_subject_4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            multi_subject_5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            multi_subject_6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            multi_subject_7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            multi_subject_8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            multi_subject_9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            sum_unit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit')
            )
            sum_multi_subject = multi_subject_1 + multi_subject_2 + multi_subject_3 + multi_subject_4 + multi_subject_5 + multi_subject_6 + multi_subject_7 + multi_subject_8 +multi_subject_9
            gpa = sum_multi_subject / sum_unit
            gpa_result = '%.2f' %gpa
            # บันทึกเกรด
            if len(Term.objects.filter(term="5")) == 0 :
                GPA.objects.update(GPA_5=gpa_result)
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject1name'],
                                    unit=request.POST['subject1Unit'], Grade=request.POST['subject1Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject2name'],
                                    unit=request.POST['subject2Unit'], Grade=request.POST['subject2Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject3name'],
                                    unit=request.POST['subject3Unit'], Grade=request.POST['subject3Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject4name'],
                                    unit=request.POST['subject4Unit'], Grade=request.POST['subject4Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject5name'],
                                    unit=request.POST['subject5Unit'], Grade=request.POST['subject5Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject6name'],
                                    unit=request.POST['subject6Unit'], Grade=request.POST['subject6Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject7name'],
                                    unit=request.POST['subject7Unit'], Grade=request.POST['subject7Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject8name'],
                                    unit=request.POST['subject8Unit'], Grade=request.POST['subject8Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject9name'],
                                    unit=request.POST['subject9Unit'], Grade=request.POST['subject9Grade'])
                return render(request, 'home.html',{'result':gpa_result})
            # แก้ไขเกรด
            else:
                Term.objects.filter(term="5").all().delete()
                GPA.objects.update(GPA_5=gpa_result)
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject1name'],
                                    unit=request.POST['subject1Unit'], Grade=request.POST['subject1Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject2name'],
                                    unit=request.POST['subject2Unit'], Grade=request.POST['subject2Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject3name'],
                                    unit=request.POST['subject3Unit'], Grade=request.POST['subject3Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject4name'],
                                    unit=request.POST['subject4Unit'], Grade=request.POST['subject4Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject5name'],
                                    unit=request.POST['subject5Unit'], Grade=request.POST['subject5Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject6name'],
                                    unit=request.POST['subject6Unit'], Grade=request.POST['subject6Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject7name'],
                                    unit=request.POST['subject7Unit'], Grade=request.POST['subject7Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject8name'],
                                    unit=request.POST['subject8Unit'], Grade=request.POST['subject8Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject9name'],
                                    unit=request.POST['subject9Unit'], Grade=request.POST['subject9Grade'])
                return render(request, 'home.html',{'result':gpa_result})

        # ถ้าผู้ใช้เลือกเทอมที่ 6
        if request.POST.get('subjectTerm') == '6':
            # ถ้าไม่ได้กรอกข้อมูลอะไรไปเลยจะแสดงผลเป็นคำว่า 'Plese check your infromation before saving.'
            if check_input == 0.0:
                return render(request, 'home.html', {'notinput': none_input_text})
            # คำนวณ GPA
            multi_subject_1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            multi_subject_2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            multi_subject_3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            multi_subject_4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            multi_subject_5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            multi_subject_6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            multi_subject_7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            multi_subject_8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            multi_subject_9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            sum_unit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit'))
            sum_multi_subject = multi_subject_1 + multi_subject_2 + multi_subject_3 + multi_subject_4 + multi_subject_5 + multi_subject_6 + multi_subject_7 + multi_subject_8 +multi_subject_9
            gpa = sum_multi_subject / sum_unit
            gpa_result = '%.2f' %gpa
            # บันทึกเกรด
            if len(Term.objects.filter(term="6")) == 0 :
                GPA.objects.update(GPA_6=gpa_result)
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject1name'],
                                    unit=request.POST['subject1Unit'], Grade=request.POST['subject1Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject2name'],
                                    unit=request.POST['subject2Unit'], Grade=request.POST['subject2Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject3name'],
                                    unit=request.POST['subject3Unit'], Grade=request.POST['subject3Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject4name'],
                                    unit=request.POST['subject4Unit'], Grade=request.POST['subject4Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject5name'],
                                    unit=request.POST['subject5Unit'], Grade=request.POST['subject5Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject6name'],
                                    unit=request.POST['subject6Unit'], Grade=request.POST['subject6Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject7name'],
                                    unit=request.POST['subject7Unit'], Grade=request.POST['subject7Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject8name'],
                                    unit=request.POST['subject8Unit'], Grade=request.POST['subject8Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject9name'],
                                    unit=request.POST['subject9Unit'], Grade=request.POST['subject9Grade'])
                return render(request, 'home.html',{'result':gpa_result})
            # แก้ไขเกรด
            else:
                Term.objects.filter(term="6").all().delete()
                GPA.objects.update(GPA_6=gpa_result)
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject1name'],
                                    unit=request.POST['subject1Unit'], Grade=request.POST['subject1Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject2name'],
                                    unit=request.POST['subject2Unit'], Grade=request.POST['subject2Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject3name'],
                                    unit=request.POST['subject3Unit'], Grade=request.POST['subject3Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject4name'],
                                    unit=request.POST['subject4Unit'], Grade=request.POST['subject4Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject5name'],
                                    unit=request.POST['subject5Unit'], Grade=request.POST['subject5Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject6name'],
                                    unit=request.POST['subject6Unit'], Grade=request.POST['subject6Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject7name'],
                                    unit=request.POST['subject7Unit'], Grade=request.POST['subject7Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject8name'],
                                    unit=request.POST['subject8Unit'], Grade=request.POST['subject8Grade'])
                Term.objects.create(term=request.POST['subjectTerm'], subject=request.POST['subject9name'],
                                    unit=request.POST['subject9Unit'], Grade=request.POST['subject9Grade'])
                return render(request, 'home.html',{'result':gpa_result})

        # ถ้าผู้ใช้เลือกเทอมที่ 7
        if request.POST.get('subjectTerm') == '7':
            # ถ้าไม่ได้กรอกข้อมูลอะไรไปเลยจะแสดงผลเป็นคำว่า 'Plese check your infromation before saving.'
            if check_input == 0.0:
                return render(request, 'home.html', {'notinput': none_input_text})
            # คำนวณ GPA
            multi_subject_1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            multi_subject_2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            multi_subject_3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            multi_subject_4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            multi_subject_5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            multi_subject_6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            multi_subject_7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            multi_subject_8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            multi_subject_9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            sum_unit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit'))
            sum_multi_subject = multi_subject_1 + multi_subject_2 + multi_subject_3 + multi_subject_4 + multi_subject_5 + multi_subject_6 + multi_subject_7 + multi_subject_8 +multi_subject_9
            gpa = sum_multi_subject / sum_unit
            gpa_result = '%.2f' %gpa
            # บันทึกเกรด
            if len(Term.objects.filter(term="7")) == 0 :
                GPA.objects.update(GPA_7=gpa_result)
                term_data = request.POST['subjectTerm']
                save_grade(request,term_data)
                return render(request, 'home.html',{'result':gpa_result})
            # แก้ไขเกรด
            else:
                Term.objects.filter(term="7").all().delete()
                GPA.objects.update(GPA_7=gpa_result)
                term_data = request.POST['subjectTerm']
                save_grade(request,term_data)
                return render(request, 'home.html',{'result':gpa_result})


        # ถ้าผู้ใช้เลือกเทอมที่ 8
        if request.POST.get('subjectTerm') == '8':
            # ถ้าไม่ได้กรอกข้อมูลอะไรไปเลยจะแสดงผลเป็นคำว่า 'Plese check your infromation before saving.'
            if check_input == 0.0:
                return render(request, 'home.html', {'notinput': none_input_text})
            # คำนวณ GPA
            multi_subject_1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
            multi_subject_2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
            multi_subject_3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
            multi_subject_4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
            multi_subject_5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
            multi_subject_6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
            multi_subject_7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
            multi_subject_8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
            multi_subject_9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))

            sum_unit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
                request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
                request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
                request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
                request.POST.get('subject9Unit'))
            sum_multi_subject = multi_subject_1 + multi_subject_2 + multi_subject_3 + multi_subject_4 + multi_subject_5 + multi_subject_6 + multi_subject_7 + multi_subject_8 +multi_subject_9
            gpa = sum_multi_subject / sum_unit
            gpa_result = '%.2f' %gpa

            # บันทึกเกรด
            if len(Term.objects.filter(term="8")) == 0 :
                GPA.objects.update(GPA_8=gpa_result)
                term_data = request.POST['subjectTerm']
                save_grade(request,term_data)
                return render(request, 'home.html', {'result': gpa_result})
            # แก้ไขเกรด
            else:
                Term.objects.filter(term="8").all().delete()
                GPA.objects.update(GPA_8=gpa_result)
                term_data = request.POST['subjectTerm']
                save_grade(request,term_data)
                return render(request, 'home.html', {'result': gpa_result})

        else:
            message = 'Please select term before saving grade'
            return render(request, 'home.html',{'message':message})



# รายละเอียดตัวต่อของวิชาต่างที่ผู้ใช้ต้องการทราบ
def flow(request):
    result = ''
    subjects = str(request.POST.get('searchFlow',''))
    if 'searchSubject' in request.POST :
        #1ProFund
        if subjects == "Programming Fundamental" :
            result = """Semister2 : Algorithms and Data Structures <br />
            Semister5 : Operating Systems"""
        #2MathI
        elif subjects == "Engineering Mathematics I" :
            result = """Semister2 : Math II <br />
            Semister3 : Statistics for Computer Engineer"""
        #3ComExplo
        elif subjects == "Computer Engineering Exploration" :
            result = "The subject hasn't other subjects to connect the flow"
        #4PhysicsI
        elif subjects == "Physics I" :
            result = "Semister2 : Physics II"
        #5PhyLabI
        elif subjects == "Physics Laboratory I" :
            result = "The subject hasn't other subjects to connect the flow"
        #6EnglishI
        elif subjects == "Language Elective Course I" :
            result = "Language Elective Course II"
        #7TableTennis
        elif subjects == "Physical Education Elective Course I" :
            result = "Physical Education Elective Course II"
        #8ManSo
        elif subjects == "Social Sciences Elective Course" :
            result = "The subject hasn't other subjects to connect the flow"
        #9Intro
        elif subjects == "Introduction to Engineer" :
            result = "The subject hasn't other subjects to connect the flow"
        #10Circuit
        elif subjects == "Electric Circuit Theory" :
            result = "Semister4 : Analog and Digital Electronics"
        #11CircuitLab
        elif subjects == "Electric Circuit Lab" :
            result = "The subject hasn't other subjects to connect the flow"
        #12Algo
        elif subjects == "Algorithms and Data Structure" :
            result = """Semister3 : Software Development Practice I <br />
            Semister5 : Computer Organization <br />
            Semister6 : Database Systems"""
        #13Work Ethics
        elif subjects == "Work Ethics" :
            result = "The subject hasn't other subjects to connect the flow"
        #14MathII
        elif subjects == "Engineering Mathematics II" :
            result = """Semister3 : Discrete Mathematics <br />
            Semister3 : Introduction to Signals and System"""
        #15PhysicsII
        elif subjects == "Physics II" :
            result = "The subject hasn't other subjects to connect the flow"
        #16PhyLab2
        elif subjects == "Physics Laboratory II" :
            result = "The subject hasn't other subjects to connect the flow"
        #17EnglishII
        elif subjects == "Language Elective Course II" :
            result = "Language Elective Course III"
        #18Basketball
        elif subjects == "Physical Education Elective Course II" :
            result = "The subject hasn't other subjects to connect the flow"
        #19Stat
        elif subjects == "Statistics for Computer Engineer" :
            result = "The subject hasn't other subjects to connect the flow"
        #20Signal
        elif subjects == "Introduction to Signals and System" :
            result = "The subject hasn't other subjects to connect the flow"
        #21Digital
        elif subjects == "Logic Design of Digital System" :
            result = """Semister3 : Digital System Design Laboratory <br />
            Semister4 : Computer Organization"""
        #22DigiLab
        elif subjects == "Digital System Design Laboratory" :
            result = "The subject hasn't other subjects to connect the flow"
        #23SoftwareI
        elif subjects == "Software Development Practice I" :
            result = "Semister4 : Software Development Practice II"
        #24Discrete Math
        elif subjects == "Discrete Mathematics" :
            result = "Semister6 : Database Systems"
        #25PhyLife
        elif subjects == "Science and Maths Elective I" :
            result = "Science and Maths Elective II"
        #26SoftwareII
        elif subjects == "Software Development Practice II" :
            result = "Semister5 : Software Engineering"
        #27NetworkI
        elif subjects == "Computer Networks I" :
            result = "Semister5 : Computer Networks II"
        #28ComOr
        elif subjects == "Computer Organization" :
            result = "Semister5 : Embedded System Design"
        #29Ubi
        elif subjects == "Ubiquitous Computing" :
            result = "The subject hasn't other subjects to connect the flow"
        #30Analog
        elif subjects == "Analog and Digital Electronics" :
            result = "Semister5 : Analog and Digital Electronics Lab"
        #31GenMath
        elif subjects == "Science and Maths Elective II" :
            result = "Science and Maths Elective III"
        #32SoftEng
        elif subjects == "Software Engineering" :
            result = "The subject hasn't other subjects to connect the flow"
        #33NetworkII
        elif subjects == "Computer Networks II" :
            result = "Semister6 : Computer Networks Lab"
        #34OS
        elif subjects == "Operating Systems" :
            result = "The subject hasn't other subjects to connect the flow"
        #35Embedded
        elif subjects == "Embedded System Design" :
            result = "Semister6 : Embedded System Design Laboratory"
        #36AnalogLab
        elif subjects == "Analog and Digital Electronics Lab" :
            result = "The subject hasn't other subjects to connect the flow"
        #37Language Elective III
        elif subjects == "Language Elective Course III" :
            result = "Language Elective Course IV"
        #38Database
        elif subjects == "Database Systems" :
            result = "The subject hasn't other subjects to connect the flow"
        #39NetworkLab
        elif subjects == "Computer Networks Lab" :
            result = "The subject hasn't other subjects to connect the flow"
        #40EmbeddedLab
        elif subjects == "Embedded System Design Laboratory" :
            result = "The subject hasn't other subjects to connect the flow"
        #41Language Elective IV
        elif subjects == "Language Elective Course IV" :
            result = "The subject hasn't other subjects to connect the flow"
        #42Computer Eng. Elective Course I
        elif subjects == "Computer Eng. Elective Course I" :
            result = "Computer Eng. Elective Course II"
        #43Computer Eng. Elective Course II
        elif subjects == "Computer Eng. Elective Course II" :
            result = "The subject hasn't other subjects to connect the flow"
        #44Humanities Elective Course I
        elif subjects == "Humanities Elective Course I" :
            result = "Humanities Elective Course II"
        #45ProjectI
        elif subjects == "Project I" :
            result = "Semister8 : Project II"
        #46Free Elective Course I
        elif subjects == "Free Elective Course I" :
            result = "Free Elective Course I"
        #47Humanities Elective Course II
        elif subjects == "Humanities Elective Course II" :
            result = "The subject hasn't other subjects to connect the flow"
        #48Computer Eng. Elective Course III
        elif subjects == "Computer Eng. Elective Course III" :
            result = "Computer Eng. Elective Course IV"
        #49Computer Eng. Elective Course IV
        elif subjects == "Computer Eng. Elective Course IV" :
            result = "The subject hasn't other subjects to connect the flow"
        #50ProjectII
        elif subjects == "Project II" :
            result = "The subject hasn't other subjects to connect the flow"
        #51Computer Eng. Seminar
        elif subjects == "Computer Eng. Seminar" :
            result = "The subject hasn't other subjects to connect the flow"
        #52Free Elective Course II
        elif subjects == "Free Elective Course II" :
            result = "The subject hasn't other subjects to connect the flow"
        #53Science and Maths Elective III
        elif subjects == "Science and Maths Elective III" :
            result = "The subject hasn't other subjects to connect the flow"
        #Other
        else :
            result = "The subject isn't in the flow"
    
    return render(request, 'flow.html',{'subjects':subjects, 'Result':result})

# รายวิชาในเทอมต่างๆ ตั้งแต่เทอมที่ 1 ถึง 8
def list_of_subject(request) :
    list_semister_1 = """ Programming Fundamental<br />
            Engineering Mathematics I<br />
            Computer Engineering Exploration<br />
            Physics I<br />
            Physics Laboratory I<br />
            Language Elective Course I<br />
            Physical Education Elective Course I<br />
            Social Sciences Elective Course<br />
            Introduction to Engineer<br />"""

    list_semister_2 = """Electric Circuit Theory<br />
            Electric Circuit Lab<br />
            Algorithms and Data Structure<br />
            Work Ethics<br />
            Engineering Mathematics II<br />
            Physics II<br />
            Physics Laboratory II<br />
            Language Elective Course II<br />
            Physical Education Elective Course II<br />"""

    list_semister_3 = """Statistics for Computer Engineer<br />
            Introduction to Signals and System<br />
            Logic Design of Digital System<br />
            Digital System Design Laboratory<br />
            Software Development Practice I<br />
            Discrete Mathematics<br />
            Science and Maths Elective I<br />"""

    list_semister_4 = """Software Development Practice II<br />
            Computer Networks I<br />
            Computer Organization<br />
            Ubiquitous Computing<br />
            Analog and Digital Electronics<br />
            Science and Maths Elective II<br />"""

    list_semister_5 = """Software Engineering<br />
            Computer Networks II<br />
            Operating Systems<br />
            Embedded System Design<br />
            Analog and Digital Electronics Lab<br />
            Language Elective Course III<br />"""

    list_semister_6 = """Database Systems<br />
            Computer Networks Lab<br />
            Embedded System Design Laboratory<br />
            Language Elective Course IV<br />
            Computer Eng. Elective Course I<br />
            Computer Eng. Elective Course II<br />
            Humanities Elective Course I<br />"""

    list_semister_7 = """Project I<br />
            Free Elective Course I<br />
            Humanities Elective Course II<br />
            Computer Eng. Elective Course III<br />
            Computer Eng. Elective Course IV<br />"""

    list_semister_8 = """Project II<br />
            Computer Eng. Seminar<br />
            Free Elective Course II<br />
            Science and Maths Elective III"""

    return render(request, 'subject.html', {'semister1':list_semister_1,'semister2':list_semister_2,'semister3':list_semister_3,'semister4':list_semister_4,'semister5':list_semister_5,'semister6':list_semister_6,'semister7':list_semister_7,'semister8':list_semister_8})

# ส่งค่า GPA ทุกเทอมไปให้หน้า Graph.html เพื่อแสดงผลออกมาเป็นกราฟ
def graph(request):
    data_gpa = GPA.objects.all()
    two_dec_gpax_result = return_gpax(data_gpa)
    return render(request, 'Graph.html', {'GPARES': data_gpa,'res_GPAX': two_dec_gpax_result})

# การแสดงเกรดและคำนวณ GPAX เทอมที่ 1
def first_term_result(request):
    data_gpa = GPA.objects.all()
    dataterm_1 = Term.objects.filter(term="1").all()
    two_dec_gpax_result = return_gpax(data_gpa)
    return render(request, 'firstTerm.html', {'dataterm1':dataterm_1,'GPARES':data_gpa,'res_GPAX': two_dec_gpax_result})

# การแสดงเกรดและคำนวณ GPAX เทอมที่ 2
def second_term_result(request):
    data_gpa = GPA.objects.all()
    dataterm_2 = Term.objects.filter(term="2").all()
    two_dec_gpax_result = return_gpax(data_gpa)
    return render(request, 'secondTerm.html', {'dataterm2':dataterm_2,'GPARES':data_gpa,'res_GPAX': two_dec_gpax_result})

# การแสดงเกรดและคำนวณ GPAX เทอมที่ 3
def third_term_result(request):
    data_gpa = GPA.objects.all()
    dataterm_3 = Term.objects.filter(term="3").all()
    two_dec_gpax_result = return_gpax(data_gpa)
    return render(request, 'thirdTerm.html', {'dataterm3':dataterm_3,'GPARES':data_gpa,'res_GPAX': two_dec_gpax_result})

# การแสดงเกรดและคำนวณ GPAX เทอมที่ 4
def fourth_term_result(request):
    data_gpa = GPA.objects.all()
    dataterm_4 = Term.objects.filter(term="4").all()
    two_dec_gpax_result = return_gpax(data_gpa)
    return render(request, 'fourthTerm.html', {'dataterm4':dataterm_4,'GPARES':data_gpa,'res_GPAX': two_dec_gpax_result})

# การแสดงเกรดและคำนวณ GPAX เทอมที่ 5
def fifth_term_result(request):
    data_gpa = GPA.objects.all()
    dataterm_5 = Term.objects.filter(term="5").all()
    two_dec_gpax_result = return_gpax(data_gpa)
    return render(request, 'fifthTerm.html', {'dataterm5':dataterm_5,'GPARES':data_gpa,'res_GPAX': two_dec_gpax_result})

# การแสดงเกรดและคำนวณ GPAX เทอมที่ 6
def sixth_term_result(request):
    data_gpa = GPA.objects.all()
    dataterm_6 = Term.objects.filter(term="6").all()
    two_dec_gpax_result = return_gpax(data_gpa)
    return render(request, 'sixthTerm.html', {'dataterm6':dataterm_6,'GPARES':data_gpa,'res_GPAX': two_dec_gpax_result})

# การแสดงเกรดและคำนวณ GPAX เทอมที่ 7
def seventh_term_result(request):
    data_gpa = GPA.objects.all()
    two_dec_gpax_result = return_gpax(data_gpa)
    dataterm_7 = Term.objects.filter(term="7").all()
    return render(request, 'seventhTerm.html', {'dataterm7':dataterm_7,'GPARES':data_gpa,'res_GPAX': two_dec_gpax_result})

# การแสดงเกรดและคำนวณ GPAX เทอมที่ 8
def eight_term_result(request):
    data_gpa = GPA.objects.all()
    two_dec_gpax_result = return_gpax(data_gpa)
    dataterm_8 = Term.objects.filter(term="8").all()
    return render(request, 'eightTerm.html', {'dataterm8':dataterm_8,'GPARES':data_gpa,'res_GPAX': two_dec_gpax_result})

# คำนวณ GPAX
def return_gpax(data):
    sum_gpa = 0
    countunit = 0
    for i in data:
        sum_gpa = float(i.GPA_1) + float(i.GPA_2) + float(i.GPA_3) + float(i.GPA_4) + float(i.GPA_5) + float(i.GPA_6) + float(i.GPA_7) + float(i.GPA_8)
    if sum_gpa > 0.0:
        for unit in data:
            if unit.GPA_1 != '0' :
                countunit+=1
            if unit.GPA_2 != '0' :
                countunit+=1
            if unit.GPA_3 != '0' :
                countunit+=1
            if unit.GPA_4 != '0' :
                countunit+=1
            if unit.GPA_5 != '0' :
                countunit+=1
            if unit.GPA_6 != '0' :
                countunit+=1
            if unit.GPA_7 != '0' :
                countunit+=1
            if unit.GPA_8 != '0' :
                countunit+=1
    else:
        countunit+=1
    result_gpax = float(sum_gpa) / float(countunit)
    two_dec_gpax = '%.2f' % result_gpax
    return two_dec_gpax

def save_grade(request,term_data):
    Term.objects.create(term=term_data, subject=request.POST['subject1name'],
                        unit=request.POST['subject1Unit'], Grade=request.POST['subject1Grade'])
    Term.objects.create(term=term_data, subject=request.POST['subject2name'],
                        unit=request.POST['subject2Unit'], Grade=request.POST['subject2Grade'])
    Term.objects.create(term=term_data, subject=request.POST['subject3name'],
                        unit=request.POST['subject3Unit'], Grade=request.POST['subject3Grade'])
    Term.objects.create(term=term_data, subject=request.POST['subject4name'],
                        unit=request.POST['subject4Unit'], Grade=request.POST['subject4Grade'])
    Term.objects.create(term=term_data, subject=request.POST['subject5name'],
                        unit=request.POST['subject5Unit'], Grade=request.POST['subject5Grade'])
    Term.objects.create(term=term_data, subject=request.POST['subject6name'],
                        unit=request.POST['subject6Unit'], Grade=request.POST['subject6Grade'])
    Term.objects.create(term=term_data, subject=request.POST['subject7name'],
                        unit=request.POST['subject7Unit'], Grade=request.POST['subject7Grade'])
    Term.objects.create(term=term_data, subject=request.POST['subject8name'],
                        unit=request.POST['subject8Unit'], Grade=request.POST['subject8Grade'])
    Term.objects.create(term=term_data, subject=request.POST['subject9name'],
                        unit=request.POST['subject9Unit'], Grade=request.POST['subject9Grade'])
