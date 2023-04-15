from django.contrib import admin
from django.utils.safestring import SafeText

# from .help_functions import get_html_user_photo
from .models import CustomUser, UserPhoto


class UserPhotoInline(admin.StackedInline):
    model = UserPhoto
    
    fields = ['image_tag', ]
    readonly_fields = ['image_tag', ]
    
    insert_after = 'surname'
    

@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    """ Отобржанеие модели "пользователи" в админ-панели
    """
    
    def userphoto_image_tag(self, obj) -> SafeText:
        return obj.userphoto.image_tag()
    
    list_display = (
        'id', 
        'userphoto_image_tag',
        'email', 
        'mail_confirmation', 
        'first_name', 
        'second_name', 
        'surname',
        'is_staff',
    )
    list_display_links = (
        'userphoto_image_tag',
        'email', 
        'first_name',
        'second_name', 
        'surname'
    )
    
    fieldsets = (
        ('Данные для авторизации', {'fields': ('email', 'password')}),
        (
            'Персональная информация', 
            {'fields': (
                'first_name', 
                'second_name', 
                'surname', 
                'mail_confirmation',
                'url_vk',
                'url_email',
                'url_github',
            )}
        ),
        ('Права доступа', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = (
        'password', 
        'mail_confirmation', 
        'last_login', 
        'date_joined',
        'url_vk',
        'url_email',
        'url_github',
    )
    
    list_filter = ('mail_confirmation', 'is_staff')
    search_fields = ('email', 'first_name', 'second_name', 'surname')
    
    userphoto_image_tag.short_description = 'Фото'
    
    inlines = [UserPhotoInline, ]
    
    change_form_template = 'admin/custom/change_form.html'

    class Media:
        css = {
            'all': (
                'css/admin.css',
            )
        }


@admin.register(UserPhoto)
class AdminUserPhoto(admin.ModelAdmin):
    """ Отобржанеие модели "фото пользователей" в админ-панели
    """
    list_display = ('id', 'user', 'image_tag')
    list_display_links = ('id', 'user', 'image_tag')
    readonly_fields = ('id', 'user', 'image_tag')
    exclude = ('photo', )
    
