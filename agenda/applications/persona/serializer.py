from rest_framework import serializers
from .models import Person, Reunion, Hobby


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"


class PersonaSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()


class ReunionSerializer(serializers.ModelSerializer):

    persona = PersonSerializer()  #! Esto indica que se hará una relación de FK

    class Meta:
        model = Reunion
        fields = ("id", "fecha", "hora", "asunto", "persona")


# * Serializer para relaciones Many to Many
class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ("hobby",)


class PersonSerializer2(serializers.ModelSerializer):

    #! similar a la relación FK indicamos un serializador pero especificamos que es relación many=True
    hobby = HobbySerializer(many=True)

    class Meta:
        model = Person
        fields = ("id", "full_name", "job", "email", "phone", "hobby")




class ReunionSerializer2(serializers.ModelSerializer):


    class Meta:
        model = Reunion
        fields = ("id", "fecha", "hora", "asunto", "persona")
        
        
class CountReunionSerializer(serializers.Serializer):
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()