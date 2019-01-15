from django.db import models
from datetime import date

class blog(models.Model) :
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title
    
    def summary(self) :
        import re
        summary = self.body
        return " ".join(re.findall('^((?:\S+\s+){10}\S+).' , summary))
    
    def pub_date_pretty(self):
        return self.pub_date.strftime(' %b %e %Y ')
        
        
