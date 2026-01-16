import time
import datetime
import calendar

# ==================== time模块学习 ====================
print("=== time模块学习 ===")

# 1. 获取当前时间戳（从1970年1月1日开始的秒数）
current_timestamp = time.time()
print(f"当前时间戳: {current_timestamp}")

# 2. 获取当前时间的结构化时间对象
current_struct_time = time.localtime()
print(f"当前结构化时间: {current_struct_time}")
print(f"年: {current_struct_time.tm_year}, 月: {current_struct_time.tm_mon}, 日: {current_struct_time.tm_mday}")

# 3. 格式化时间输出
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(f"格式化时间: {formatted_time}")

# 4. 暂停程序执行
print("程序将暂停2秒...")
time.sleep(2)
print("暂停结束")

# 5. 计算代码执行时间
start_time = time.time()
# 模拟一些计算
sum_result = sum(range(1000000))
end_time = time.time()
print(f"计算1到1000000的和耗时: {end_time - start_time:.6f}秒")

# ==================== datetime模块学习 ====================
print("\n=== datetime模块学习 ===")

# 1. 获取当前日期和时间
now = datetime.datetime.now()
print(f"当前日期和时间: {now}")

# 2. 获取当前日期
today = datetime.date.today()
print(f"今天的日期: {today}")

# 3. 获取当前时间
current_time = datetime.datetime.now().time()
print(f"当前时间: {current_time}")

# 4. 创建特定的日期和时间
specific_datetime = datetime.datetime(2023, 12, 25, 15, 30, 45)
print(f"特定日期时间: {specific_datetime}")

# 5. 日期和时间的格式化
formatted_datetime = now.strftime("%Y年%m月%d日 %H:%M:%S")
print(f"格式化后的日期时间: {formatted_datetime}")

# 6. 解析字符串为日期时间对象
parsed_datetime = datetime.datetime.strptime("2023-12-25 15:30:45", "%Y-%m-%d %H:%M:%S")
print(f"解析后的日期时间: {parsed_datetime}")

# 7. 日期时间计算
future_date = today + datetime.timedelta(days=30)
print(f"30天后的日期: {future_date}")

past_date = today - datetime.timedelta(days=7)
print(f"7天前的日期: {past_date}")

# 8. 计算两个日期之间的差值
date1 = datetime.date(2023, 1, 1)
date2 = datetime.date(2023, 12, 31)
delta = date2 - date1
print(f"2023年1月1日到2023年12月31日相差: {delta.days}天")

# 9. 时区处理
print("\n=== 时区处理 ===")
# 获取UTC时间
utc_now = datetime.datetime.time(datetime.UTC)
print(f"UTC时间: {utc_now}")

# 创建时区对象
import pytz  # 需要安装: pip install pytz
try:
    tz_beijing = pytz.timezone('Asia/Shanghai')
    beijing_time = datetime.datetime.now(tz_beijing)
    print(f"北京时间: {beijing_time}")
    
    tz_new_york = pytz.timezone('America/New_York')
    new_york_time = datetime.datetime.now(tz_new_york)
    print(f"纽约时间: {new_york_time}")
except ImportError:
    print("pytz模块未安装，跳过时区示例。请使用 'pip install pytz' 安装。")

# ==================== calendar模块学习 ====================
print("\n=== calendar模块学习 ===")

# 1. 获取某年某月的日历
year = 2023
month = 12
month_calendar = calendar.month(year, month)
print(f"{year}年{month}月的日历:")
print(month_calendar)

# 2. 判断是否为闰年
is_leap = calendar.isleap(2024)
print(f"2024年是闰年吗? {'是' if is_leap else '否'}")

# 3. 获取某月的第一天是星期几和该月的天数
first_weekday, days_in_month = calendar.monthrange(2023, 12)
print(f"2023年12月的第一天是星期{first_weekday} (0=星期一, 6=星期日)")
print(f"2023年12月有{days_in_month}天")

# 4. 获取某年某月所有星期几的列表
month_days = calendar.monthcalendar(2023, 12)
print(f"2023年12月的日历矩阵:")
for week in month_days:
    print(week)

# ==================== 实用示例 ====================
print("\n=== 实用示例 ===")

# 1. 计算程序运行时间
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

start = time.time()
result = fibonacci(30)
end = time.time()
print(f"斐波那契数列第30项是: {result}")
print(f"计算耗时: {end - start:.6f}秒")

# 2. 计算下一个工作日
def next_business_day(date_obj):
    next_day = date_obj + datetime.timedelta(days=1)
    # 如果是周六(5)或周日(6)，则跳到下周一
    while next_day.weekday() >= 5:
        next_day += datetime.timedelta(days=1)
    return next_day

today = datetime.date.today()
next_bd = next_business_day(today)
print(f"今天({today})的下一个工作日是: {next_bd}")

# 3. 计算年龄
def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

birth_date = datetime.date(1990, 5, 15)
age = calculate_age(birth_date)
print(f"出生日期为{birth_date}的人现在的年龄是: {age}岁")