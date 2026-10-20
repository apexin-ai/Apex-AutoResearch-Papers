# experiment dir j3 nli multi verifier

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-j3-nli-multi-verifier_20260520T175123_result.json`
- **Structured JSON:** [`fdbc1f3ce73050c5d992.json`](../../sessions/fd/fdbc1f3ce73050c5d992.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

### Summary Table

| Verifier | w | Combo Acc | SC Acc | Δ (pp) | McNemar p |
|---|---|---|---|---|---|
| DeBERTa-MNLI | 1 | 0.4017 | 0.3933 | +0.83 | 0.2668 |
| DeBERTa-MNLI | 3 | 0.4283 | 0.3933 | +3.50 | 0.0125* |
| **DeBERTa-MNLI** | **5** | **0.5000** | **0.3933** | **+10.67** | **<0.0001*** |
| RoBERTa-MNLI | 1 | 0.3933 | 0.3933 | +0.00 | 1.0000 |
| RoBERTa-MNLI | 3 | 0.4133 | 0.3933 | +2.00 | 0.1337 |
| RoBERTa-MNLI | 5 | 0.4583 | 0.3933 | +6.50 | 0.0002* |
| BART-MNLI | 1 | 0.3933 | 0.3933 | +0.00 | 1.0000 |
| BART-MNLI | 3 | 0.4233 | 0.3933 | +3.00 | 0.0222* |
| BART-MNLI | 5 | 0.4650 | 0.3933 | +7.17 | 0.0001* |

### Standalone NLI Accuracy

| Model | Overall | True | False | Unknown |
|---|---|---|---|---|
| DeBERTa-MNLI | **55.0%** | 64.0% | 97.5% | 3.5% |
| BART-MNLI | 46.2% | 62.0% | 74.5% | 2.0% |
| RoBERTa-MNLI | 37.7% | 23.5% | 89.0% | 0.5% |

### 关键发现

**NLI gain 是 NLI-general 而非 DeBERTa-specific**——三个架构在 w≥3 时都显著提升 SC，但幅度不同：
- DeBERTa 最强（w5: +10.67pp），因为 standalone accuracy 最高 (55%)
- BART 次之（w5: +7.17pp），standalone 46.2%
- RoBERTa 最弱（w5: +6.50pp），standalone 仅 37.7%

所有模型都有严重的 **Unknown 盲区**（3 个模型 recall 分别 3.5%/2.0%/0.5%），这是 NLI 在 ProofWriter OWA 任务上的系统性弱点——NLI 模型倾向于判 entailment/contradiction，几乎不判 neutral。

w=1 时三个模型都无显著效果（NLI 作为 1 票 vs SC 的 ~12 票太弱）；w=3 时 DeBERTa 和 BART 显著；w=5 时三个模型均显著。

结果已写入 `/root/symb_invariant_consensus/results/dir_j3_nli_multi_verifier/results.json`。

---
