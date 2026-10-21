# openvla_spatial_standardized_v1 实验失败诊断

## 失败摘要

| 项目 | 详情 |
|------|------|
| 失败 Phase | **无**（在 import 阶段崩溃，0 个 phase 执行） |
| 失败文件 | `/root/autodl-tmp/vla-ssd/scripts/libero_spatial_full_pipeline.py:26` |
| 错误类型 | `ImportError: cannot import name 'AutoModelForVision2Seq' from 'transformers'` |
| GPU 时间浪费 | ~5.74 小时（全部用于等待 checkpoint 下载，非 GPU 计算） |

## Traceback

```
Traceback (most recent call last):
  File "/root/autodl-tmp/vla-ssd/scripts/libero_spatial_full_pipeline.py", line 26, in <module>
    from transformers import AutoModelForVision2Seq, AutoProcessor
ImportError: cannot import name 'AutoModelForVision2Seq' from 'transformers' (/root/miniconda3/lib/python3.12/site-packages/transformers/__init__.py)
EXIT_CODE=1
```

## 已完成 Phase

**无。** 脚本从 09:37 开始等待 checkpoint 下载（15GB），到 15:21 下载完成后立即在 import 阶段崩溃，6 个 phase 均未执行。

结果目录 `/root/autodl-tmp/vla-ssd/results/libero_spatial/` 不存在。

## 根因分析

### transformers 版本不兼容

| 事实 | 值 |
|------|-----|
| 当前 transformers 版本 | **5.9.0** |
| 安装时间 | 2026-05-22 10:21:51（今天） |
| `AutoModelForVision2Seq` 存在 | **否**（5.x 已移除） |
| `AutoModelForImageTextToText` 存在 | **是**（5.x 替代类） |

`AutoModelForVision2Seq` 是 transformers 4.x 的类名，在 4.45+ 被重命名为 `AutoModelForImageTextToText`，5.x 彻底移除了旧名。

服务器上 transformers 在今天 10:21 被更新到 5.9.0，而 pipeline 脚本仍使用旧 import。

### 代码现状

`libero_spatial_full_pipeline.py` **已被修复**为 `AutoModelForImageTextToText`（当前代码 vs 日志中的错误不同），但实验未重新运行。

**其他脚本仍有同样问题：**
- `libero_object_full_pipeline.py`
- `libero_long_full_pipeline.py`
- `libero_object_untrained_full_pipeline.py`
- `libero_goal_full_pipeline.py`
- `counterfactual_batch.py`
- `libero_long_full_pipeline.py.bak`

## 修复建议

### 方案 A：修复 import（推荐）

将所有脚本中的 `AutoModelForVision2Seq` 替换为 `AutoModelForImageTextToText`：

```bash
cd /root/autodl-tmp/vla-ssd
grep -rl "AutoModelForVision2Seq" scripts/ | xargs sed -i 's/AutoModelForVision2Seq/AutoModelForImageTextToText/g'
```

`libero_spatial_full_pipeline.py` 已修复，只需修复其余 5 个文件 + 1 个 .bak，然后重跑实验。

### 方案 B：降级 transformers

```bash
pip install transformers==4.51.3
```

回到 4.x 可以保留旧 import，但不推荐——5.x 可能有模型加载优化且最终需要迁移。

### 方案 C：兼容写法

```python
try:
    from transformers import AutoModelForVision2Seq
except ImportError:
    from transformers import AutoModelForImageTextToText as AutoModelForVision2Seq
```

不推荐——增加复杂性，不如直接改名。

**推荐方案 A**，修复剩余脚本后重跑 `openvla_spatial_standardized_v1`。由于 checkpoint（15GB）已下载完成，重跑时不会再有 5+ 小时的等待。
