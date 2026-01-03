def map_to_form(entities, form_template):
    filled_form = {}

    for field in form_template:
        filled_form[field] = entities.get(field, "")

    return filled_form
