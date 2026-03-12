from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, username=None, **extra_fields):
        if not phone_number:
            raise ValueError("Telefon raqami kiritilishi shart!")
        
        extra_fields.setdefault('username', username)  # None bo'lsa ham muammo yo'q
        
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, username=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('phone_verified', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser is_staff=True bo\'lishi kerak')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser is_superuser=True bo\'lishi kerak')

        return self.create_user(phone_number, password, username=username, **extra_fields)