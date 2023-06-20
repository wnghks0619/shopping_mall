from django.db import models

class User(models.Model):
    email = models.EmailField(verbose_name='이메일') # 관리자 화면에서 좀더 편하게 한글화된 이름을 보도록 할게요.
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜') # 처음 객체가 생성된 날짜를 자연스럽게 지정하기 위해 auto_now_add로 지정해요.

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'my_user'
        verbose_name = '고객'
        verbose_name_plural = '고객'