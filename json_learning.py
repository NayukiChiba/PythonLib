import json

# Python对象转json字符串
python_dict = {
    "name": "张三",
    "age": 30,
    "is_student": False,
    "courses": ["数学", "物理", "化学"],
    "address": {
        "street": "人民路",
        "city": "北京"
    }
}

# 转化为json字符串
# type是string
json_str = json.dumps(python_dict, ensure_ascii=False, indent=4)
print("Python字典转json字符串")
print(json_str)

# json字符串转python对象
json_data = '{"name": "李四", "age": 25, "is_student": true}'
python_obj = json.loads(json_data)
print("\nJSON字符串转Python对象:")
print(python_obj)
print(f"姓名: {python_obj['name']}, 年龄: {python_obj['age']}")


# 3. 从文件读取JSON
# 先创建一个JSON文件
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(python_dict, f, ensure_ascii=False, indent=4)

# 从文件读取JSON
with open('data.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
    print("\n从文件读取的JSON数据:")
    print(loaded_data)

# 4. 处理更复杂的数据结构
complex_data = {
    "users": [
        {"id": 1, "name": "用户1", "tags": ["admin", "user"]},
        {"id": 2, "name": "用户2", "tags": ["user"]}
    ],
    "metadata": {
        "created_at": "2023-01-01",
        "version": 1.0
    }
}


complex_json = json.dumps(complex_data, ensure_ascii=False, indent=2)
print("\n复杂数据结构转JSON:")
print(complex_json)


# 5. 自定义JSON编码器
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def to_dict(self):
        return {"name": self.name, "age": self.age}
    
person = Person("王五", 35)
person_json = json.dumps(person.to_dict(), ensure_ascii=False)
print("\n自定义对象转JSON:")
print(person_json)
