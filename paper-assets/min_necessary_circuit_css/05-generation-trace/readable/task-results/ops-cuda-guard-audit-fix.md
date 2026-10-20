# ops cuda guard audit fix

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda-guard-audit-fix_20260513T021918_result.json`
- **Structured JSON:** [`aa0342083fefdc449871.json`](../../sessions/aa/aa0342083fefdc449871.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。以下是完整产出：

---

## 1. analysis_fix_v3.py 修复确认

| | 修改前 | 修改后 |
|---|---|---|
| 第 2 行 | `os.environ.setdefault("CUDA_VISIBLE_DEVICES", "5")` | `os.environ["CUDA_VISIBLE_DEVICES"] = "5"` |

已确认生效。

---

## 2. 全量 CUDA guard 扫描结果

| 文件 | torch 导入行 | guard 类型 | 状态 |
|------|-------------|-----------|------|
| `run_mvp.py` | L11 | 硬覆盖 `os.environ[...] = "5"` (L2) | ✅ 入口脚本，正确 |
| `run_arithmetic.py` | L13 | 硬覆盖 (L2) | ✅ 入口脚本，正确 |
| `run_phase_d_only.py` | L13 | 硬覆盖 (L6) | ✅ 入口脚本，正确 |
| `run_circus_fix.py` | L8 | 硬覆盖 (L3) | ✅ 入口脚本，正确 |
| `eval_faithfulness.py` | L5 | 硬覆盖 (L2) | ✅ 入口脚本，正确 |
| `analysis_fix_v3.py` | (间接) | 硬覆盖 (L2) — **刚修复** | ✅ 入口脚本，已修复 |
| `evaluation.py` | L11 | `setdefault` (L2) | ✅ 库模块，正确 |
| `edge_pruning_l0.py` | L18 | `setdefault` (L2) | ✅ 库模块，正确 |
| `ifr_discovery.py` | L19 | `setdefault` (L2) | ✅ 库模块，正确 |

**结论：所有文件 guard 均在 import torch 之前，且类型正确。除 `analysis_fix_v3.py`（已修复）外无其他问题。**

---

## 3. 修复文件清单

仅 1 个文件需修复：
- `/root/min_necessary_circuit_css/analysis_fix_v3.py` — `setdefault` → 硬覆盖

---

## 4. D022 根因补充调查

**python vs python3 关系：**
```
/root/miniconda3/bin/python  -> python3.12 (symlink)
/root/miniconda3/bin/python3 -> python3.12 (symlink)
```
两者指向同一个二进制 `python3.12`。系统 PATH 中没有独立的 `/usr/bin/python`，只有 conda 环境下的 `python`。

**当前运行的 `python`（非 python3）进程：**
- `python extraction/batch_extract.py` — 批量 CodeQL 提取（PID 577872 起，多进程）
- `python training/train.py` — M2 pilot 训练（PID 795791 起，多子进程）

**bash_history：** 文件不存在（`~/.bash_history: No such file or directory`），无法追溯历史命令。

**结论：** 该服务器上 `python` 和 `python3` 是同一个二进制（conda 的 python3.12）。被杀进程（D022）使用 `python` 而非 `python3` 启动，来源是 conda 环境下的默认调用习惯。当前仍有多个 `python` 进程在运行（extraction 和 training），它们通过 conda 的 `python` 符号链接执行，与直接调用 `python3` 效果完全相同。D022 被杀进程最可能是之前某次手动或脚本启动的 training/extraction 任务。

---
