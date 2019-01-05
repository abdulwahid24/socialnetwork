def extract_dict(data, extracted={}):
    for k, v in data.items():
        if isinstance(v, dict):
            extract_dict(v)
        elif v:
            extracted[k] = v
    return extracted
