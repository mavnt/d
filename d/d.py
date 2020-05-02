import inspect


def d(*args, **kwargs):
    result = {}
    result.update(kwargs)
    frame = inspect.currentframe()
    prev_locals = frame.f_back.f_locals
    values = []
    for arg in args:
        for k, v in prev_locals.items():
            if v is arg:
                idv = id(v)
                if idv in values:
                    raise ValueError(f"duplicate key for {v}")
                result[k] = v
                values.append(idv)
    return result
