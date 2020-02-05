import os
from django.core.mail import send_mail


os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


if __name__ == '__main__':

    send_mail(
        '来自www.droughts.com的测试邮件',
        '欢迎访问www.droughts.com，这里是涸泽书屋，专注于大学生二手书交易。',
        'droughts@sina.com',
        ['279978482@qq.com'],
    )