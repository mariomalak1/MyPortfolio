from django.db import models

# Create your models here.

class Owner(models.Model):
	name = models.CharField(max_length = 100)
	Custom_image = models.ImageField(upload_to = "Media/Owner/OwnerPic")
	Age = models.IntegerField()
	Resume_url = models.CharField(max_length=250)
	description = models.TextField()

	def __str__(self):
		return self.name

class Contact(models.Model):
	Phone_number = models.CharField(max_length=11)
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

	def __str__(self):
		return self.owner.name + " : " + self.Phone_number 


def MainImageFilePathProject(self, fileName):
	return f"Media/Projects/{self.name}/Main_Image_{fileName}"

class Project(models.Model):
	name = models.CharField(max_length= 100, unique=True)
	date = models.DateField(null=True, blank=True)
	description = models.TextField()
	project_link = models.CharField(max_length=250, null=True, blank=True)
	source_code_link_github = models.CharField(max_length=250, null=True, blank=True)
	Main_image = models.ImageField(upload_to=MainImageFilePathProject)

	def __str__(self):
		return self.name


def ImageFilePathProject(self, fileName):
	return f"Media/Projects/{self.Project.name}/{fileName}"

class Image(models.Model):
	image_id = models.IntegerField(default=1)
	Project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name= "images")
	image = models.ImageField(upload_to=ImageFilePathProject)
	description = models.TextField(null=True, blank=True)

	class Meta:
		unique_together = (('image_id', 'Project'),)

	def __str__(self):
		return self.Project.name + " " + self.image.name

class Tag(models.Model):
	name = models.CharField(max_length=50)
	Project = models.ManyToManyField(Project)

	def __str__(self):
		return self.name
