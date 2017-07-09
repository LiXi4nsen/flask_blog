# -*- coding: utf-8 -*- 

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User




class LoginForm(FlaskForm):
    email = StringField(u'您的邮箱', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField(u'您的密码', validators=[Required()])
    remember_me = BooleanField(u'下次自动登陆')
    submit = SubmitField(u'登陆')


class RegistrationForm(FlaskForm):
    email = StringField(u'您的邮箱', validators=[Required(), Length(1, 64),
                                           Email()])
    username = StringField(u'您的昵称', validators=[
        Required(), Length(1, 64)])
    password = PasswordField(u'您的密码', validators=[
        Required(), EqualTo('password2', message=u'两次输入的密码必须一致')])
    password2 = PasswordField(u'请再次输入密码', validators=[Required()])
    submit = SubmitField(u'注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'这个邮箱已经注册过了')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'这个昵称已经被使用了')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(u'旧密码', validators=[Required()])
    password = PasswordField(u'新密码', validators=[
        Required(), EqualTo('password2', message=u'请确认旧密码输入无误')])
    password2 = PasswordField('请再次输入新密码', validators=[Required()])
    submit = SubmitField(u'确认修改')
    
class PasswordResetRequestForm(FlaskForm):
    email = StringField(u'您的邮箱', validators=[Required(), Length(1, 64),
                                             Email()])
    submit = SubmitField(u'确认重置')


class PasswordResetForm(FlaskForm):
    email = StringField(u'您的邮箱', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField(u'新密码', validators=[
        Required(), EqualTo('password2', message=u'两次输入的密码必须一致')])
    password2 = PasswordField(u'请再次输入密码', validators=[Required()])
    submit = SubmitField(u'确认重置')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError(u'请邮箱格式无误')
