import json

from IPython.display import HTML, display
import tabulate


def table(headers, rows):
    display(HTML(tabulate.tabulate(rows,
                                   headers=headers,
                                   tablefmt='html')))

def displayjson(js):
    print(json.dumps(js, indent=4))