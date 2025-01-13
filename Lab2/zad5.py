def dynamic_code_generator(template, **kwargs):
    code = template.format(**kwargs)
    try:
        exec(code)
    except Exception as e:
        return f"Error: {e}"
