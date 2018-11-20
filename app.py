from flask import Flask,render_template,request,redirect,url_for
from random import choice
from flask_bootstrap import Bootstrap
from .forms import  CForm


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']='aaaa'
zikabaobao = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/list',methods=['GET','POST'])
def list():
    from zika import c01,c02
    global zikabaobao
    zikabaobao = c01 + c02
    return render_template('list.html', list_result=zikabaobao)


@app.route('/cho', methods=['GET', 'POST'])
def cho():
    from zika import a01,a02,a03,a04,a05,a06,a07,a08,a09,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30
    from zika import c01,c02,c03,c04,c05,c06,c07,c08,c09
    global zikabaobao
    form = CForm()
    if form.validate_on_submit():
        if form.c01.data == True:
            zikabaobao = zikabaobao + c01
        if form.c02.data == True:
            zikabaobao = zikabaobao + c02
        if form.c03.data == True:
            zikabaobao = zikabaobao + c03
        if form.c04.data == True:
            zikabaobao = zikabaobao + c04
        if form.c05.data == True:
            zikabaobao = zikabaobao + c05
        if form.c06.data == True:
            zikabaobao = zikabaobao + c06
        if form.c07.data == True:
            zikabaobao = zikabaobao + c07
        if form.c08.data == True:
            zikabaobao = zikabaobao + c08
        if form.c09.data == True:
            zikabaobao = zikabaobao + c09

        if form.a01.data == True:
            zikabaobao = zikabaobao + a01
        if form.a02.data == True:
            zikabaobao = zikabaobao + a02
        if form.a03.data == True:
            zikabaobao = zikabaobao + a03
        if form.a04.data == True:
            zikabaobao = zikabaobao + a04
        if form.a05.data == True:
            zikabaobao = zikabaobao + a05
        if form.a06.data == True:
            zikabaobao = zikabaobao + a06
        if form.a07.data == True:
            zikabaobao = zikabaobao + a07
        if form.a08.data == True:
            zikabaobao = zikabaobao + a08
        if form.a09.data == True:
            zikabaobao = zikabaobao + a09
        if form.a10.data == True:
            zikabaobao = zikabaobao + a10
        if form.a11.data == True:
            zikabaobao = zikabaobao + a11
        if form.a12.data == True:
            zikabaobao = zikabaobao + a12
        if form.a13.data == True:
            zikabaobao = zikabaobao + a13
        if form.a14.data == True:
            zikabaobao = zikabaobao + a14
        if form.a15.data == True:
            zikabaobao = zikabaobao + a15
        if form.a16.data == True:
            zikabaobao = zikabaobao + a16
        if form.a17.data == True:
            zikabaobao = zikabaobao + a17
        if form.a18.data == True:
            zikabaobao = zikabaobao + a18
        if form.a19.data == True:
            zikabaobao = zikabaobao + a19
        if form.a20.data == True:
            zikabaobao = zikabaobao + a20
        if form.a21.data == True:
            zikabaobao = zikabaobao + a21
        if form.a22.data == True:
            zikabaobao = zikabaobao + a22
        if form.a23.data == True:
            zikabaobao = zikabaobao + a23
        if form.a24.data == True:
            zikabaobao = zikabaobao + a24
        if form.a25.data == True:
            zikabaobao = zikabaobao + a25
        if form.a26.data == True:
            zikabaobao = zikabaobao + a26
        if form.a27.data == True:
            zikabaobao = zikabaobao + a27
        if form.a28.data == True:
            zikabaobao = zikabaobao + a28
        if form.a29.data == True:
            zikabaobao = zikabaobao + a29
        if form.a30.data == True:
            zikabaobao = zikabaobao + a30
        return redirect(url_for('cai'))
    return render_template('choice.html',form=form)


@app.route('/cai')
def cai():
    global zikabaobao
    i = len(zikabaobao)
    while i>0:
        print(i)
        try:
            cai_word = choice(zikabaobao)
            print(cai_word)
            zikabaobao.remove(cai_word)
            i=i-1;
            return render_template('cai.html', cai_word=cai_word)
        except IndexError as e:
            return render_template('index.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
