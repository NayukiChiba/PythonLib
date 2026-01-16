# os库: 操作系统接口
import os
import sys
import shutil
import tempfile
import zipfile
import tarfile
import traceback
from io import StringIO


# ============== os ================
# 创建目录
def create_new_folder():
    if not os.path.exists("single_dir"):
        print("目录不存在, 创建单级目录")
        os.mkdir("single_dir") # 创建单级目录
    else:
        print("目录存在, 删除单级目录")
        os.rmdir("single_dir") # 删除单级目录


def delete_folder():
    if not os.path.exists("multi/level/dir"):
        print("目录不存在, 创建多级目录")
        os.makedirs("multi/level/dir") # 创建多级目录
    else:
        print("目录存在, 删除多级目录")
        os.removedirs("multi/level/dir") # 递归删除目录


# 列出目录内容
def listcwd():
    files = os.listdir(os.getcwd())
    print(f"当前目录内容: {files}")

# 删除文件
def delete_file():
    test_file = "files.txt"
    if os.path.exists(test_file):
        print("存在files.txt, 删除")
        os.remove(test_file)
    else:
        with open(test_file, "w") as fd:
            pass
        print("files.txt已创建")

# 重命名文件或者目录
def rename(filename, new_filename):
    if os.path.exists(filename):
        os.rename(filename, new_filename)
        print(f"已重命名: {filename} -> {new_filename}")

    if os.path.exists(new_filename):
        print(f"{new_filename}已存在, 删除")
        os.remove(new_filename)

# 获取当前工作目录
def getcwd():
    print(f"当前工作目录为: {os.getcwd()}")

# 检查是否为文件
def check_file():
    is_file = os.path.isfile(os.getcwd())
    print(f"当前路径是文件: {is_file}")

# 检查是否是目录
def check_dir():
    is_dir = os.path.isdir(os.getcwd())  # 返回True或False
    print(f"当前路径是目录: {is_dir}")

# 路径操作
def path_process():
    # 路径拼接
    path = os.path.join("folder", "subfolder", "file.txt")  # 自动处理路径分隔符
    print(f"拼接路径: {path}")
    
    # 获取绝对路径
    if os.path.exists("README.md"):
        abs_path = os.path.abspath("./README.md")  # 将相对路径转换为绝对路径
        print(f"README的完整路径为: {abs_path}")
        
        # 获取路径的目录名和文件名
        fullname = os.path.join(os.getcwd(), "README.md")
        dir_name = os.path.dirname(fullname)  # 返回 os.getcwd()
        file_name = os.path.basename(fullname)  # 返回 README.md

        print(f"README的完整地址为: {fullname}")
        print(f"README在{dir_name}文件夹下")
        print(f"README的名字为: {file_name}")

        # 分割路径
        parts = os.path.split(fullname)  # 返回 (os.getwd(), README.md)
        print(f"README完整地址分割为: {parts}")

        # 获取文件扩展名
        root, ext = os.path.splitext("README.md")  # 返回 ("README", ".md")
        print(f"README.md的名字为{root}, 拓展名为{ext}")

        # 获取文件大小
        size = os.path.getsize("README.md")  # 返回文件大小（字节）
        print(f"README.md文件大小: {size} 字节")

        # 获取文件最后修改时间
        mtime = os.path.getmtime("README.md")  # 返回时间戳
        import time
        print(f"README.md最后修改时间: {time.ctime(mtime)}")

        # 获取文件最后访问时间
        atime = os.path.getatime("README.md")  # 返回时间戳
        print(f"README.md最后访问时间: {time.ctime(atime)}")

        # 获取文件创建时间（Windows）
        ctime = os.path.getctime("README.md")  # 返回时间戳
        print(f"README.md创建时间: {time.ctime(ctime)}")
    else:
        print("README.md文件不存在，跳过文件信息获取")


