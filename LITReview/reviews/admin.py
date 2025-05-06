from django.contrib import admin
from authentication.models import User
from reviews.models import Ticket, Review, UserFollows


admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(UserFollows)
admin.site.register(User)
