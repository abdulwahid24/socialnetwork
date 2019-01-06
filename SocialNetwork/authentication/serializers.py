from rest_framework import serializers

from authentication.models import User


class SignUpSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField()
    # password = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        if password:
            user.set_password(password)
            user.is_staff = True
            user.save()
        return user
