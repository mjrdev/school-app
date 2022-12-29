from rest_framework import serializers
from schoolapi.models import Student, Course, Teacher, StudentOnCourse

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['id', 'name', 'cpf']

class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = ['id', 'title', 'description', 'teacher_id']

class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = ['id', 'name', 'cpf']

class StudentOnCourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = StudentOnCourse
    fields = ['id', 'course_id', 'student_id']

