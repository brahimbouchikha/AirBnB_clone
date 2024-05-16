#!/usr/bin/python3


from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto  """
    user_id = ""
    text = ""
    place_id = ""
