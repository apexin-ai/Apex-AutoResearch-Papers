# ssh rename safety eval

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rename_safety_eval_20260513T204556_result.json`
- **Structured JSON:** [`8c0e444e249199bdaaf0.json`](../../sessions/8c/8c0e444e249199bdaaf0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成，编制评估报告。

---

## 安全评估报告：`/root/structfuse` → `/root/structfuse-context` 重命名

### 结论：**CONDITIONAL** — 裸 `mv` 会破坏正在运行的训练，但 `mv` + 符号链接方案可行

---

### 1. 进程 CWD 分析

| PID | 进程 | CWD | 风险 |
|-----|-------|-----|------|
| 73544 | m2_full_qwen (bash wrapper) | `/root/structfuse` | 见下 |
| 73558 | python train.py (qwen 实际训练) | `/root/structfuse` | 见下 |
| 74122 | m2_full_starcoder (bash wrapper) | `/root/structfuse` | 见下 |
| 209827 | batch_extract.py (M1 重提取) | `/root/structfuse` | 见下 |

Linux 上 `mv` 是 inode 级操作——进程 CWD 跟随 inode 移动，`os.getcwd()` 会返回新路径。**CWD 本身不会断。**

### 2. 文件描述符分析

| PID | 打开的文件 | 是否在 /root/structfuse/ 下 |
|-----|-----------|---------------------------|
| 73544 | `/root/runs/structfuse-context/m2_full_qwen.log` | 否 ✓ |
| 73558 | `/root/runs/m2_full_qwen/random_s42.log`, `/root/autodl-tmp/structfuse/wandb_logs/...`, nvidia devices, pipes | 否 ✓ |
| 74122 | `/root/runs/structfuse-context/m2_full_starcoder.log` | 否 ✓ |
| 209827 | pipes, /dev/null, /dev/pts | 否 ✓ |

**所有 fd 都不指向 `/root/structfuse/` 目录下的文件。** 数据文件在 `/root/autodl-tmp/structfuse/`，日志在 `/root/runs/`，不受影响。

### 3. 致命风险：Bash 变量中的硬编码绝对路径

**这是唯一的 breaking point。** 两个训练脚本把 `/root/structfuse` 存在 bash 变量里，后续循环迭代会用这些变量启动新 python 进程：

**run_m2_full_qwen.sh (第 20 行):**
```bash
TRAIN_SCRIPT="/root/structfuse/training/train.py"
# 每轮循环执行: python "${TRAIN_SCRIPT}" ...
```
当前 run (random_s42) 结束后，下一个 run 尝试 `python /root/structfuse/training/train.py` → **文件不存在，崩溃**

**run_m2_full_starcoder.sh (第 21 行):**
```bash
PROJECT_ROOT="/root/structfuse"
# 每轮执行: python -u "${PROJECT_ROOT}/training/train.py" ...
```
同理，starcoder 当前可能还在 Phase 1 数据构建阶段，后续的 `BUILD_SCRIPT="${PROJECT_ROOT}/scripts/build_m1_training_data.py"` 和所有训练调用都会断。

### 4. M1 重提取 (batch_extract.py)

- `rerun_m1_failed.sh` 在开头 `cd /root/structfuse`（已执行完毕）
- `batch_extract.py` 不包含硬编码 `/root/structfuse` 路径（grep 确认）
- CodeQL 查询路径在进程内动态解析（基于 CWD 或 `__file__`），rename 后 CWD 返回新路径
- **M1 重提取不受影响**（前提是用符号链接方案）

### 5. Editable Install

无。`site-packages` 中没有 `structfuse` 包。

### 6. 硬编码 `/root/structfuse` 路径清单

**正在运行的脚本（会影响当前进程）：**
| 文件 | 行号 | 内容 |
|------|------|------|
| `run_m2_full_qwen.sh` | 20 | `TRAIN_SCRIPT="/root/structfuse/training/train.py"` |
| `run_m2_full_starcoder.sh` | 21 | `PROJECT_ROOT="/root/structfuse"` |
| `scripts/rerun_m1_failed.sh` | 22 | `cd /root/structfuse` (已执行，无影响) |

**未在运行但需要清理的文件：**
| 文件 | 行号 | 内容 |
|------|------|------|
| `scripts/build_p2b_data.py` | 14 | `OUTPUT_DIR = "/root/structfuse/mvp_data/training_data"` |
| `scripts/run_p2b_all.sh` | 5,11,13 | `cd /root/structfuse`, DATA_DIR, MODEL 路径 |
| `scripts/eval_p2b.py` | 99,100 | model-name, val-file 默认值 |
| `scripts/run_eval_all.sh` | 6,10 | cd, MODEL 路径 |
| `scripts/run_m1_extraction.sh` | 12 | `cd /root/structfuse` |
| `scripts/eval_p2b_pooled.py` | 137,138 | model-name, val-file 默认值 |
| `scripts/run_eval_p50.sh` | 6,10 | cd, MODEL 路径 |
| `scripts/run_eval_5missing.sh` | 6,10 | cd, MODEL 路径 |
| `scripts/run_50repo_overlap.py` | 26,27 | CodeQL QL 文件路径 |
| `scripts/run_m2_pilot.sh` | 18 | `cd /root/structfuse` |
| `scripts/build_full_m2_data.sh` | 22 | `PROJECT_ROOT="/root/structfuse"` |
| `scripts/run_full_m2_training.sh` | 42 | `PROJECT_ROOT="/root/structfuse"` |
| `scripts/compute_full_z_percent.py` | 30 | 输出路径默认值 |
| `mvp_phase1.py` | 18 | `CODEQL_QUERIES = Path("/root/structfuse/extraction/codeql_queries")` |

---

### 建议方案：`mv` + 符号链接（现在就可以做）

```bash
# Step 1: 重命名
mv /root/structfuse /root/structfuse-context

# Step 2: 创建符号链接，让旧路径仍可访问
ln -s /root/structfuse-context /root/structfuse
```

**效果：**
- 所有正在运行的进程中的硬编码 `/root/structfuse/...` 路径通过符号链接透明解析，不会中断
- 新启动的命令使用 `/root/structfuse-context` 即可
- M1 重提取、两个 M2 训练全部 9 runs 正常跑完

**后续清理（所有训练跑完后）：**
1. 删除符号链接 `rm /root/structfuse`
2. 批量替换上述清单中的硬编码路径 `sed -i 's|/root/structfuse|/root/structfuse-context|g'`

---