def getenv():
    path = os.environ.get("PATH", "")  # 获取PATH环境变量，如果不存在则返回空字符串
    print(f"PATH环境变量长度: {len(path)} 字符")
    
    if "HOME" in os.environ:
        home = os.environ["HOME"]  # 获取HOME环境变量
        print(f"HOME环境变量: {home}")
    elif "USERPROFILE" in os.environ:
        home = os.environ["USERPROFILE"]  # Windows用户目录
        print(f"USERPROFILE环境变量: {home}")
    
    # 设置环境变量
    os.environ["MY_VAR"] = "my_value"  # 设置环境变量
    print("已设置环境变量 MY_VAR = my_value")

    # 检查环境变量是否存在
    if "MY_VAR" in os.environ:
        print("MY_VAR exists")

    # 删除环境变量
    del os.environ["MY_VAR"]  # 删除环境变量
    print("已删除环境变量 MY_VAR")


def process_manage():
    # 获取当前进程ID
    pid = os.getpid()  # 返回当前进程的ID
    print(f"当前进程ID: {pid}")

    # 获取父进程ID
    ppid = os.getppid()  # 返回父进程的ID
    print(f"父进程ID: {ppid}")

    # 获取用户ID（Unix系统）
    if hasattr(os, 'getuid'):
        uid = os.getuid()
        print(f"用户ID: {uid}")
        gid = os.getgid()
        print(f"组ID: {gid}")
    else:
        print("当前系统不支持获取用户ID和组ID")

    # 执行系统命令
    print("\n执行系统命令:")
    if os.name == 'nt':  # Windows
        os.system("echo Windows系统命令执行成功")
    else:  # Unix/Linux
        os.system("echo 'Unix/Linux系统命令执行成功'")


def getsysteminfo():
    # 获取操作系统名称
    os_name = os.name  # 返回 'nt' (Windows), 'posix' (Unix/Linux), 'java' (Jython)
    print(f"操作系统名称: {os_name}")

    # 获取当前登录用户名
    try:
        user = os.getlogin()  # 返回当前登录用户名
        print(f"当前登录用户: {user}")
    except Exception as e:
        print(f"无法获取用户名: {e}")
    
    # 获取终端大小
    try:
        size = os.get_terminal_size()
        print(f"终端大小: {size.columns}列 x {size.rows}行")
    except Exception as e:
        print("无法获取终端大小")

    # 获取CPU核心数
    cpu_count = os.cpu_count()  # 返回CPU核心数
    print(f"CPU核心数: {cpu_count}")


def file_op():
    test_file = "file_op_test.txt"
    
    # 创建测试文件
    with open(test_file, "w") as f:
        f.write("Hello, World!")
    
    # 打开文件描述符
    fd = os.open(test_file, os.O_RDONLY)  # 以只读方式打开文件，返回文件描述符
    print(f"文件描述符: {fd}")

    # 读取文件描述符
    data = os.read(fd, 1024)  # 从文件描述符读取最多1024字节
    print(f"读取内容: {data.decode()}")

    # 关闭文件描述符
    os.close(fd)  # 关闭文件描述符
    print("文件描述符已关闭")

    # 重新打开以写入
    fd = os.open(test_file, os.O_WRONLY | os.O_TRUNC)
    # 写入文件描述符
    os.write(fd, b"Hello, Python!")  # 向文件描述符写入字节
    print("已写入新内容")
    
    # 关闭文件描述符
    os.close(fd)
    
    # 复制文件描述符
    fd = os.open(test_file, os.O_RDONLY)
    new_fd = os.dup(fd)  # 复制文件描述符
    print(f"复制文件描述符: {new_fd}")
    
    # 关闭所有文件描述符
    os.close(fd)
    os.close(new_fd)
    
    # 清理
    os.remove(test_file)
    print("测试文件已删除")


"""
sys库学习示例
sys库提供了访问Python解释器相关变量和函数的功能
"""

def python_info():
    """演示Python版本和平台信息"""
    print("\n" + "="*50)
    print("Python版本和平台信息")
    print("="*50)
    
    # 1. Python版本信息
    print(f"Python版本: {sys.version}")
    print(f"Python版本信息: {sys.version_info}")
    print(f"Python主版本号: {sys.version_info.major}")
    print(f"Python次版本号: {sys.version_info.minor}")
    print(f"Python微版本号: {sys.version_info.micro}")
    
    # 2. 平台信息
    print(f"平台: {sys.platform}")
    print(f"字节序: {sys.byteorder}")  # 'little' 或 'big'
    
    # 3. Python实现信息
    print(f"Python实现: {sys.implementation}")
    print(f"API版本: {sys.api_version}")


