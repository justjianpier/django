from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'posts'

class Comment(models.Model):
    post = models.ForeignKey(
        Post, # 1ero indicar con que model se encuentra relacionado
        on_delete=models.CASCADE, # 2do como queremos que se elimine cuando esté relacionado con la otra tabla
        db_column='post_id',# 3ro como querermos que se llame en la base de datos esta columna
        related_name='comments'# 4to para la relación inversa, qureremos recuperar estos comentarios desde el post con el nombre 'comments'
    )
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content
    
    class Meta:
        db_table = 'comments'
    