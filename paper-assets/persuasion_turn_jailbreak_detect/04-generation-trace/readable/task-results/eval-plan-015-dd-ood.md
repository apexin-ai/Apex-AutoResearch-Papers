# eval plan 015 dd ood

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan_015_dd_ood_20260518T024643_result.json`
- **Structured JSON:** [`2930787ae274c252e161.json`](../../sessions/29/2930787ae274c252e161.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。结果汇总：

## Plan 015 DD OOD 评估结果

### Treatment (Persuasion DeBERTa + Mean Pooling) vs GRU

| K | MeanPool-T F1 | GRU-T F1 | Delta |
|---|---|---|---|
| k1 | 1.0000 | 1.0000 | +0.0000 |
| k2 | 1.0000 | 0.9904 | +0.0096 |
| k3 | 0.9937 | 0.9904 | +0.0033 |
| k5 | 1.0000 | 1.0000 | +0.0000 |
| full | 1.0000 | 1.0000 | +0.0000 |

### Baseline (Vanilla DeBERTa + Mean Pooling)

| K | Baseline F1 |
|---|---|
| k1 | 0.8286 |
| k2 | 0.6387 |
| k3 | 0.5614 |
| k5 | 0.3922 |
| full | 0.2947 |

### 结论：**comparable**

- GRU temporal modeling 在 DD OOD 场景**无额外价值**：mean pooling 与 GRU 表现几乎相同（均接近满分）
- **Persuasion embeddings 是核心驱动力**：baseline (vanilla DeBERTa + mean pooling) 在 DD 上 F1 仅 0.29 (full)，而 treatment 达到 1.0。这证明是 persuasion-grounded 表示（而非 temporal modeling）提供了 OOD 泛化能力
- 有趣的是 baseline 在 K=1 时 F1=0.83 但随 K 增大急剧下降，说明 vanilla embeddings 在单轮时有部分区分力但无法处理多轮对话的复杂模式

结果已保存至服务器 `results/plan_015_dd_eval.json`。

---
