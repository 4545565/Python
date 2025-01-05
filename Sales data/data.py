class Record:
    def __init__(
        self,
        date:str='',
        order_id:str='',
        money:int=0,
        province:str=''
    ):
        self.date=date
        self.order_id=order_id
        self.money=money
        self.province=province
    def __str__(self) -> str:
        return(f"date:{self.date},order_id={self.order_id},money:{self.money},province={self.province}")
