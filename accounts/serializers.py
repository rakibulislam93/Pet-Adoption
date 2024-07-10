from rest_framework import serializers
from django.contrib.auth.models import User



class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password']


    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password1 = self.validated_data['password']
        password2 = self.validated_data['confirm_password']


        if password1 != password2 :
            raise serializers.ValidationError('Two Password Does not Match')
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email Already exist')
        
        account = User(username=username,email=email,first_name=first_name,last_name=last_name)
        account.set_password(password1)
        account.is_active = False
        account.save()

        return account
    



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required=True)