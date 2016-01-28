from django.contrib import admin

from mainapp.models import Piece, Software, Skill

class PieceAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


admin.site.register(Piece, PieceAdmin)
admin.site.register(Skill)
admin.site.register(Software)