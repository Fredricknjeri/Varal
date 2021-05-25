from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django_object_actions import DjangoObjectActions
from .models import Mto, MalRequirements

# Register your models here.
admin.site.site_header = 'Varal Admin Dashboard'


# overide the model form
def publish_obj(obj):
    pass


class MalRequirementsAdmin(admin.ModelAdmin):
    fields = ['name_of_microtask',]
    list_display = ('name_of_microtask', 'status')

    actions = ['submit']


    def submit(self,request, queryset):
        # All requests here will actually be of type POST
        # so check for the special key 'apply'
        # rather than the actual request type
        if 'apply' in request.POST:
            # Perform update action:
            queryset.update(status="NEW_STATUS")

            self.message_user(request,
                              "Job posted on User page")
            return HttpResponseRedirect(request.get_full_path())

        return render(request,
                      'admin/submit_intermediate.html',
                      context={'submit':queryset})

    submit.short_description = "submit"

    # Solution to the The N+1 problem in ORMs
    list_select_related = (
        'name_of_microtask',
    )
    # efficient Solution to the The N+1 problem in ORMs for
    # readonly_fields = (
    #     'name_of_microtask',
    # )


# lists can be filtered using date when created
class MtoAdmin(admin.ModelAdmin):
    list_display = ('microtask', 'date')
    list_filter = ('date',)


admin.site.register(Mto, MtoAdmin)
admin.site.register(MalRequirements, MalRequirementsAdmin)
