# ops verify train py consistency

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-train-py-consistency_20260515T144312_result.json`
- **Structured JSON:** [`47f12a3b843646782eb6.json`](../../sessions/47/47f12a3b843646782eb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**`/root/structfuse` 是指向 `/root/structfuse-context` 的符号链接（symlink）。两个路径指向同一个目录，不存在不一致问题。**

具体证据：

| 检查项 | 结果 |
|--------|------|
| `/root/structfuse` | `symbolic link -> /root/structfuse-context` |
| train.py inode | 两个路径都是 `25993484623`，同一个文件 |
| training/ 目录 inode | 都是 `25872658963` |
| 文件大小/时间戳 | 完全一致（25494 bytes, May 15 03:38） |
| training/ 下所有文件 inode | 全部一致 |

**脚本引用路径：**
- `run_m2_full_bm25_qwen.sh` 第14行：`PROJECT_ROOT="/root/structfuse"` → 解析到 `/root/structfuse-context/training/train.py`
- `run_m2_full_bm25_starcoder.sh` 第16行：`PROJECT_ROOT="/root/structfuse"` → 同上

**两个脚本用的是同一份 train.py，M2 Qwen 和 StarCoder 结果可比。不需要任何修复。**

---
