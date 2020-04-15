from django.test import TestCase
from django.contrib.auth.models import User
from lists.models import Userinfo,Term1,Term2,Term3,Term4,Term5,Term6,Term7,Term8,GPA

class HomePageTest(TestCase):
    # การทดสอบว่าหน้า template ที่เรียกใช้ยังเป็นหน้า base.html
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'base.html')

class SignUpTest(TestCase):
    # การทดสอบว่าผู้ใช้งานสามารถสมัครสมาชิกได้
    def test_user_signup(self):
        self.example_user = User.objects.create_user(username='Panachai', password='mypasswordisveryeasy',
                                                     email='panachai@test.com')
        self.example_user.save()

        example_users = User.objects.all()
        self.assertEqual(example_users.count(), 1)

    # การทดสอบว่าผู้ใช้งานหลายคนสามารถสมัครสมาชิกได้
    def test_many_users_signup(self):
        self.example_user1 = User.objects.create_user(username='Panachai', password='Panachaipasswordisveryeasy',
                                                      email='panachai@test.com')
        self.example_user1.save()
        self.example_user2 = User.objects.create_user(username='Kristamet', password='Kristametpasswordisveryeasy',
                                                      email='Kristamet@test.com')
        self.example_user2.save()
        self.example_user3 = User.objects.create_user(username='Nutnicha', password='Nutnichapasswordisveryeasy',
                                                      email='Nutnicha@test.com')
        self.example_user3.save()
        self.example_user4 = User.objects.create_user(username='Watsawat', password='Watsawatpasswordisveryeasy',
                                                      email='Watsawat@test.com')
        self.example_user4.save()

        example_users = User.objects.all()
        self.assertEqual(example_users.count(), 4)

class LogInTest(TestCase):
    # การทดสอบว่าผู้ใช้งานสามารถลงทะเบียนเข้าใช้ได้
    def test_user_login(self):
        User.objects.create_user(username='Panachai', password='Panachaipasswordisveryeasy')
        self.client.login(username="Panachai", password="Panachaipasswordisveryeasy")

class GradeCalTest(TestCase):
    # การทดสอบว่าหน้า grade calculator สามารถบันทึกข้อมูลเทอมแรกได้
    def test_gradeCal_can_save_first_term_data(self):
        example_user = Userinfo.objects.create(name='example_user ')
        example_data = Term1.objects.create(subject='example_subject', unit='1', Grade='A')
        example_user.term1.add(example_data)
        user = Userinfo.objects.all()
        example_saved_user = user[0]
        self.assertEqual(example_saved_user.term1.first().subject, 'example_subject')
        self.assertEqual(example_saved_user.term1.first().unit, '1')
        self.assertEqual(example_saved_user.term1.first().Grade, 'A')

    # การทดสอบว่าหน้า grade calculator สามารถบันทึกข้อมูลทุกเทอมได้
    def test_gradeCal_can_save_all_term_data(self):
        example_user = Userinfo.objects.create(name='example_user ')
        example_data1 = Term1.objects.create(subject='example_subject1', unit='1', Grade='A')
        example_data2 = Term2.objects.create(subject='example_subject2', unit='2', Grade='B+')
        example_data3 = Term3.objects.create(subject='example_subject3', unit='3', Grade='B')
        example_data4 = Term4.objects.create(subject='example_subject4', unit='4', Grade='C')
        example_data5 = Term5.objects.create(subject='example_subject5', unit='5', Grade='C+')
        example_data6 = Term6.objects.create(subject='example_subject6', unit='6', Grade='D')
        example_data7 = Term7.objects.create(subject='example_subject7', unit='7', Grade='D+')
        example_data8 = Term8.objects.create(subject='example_subject8', unit='8', Grade='F')

        example_user.term1.add(example_data1)
        example_user.term2.add(example_data2)
        example_user.term3.add(example_data3)
        example_user.term4.add(example_data4)
        example_user.term5.add(example_data5)
        example_user.term6.add(example_data6)
        example_user.term7.add(example_data7)
        example_user.term8.add(example_data8)

        user = Userinfo.objects.all()
        example_saved_user = user[0]

        self.assertEqual(example_saved_user.term1.first().subject, 'example_subject1')
        self.assertEqual(example_saved_user.term2.first().subject, 'example_subject2')
        self.assertEqual(example_saved_user.term3.first().subject, 'example_subject3')
        self.assertEqual(example_saved_user.term4.first().subject, 'example_subject4')
        self.assertEqual(example_saved_user.term5.first().subject, 'example_subject5')
        self.assertEqual(example_saved_user.term6.first().subject, 'example_subject6')
        self.assertEqual(example_saved_user.term7.first().subject, 'example_subject7')
        self.assertEqual(example_saved_user.term8.first().subject, 'example_subject8')

    # การทดสอบว่าหน้า grade calculator สามารถบันทึก GPA ได้
    def test_gradeCal_can_save_GPA(self):
        example_user = Userinfo.objects.create(name='example_user ')
        example_GPA_data = GPA.objects.create(GPA_1 = "4",GPA_2 = "3.5",GPA_3 = "3",GPA_4 = "2.5",GPA_5 = "2",GPA_6 = "1.5",GPA_7 = "1",GPA_8 = "0.5")
        example_user.gpa.add(example_GPA_data)
        user = Userinfo.objects.all()
        example_saved_user = user[0]
        self.assertEqual(example_saved_user.gpa.first().GPA_1, '4')
        self.assertEqual(example_saved_user.gpa.first().GPA_2, '3.5')
        self.assertEqual(example_saved_user.gpa.first().GPA_3, '3')
        self.assertEqual(example_saved_user.gpa.first().GPA_4, '2.5')
        self.assertEqual(example_saved_user.gpa.first().GPA_5, '2')
        self.assertEqual(example_saved_user.gpa.first().GPA_6, '1.5')
        self.assertEqual(example_saved_user.gpa.first().GPA_7, '1')
        self.assertEqual(example_saved_user.gpa.first().GPA_8, '0.5')