def command_line_args():
    """演示命令行参数处理"""
    print("\n" + "="*50)
    print("命令行参数处理")
    print("="*50)
    
    # 1. 获取命令行参数
    print(f"脚本名称: {sys.argv[0]}")
    print(f"命令行参数: {sys.argv[1:]}")
    
    # 2. 参数数量
    print(f"参数数量: {len(sys.argv)}")
    
    # 3. 解析命令行参数示例
    if len(sys.argv) > 1:
        print("\n解析命令行参数:")
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"参数 {i}: {arg}")
    else:
        print("\n没有提供命令行参数")
        print("使用方法: python system.py 参数1 参数2 ...")


def module_paths():
    """演示模块搜索路径"""
    print("\n" + "="*50)
    print("模块搜索路径")
    print("="*50)
    
    # 1. 显示模块搜索路径
    print(f"模块搜索路径数量: {len(sys.path)}")
    
    # 2. 显示前几个路径
    print("\n前5个模块搜索路径:")
    for i, path in enumerate(sys.path[:5]):
        print(f"{i+1}. {path}")
    
    # 3. 添加自定义路径
    custom_path = r"d:\custom\modules"
    if custom_path not in sys.path:
        sys.path.insert(0, custom_path)
        print(f"\n已添加自定义路径到搜索路径: {custom_path}")
    
    # 4. 显示当前工作目录是否在路径中
    cwd = os.getcwd()
    if cwd in sys.path:
        print(f"当前工作目录在模块搜索路径中: {cwd}")
    else:
        print(f"当前工作目录不在模块搜索路径中: {cwd}")


def standard_streams():
    """演示标准输入输出流"""
    print("\n" + "="*50)
    print("标准输入输出流")
    print("="*50)
    
    # 1. 显示标准流对象
    print(f"标准输入: {sys.stdin}")
    print(f"标准输出: {sys.stdout}")
    print(f"标准错误: {sys.stderr}")
    
    # 2. 写入标准输出
    print("\n使用sys.stdout写入:")
    sys.stdout.write("这是通过sys.stdout写入的内容\n")
    
    # 3. 写入标准错误
    print("\n使用sys.stderr写入:")
    sys.stderr.write("这是通过sys.stderr写入的错误信息\n")
    
    # 4. 重定向标准输出示例
    print("\n重定向标准输出示例:")
    original_stdout = sys.stdout  # 保存原始标准输出
    
    # 创建一个字符串缓冲区
    buffer = StringIO()
    
    # 重定向标准输出到缓冲区
    sys.stdout = buffer
    
    # 这些输出不会显示在控制台，而是写入缓冲区
    print("这行文本被重定向到缓冲区")
    print("这行文本也被重定向到缓冲区")
    
    # 恢复标准输出
    sys.stdout = original_stdout
    
    # 获取缓冲区内容
    redirected_content = buffer.getvalue()
    print(f"重定向的内容:\n{redirected_content}")


def system_functions():
    """演示系统相关函数"""
    print("\n" + "="*50)
    print("系统相关函数")
    print("="*50)
    
    # 1. 获取和设置递归限制
    print(f"当前递归限制: {sys.getrecursionlimit()}")
    sys.setrecursionlimit(2000)  # 设置递归限制
    print(f"新的递归限制: {sys.getrecursionlimit()}")
    
    # 2. 获取整数最大值
    print(f"整数最大值: {sys.maxsize}")
    
    # 3. 获取浮点数信息
    print(f"浮点数信息: {sys.float_info}")
    
    # 4. 获取哈希信息
    print(f"哈希种子: {sys.hash_info}")
    
    # 5. 获取路径信息
    print(f"路径分隔符: {repr(os.pathsep)}")
    print(f"文件扩展名分隔符: {repr(os.extsep)}")


def module_info():
    """演示模块信息"""
    print("\n" + "="*50)
    print("模块信息")
    print("="*50)
    
    # 1. 已加载的模块
    print(f"已加载模块数量: {len(sys.modules)}")
    
    # 2. 显示几个常用模块
    common_modules = ['os', 'sys', 'json', 'math']
    print("\n常用模块信息:")
    for module_name in common_modules:
        if module_name in sys.modules:
            module = sys.modules[module_name]
            print(f"{module_name}: {module}")
    
    # 3. 内置模块
    print(f"\n内置模块数量: {len(sys.builtin_module_names)}")
    print("前10个内置模块:")
    for i, module_name in enumerate(list(sys.builtin_module_names)[:10]):
        print(f"{i+1}. {module_name}")


