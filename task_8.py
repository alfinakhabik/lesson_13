def s(f):
    def ren(field):
        return '<p>' + f(field)
    return ren

def e(f):
    def ren_1(field):
        return f(field) + '</p>'
    return ren_1

@s
@e
def res(field):
    return f'<input id="id_{field}" name="{field}">'
username = res('username')
print(username)