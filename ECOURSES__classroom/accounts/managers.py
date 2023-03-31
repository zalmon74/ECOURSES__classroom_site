from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """ Перегруженный менеджер для пользователя. 
    
    Добавлены новые обязательные поля: Имя, Фамилия, email

    Добавлен новый метод: создание администратора, который создает пользователя 
    с правами администратора (персонала)
    """

    def _create_user(self, email: str, password: str , first_name: str, 
                    second_name: str, surname: str = '', 
                    **extra_fields: dict):
        """ Создание пользователя

        Args:
            email (str): Email пользователя
            password (str): Пароль
            first_name (str): Имя пользователя
            second_name (str): Фамилия пользователя
            surname (str): Отчество пользователя. По умолчанию ' '.
            
        Returns:
            CustomUser: Созданная модель пользователя
        """
        if not email:
            raise ValueError('email - является обязательным полем')
        if not password:
            raise ValueError('password - является обязательным полем')
        if not first_name:
            raise ValueError('first_name - является обязательным полем')
        if not second_name:
            raise ValueError('second_name - является обязательным полем')
        
        email = self.normalize_email(email)
        
        user = self.model(email=email, first_name=first_name, 
                          second_name=second_name, surname=surname,
                          **extra_fields)
        
        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, email: str, password: str , first_name: str, 
                    second_name: str, surname: str = '', 
                    **extra_fields: dict):
        """ Создание обычного пользователя

        Args:
            email (str): Email пользователя
            password (str): Пароль
            first_name (str): Имя пользователя
            second_name (str): Фамилия пользователя
            surname (str): Отчество пользователя. По умолчанию ' '.

        Returns:
            CustomUser: Созданная модель пользователя
        """        
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        
        if extra_fields.get('is_staff') is not False:
            raise ValueError('Пользователь должен иметь is_staff=False')
        if extra_fields.get('is_superuser') is not False:
            raise ValueError('Пользователь должен иметь is_superuser=False')

        return self._create_user(
            email=email, 
            password=password, 
            first_name=first_name, 
            second_name=second_name, 
            surname=surname, 
            **extra_fields
        )
        
    def create_staff_user(self, email: str, password: str , first_name: str, 
                          second_name: str, surname: str = '', 
                          **extra_fields: dict):
        """ Создание администратора

        Args:
            email (str): Email администратора
            password (str): Пароль
            first_name (str): Имя администратора
            second_name (str): Фамилия администратора
            surname (str): Отчество администратора. По умолчанию ' '.

        Returns:
            CustomUser: Созданная модель администратора
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Администратор должен иметь is_staff=True')
        if extra_fields.get('is_superuser') is not False:
            raise ValueError('Администратор должен иметь is_superuser=False')
        
        return self._create_user(
            email=email, 
            password=password, 
            first_name=first_name, 
            second_name=second_name, 
            surname=surname, 
            **extra_fields
        )

    def create_superuser(self, email: str, password: str , first_name: str, 
                         second_name: str, surname: str = '', 
                         **extra_fields: dict):
        """ Создание суперпользователя

        Args:
            email (str): Email суперпользователя
            password (str): Пароль
            first_name (str): Имя суперпользователя
            second_name (str): Фамилия суперпользователя
            surname (str): Отчество суперпользователя. По умолчанию ' '.

        Returns:
            CustomUser: Созданная модель суперпользователя
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True')
        return self._create_user(
            email=email, 
            password=password, 
            first_name=first_name, 
            second_name=second_name, 
            surname=surname, 
            **extra_fields
        )
