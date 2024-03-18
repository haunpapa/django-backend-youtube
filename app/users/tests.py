from django.test import TestCase
from django.contrib.auth import get_user_model



# TDD (User 관련 테스트)
# TDD : Test Driven Development

class UserTestCase(TestCase):
    # 일반 유저 생성테스트
    def test_create_user(self):
        email = 'good78912@gmail.com'
        password = '1234'

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        # self.assertEqual(user.check_password(password), True)
        self.assertTrue(user.check_password(password))
        # self.assertEqual(user.is_superuser, False)
        self.assertFalse(user.is_superuser)

    # docker-compose run --rm app sh -c 'python manage.py test users'


    # 관리자 유저 생성 테스트
    def test_create_superuser(self):
        email = 'good78912@gmail.com'
        password = '1234'

        super_user = get_user_model().objects.create_superuser(email=email, password=password)

        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)

        