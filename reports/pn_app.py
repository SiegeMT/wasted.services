import panel as pn

from .pn_model import Report


def app(doc):
    rpt = Report()
    viewme = pn.Viewer(rpt.param_)