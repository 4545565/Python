from pyecharts.charts import Bar
from pyecharts.options import InitOpts,LabelOpts,TitleOpts
from pyecharts.globals import ThemeType
from file import TextFileReader,JsonFileReader,Record
textfilereader=TextFileReader("Sales data\\2011年1月销售数据.txt")
jsonfilereader=JsonFileReader("Sales data\\2011年2月销售数据JSON.txt")
jan_record:list[Record]=textfilereader.read_data()
feb_record:list[Record]=jsonfilereader.read_data()
all_record:list[Record]=jan_record+feb_record
record_dict={}
for record in all_record:
    if(record in record_dict):
        record_dict[record.date]+=record.money
    else:
        record_dict[record.date]=record.money
bar=Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(record_dict.keys()))
bar.add_yaxis(
    "销售额",
    list(record_dict.values()),
    label_opts=LabelOpts(is_show=False)
)
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render("Sales data\\2011年1-2月销售数据.html")