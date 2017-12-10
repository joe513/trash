import bottle


@bottle.route('/todo')
@bottle.route('/')
def responce():

    result = 'Hello world!'
    out = bottle.template('make_table', rows=result)

    return out

@bottle.route('/getter', method='GET')
def new_item():
    new = bottle.request.GET.get('task', '').strip()

    return 'Hello'

@bottle.error(404)
def error(c):
    return 'Hello its me!'

bottle.run(reloader=True, port=80, host='192.168.0.103')
