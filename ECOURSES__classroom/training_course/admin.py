from django.contrib import admin
from django.utils.safestring import SafeText
from rangefilter.filters import DateRangeFilterBuilder

from .models import *


@admin.register(Category)
class CategoryAdminModel(admin.ModelAdmin):
    
    def category_photo_image(self, obj) -> SafeText:
        return obj.image_tag()
    
    list_display = ('id', 'name', 'name_visible', 'category_photo_image')
    list_display_links = ('name', 'name_visible', 'category_photo_image')
    
    search_fields = ('name', 'name_visible')
    
    category_photo_image.short_description = 'Изображение категории'


@admin.register(Tag)
class TagAdminModel(admin.ModelAdmin):
    
    list_display = ('id', 'name', 'name_visible')
    list_display_links = ('name', 'name_visible')
    
    search_fields = ('name', 'name_visible')


class MoreInformationAboutCoursesInline(admin.StackedInline):
    model = MoreInformationAboutCourses
    
    fields = ['description', 'course_program']
    readonly_fields = ['description', 'course_program']


@admin.register(TrainingCourseModel)
class TrainingCourseAdminModel(admin.ModelAdmin):
    
    list_display = (
        'id', 
        'name', 
        'author', 
        'category', 
        'f_stop', 
        'datetime_course_start', 
        'datetime_course_end',
    )
    list_display_links = ('name', 'author', 'category')

    fieldsets = (
        ('Информация о курсе', {'fields': ('photo', 'name', 'author', 'category', 'tags', 'price', 'f_stop',)}),
        ('Учителя', {'fields': ('max_count_teachers', 'teachers')}),
        ('Студенты', {'fields': ('max_count_students', 'students')}),
        ('Даты', {'fields': ('datetime_course_start', 'datetime_course_end', 'created')}),
    )
    
    readonly_fields = [el.name for el in TrainingCourseModel._meta.fields] + \
                      [el.name for el in TrainingCourseModel._meta.many_to_many]
    
    list_filter = (
        ('datetime_course_start', DateRangeFilterBuilder()),
        ('datetime_course_end', DateRangeFilterBuilder()),
        'f_stop',
        'category',
        'tags',
    )
    search_fields = (
        'name', 
        'author__first_name', 'author__second_name', 'author__last_name',
        'category__name', 'category__name_visible',
        'tags__name', 'tags__name_visible',
    )
    
    inlines = [MoreInformationAboutCoursesInline, ]
                          
    def has_add_permission(self, request):
        return False


@admin.register(ReviewCourse)
class ReviewCourseAdminModel(admin.ModelAdmin):
    
    list_display = ['id', 'course', 'author', 'grade', 'f_deleted', 'updated', 'created',]
    list_display_links = ['course', 'author', 'grade',]
    
    readonly_fields = [el.name for el in ReviewCourse._meta.fields] + \
                      [el.name for el in ReviewCourse._meta.many_to_many]
    
    list_filter = [
        ('updated', DateRangeFilterBuilder()),
        ('created', DateRangeFilterBuilder()),
        'f_deleted',
        'grade',
    ]
    search_fields = ['corse', 'author', 'grade',]

    def has_add_permission(self, request):
        return False
