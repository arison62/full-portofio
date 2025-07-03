from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from .utils import generate_unique_filepath



def generate_profile_picture_path(instance, filename):
    return generate_unique_filepath(instance, filename, 'profile/')


def generate_banner_image_path(instance, filename):
    return generate_unique_filepath(instance, filename, 'banner/')

def generate_image_project_path(instance, filename):
    return generate_unique_filepath(instance, filename, 'project/')

def generate_logo_company_path(instance, filename):
    return generate_unique_filepath(instance, filename, 'company/')

class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=150, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to= generate_profile_picture_path, blank=True, null=True)
    banner_image = models.ImageField(upload_to= generate_banner_image_path, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, help_text='Slug will be generated automatically from User.username.')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)
    
   

    def __str__(self):
        return f"Profil {self.user.username}"

class SocialLink(models.Model):
    PLATFORMS_CHOICES = [
        ('github', 'Github'),
        ('linkedin', 'Linkedin'),
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('youtube', 'Youtube'),
        ('website', 'Site web'),
        ('other', 'Autre'),
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='social_links')
    name = models.CharField(max_length=100)
    link = models.URLField()
    platform = models.CharField(max_length=20, choices=PLATFORMS_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.profile.user.username})"

class Skill(models.Model):
    SKILL_TYPE_CHOISES = [
        ('language', 'Langage'),
        ('frontend', 'Front-end'),
        ('backend', 'Back-end'),
        ('database', 'Base de données'),
        ('tools', 'Outils'),
        ('platform', 'Plateforme'),
        ('other', 'Autre'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    skill_type = models.CharField(max_length=20, choices=SKILL_TYPE_CHOISES)

    class Meta:
        ordering = ['name']
    def __str__(self):
        return f"{self.name} ({self.profile.user.username})"

class Project(models.Model):
    PROJECT_TYPE_CHOISES = [
        ('personal', 'Personnel'),
        ('client', 'Client'),
    ]
    STATUS_CHOICES = [
        ('compled', 'Terminé'),
        ('in_progress', 'En cours'),
        ('planned', 'Planifié'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to=  generate_image_project_path, blank=True, null=True)
    technologies = models.ManyToManyField(Skill, related_name='projects', blank=True)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOISES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    demo_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)


    class Meta:
        ordering = ['-start_date', '-end_date']
    def __str__(self):
        return f"{self.name} ({self.profile.user.username})"


class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to= generate_logo_company_path, blank=True, null=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    is_current = models.BooleanField(default=False)
    

    class Meta:
        ordering = ['-start_date']
    def __str__(self):
        return f"{self.title} @ ({self.profile.user.username})"

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=200, verbose_name='Diplôme / Formation')
    institution = models.CharField(max_length=200)
    institution_logo = models.ImageField(upload_to= generate_logo_company_path, blank=True, null=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ['-end_date']
    def __str__(self):
        return f"{self.degree} @ ({self.profile.user.username})"