def exit_functions():
    """演示退出函数"""
    print("\n" + "="*50)
    print("退出函数")
    print("="*50)
    
    # 1. 正常退出
    print("使用sys.exit()退出程序")
    print("(已注释，取消注释以测试)")
    # sys.exit(0)  # 取消注释以测试正常退出
    
    # 2. 带消息退出
    print("使用sys.exit()带消息退出")
    print("(已注释，取消注释以测试)")
    # sys.exit("程序正常结束")  # 取消注释以测试带消息退出
    
    # 3. 立即退出
    print("使用os._exit()立即退出")
    print("(已注释，取消注释以测试)")
    # os._exit(0)  # 取消注释以测试立即退出


def exception_info():
    """演示异常信息"""
    print("\n" + "="*50)
    print("异常信息")
    print("="*50)
    
    try:
        # 故意引发一个异常
        x = 1 / 0
    except Exception as e:
        # 获取异常信息
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(f"异常类型: {exc_type}")
        print(f"异常值: {exc_value}")
        print(f"异常跟踪: {exc_traceback}")
        
        # 打印异常跟踪
        print("\n异常跟踪详情:")
        traceback.print_tb(exc_traceback)


def performance():
    """演示性能相关功能"""
    print("\n" + "="*50)
    print("性能相关功能")
    print("="*50)
    
    # 1. 获取当前帧
    current_frame = sys._getframe()
    print(f"当前帧: {current_frame}")
    print(f"当前帧代码对象: {current_frame.f_code}")
    print(f"当前行号: {current_frame.f_lineno}")
    
    # 2. 调用跟踪
    def trace_calls(frame, event, arg):
        if event == 'call':
            print(f"调用函数: {frame.f_code.co_name}")
        return trace_calls
    
    print("\n调用跟踪示例:")
    print("(已注释，取消注释以启用)")
    # 设置跟踪函数
    # sys.settrace(trace_calls)  # 取消注释以启用调用跟踪
    
    # 调用一个函数
    def test_function():
        return "测试函数"
    
    result = test_function()
    print(f"函数结果: {result}")
    
    # 禁用跟踪
    # sys.settrace(None)  # 取消注释以禁用调用跟踪


"""
shutil库学习示例
shutil库提供了高级文件操作功能，如复制、移动、删除等
"""

def file_copy():
    """演示文件复制功能"""
    print("\n" + "="*50)
    print("文件复制功能")
    print("="*50)
    
    # 创建测试文件
    test_file = "test_file.txt"
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write("这是一个测试文件\n用于演示shutil的复制功能")
    
    # 1. 简单复制
    copy_file = "copy_file.txt"
    shutil.copy(test_file, copy_file)
    print(f"复制文件: {test_file} -> {copy_file}")
    
    # 2. 复制并保留元数据
    copy_meta_file = "copy_meta_file.txt"
    shutil.copy2(test_file, copy_meta_file)
    print(f"复制文件并保留元数据: {test_file} -> {copy_meta_file}")
    
    # 3. 复制文件对象
    copy_fileobj_file = "copy_fileobj_file.txt"
    with open(test_file, 'rb') as src, open(copy_fileobj_file, 'wb') as dst:
        shutil.copyfileobj(src, dst)
    print(f"复制文件对象: {test_file} -> {copy_fileobj_file}")
    
    # 4. 复制文件内容
    copy_file_content = "copy_file_content.txt"
    shutil.copyfile(test_file, copy_file_content)
    print(f"复制文件内容: {test_file} -> {copy_file_content}")
    
    # 清理
    for file in [copy_file, copy_meta_file, copy_fileobj_file, copy_file_content, test_file]:
        if os.path.exists(file):
            os.remove(file)
    print("清理测试文件完成")


