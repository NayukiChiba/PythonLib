# typing模块学习 - Python类型提示

# ==================== 基本类型提示 ====================
print("=== 基本类型提示 ===")

# 导入基本类型
from typing import Any, List, Dict, Tuple, Set, Optional, Union, Callable, TypeVar, Generic

# 基本类型提示示例
def greet(name: str) -> str:
    """返回问候语"""
    return f"Hello, {name}!"

print(greet("Python"))

# 多种类型提示
def process_data(data: List[int]) -> int:
    """处理整数列表并返回总和"""
    return sum(data)

numbers = [1, 2, 3, 4, 5]
print(f"列表 {numbers} 的总和是: {process_data(numbers)}")

# ==================== 容器类型提示 ====================
print("\n=== 容器类型提示 ===")

# 字典类型提示
def get_user_info(user_id: int) -> Dict[str, Any]:
    """获取用户信息"""
    return {
        "id": user_id,
        "name": f"User_{user_id}",
        "email": f"user_{user_id}@example.com",
        "active": True
    }

user = get_user_info(123)
print(f"用户信息: {user}")

# 元组类型提示
def get_coordinates() -> Tuple[float, float]:
    """返回坐标"""
    return 40.7128, -74.0060

lat, lon = get_coordinates()
print(f"坐标: 纬度 {lat}, 经度 {lon}")

# 集合类型提示
def unique_items(items: List[str]) -> Set[str]:
    """返回唯一项集合"""
    return set(items)

items = ["apple", "banana", "apple", "orange", "banana"]
unique = unique_items(items)
print(f"原始列表: {items}")
print(f"唯一项集合: {unique}")

# ==================== 可选类型和联合类型 ====================
print("\n=== 可选类型和联合类型 ===")

# Optional类型 (相当于Union[T, None])
def find_user(user_id: int) -> Optional[Dict[str, Any]]:
    """查找用户，可能返回None"""
    users = {
        1: {"name": "Alice", "age": 30},
        2: {"name": "Bob", "age": 25},
        3: {"name": "Charlie", "age": 35}
    }
    return users.get(user_id)

user = find_user(2)
if user:
    print(f"找到用户: {user}")
else:
    print("用户不存在")

# Union类型 - 可以是多种类型之一
def process_value(value: Union[int, str, float]) -> str:
    """处理不同类型的值"""
    if isinstance(value, int):
        return f"整数: {value}"
    elif isinstance(value, str):
        return f"字符串: {value}"
    else:
        return f"浮点数: {value:.2f}"

print(process_value(42))
print(process_value("Hello"))
print(process_value(3.14159))

# ==================== 函数类型提示 ====================
print("\n=== 函数类型提示 ===")

# Callable类型 - 表示可调用对象
def apply_operation(numbers: List[int], operation: Callable[[int], int]) -> List[int]:
    """对列表中的每个数字应用操作"""
    return [operation(num) for num in numbers]

def square(x: int) -> int:
    """平方函数"""
    return x * x

def cube(x: int) -> int:
    """立方函数"""
    return x * x * x

numbers = [1, 2, 3, 4, 5]
squared = apply_operation(numbers, square)
cubed = apply_operation(numbers, cube)

print(f"原始数字: {numbers}")
print(f"平方结果: {squared}")
print(f"立方结果: {cubed}")

# ==================== 泛型类型 ====================
print("\n=== 泛型类型 ===")

# TypeVar - 类型变量
T = TypeVar('T')

def first_item(items: List[T]) -> Optional[T]:
    """返回列表中的第一项"""
    return items[0] if items else None

int_list = [10, 20, 30]
str_list = ["a", "b", "c"]

print(f"整数列表的第一项: {first_item(int_list)}")
print(f"字符串列表的第一项: {first_item(str_list)}")

# 泛型类
class Stack(Generic[T]):
    """泛型栈类"""
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        """入栈"""
        self._items.append(item)
    
    def pop(self) -> T:
        """出栈"""
        return self._items.pop()
    
    def is_empty(self) -> bool:
        """检查栈是否为空"""
        return not self._items

# 使用泛型栈
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
int_stack.push(3)

