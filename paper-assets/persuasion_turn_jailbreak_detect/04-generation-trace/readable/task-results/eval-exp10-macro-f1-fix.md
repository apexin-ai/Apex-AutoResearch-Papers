# eval exp10 macro f1 fix

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp10-macro-f1-fix_20260518T171132_result.json`
- **Structured JSON:** [`64d8eb400d618d673c21.json`](../../sessions/64/64d8eb400d618d673c21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### exp10 few-shot (Qwen3-8B, 3-shot) — macro F1 补算

Per-sample predictions 仅保存了 `full`，k1-k5 通过 precision/recall/样本数反推 confusion matrix 计算。`full` 两种方法交叉验证一致。

**DD (Dangerous Demonstrations):**

| K | binary_f1 | macro_f1 | TP | FP | FN | TN |
|---|-----------|----------|----|----|----|----|
| k1 | 0.0247 | **0.2575** | 1 | 0 | 79 | 38 |
| k2 | 0.1609 | **0.3355** | 7 | 0 | 73 | 38 |
| k3 | 0.3838 | **0.4693** | 19 | 0 | 61 | 38 |
| k5 | 0.4158 | **0.4894** | 21 | 0 | 59 | 38 |
| full | 0.5405 | **0.5663** | 30 | 1 | 50 | 37 |

**ActorAttack:**

| K | binary_f1 | macro_f1 | TP | FP | FN | TN |
|---|-----------|----------|----|----|----|----|
| k1 | 0.2796 | **0.4055** | 13 | 0 | 67 | 38 |
| k2 | 0.3158 | **0.4274** | 15 | 0 | 65 | 38 |
| k3 | 0.4906 | **0.5376** | 26 | 0 | 54 | 38 |
| k5 | 0.6325 | **0.6356** | 37 | 0 | 43 | 38 |
| full | 0.6612 | **0.6523** | 40 | 1 | 40 | 37 |

### exp5 zero-shot (Qwen3-8B)

- DD: binary_f1 = 0.0000, **macro_f1 = 0.2436** (全部预测为 benign，TP=0)
- ActorAttack: exp5 中没有 ActorAttack 数据集（只有 dd_ood 和 fitd_ood）

零-shot 的 `llm_judge_ood.py` 同样使用 `average="binary"`，也需要统一为 macro。

---
