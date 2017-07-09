# -*- coding: utf-8 -*- 

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from ..models import Role, User


class NameForm(FlaskForm):
    name = StringField(u'您的名字？', validators=[Required()])
    submit = SubmitField(u'提交')


class EditProfileForm(FlaskForm):
    name = StringField(u'真实姓名', validators=[Length(0, 64)])
    location = StringField(u'身在何处', validators=[Length(0, 64)])
    about_me = TextAreaField(u'社交标签')
    submit = SubmitField(u'确认修改')


class EditProfileAdminForm(FlaskForm):
    email = StringField(u'您的邮箱', validators=[Required(), Length(1, 64),
                                             Email()])
    username = StringField(u'您的昵称', validators=[
        Required(), Length(1, 64)])
    confirmed = BooleanField(u'确定')
    role = SelectField('Role', coerce=int)
    name = StringField(u'真实姓名', validators=[Length(0, 64)])
    location = StringField(u'身在何方', validators=[Length(0, 64)])
    about_me = TextAreaField(u'社交标签')
    submit = SubmitField(u'确定')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError(u'这个邮箱已经被注册过了')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError(u'这个昵称已经被注册过了')


class PostForm(FlaskForm):
    body = TextAreaField(u"今天想到了什么？", validators=[Required()])
    submit = SubmitField(u'发布')
