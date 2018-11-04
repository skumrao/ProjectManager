# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=20)
    course_name = models.CharField(max_length=50)
    dept_name = models.CharField(max_length=50)
    user = models.ForeignKey('CourseInstructor', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class CourseInstructor(models.Model):
    ci_id = models.CharField(primary_key=True, max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(unique=True, max_length=30, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    dept_name = models.CharField(max_length=40)
    contact = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_instructor'


class Project(models.Model):
    project_id = models.CharField(primary_key=True, max_length=20)
    project_name = models.CharField(max_length=50)
    project_idea = models.CharField(max_length=1000, blank=True, null=True)
    course = models.ForeignKey(Course, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectComment(models.Model):
    comment = models.CharField(max_length=1000, blank=True, null=True)
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_comment'


class ProjectReports(models.Model):
    report = models.CharField(max_length=1000)
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=True, null=True)
    report_id = models.CharField(primary_key=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'project_reports'


class Review(models.Model):
    review_id = models.CharField(primary_key=True, max_length=20)
    review_content = models.CharField(max_length=1000, blank=True, null=True)
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=True, null=True)
    reviewer = models.ForeignKey('Reviewer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class ReviewComment(models.Model):
    comment = models.CharField(max_length=1000, blank=True, null=True)
    review = models.ForeignKey(Review, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_comment'


class Reviewer(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(unique=True, max_length=40, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    contact = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviewer'


class Student(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    rollno = models.CharField(unique=True, max_length=7, blank=True, null=True)
    email = models.CharField(unique=True, max_length=50, blank=True, null=True)
    password = models.CharField(max_length=15, blank=True, null=True)
    contact = models.BigIntegerField(blank=True, null=True)
    student_id = models.CharField(primary_key=True, max_length=15)

    class Meta:
        managed = False
        db_table = 'student'


class Teammembers(models.Model):
    user = models.ForeignKey(Student, models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teammembers'