print(f"弹出栈顶元素: {int_stack.pop()}")
print(f"栈是否为空: {int_stack.is_empty()}")

str_stack = Stack[str]()
str_stack.push("hello")
str_stack.push("world")

print(f"弹出栈顶元素: {str_stack.pop()}")
print(f"栈是否为空: {str_stack.is_empty()}")

# ==================== 高级类型提示 ====================
print("\n=== 高级类型提示 ===")

# 字面量类型
from typing import Literal

def set_status(status: Literal["pending", "approved", "rejected"]) -> str:
    """设置状态"""
    return f"状态已设置为: {status}"

print(set_status("approved"))
# 以下行会引发类型检查错误:
# print(set_status("unknown"))

# 协议类型
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str: ...

class Circle:
    def draw(self) -> str:
        return "绘制圆形"

class Square:
    def draw(self) -> str:
        return "绘制正方形"

def render_shape(shape: Drawable) -> None:
    """渲染形状"""
    print(shape.draw())

render_shape(Circle())
render_shape(Square())

# ==================== 类型别名 ====================
print("\n=== 类型别名 ===")

# 创建类型别名
UserID = int
UserName = str
UserInfo = Dict[str, Any]

def get_user_by_id(user_id: UserID) -> UserInfo:
    """根据ID获取用户信息"""
    return {
        "id": user_id,
        "name": f"User_{user_id}",
        "email": f"user_{user_id}@example.com"
    }

user = get_user_by_id(456)
print(f"用户信息: {user}")

# ==================== 类型检查工具 ====================
print("\n=== 类型检查工具 ===")

# 使用isinstance进行运行时类型检查
def safe_divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    """安全除法，避免除以零"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("错误: 参数必须是数字")
        return None
    
    if b == 0:
        print("错误: 除数不能为零")
        return None
    
    return a / b

result1 = safe_divide(10, 2)
result2 = safe_divide(10, 0)
result3 = safe_divide("10", 2)

print(f"10 ÷ 2 = {result1}")
print(f"10 ÷ 0 = {result2}")
print(f"'10' ÷ 2 = {result3}")

# ==================== 实用示例 ====================
print("\n=== 实用示例 ===")

# 示例1: 类型提示的数据库查询函数
from typing import List, Dict, Any, Optional

def query_database(table: str, filters: Dict[str, Any]) -> List[Dict[str, Any]]:
    """模拟数据库查询"""
    # 这里只是模拟，实际实现会连接真实数据库
    print(f"查询表: {table}, 过滤条件: {filters}")
    # 模拟返回结果
    if table == "users":
        return [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"}
        ]
    elif table == "products":
        return [
            {"id": 101, "name": "Laptop", "price": 999.99},
            {"id": 102, "name": "Phone", "price": 699.99}
        ]
    return []

users = query_database("users", {"active": True})
products = query_database("products", {"category": "electronics"})

print("用户查询结果:")
for user in users:
    print(f"  {user}")

print("产品查询结果:")
for product in products:
    print(f"  {product}")

# 示例2: 类型提示的API响应处理
from typing import TypedDict

class UserResponse(TypedDict):
    id: int
    name: str
    email: str
    active: bool

def process_user_response(response: UserResponse) -> str:
    """处理用户API响应"""
    status = "活跃" if response["active"] else "非活跃"
    return f"用户 {response['name']} (ID: {response['id']}, 邮箱: {response['email']}) 状态: {status}"

user_response: UserResponse = {
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com",
    "active": True
}

print(process_user_response(user_response))

# 示例3: 类型提示的装饰器
from typing import Callable, TypeVar, cast

F = TypeVar('F', bound=Callable[..., Any])

def log_execution(func: F) -> F:
    """记录函数执行的装饰器"""
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"执行函数: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"函数 {func.__name__} 执行完成")
        return result
    return cast(F, wrapper)

@log_execution
def add_numbers(a: int, b: int) -> int:
    """加法函数"""
    return a + b

@log_execution
def concatenate_strings(s1: str, s2: str) -> str:
    """字符串连接函数"""
    return s1 + s2

print(f"5 + 3 = {add_numbers(5, 3)}")
print(f"'Hello' + 'World' = {concatenate_strings('Hello', 'World')}")