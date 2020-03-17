import os
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# if __name__ == '__main__':

    # send_mail(
    #     '来自测试邮件',
    #     'This is Test email ,dont reply.',
    #     '10shadow@163.com',
    #     ['16shadow@163.com'],
    # )


    # subject, from_email, to = '来自www.blog.com', '10shadow@163.com', '16shadow@163.com'
    # text_content = 'www.log.com，'
    # html_content = '<p>访问<a href="http://www.blog.com" target=blank>www.blog.com</a>，这里是点</p>'
    # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    # msg.attach_alternative(html_content, "text/html")
    # msg.send()