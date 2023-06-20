from django import forms
from user.models import User

class RegisterForm(forms.Form): # forms.Form을 상속받아요.
    email = forms.EmailField(
        error_messages={    # 입력하지 않을시 생성되는 오류 메시지
        'required': '이메일을 입력해주세요'
        },
        max_length=64,
        label='이메일',
    )
    password = forms.CharField(
        error_messages={
            'required':'비밀번호를 입력하세요'
        },
        widget=forms.PasswordInput, # 추측컨데 비밀번호 입력 요건을 갖춘 입력방식이 될듯함.
        label='비밀번호'            # 라벨 이름을 표기함.
    )
    re_password = forms.CharField(
        error_messages={
            'required':'비밀번호를 입력하세요'
        },
        widget=forms.PasswordInput,
        label='비밀번호'
    )

    def clean(self): # validation을 진행하는 메서드
        cleaned_data = super().clean() # 부모 클래스에서 갖고 있던 clean을 상속 받아요.
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password: # 비밀번호 입력란 2개가 입력되어야하고
            if password != re_password: # 2개가 입력되었지만 서로 다른 경우 오류 메시지를 출력하도록함.
                self.add_error('password', '비밀번호가 서로 다릅니다.')
                self.add_error('re_password', '비밀번호가 서로 다릅니다.')
            else:
                user = User(
                email = email,
                password=password,
                )
                user.save() # db저장