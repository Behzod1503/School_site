from rest_framework.filters import BaseFilterBackend
import coreapi


class DocSearchFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(
                name='key_word',
                location='query',
                required=True,
                type='str',
                description='Search docs by name',
            )
        ]
        return fields

    def filter_queryset(self, request, queryset, view):
        return queryset
