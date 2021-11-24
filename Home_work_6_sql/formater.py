
def list_rec_html(param):
    for _ in param:
        return "<br/>".join(str(_).strip(",)").strip("(") for _ in param)
