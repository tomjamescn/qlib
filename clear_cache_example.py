"""清理qlib缓存示例脚本"""
import shutil
from pathlib import Path
from qlib import init
from qlib.config import C
from qlib.data.cache import H

def clear_all_cache():
    """清理所有qlib缓存"""

    print("=" * 60)
    print("开始清理 qlib 缓存")
    print("=" * 60)

    # 1. 清理内存缓存
    print("\n[1/3] 清理内存缓存...")
    try:
        H.clear()
        print("  ✓ 内存缓存已清理")
    except Exception as e:
        print(f"  ✗ 内存缓存清理失败: {e}")

    # 2. 清理磁盘缓存
    print("\n[2/3] 清理磁盘缓存...")

    # 获取数据路径
    try:
        data_path = Path(C.get_data_path())

        # features_cache
        features_cache = data_path / "features_cache"
        if features_cache.exists():
            shutil.rmtree(features_cache)
            print(f"  ✓ 已删除: {features_cache}")
        else:
            print(f"  - 不存在: {features_cache}")

        # dataset_cache
        dataset_cache = data_path / "dataset_cache"
        if dataset_cache.exists():
            shutil.rmtree(dataset_cache)
            print(f"  ✓ 已删除: {dataset_cache}")
        else:
            print(f"  - 不存在: {dataset_cache}")

    except Exception as e:
        print(f"  ✗ 磁盘缓存清理失败: {e}")

    # 3. 清理简单缓存
    print("\n[3/3] 清理简单缓存...")
    simple_cache = Path.home() / ".cache" / "qlib_simple_cache"
    if simple_cache.exists():
        try:
            shutil.rmtree(simple_cache)
            print(f"  ✓ 已删除: {simple_cache}")
        except Exception as e:
            print(f"  ✗ 删除失败: {e}")
    else:
        print(f"  - 不存在: {simple_cache}")

    print("\n" + "=" * 60)
    print("缓存清理完成！")
    print("=" * 60)
    print("\n提示: 下次加载数据时会重新生成缓存，可能会较慢")

if __name__ == "__main__":
    # 先初始化qlib（需要根据你的实际配置调整）
    try:
        init(provider_uri="~/.qlib/qlib_data/cn_data", region="cn")
    except Exception as e:
        print(f"初始化失败: {e}")
        print("请根据你的实际配置修改 provider_uri 参数")

    # 执行清理
    clear_all_cache()