def directory_operations():
    """演示目录操作"""
    print("\n" + "="*50)
    print("目录操作")
    print("="*50)
    
    # 创建测试目录结构
    src_dir = "src_dir"
    os.makedirs(os.path.join(src_dir, "subdir"), exist_ok=True)
    
    # 在源目录中创建文件
    with open(os.path.join(src_dir, "file1.txt"), 'w') as f:
        f.write("源目录中的文件1")
    
    with open(os.path.join(src_dir, "subdir", "file2.txt"), 'w') as f:
        f.write("源目录子目录中的文件2")
    
    # 1. 复制整个目录
    dst_dir = "dst_dir"
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    shutil.copytree(src_dir, dst_dir)
    print(f"复制目录: {src_dir} -> {dst_dir}")
    
    # 2. 删除目录
    print(f"删除目录: {dst_dir}")
    shutil.rmtree(dst_dir)
    
    # 3. 移动目录
    move_dir = "move_dir"
    shutil.move(src_dir, move_dir)
    print(f"移动目录: {src_dir} -> {move_dir}")
    
    # 清理
    if os.path.exists(move_dir):
        shutil.rmtree(move_dir)
    print("清理测试目录完成")


def disk_usage():
    """演示磁盘使用情况"""
    print("\n" + "="*50)
    print("磁盘使用情况")
    print("="*50)
    
    # 获取当前目录的磁盘使用情况
    total, used, free = shutil.disk_usage(".")
    
    # 转换为GB
    total_gb = total // (1024**3)
    used_gb = used // (1024**3)
    free_gb = free // (1024**3)
    
    print(f"磁盘总空间: {total_gb} GB")
    print(f"已使用空间: {used_gb} GB")
    print(f"剩余空间: {free_gb} GB")
    print(f"使用率: {used/total*100:.1f}%")
    
    # 获取不同驱动器的使用情况（Windows）
    if os.name == 'nt':
        print("\n各驱动器使用情况:")
        for drive in ['C:\\', 'D:\\', 'E:\\']:
            if os.path.exists(drive):
                try:
                    total, used, free = shutil.disk_usage(drive)
                    total_gb = total // (1024**3)
                    used_gb = used // (1024**3)
                    free_gb = free // (1024**3)
                    print(f"{drive}: 总空间 {total_gb}GB, 已用 {used_gb}GB, 剩余 {free_gb}GB")
                except Exception as e:
                    print(f"{drive}: 无法获取信息 - {e}")


