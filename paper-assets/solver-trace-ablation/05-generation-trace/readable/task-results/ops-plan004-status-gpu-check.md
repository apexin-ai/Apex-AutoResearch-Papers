# ops plan004 status gpu check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan004-status-gpu-check_20260515T060134_result.json`
- **Structured JSON:** [`469e38ee0bbfc4283905.json`](../../sessions/46/469e38ee0bbfc4283905.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### plan004-o1-ablation-s42 状态：**已完成**

训练正常跑完 500 步（52 分钟），checkpoint-500 已保存。模型权重 ~15GB。

训练日志最终统计：
- prove_rate: 0.658, mean_isr: 0.653, parse_rate: 1.0

### Eval 指标（eval_sta.py, proofwriter_fol_100.jsonl）

| 指标 | 值 |
|------|-----|
| Prove Rate (PR) | **63.0%** (63/100) |
| Mean ISR | **0.0072** (std=0.029) |
| Median ISR | 0.000 |
| Proved-only ISR | 0.0115 |
| Max ISR | 0.190 |

按 answer_type 分：
- true: 24/34 proved (70.6%), ISR=0.007
- unknown: 25/41 proved (61.0%), ISR=0.010
- false: 14/25 proved (56.0%), ISR=0.004

**关键观察**：ISR 极低（~0.01），100 个样本中绝大多数 ISR=0.000，仅有少数几个非零（max=0.190）。模型生成大量重复 ground facts（如 folio_765 输出了 62+ 重复前提），每个 clause 被重复多次，per-clause ablation 删任一重复不影响结果，所以 ISR 趋近于 0。这符合 C006 描述的 "exec-only 的 low ISR = 冗余编码" 模式。

### GPU 健康

| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| cuda:0 | RTX PRO 6000 Blackwell | **0 MiB / 97887 MiB** | 0% |
| cuda:1 | RTX PRO 6000 Blackwell | **0 MiB / 97887 MiB** | 0% |

**两张 GPU 完全空闲**，eval 进程已结束。cuda:0 和 cuda:1 均可用于新实验。

---
