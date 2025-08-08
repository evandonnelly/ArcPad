from dataclasses import dataclass


@dataclass
class VOD:
    VOD_ID : str
    pre_review_notes : str
    post_review_notes : str