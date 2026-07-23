from rest_framework import serializers
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)


    class Meta:
        model = Movie
        fields = [
            "id", "title", "slug", "description",
            "genres",
        ]

    # def get_poster(self, obj):
    #     if obj.poster:
    #         request = self.context.get("request")
    #
    #         return request.build_absolute_uri(url) if request else url
    #     return None