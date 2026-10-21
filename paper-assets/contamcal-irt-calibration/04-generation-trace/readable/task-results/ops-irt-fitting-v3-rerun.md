# ops irt fitting v3 rerun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_irt-fitting-v3-rerun_20260520T060841_result.json`
- **Structured JSON:** [`6c07178070d5d1310a8e.json`](../../sessions/6c/6c07178070d5d1310a8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

IRT 2PL+γ fitting 完成，汇报如下：

| 项目 | 结果 |
|------|------|
| h5netcdf | 已安装（requirement already satisfied） |
| Respondent 数据 | **25/25** (5 families × 5 dosages) |
| Fitting | 成功完成，退出码 0，ADVI 20000 iterations，Average Loss = 1.6079e+05 |
| trace_mmlu.nc | **432MB**，内容完整 |

**trace_mmlu.nc 内容：**
- **Groups**: posterior, sample_stats, observed_data
- **Posterior variables**: `theta` (1×1000×25), `a` (1×1000×14042), `b` (1×1000×14042), `gamma` (1×1000×14042), `log_a` (1×1000×14042)
- **Dimensions**: 1 chain, 1000 draws, 25 respondents, 14042 items
- **Library**: ArviZ 1.1.0, PyMC 6.0.0

**Gamma (contamination effect) 摘要：**
- mean(γ) = 0.0251 ± 0.3593
- median(γ) = 0.0771
- 58.0% items with γ > 0

---
