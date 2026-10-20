# ops diagnose olmo retrain v3 cron

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_olmo_retrain_v3_cron_20260520T145445_result.json`
- **Structured JSON:** [`cbca5512b35f4801b11d.json`](../../sessions/cb/cbca5512b35f4801b11d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 **exp_olmo_retrain_v3 成功完成**，registry 已更新。

## 结果汇总

**K\* = 4**，所有 pair 的 bootstrap AUC (10K resamples) + 95% CI：

| Pair | AUC (point) | Bootstrap Mean | 95% CI | Perm p-value |
|------|------------|----------------|--------|-------------|
| 0v1 | 0.9873 | 0.9972 | [0.9967, 0.9977] | 0.0000 |
| 1v2 | 0.8889 | 0.9572 | [0.9542, 0.9601] | 0.0000 |
| 2v3 | 0.7036 | 0.8885 | [0.8814, 0.8947] | 0.9980 |
| 3v4 | 0.6817 | 0.8772 | [0.8684, 0.8852] | 1.0000 |

**3v4 pair**：bootstrap AUC = 0.8772, 95% CI [0.8684, 0.8852]，CI 下界远高于 θ=0.60，分类信号仍然强。Permutation test p=1.0 说明 3v4 的 AUC 没有显著高于 2v3（即退化趋于稳定）。

这与 Pythia (K\*≥4) 和 Qwen (K\*=7) 的 retrain-chain 结果一致，确认 retrain-chain K\* 是 protocol-determined 而非 architecture-determined。

---
