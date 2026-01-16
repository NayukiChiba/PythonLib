import csv
import json
import pandas as pd
from io import StringIO
import os

def csv_basic_operations():
    """CSV基本操作示例"""
    
    # 1. 写入CSV文件
    with open('data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['姓名', '年龄', '城市'])
        writer.writerow(['张三', 25, '北京'])
        writer.writerow(['李四', 30, '上海'])
        writer.writerow(['王五', 28, '广州'])
    
    # 2. 读取CSV文件
    with open('data.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'行数据: {row}')
    
    # 3. 使用DictWriter写入
    with open('data_dict.csv', 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['姓名', '年龄', '城市']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'姓名': '赵六', '年龄': 35, '城市': '深圳'})
        writer.writerow({'姓名': '钱七', '年龄': 27, '城市': '杭州'})
    
    # 4. 使用DictReader读取
    with open('data_dict.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f'字典数据: {dict(row)}')

def csv_advanced_operations():
    """CSV高级操作示例"""
    
    # 5. 处理带引号的字段
    data_with_quotes = [
        ['姓名', '备注'],
        ['张三', '喜欢"编程"和"音乐"'],
        ['李四', '住在"北京市朝阳区"']
    ]
    
    with open('data_quotes.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data_with_quotes)
    
    # 6. 自定义分隔符
    with open('data_custom.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['姓名', '年龄', '城市'])
        writer.writerow(['张三', '25', '北京'])
    
    # 7. 过滤和转换数据
    with open('data.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # 跳过标题行
        
        # 过滤年龄大于25的记录
        filtered_data = []
        for row in reader:
            if int(row[1]) > 25:
                filtered_data.append(row)
        
        print(f'过滤后的数据: {filtered_data}')

def csv_error_handling():
    """CSV错误处理示例"""
    
    try:
        # 尝试读取不存在的文件
        with open('nonexistent.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print('文件不存在')
    except csv.Error as e:
        print(f'CSV错误: {e}')
    except Exception as e:
        print(f'其他错误: {e}')

def csv_large_file_processing():
    """大文件处理示例"""
    
    # 8. 逐行处理大文件（内存友好）
    def process_large_file(input_file, output_file):
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            
            # 处理标题
            header = next(reader)
            writer.writerow(header + ['处理结果'])
            
            # 逐行处理
            for row_num, row in enumerate(reader, 1):
                try:
                    # 示例：计算年龄是否大于30
                    age = int(row[1])
                    result = '高龄' if age > 30 else '正常'
                    writer.writerow(row + [result])
                    
                    if row_num % 1000 == 0:
                        print(f'已处理 {row_num} 行')
                        
                except ValueError:
                    print(f'第 {row_num} 行数据格式错误')
    
    # 创建测试大文件
    with open('large_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['姓名', '年龄', '城市'])
        for i in range(10000):
            writer.writerow([f'用户{i}', 20 + i % 50, ['北京', '上海', '广州'][i % 3]])
    
    process_large_file('large_data.csv', 'processed_large_data.csv')

def csv_data_conversion():
    """数据格式转换示例"""
    
    # 9. CSV转JSON
    def csv_to_json(csv_file, json_file):
        data = []
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    
    # 10. JSON转CSV
    def json_to_csv(json_file, csv_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        if data:
            with open(csv_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
    
    # 11. CSV转Excel（使用pandas）
    def csv_to_excel(csv_file, excel_file):
        df = pd.read_csv(csv_file, encoding='utf-8')
        df.to_excel(excel_file, index=False)
    
    csv_to_json('data.csv', 'data.json')
    json_to_csv('data.json', 'data_from_json.csv')
    csv_to_excel('data.csv', 'data.xlsx')

def csv_data_analysis():
    """数据分析示例"""
    
    # 12. 统计分析
    def analyze_csv(csv_file):
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            ages = []
            cities = set()
            
            for row in reader:
                try:
                    ages.append(int(row['年龄']))
                    cities.add(row['城市'])
                except (ValueError, KeyError):
                    continue
            
            if ages:
                print(f'平均年龄: {sum(ages) / len(ages):.1f}')
                print(f'最大年龄: {max(ages)}')
                print(f'最小年龄: {min(ages)}')
                print(f'城市列表: {list(cities)}')
    
    # 13. 数据聚合
    def aggregate_data(csv_file):
        city_stats = {}
        
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                city = row['城市']
                age = int(row['年龄'])
                
                if city not in city_stats:
                    city_stats[city] = {'count': 0, 'total_age': 0}
                
                city_stats[city]['count'] += 1
                city_stats[city]['total_age'] += age
        
        for city, stats in city_stats.items():
            avg_age = stats['total_age'] / stats['count']
            print(f'{city}: {stats["count"]}人, 平均年龄: {avg_age:.1f}')
    
    analyze_csv('data.csv')
    aggregate_data('data.csv')

def csv_advanced_features():
    """高级功能示例"""
    
    # 14. 内存中处理CSV
    def process_in_memory():
        csv_data = """姓名,年龄,城市
张三,25,北京
李四,30,上海
王五,28,广州"""
        
        # 使用StringIO模拟文件
        csv_file = StringIO(csv_data)
        reader = csv.reader(csv_file)
        
        for row in reader:
            print(f'内存处理: {row}')
    
    # 15. 自定义方言
    def custom_dialect():
        # 注册自定义方言
        csv.register_dialect('custom', delimiter='|', quoting=csv.QUOTE_MINIMAL)
        
        with open('data_custom_dialect.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, dialect='custom')
            writer.writerow(['姓名', '年龄', '城市'])
            writer.writerow(['张三', '25', '北京'])
        
        with open('data_custom_dialect.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file, dialect='custom')
            for row in reader:
                print(f'自定义方言: {row}')
    
    # 16. 数据验证
    def validate_data(csv_file):
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row_num, row in enumerate(reader, 1):
                errors = []
                
                # 验证姓名
                if not row['姓名'] or len(row['姓名']) < 2:
                    errors.append('姓名无效')
                
                # 骜证年龄
                try:
                    age = int(row['年龄'])
                    if age < 0 or age > 150:
                        errors.append('年龄超出范围')
                except ValueError:
                    errors.append('年龄格式错误')
                
                # 验证城市
                valid_cities = ['北京', '上海', '广州', '深圳', '杭州']
                if row['城市'] not in valid_cities:
                    errors.append('城市无效')
                
                if errors:
                    print(f'第 {row_num} 行错误: {", ".join(errors)}')
    
    process_in_memory()
    custom_dialect()
    validate_data('data.csv')

def csv_performance_tips():
    """性能优化技巧"""
    
    # 17. 批量写入优化
    def batch_write():
        data = [[f'用户{i}', 20 + i % 50, '北京'] for i in range(10000)]
        
        with open('batch_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['姓名', '年龄', '城市'])
            writer.writerows(data)  # 批量写入比逐行写入快
    
    # 18. 使用生成器处理大文件
    def csv_generator(csv_file):
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                yield row
    
    batch_write()
    
    # 使用生成器
    for row in csv_generator('batch_data.csv'):
        if int(row['年龄']) > 60:
            print(f'高龄用户: {row["姓名"]}')
            break  # 只处理第一个符合条件的记录

if __name__ == '__main__':
    print('=== CSV基本操作 ===')
    csv_basic_operations()
    
    print('\n=== CSV高级操作 ===')
    csv_advanced_operations()
    
    print('\n=== CSV错误处理 ===')
    csv_error_handling()
    
    print('\n=== 大文件处理 ===')
    csv_large_file_processing()
    
    print('\n=== 数据格式转换 ===')
    csv_data_conversion()
    
    print('\n=== 数据分析 ===')
    csv_data_analysis()
    
    print('\n=== 高级功能 ===')
    csv_advanced_features()
    
    print('\n=== 性能优化 ===')
    csv_performance_tips()