# check westd cwm eval results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_westd-cwm-eval-results_20260514T115455_result.json`
- **Structured JSON:** [`a3fa4d27abbe61a7c3ef.json`](../../sessions/a3/a3fa4d27abbe61a7c3ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## GPU 状态
4 卡全部占用，**GPU 0/1 未释放**（CWM eval 仍在跑）。

| GPU | 显存 | 利用率 | 任务 |
|-----|------|--------|------|
| 0 | 13.0/32.6 GB | 88% | CWM v12 eval |
| 1 | 13.0/32.6 GB | 70% | CWM seed123 eval |
| 2 | 31.5/32.6 GB | 97% | CWM 8B 训练 |
| 3 | 23.6/32.6 GB | 99% | CLS 8B seed123 训练 |

## CWM Eval 进度（仍在跑）

| 任务 | 进度 | running_acc | ETA |
|------|------|-------------|-----|
| **CWM v12** | 6192/9784 (63.3%) | 57.9% | ~6h → 约 02:00 AM |
| **CWM seed123** | 6112/9784 (62.5%) | 58.6% | ~6.3h → 约 02:15 AM |

速率约 ~6.2s/sample，两个 eval 预计凌晨 2 点左右完成。

## 8B 训练当前 step

| 任务 | 最新 checkpoint | 启动时间 |
|------|----------------|----------|
| **CWM 8B** (Qwen3-8B, seed42) | checkpoint-900 | 13:48 |
| **CLS 8B seed123** (Qwen3-8B, seed123) | checkpoint-1600 | 13:48 |

---
