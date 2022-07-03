from datetime import datetime

from bson import ObjectId

custom_encoder = {datetime: lambda x: x}