def archive_operations():
    """演示归档操作"""
    print("\n" + "="*50)
    print("归档操作")
    print("="*50)
    
    # 创建测试目录和文件
    test_dir = "archive_test_dir"
    os.makedirs(os.path.join(test_dir, "subdir"), exist_ok=True)
    
    with open(os.path.join(test_dir, "file1.txt"), 'w') as f:
        f.write("归档测试文件1")
    
    with open(os.path.join(test_dir, "subdir", "file2.txt"), 'w') as f:
        f.write("归档测试文件2")
    
    # 1. 创建ZIP归档
    zip_archive = "test_archive.zip"
    shutil.make_archive(zip_archive.replace('.zip', ''), 'zip', test_dir)
    print(f"创建ZIP归档: {zip_archive}")
    
    # 2. 创建TAR归档
    tar_archive = "test_archive.tar"
    shutil.make_archive(tar_archive.replace('.tar', ''), 'tar', test_dir)
    print(f"创建TAR归档: {tar_archive}")
    
    # 3. 创建TAR.GZ归档
    tar_gz_archive = "test_archive.tar.gz"
    shutil.make_archive(tar_gz_archive.replace('.tar.gz', ''), 'gztar', test_dir)
    print(f"创建TAR.GZ归档: {tar_gz_archive}")
    
    # 4. 解压归档
    extract_dir = "extracted"
    if os.path.exists(extract_dir):
        shutil.rmtree(extract_dir)
    
    shutil.unpack_archive(zip_archive, extract_dir)
    print(f"解压归档到: {extract_dir}")
    
    # 列出解压后的内容
    print("解压后的内容:")
    for root, dirs, files in os.walk(extract_dir):
        level = root.replace(extract_dir, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")
    
    # 清理
    for archive in [zip_archive, tar_archive, tar_gz_archive]:
        if os.path.exists(archive):
            os.remove(archive)
    
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    
    if os.path.exists(extract_dir):
        shutil.rmtree(extract_dir)
    
    print("清理测试文件和目录完成")


def file_permissions():
    """演示文件权限操作"""
    print("\n" + "="*50)
    print("文件权限操作")
    print("="*50)
    
    # 创建测试文件
    test_file = "permission_test.txt"
    with open(test_file, 'w') as f:
        f.write("权限测试文件")
    
    # 1. 获取文件权限
    file_stat = os.stat(test_file)
    print(f"原始权限: {oct(file_stat.st_mode)}")
    
    # 2. 复制权限
    copy_file = "permission_copy.txt"
    shutil.copy(test_file, copy_file)
    print(f"复制文件: {test_file} -> {copy_file}")
    
    # 3. 修改权限（Unix系统）
    if os.name != 'nt':
        # 添加执行权限
        os.chmod(test_file, 0o755)
        print(f"修改权限后: {oct(os.stat(test_file).st_mode)}")
        
        # 复制权限
        shutil.copymode(test_file, copy_file)
        print(f"复制权限后: {oct(os.stat(copy_file).st_mode)}")
    else:
        print("Windows系统，跳过权限修改演示")
    
    # 4. 复制统计信息（包括权限）
    stat_file = "permission_stat.txt"
    shutil.copy2(test_file, stat_file)
    print(f"复制统计信息: {test_file} -> {stat_file}")
    
    # 清理
    for file in [test_file, copy_file, stat_file]:
        if os.path.exists(file):
            os.remove(file)
    
    print("清理测试文件完成")


def special_operations():
    """演示特殊操作"""
    print("\n" + "="*50)
    print("特殊操作")
    print("="*50)
    
    # 1. 查找可执行文件
    print("查找可执行文件:")
    executables = ["python", "pip", "git", "node"]
    for exe in executables:
        try:
            path = shutil.which(exe)
            print(f"{exe}: {path}")
        except Exception as e:
            print(f"{exe}: 未找到 - {e}")
    
    # 2. 注册归档格式
    print("\n注册归档格式:")
    print(f"已注册的归档格式: {shutil.get_archive_formats()}")
    
    # 3. 注册解压格式
    print(f"\n已注册的解压格式: {shutil.get_unpack_formats()}")
    
    # 4. 临时文件操作
    print("\n临时文件操作:")
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write("临时文件内容".encode())
        temp_path = temp_file.name
        print(f"创建临时文件: {temp_path}")
    
    # 移动临时文件
    moved_temp = "moved_temp.txt"
    shutil.move(temp_path, moved_temp)
    print(f"移动临时文件: {temp_path} -> {moved_temp}")
    
    # 清理
    if os.path.exists(moved_temp):
        os.remove(moved_temp)
    
    print("清理临时文件完成")


def main():
    """主函数，运行所有演示"""
    print("="*60)
    print("Python系统库学习示例 - os, sys, shutil")
    print("="*60)
    
    # os库演示
    print("\n\n" + "="*60)
    print("OS库功能演示")
    print("="*60)
    
    print("\n1. 目录操作:")
    create_new_folder()
    delete_folder()
    listcwd()
    getcwd()
    check_file()
    check_dir()
    
    print("\n2. 文件操作:")
    delete_file()
    rename("files.txt", "renamed_files.txt")
    path_process()
    
    print("\n3. 环境变量:")
    getenv()
    
    print("\n4. 进程管理:")
    process_manage()
    
    print("\n5. 系统信息:")
    getsysteminfo()
    
    print("\n6. 文件描述符操作:")
    file_op()
    
    # sys库演示
    print("\n\n" + "="*60)
    print("SYS库功能演示")
    print("="*60)
    
    python_info()
    command_line_args()
    module_paths()
    standard_streams()
    system_functions()
    module_info()
    exit_functions()
    exception_info()
    performance()
    
    # shutil库演示
    print("\n\n" + "="*60)
    print("SHUTIL库功能演示")
    print("="*60)
    
    file_copy()
    directory_operations()
    disk_usage()
    archive_operations()
    file_permissions()
    special_operations()
    
    print("\n\n" + "="*60)
    print("所有演示完成！")
    print("="*60)


if __name__ == "__main__":
    main()