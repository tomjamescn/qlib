"""检查日历加载逻辑的脚本"""
from qlib.data import D
import numpy as np
import pandas as pd
from pathlib import Path

# 1. 检查返回的日历范围
cal_default = D.calendar(freq='day')
print(f"默认日历范围:")
print(f"  起始: {cal_default[0]}")
print(f"  结束: {cal_default[-1]}")
print(f"  数量: {len(cal_default)}")
print()

# 2. 包含future的日历
try:
    cal_with_future = D.calendar(freq='day', future=True)
    print(f"包含future的日历范围:")
    print(f"  起始: {cal_with_future[0]}")
    print(f"  结束: {cal_with_future[-1]}")
    print(f"  数量: {len(cal_with_future)}")
    print(f"  差异: {len(cal_with_future) - len(cal_default)} 天")
    print()
except Exception as e:
    print(f"加载future日历失败: {e}")
    print()

# 3. 检查底层文件
from qlib.config import C
provider_uri = Path(C.get_data_path())
print(f"数据路径: {provider_uri}")

calendars_dir = provider_uri / "calendars"
if calendars_dir.exists():
    print(f"\n可用的日历文件:")
    for cal_file in sorted(calendars_dir.glob("*.txt")):
        print(f"  - {cal_file.name}")
        # 读取文件内容
        with open(cal_file, 'r') as f:
            lines = f.readlines()
            print(f"    文件包含 {len(lines)} 行")
            if len(lines) > 0:
                print(f"    首行: {lines[0].strip()}")
                print(f"    末行: {lines[-1].strip()}")
else:
    print(f"\n日历目录不存在: {calendars_dir}")

# 4. 检查不同频率的差异
print(f"\n不同频率的日历数量对比:")
for freq in ['1min', '5min', '30min', 'day', 'week', 'month']:
    try:
        cal = D.calendar(freq=freq)
        print(f"  {freq:>6}: {len(cal):>6} 个时间点")
    except Exception as e:
        print(f"  {freq:>6}: 加载失败 - {e}")
