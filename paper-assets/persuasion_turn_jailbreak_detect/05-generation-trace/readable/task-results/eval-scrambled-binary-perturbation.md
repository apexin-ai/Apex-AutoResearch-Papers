# eval scrambled binary perturbation

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_scrambled-binary-perturbation_20260518T064731_result.json`
- **Structured JSON:** [`59ef8d2099d73f186af0.json`](../../sessions/59/59ef8d2099d73f186af0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

### Eval 2: Binary Labels Perturbation (plan_013) -- 完成

| K | Clean F1 | Perturbed F1 | Delta |
|---|---|---|---|
| full | 1.000 | 1.000 | **0.000** |
| k=5 | 1.000 | 1.000 | **0.000** |
| k=3 | 1.000 | 1.000 | **0.000** |
| k=2 | 1.000 | 0.974 | **-0.026** |
| k=1 | 1.000 | 0.908 | **-0.092** |

**Hypothesis partially falsified**: Binary 模型在 k>=3 和 full 时与 9-class 一样零退化，但在 k=1 (-0.092) 和 k=2 (-0.026) 时退化，与 JB MLM 量级相当。说明 fine-grained 9-class labels 对早期 turn 的 perturbation robustness 有额外贡献。

### Eval 1: Scrambled Labels Perturbation (plan_003) -- **BLOCKED**

**plan_003 scrambled checkpoint 不存在**。服务器上 `checkpoints/` 目录没有 `plan_003_scrambled`，`autodl-tmp/checkpoints_backup/` 也没有。只找到数据目录 `data/plan_003_v2`。需要重新训练 scrambled DeBERTa + GRU 才能做 perturbation eval。

### 当前 perturbation robustness 全景（delta, full turns）

| Model | Delta (full) |
|---|---|
| 9-class treatment | **0.000** |
| Binary (plan_013) | **0.000** |
| JB MLM (plan_017) | -0.026 |
| Vanilla baseline | -0.118 |
| Wiki MLM (plan_018) | -0.121 |
| Scrambled (plan_003) | **TBD (checkpoint missing)** |

---
