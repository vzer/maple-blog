#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# *************************************************************************
#   Copyright © 2015 JiangLin. All rights reserved.
#   File Name: index.py
#   Author:JiangLin
#   Mail:xiyang0807@gmail.com
#   Created Time: 2015-11-25 02:21:04
# *************************************************************************
from flask import (Blueprint, render_template)
from maple import cache
from maple.blog.models import Articles
from maple.question.models import Questions
from maple.admin.models import Notices
# from maple.blog.forms import SearchForm

site = Blueprint('index', __name__)


@site.route('/')
@site.route('/index')
@cache.cached(timeout=180)
def index():
    articles = Articles.query.limit(7)
    questions = Questions.query.filter_by(private=False).limit(7)
    notice = Notices.query.first()
    return render_template('index/index.html',
                           articles=articles,
                           questions=questions,
                           notice=notice)


@site.route('/about')
@cache.cached(timeout=180)
def about():
    return render_template('index/about_me.html')
