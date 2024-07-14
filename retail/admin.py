from django.contrib import admin

from retail.models import Seller, Contact, Product

admin.site.register(Contact)
admin.site.register(Product)


class CityFilter(admin.SimpleListFilter):
    title = "Город"
    parameter_name = "city"

    def lookups(self, request, model_admin):
        return list(set([(contact.city, contact.city) for contact in Contact.objects.all()]))

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(
                pk__in=[contact.seller.pk for contact in Contact.objects.filter(city__exact=self.value())])
        else:
            return queryset


@admin.action(description="Списание задолженности")
def debt_write_off(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller_type', 'provider', 'debt', 'contact_city')
    list_filter = ('seller_type', CityFilter)
    actions = [debt_write_off]

    @admin.display(description="Город")
    def contact_city(self, obj):
        return list(set([contact.city for contact in Contact.objects.filter(seller=obj.pk)]))
