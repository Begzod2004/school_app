from rest_framework import serializers
from .models import *
from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from account.api.v1.serializers import RegisterSerializer



class CourseSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Course)
    class Meta:
        model = Course
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()
    courses = CourseSerializer(many=True)

    class Meta:
        model = Teacher
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        user_type = self.context.get('request').data.get('user_type')
        if user_type != 'teacher':
            raise serializers.ValidationError("Only teacher can be created using this serializer")
        return attrs

    def create(self, validated_data):
        validated_data['is_teacher'] = True
        return super().create(validated_data)    



class ParentSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()
    children = serializers.StringRelatedField(many=True)

    class Meta:
        model = Parent
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        user_type = self.context.get('request').data.get('parent')
        if user_type != 'parent':
            raise serializers.ValidationError("Only parent can be created using this serializer")
        return attrs

    def create(self, validated_data):
        validated_data['is_parent'] = True
        return super().create(validated_data)      


class StudentSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()
    courses = CourseSerializer(many=True)
    teachers = TeacherSerializer(many=True)

    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        user_type = self.context.get('request').data.get('student')
        if user_type != 'student':
            raise serializers.ValidationError("Only student can be created using this serializer")
        return attrs

    def create(self, validated_data):
        validated_data['is_student'] = True
        return super().create(validated_data)       


class RegistrarSerializer(serializers.ModelSerializer):
    user = RegisterSerializer()

    class Meta:
        model = Registrar
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        user_type = self.context.get('request').data.get('registrar')
        if user_type != 'registrar':
            raise serializers.ValidationError("Only registrar can be created using this serializer")
        return attrs

    def create(self, validated_data):
        validated_data['is_registrar'] = True
        return super().create(validated_data)    


class ClassSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    student = StudentSerializer()
    course = CourseSerializer()

    class Meta:
        model = Class
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Lesson
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()
    student = StudentSerializer()

    class Meta:
        model = Attendance
        fields = '__all__'
        
class PaymentSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    course = CourseSerializer()

    class Meta:
        model = Payment
        fields = '__all__'


       
class InvoiceSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    course = CourseSerializer()

    class Meta:
        model = Invoice
        fields = '__all__'
