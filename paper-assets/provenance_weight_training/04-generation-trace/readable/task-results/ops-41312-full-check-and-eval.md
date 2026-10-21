# ops 41312 full check and eval

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_41312_full_check_and_eval_20260518T052141_result.json`
- **Structured JSON:** [`96f9a78672c9094513e0.json`](../../sessions/96/96f9a78672c9094513e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

adaptive 在 97% (5911/6103)，约 7-8 分钟完成。

## 汇总报告

### westd-41312 实验状态

| GPU | 实验 | 状态 | Eval PPL | Eval Loss | Tokens |
|-----|------|------|----------|-----------|--------|
| cuda:0 | contamination_60_adaptive_seed456 | **运行中** (97%, ~7min) | - | - | - |
| cuda:1 | contamination_60_uniform_seed456 | **DONE + Eval 完成** | 17.769 | 2.8775 | 4,077,068 |
| cuda:2 | grid_b0_1_seed123 | **DONE + Eval 完成** | 17.646 | 2.8705 | 4,077,068 |
| cuda:3 | grid_b0_1_seed456 | **DONE + Eval 完成** | 17.663 | 2.8715 | 4,077,068 |

### 已完成操作
- 3 个已完成实验全部 eval 完毕
- eval_results.json 已保存到各 final/ 目录
- Registry 已更新（status=DONE, conclusion=success, metrics, checkpoint_path, log_path）

### 待处理
- contamination_60_adaptive_seed456 预计 ~7 分钟后完成，需要后续 eval

---
