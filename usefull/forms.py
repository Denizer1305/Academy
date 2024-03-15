from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import SubmitField
from wtforms.validators import Email, DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[Email("Некорректный email")])
    psw = PasswordField("Пароль: ", validators=[DataRequired(), Length(min=4, max=100, message="Пароль должен содержать от 4 до 100 символов")])
    remember = BooleanField("Запомнить: ", default=False)
    submit = SubmitField("Войти")


class RegisterForm(FlaskForm):
    name = StringField("Имя: ", validators=[Length(min=4, max=30, message="Имя должен содержать от 4 до 30 символов")])
    email = StringField("Email: ", validators=[Email("Некорректный email")])
    psw = PasswordField("Пароль: ", validators=[DataRequired(), Length(min=4, max=100, message="Пароль должен содержать от 4 до 100 символов")])
    psw2 = PasswordField("Пароль: ", validators=[DataRequired(), EqualTo("psw2", message='Пароли должны совпадать')])
    submit = SubmitField("Регистрация")