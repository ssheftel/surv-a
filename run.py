# -*- coding: utf-8 -*-
from eve import Eve
import os

app = Eve()

if __name__ == '__main__':
    host = '0.0.0.0'
    port = int(os.environ.get('PORT')) if 'PORT' in os.environ else 5000
    app.run(host=host, port=port, debug=True)
