from django.db import models

class Order(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='사용자')
    # 유의할 것은 Foreign키의 필수 매개변수가 삭제될 경우 참조한 객체는 어떻게 할지를 결정하는 옵션이 on_delete에요.
    # 첫번째 인자는 settings앱에 등록된 user앱의 models.py의 User클래스를 사용하겠다는 의미에요.

    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name=['수량'])
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self): # 관리자 페이지에서 객체를 확인할때 속성값으로 받게되면 해당 값의 명이 출력되요. 아니면 이상한 `object`라는 명으로 출력되요.
        return self.user

    class Meta: # 관리자 페이지 설정
        db_table = 'my_order' # DB에 저장될 테이블 이름 지정
        verbose_name = '주문'
        verbose_name_plural = '주문'
        # 복수형 지정안하면 "주문s"가 되는데요. s붙이지 않기 위해서 그래요.