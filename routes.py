import os
from flask import Blueprint, render_template
from flask import current_app as app

import datetime

main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

routeMinuteCount = datetime.datetime.now().minute


@main_bp.route("/")
def home():
    """Landing page."""
    default_title = 'Dashboard-Prototype',
    default_template = 'home-template',
    default_style_frame = """ #mainFrame {width:90vw; 
                               height:80vh; 
                               margin:0;
                               padding:0;
                               border:0 none;
                               box-sizing:border-box;}"""
    video_style_frame = """ #mainFrame {width:90vw;
                               height:80vh; 
                               margin:0;
                               padding:0;
                               border:0 none;
                               box-sizing:border-box;}"""
    # videoEmbedWidth = "1280px"
    # videoEmbedHeight = "720px"
    ten_minutes = 6000
    twenty_minutes = 12000

    if routeMinuteCount <= 20:
        return render_template('index.html',
                               title=default_title,
                               template=default_template,
                               styleFrame=video_style_frame,
                               timerSet=twenty_minutes,
                               iframePointer='https://www.youtube.com/embed/NvqKZHpKs-g?autoplay=1',
                               body="This is a demonstration of flask, first twenty minutes display")
    elif 20 < routeMinuteCount <= 30:
        return render_template('index.html',
                               title=default_title,
                               template=default_template,
                               styleFrame=video_style_frame,
                               timerSet=ten_minutes,
                               iframePointer='https://www.youtube.com/embed/EEIk7gwjgIM?autoplay=1',
                               body="This is a demonstration of flask, bottom of the hour display")
    elif 35 < routeMinuteCount <= 50:
        return render_template('index.html',
                               title=default_title,
                               template=default_template,
                               styleFrame=default_style_frame,
                               timerSet=twenty_minutes,
                               iframePointer='https://www.youtube.com/embed/k3LsmjrMPGs?autoplay=1',
                               body="Three-quarters hour display")
    else:
        return render_template('index.html',
                               title=default_title,
                               template=default_template,
                               styleFrame=default_style_frame,
                               iframePointer='https://www.weather.gov/shv/',
                               timerSet=ten_minutes,
                               body="This is a demonstration of flask, weather display")


# @main_bp.route('/')

@main_bp.route('/dashboards')
def tableOfContents():
    """Directory"""
    return render_template('directory.html',
                           title='Dashboard/pi-prototype-directory',
                           template='directory-template',
                           flaskDocumentationLink='https://flask.palletsprojects.com/en/1.1.x/',
                           tutorialForJinjaAsyncLink='https://jinja.palletsprojects.com/en/2.10.x/api/',
                           jinjaDescriptor='This is a guide to using HTML generation in the Jinja2 template engine',
                           fastAPIDescriptor='This is a link to documentation for flask.')
