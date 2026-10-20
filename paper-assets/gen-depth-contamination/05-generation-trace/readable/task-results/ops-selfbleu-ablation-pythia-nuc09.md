# ops selfbleu ablation pythia nuc09

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_selfbleu_ablation_pythia_nuc09_20260521T123414_result.json`
- **Structured JSON:** [`80c411b3997a079d4902.json`](../../sessions/80/80c411b3997a079d4902.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报结果：

---

## 修复

- **Before**: Pythia 行指向 `data_exp020_pythia_greedy/features.csv`（greedy 数据，旧 1v2 AUC=.8840）
- **After**: 改为 `data_exp020_pythia_nuc09/features.csv`（nucleus p=0.9 数据）

## 全部结果（4 模型 × 15D/14D）

### Qwen-base (K\*_15D=2, K\*_14D=2)

| Pair | AUC_15D | CI_15D | AUC_14D | CI_14D | Delta |
|------|---------|--------|---------|--------|-------|
| 0v1 | .9874 | [.9858, .9889] | .9874 | [.9858, .9889] | −.0000 |
| **1v2** | **.6288** | [.6197, .6379] | **.6258** | [.6163, .6350] | −.0031 |
| 2v3 | .5548 | [.5449, .5647] | .5517 | [.5415, .5618] | −.0031 |
| 3v4 | .5269 | [.5165, .5374] | .5207 | [.5102, .5313] | −.0062 |
| 4v5 | .5195 | [.5093, .5302] | .5210 | [.5106, .5316] | +.0015 |

### Pythia-1.4B (K\*_15D=2, K\*_14D=2) — 修复后

| Pair | AUC_15D | CI_15D | AUC_14D | CI_14D | Delta |
|------|---------|--------|---------|--------|-------|
| 0v1 | .9947 | [.9937, .9956] | .9945 | [.9934, .9955] | −.0002 |
| **1v2** | **.6754** | [.6665, .6842] | **.6751** | [.6662, .6838] | −.0003 |
| 2v3 | .5593 | [.5491, .5693] | .5559 | [.5457, .5664] | −.0034 |
| 3v4 | .5235 | [.5130, .5341] | .5134 | [.5027, .5240] | −.0101 |
| 4v5 | .5009 | [.4894, .5122] | .5020 | [.4907, .5134] | +.0010 |

### LLaMA-8B (K\*_15D=2, K\*_14D=2)

| Pair | AUC_15D | CI_15D | AUC_14D | CI_14D | Delta |
|------|---------|--------|---------|--------|-------|
| 0v1 | .9229 | [.9180, .9277] | .9222 | [.9171, .9270] | −.0007 |
| **1v2** | **.6075** | [.5979, .6171] | **.6074** | [.5978, .6170] | −.0001 |
| 2v3 | .5273 | [.5169, .5380] | .5282 | [.5178, .5385] | +.0008 |
| 3v4 | .5284 | [.5178, .5392] | .5247 | [.5141, .5353] | −.0037 |
| 4v5 | .5158 | [.5048, .5266] | .5082 | [.4971, .5191] | −.0075 |

### Mistral-7B (K\*_15D=1, K\*_14D=1)

| Pair | AUC_15D | CI_15D | AUC_14D | CI_14D | Delta |
|------|---------|--------|---------|--------|-------|
| 0v1 | .9844 | [.9826, .9861] | .9842 | [.9824, .9859] | −.0002 |
| **1v2** | **.5902** | [.5801, .6001] | **.5903** | [.5803, .6003] | +.0002 |
| 2v3 | .5365 | [.5256, .5473] | .5337 | [.5228, .5446] | −.0028 |
| 3v4 | .5252 | [.5147, .5356] | .5273 | [.5164, .5381] | +.0021 |
| 4v5 | .5272 | [.5162, .5384] | .5252 | [.5142, .5358] | −.0020 |

## K\* 汇总

| Model | K\*_15D | K\*_14D | 变化 |
|-------|---------|---------|------|
| Qwen-base | 2 | 2 | 不变 |
| **Pythia-1.4B** | **2** | **2** | **不变** |
| LLaMA-8B | 2 | 2 | 不变 |
| Mistral-7B | 1 | 1 | 不变 |

## 结论

1. **Pythia-1.4B 修复前后对比**：旧 greedy 数据 1v2 AUC=.8840 → 新 nucleus 数据 1v2 AUC=.6754，差异显著。greedy 数据大幅高估了区分度。
2. **Ablation 结论不变**：所有 4 个模型移除 self_bleu 后 K\* 均不变（15D delta 全部在 ±.01 以内），self_bleu 对 K\* 判定无实质影响。
3. 结果已保存至 `artifacts/exp_14d_ablation_detail.json` 和 `artifacts/exp_14d_ablation_detail.csv`。

---
