from flask import Flask,request,jsonify,render_template
from extraUtil import poker as p
from extraUtil import fibonacci
from extraUtil import model
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Flask!"

@app.route('/helloFlask/<username>')
def helloFlask(username):
    outStr = "<h1>Hello {} !</h1>"
    return outStr.format(username)

@app.route('/helloFlask2/<username>')
def helloFlask2(username):
    return render_template('helloFlask.html', username=username)

@app.route('/hello_get')
def hello_get():
    username = request.args.get('username')
    userage = request.args.get('userage')
    outStr = """Hello {} , you are {} years old."""
    if username == None:
        return "What's your name?   "
    if userage == None:
        return "<h1>Hello {} !</h1>".format(username)
    return outStr.format(username,userage)

@app.route('/hello_get2')
def hello_get2():
    username = request.args.get('username')
    userage = request.args.get('userage')
    return render_template('hello_get.html',username=username,userage=userage)                           

@app.route('/add')
def add():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    return str(x**y)

@app.route('/hello_post', methods = ['GET','POST'])
def hello_post():
    outStr = """
    <form action="/hello_post" method="POST">
        <input name="username">
        <button type="submit">SUBMIT</button>
    </form>
    """
    method = request.method
    if request.method == 'POST':
        username = request.form.get('username')
        outStr +="""
        <div>Hello {}.</div>
        """.format(username)

    return outStr

@app.route('/poker', methods = ['GET','POST'])
def poker():
    outStr = """
    <form action="/poker" method="POST">
        <input name="player">
        <button type="submit">SUBMIT</button>
    </form>
    """
    method = request.method
    if method == 'GET':
        return outStr
    if method == 'POST':
        player = int(request.form.get('player'))
        return jsonify(p.poker(player))

@app.route('/poker2', methods=['GET', 'POST'])
def poker2():
    request_method = request.method
    players = 0
    cards = dict()
    if request_method == 'POST':
        players = int(request.form.get('players'))
        cards = p.poker(players)
    return render_template('poker.html', request_method=request_method,
                                         cards=cards)

@app.route('/fibonacci', methods = ['GET','POST'])
def fibo():
    outStr = """
    <form action="/fibonacci" method="POST">
        <input name="nums">
        <button type="submit">SUBMIT</button>
    </form>
    """
    method = request.method
    if method == 'GET':
        return outStr
    if method == 'POST':
        nums = int(request.form.get('nums'))
        return str(fibonacci.Funct(nums))

@app.route('/getSeries/<n>')
def getSeries(n):
    return str(fibonacci.Funct(int(n)))

@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)