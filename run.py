#!flask/bin/python3
from aplikacja import aplikacja

aplikacja.app.run(host="0.0.0.0", port=5070, debug=True)

'''
leszczyna:
app.run(host="0.0.0.0", port=5002, debug=True)
standardowe:
app.run(debug=True)
app.run(host="127.0.0.1", port=5002, debug=True)
'''
