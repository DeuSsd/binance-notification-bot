from pydantic import BaseModel

# {
#     'stream': 'btcusdt@markPrice',
#     'data': {
#         'e': 'markPriceUpdate', 
#         'E': 1655585001000, 
#         's':'BTCUSDT', 
#         'p': '17779.63167273', 
#         'P': '17948.89003048',
#         'i': '17793.40782815', 
#         'r': '0.00002174',
#         'T': 1655596800000
#         }
#     }

class MarkPriceData(BaseModel):
    e: str 
    E: int
    s: str 
    p: str 
    P: str
    i: str
    r: str
    T: int


class MarkPrice(BaseModel):
    stream: str
    data: MarkPriceData
