from django.db import models
from django.core.validators import MinValueValidator
from student.models import Student

class Course(models.Model):
    course_name = models.CharField(max_length=50, unique=True)
    question_number = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    total_marks = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.course_name

    class Meta:
        ordering = ['course_name']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    question = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    cat = (('Option1', 'Option1'), ('Option2', 'Option2'), ('Option3', 'Option3'), ('Option4', 'Option4'))
    answer = models.CharField(max_length=200, choices=cat)

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
        indexes = [
            models.Index(fields=['student']),
            models.Index(fields=['exam']),
        ]
