# fix exp003s2 restart

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp003s2-restart_20260519T235657_result.json`
- **Structured JSON:** [`470164df853a74de24b7.json`](../../sessions/47/470164df853a74de24b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本 import 正常。checkpoint 目录是空的（之前 step 12 被 kill 后无残留），无需额外清理。

## 报告

### 1. 崩溃原因
```
FileNotFoundError: No usable temporary directory found in ['/tmp', '/var/tmp', '/usr/tmp', '/root/contrastive_entrain_calib']
```
**根分区 100% 满（30G/30G，仅剩 16K）**，导致 `/tmp` 不可写。Python `tempfile` 模块在 `dill` 初始化时失败，`import torch` 直接崩溃。

空间占用大户：`.cache/pip` 3.8G、`.cache/huggingface` 5.9G、`miniconda3/pkgs` 524M。

### 2. 修复措施
- 清理 pip 缓存：`pip cache purge` → 释放 3.8G
- 清理 conda 包缓存：`conda clean --all -y` → 释放 ~107M
- 根分区恢复到 **3.8G 可用**（88% 使用率）

### 3. 验证结果
- `import torch` ✅ (torch=2.8.0+cu128, cuda=True)
- `from training.run_exp003s2_r3only import *` ✅
- `/root/autodl-tmp/checkpoints/exp003_r3only_seed2/` 目录为空，无残留冲突

### 4. GPU 状态
| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| 0 | RTX PRO 6000 Blackwell (98GB) | **0 MiB** | **0%** ✅ 空闲 |
| 1 | RTX PRO 6000 Blackwell (98GB) | 38161 MiB | 95% (有其他任务) |

**GPU 0 空闲，可立即重启 exp-003-s2。**

---
