# check full status westd

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_full-status-westd_20260514T051859_result.json`
- **Structured JSON:** [`df1d91b3284d06aef3fd.json`](../../sessions/df/df1d91b3284d06aef3fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## GPU 状态

| GPU | 利用率 | 显存 | 状态 |
|-----|--------|------|------|
| 0 | 88% | 13.0/31.8 GB | **BUSY** — eval_cwm_seed123 |
| 1 | 87% | 13.0/31.8 GB | **BUSY** — eval_cwm_v12 |
| 2 | 0% | 0/31.8 GB | **空闲** |
| 3 | 0% | 0/31.8 GB | **空闲** |

---

## 已完成 Eval（CLS 分类任务）

| 模型 | Checkpoint | Acc | F1 macro | fail F1 | pass F1 | Unparseable |
|------|-----------|-----|----------|---------|---------|-------------|
| **8B-conda** | default (最终) | 70.22% | 68.21% | 60.2% | 76.2% | 136 (1.4%) |
| **8B-conda** | **ckpt-400** | **84.52%** | **80.89%** | **72.6%** | **89.2%** | 136 (1.4%) |
| **8B-conda** | ckpt-600 | 78.51% | 74.56% | 64.5% | 84.6% | 136 (1.4%) |
| v5-conda | default (最终) | 52.96% | 52.89% | 51.0% | 54.8% | 132 (1.3%) |
| v5-conda | ckpt-400 | 78.43% | 68.41% | 50.6% | 86.2% | 132 (1.3%) |
| v5-conda | ckpt-600 | 76.37% | 71.17% | 58.9% | 83.4% | 132 (1.3%) |

**8B-conda ckpt-400 是 CLS 最佳结果**：Acc 84.5%, F1 macro 80.9%。两个模型都在 ckpt-400 之后出现过拟合退化，最终 checkpoint 反而最差。

---

## 进行中 Eval（CWM 任务）

| 任务 | GPU | 进度 | Running Acc | 预计剩余 |
|------|-----|------|-------------|---------|
| eval_cwm_seed123 (ckpt-500) | 0 | 2400/9784 (24.5%) | **57.2%** | ~5.2h |
| eval_cwm_v12 (ckpt-500) | 1 | 2424/9784 (24.8%) | **58.5%** | ~5.1h |

速度约 ~8 samples/52s ≈ 0.15 samples/s，预计今晚 ~18:30 完成。

---

## 未 eval 的 Checkpoint

8B-conda 还有 **checkpoint-200** 未 eval（已 eval ckpt-400 和 ckpt-600）。考虑到 ckpt-400 已是最佳且 ckpt-200 训练更少，优先级不高。

---
