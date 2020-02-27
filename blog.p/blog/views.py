from django.shortcuts import render
from . import models
import markdown,pygments


def index(request):
    entries = models.Entry.objects.all()      # index.html


    return render(request, 'blog/index.html', locals())


def detail(request, blog_id):
    entry = models.Entry.objects.get(id=blog_id)    # detail.html

    md = markdown.Markdown(extensions = [
        'markdown.extensions.extra',
        'markdown.extensions.highlight',    # codehilite' 高亮无效
        'markdown.extensions.toc',
    ])
    entry.body = md.convert(entry.body)
    entry.toc = md.toc
    entry.increase_visiting()


    return render(request, 'blog/detail.html', locals())