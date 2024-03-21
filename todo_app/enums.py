from enum import Enum
import os

TO_DO_LIST_ID = os.getenv('TO_DO_LIST_ID')
DONE_LIST_ID = os.getenv('DONE_LIST_ID')


class Status(Enum):
    INCOMPLETE = 0
    COMPLETE = 1

class List_Ids(Enum):
    TO_DO_LIST = TO_DO_LIST_ID
    DONE_LIST = DONE_LIST_ID