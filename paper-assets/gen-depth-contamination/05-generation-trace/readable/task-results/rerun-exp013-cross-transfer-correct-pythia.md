# rerun exp013 cross transfer correct pythia

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_rerun_exp013_cross_transfer_correct_pythia_20260521T161340_result.json`
- **Structured JSON:** [`6bc067dc064ced97c315.json`](../../sessions/6b/6bc067dc064ced97c315.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Self K\***: OLMo=1, Pythia=2, Qwen=2（全部正确）

**K\* Transfer Matrix**:

| Train\Test | OLMo | Pythia | Qwen |
|------------|------|--------|------|
| OLMo       | 1    | 1 ✗    | 1 ✗  |
| Pythia     | 1 ✓  | 2      | 2 ✓  |
| Qwen       | 1 ✓  | 2 ✓    | 2    |

**Aggregate accuracy: 7/9 = 77.8%**（上次 greedy 数据 6/9 = 66.7%）

关键修正：**Pythia → Qwen** 从 K\*=1(✗) 变为 K\*=2(✓)。Nucleus Pythia 的 AUC(1v2)=0.6328 成功迁移到 Qwen（greedy 版本为 0.4882 随机水平）。

数据源：`data_exp020_pythia_nuc09/features.csv`（nucleus p=0.9, self AUC\_1v2=0.6756）。注意：`data_exp001_pythia/` 和 `data/exp_pythia14b_c4/` 均不存在于服务器上，使用了 exp020 的 nucleus 数据作为替代。

Artifact 已注册，服务器结果保存在 `results/exp013_olmo_rerun_v2/`。

---
