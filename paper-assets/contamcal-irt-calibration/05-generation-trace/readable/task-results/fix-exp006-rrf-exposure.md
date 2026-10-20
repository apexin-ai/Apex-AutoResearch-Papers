# fix exp006 rrf exposure

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp006_rrf_exposure_20260514T223737_result.json`
- **Structured JSON:** [`36a0eaa0b1a0f59c70ef.json`](../../sessions/36/36a0eaa0b1a0f59c70ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 修复结果

**Bug**: `load_exp002_signals()` 使用单一 `s1_embedding` 信号，导致同 dosage 下 0.5B 和 1.5B 的 exposure 值完全相同。

**Fix**: 改为 3-signal RRF fusion (S1+S2+S4)，S2 polarity flip，min-max 归一化到 [0,1]。

### GSM8K Pooled IRT

| | v2 (bug) | v3_rrf (fix) |
|--|----------|-------------|
| gamma | 0.187 (CI 含零) | **2.096** (CI=[0.97, 3.30], 排除零) |
| Rhat | 1.015 (NOT OK) | **1.009** (OK) |
| ESS | 330 (NOT OK) | **492** (OK) |
| 0.5B==1.5B exposure? | **是（bug）** | 否（正确区分） |

### ARC Pooled IRT

| | v2 (bug) | v3_rrf (fix) |
|--|----------|-------------|
| gamma | -2.347 | **-7.620** (更强负效应) |
| Rhat | 1.010 | **1.008** (改善) |
| ESS | 817 | **1133** (改善) |
| 0.5B==1.5B exposure? | **是（bug）** | 否（正确区分） |

3 个 artifacts 已注册：comparison report + GSM8K/ARC data summaries。

---
