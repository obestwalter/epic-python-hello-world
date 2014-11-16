from cement.core import foundation

app = foundation.CementApp('epichelloworld')
try:
    app.setup()
    app.run()
    print('Hello World')
finally:
    app.close()
