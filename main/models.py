from django.db import models

from datetime import datetime, timedelta

import re
import os
from user.models import User
def category_directory_path(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return 'category/'+re.sub('[-:. ]','',str(datetime.today()))+file_extension

class Category(models.Model):
    name = models.CharField(max_length=100, null=False)
    name_ar = models.CharField(max_length=100, null=False)
    category_banner = models.ImageField(upload_to=category_directory_path, null=True, blank=True)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE ,related_name="category_parent" ,null = True, blank = True)
    
    
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name