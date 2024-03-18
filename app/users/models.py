from typing import Any
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, 
                                        PermissionsMixin, 
                                        UserManager,
                                        BaseUserManager)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수입니다.')

        user = self.model(email=self.normalize_email(email=email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
        

class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255, null=True)
    is_bussiness = models.BooleanField(default=False)

    # PermissionMixin : 권한관리
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager() # 유저를 생성 및 관리 ( 일반 계정 과 관리자 계정 ㄱ분)

    def __str__(self) :
        return f'email : {self.email}, nickname : {self.nickname} '