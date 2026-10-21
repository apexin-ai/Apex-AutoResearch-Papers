# analysis xnli mlp probe collect

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_xnli-mlp-probe-collect_20260522T062653_result.json`
- **Structured JSON:** [`95a43de3a9514abd177e.json`](../../sessions/95/95a43de3a9514abd177e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

## XNLI MLP Probe — C3 验证结果

**C3 成立：非线性 encoding 是冲突任务特有的。**

关键 EN→ZH 方向 MLP gains 对比：

| Model | XNLI EN→ZH Δ | Conflict EN→ZH Δ |
|-------|:-----------:|:----------------:|
| Qwen3 | **-2.0pp** | **+2.4pp** |
| Llama3.1 | **-0.5pp** | **+9.2pp** |

XNLI 上 MLP probe 相比 linear probe 完全没有增益（甚至为负），而冲突任务上 MLP 有显著提升。这说明冲突任务中 EN→ZH 方向的 representation 需要非线性变换才能解码，而这种 non-linear encoding 在普通 NLI 任务中不存在。

报告已保存至 `artifacts/xnli_mlp_probe_report.md` 并注册到 manifest。

---
