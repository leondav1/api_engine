from django.contrib import admin

from .models import Worker, Store, Visit


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    search_fields = ['title']


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    search_fields = ['store__title', 'store__worker__name']
    readonly_fields = ('visited_at', )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass
