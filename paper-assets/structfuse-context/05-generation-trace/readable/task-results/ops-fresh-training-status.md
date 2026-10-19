# ops fresh training status

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fresh-training-status_20260516T023222_result.json`
- **Structured JSON:** [`88a3c360e9c0e69dca72.json`](../../sessions/88/88a3c360e9c0e69dca72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### GPU
| GPU | 型号 | 利用率 | 显存 |
|-----|------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 99% | 51GB / 98GB |
| 1 | RTX PRO 6000 Blackwell | 100% | 53GB / 98GB |

### 实验状态

| Exp | Model | Subrun | Step | Best R@1 | Best val_loss | PID | Status |
|-----|-------|--------|------|----------|---------------|-----|--------|
| **Qwen s43+** | Qwen2.5-Coder-3B | random_s43 | 1500 (ES) | **0.5554** | 0.4476 | - | Done |
| | | random_s44 | ES | **0.5542** | - | - | Done |
| | | embed_s43 | ES | **0.5655** | 0.4876 | - | Done |
| | | embed_s44 | 2000 (ES) | **0.5470** | 0.4341 | - | Done |
| | | dataflow_s43 | 1500 (ES) | **0.5541** | 0.4617 | 18427 | **Just finished** |
| | | dataflow_s44 | - | - | - | - | Not started |
| **StarCoder** | starcoder2-3b | embed_s42 | 1500 (ES) | **0.4376** | 0.6154 | - | Done |
| | | embed_s43 | **~100**/2810 | - | - | 130074 | **Training** |
| **SWE-bench** | random_s42 ckpt | 4/300 | - | - | - | 61328 | **DEAD (Terminated)** |

### 详情

**1. SWE-bench eval** — PID 61328 已死。全量 300 实例 eval 在第 4 个实例被 Terminated。100 实例子集已完成：
- R@1=**0.04**, R@5=0.11, R@10=0.14, R@20=0.16, MRR=0.070
- 指标极差，说明 random_s42 模型在 SWE-bench 跨 repo 检索上基本不可用

**2. Qwen dataflow_s43** — Early stop @1500，best R@1=0.5541（eval@1500 比 eval@500 的 0.5495 略有提升，未触发 early stop by R@1 下降）。val_loss 连续 2 次不改善触发 stop。进度 5/9，dataflow_s44 尚未启动（PID 18427 可能正在做 cleanup/wandb 写入）。

**3. StarCoder embed_s43** — 刚启动 ~27 分钟，step 100/2810。按 embed_s42 的速度（~25s/step），预计 **~19h** 完成全部 2810 步（如果不 early stop 的话）。embed_s42 在 step 1500 early stop，若 s43 类似，ETA **~10h**。

**4. 其他进程** — M1 re-extraction (batch_extract.py, 4 workers + CodeQL) 仍在运行（PID 209821, 已运行 2d6h）。

### Qwen 各 subrun 最佳 R@1 排名
1. embed_s43: **0.5655**
2. random_s43: **0.5554**
3. random_s44: **0.5542**
4. dataflow_s43: **0.5541**
5. embed_s44: **0.5470**

---
