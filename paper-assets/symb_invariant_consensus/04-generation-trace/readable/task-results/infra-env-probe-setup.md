# infra env probe setup

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_env-probe-setup_20260515T084922_result.json`
- **Structured JSON:** [`927d5f15ba29a7fb90ec.json`](../../sessions/92/927d5f15ba29a7fb90ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ModelScope 正在下载，速度 1.5-3 MB/s，已下载 831MB。QwQ-32B 约 65GB，预计下载需要较长时间。

以下是当前已完成的全部环境搭建和数据准备的汇报：

---

### 产出汇报

| 项目 | 结果 |
|------|------|
| **GPU** | NVIDIA RTX PRO 6000 Blackwell Server Edition, **98GB VRAM** |
| **CUDA** | 12.8 (nvcc V12.8.93) |
| **Python 环境策略** | **conda** (`/root/miniconda3`, Python 3.12.3, base 环境) |
| **核心依赖** | 全部已装：z3-solver 4.15.4, sympy 1.14.0, datasets 4.8.4 ✅ |
| **ML 依赖** | torch 2.11.0+cu130, transformers 5.8.1, accelerate 1.13.0 ✅ |
| **vllm** | 已安装 v0.20.2 ✅（VRAM 98GB ≥ 40GB） |
| **QwQ-32B 模型** | 通过 ModelScope 后台下载中 (PID=92103)，~65GB，预计数小时 |
| **MATH-500 子集** | `/root/symb_invariant_consensus/data/math500_subset.json` ✅ |
| **分层分布** | Level 1: 10, Level 2: 10, Level 3: 10, Level 4: 10, Level 5: 10 (共 50 题) |
| **磁盘** | 根分区 30GB (50% used, 16GB free)；数据盘 250GB (8% used, 232GB free) |

QwQ-32B 模型下载是唯一未完成的项，后台进程运行中。可用 `tail /root/autodl-tmp/model_download_qwq_ms.log` 监控进度。

---
