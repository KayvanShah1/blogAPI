def remove_none_from_data_dict(data: dict):
    data = {k: v for k, v in data.items() if v is not None}
    return data
