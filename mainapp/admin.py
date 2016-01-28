from django.contrib import admin

from mainapp.models import Piece, Software

class PieceAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


admin.site.register(Piece, PieceAdmin)
admin.site.register(Software)