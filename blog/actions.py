from django.contrib import messages


def activate_coupon(modeladmin, request, queryset): 
    activated = queryset.filter(
        is_activated=False).update(is_activated=True)
    
    messages.success(
        request, "{} coupons have been activated successfully.\
            ".format(activated)
    )


activate_coupon.short_description = "Activate Selected Coupons" 
