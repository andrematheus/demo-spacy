from IPython.display import HTML, display
import tabulate


def table(headers, rows):
    display(HTML(tabulate.tabulate(rows,
                                   headers=headers,
                                   tablefmt='html')))
