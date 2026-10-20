# analysis smollm3 k3 discrepancy resolve

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_smollm3_k3_discrepancy_resolve_20260519T193711_result.json`
- **Structured JSON:** [`b6607ec75654eb160211.json`](../../sessions/b6/b6607ec75654eb160211.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete analysis.

---

## Part 1: SmolLM3 K≥3 差异解决

### 根因

SmolLM3 **没有 `unified_5method.json`**。两个 Worker 用了不同的源文件：
- **"0/8" Worker** → 用了 `5method_leadlag.json` 的 consensus 字段（`robust_pairs: 0`）
- **"3/8" Worker** → 用了 `3sigma_recompute_v2.json`（`robust_pairs_K3_3sigma: "3/8"`）

差异原因：**`3sigma_recompute_v2.json` 对 naive_xcorr 不检查方向**（只查 `significant` 字段），导致 ECE 对被错误计入。

### 关键证据：ECE pairs 的 naive_xcorr forward peak_lag 全为负

| Pair | peak_lag | 含义 |
|------|---------|------|
| ece→d1 | **-1** | downstream 领先 canary |
| ece→d2 | **-1** | downstream 领先 canary |
| ece→d3 | **-2** | downstream 领先 canary |
| ece→mauve | **-3** | downstream 领先 canary |

对比 entropy pairs 全为正：d1/d2/d3 peak_lag=+5，mauve peak_lag=+4。

### 权威 8×5 矩阵（来自 `5method_leadlag.json`，应用方向检查）

| Pair | naive_xcorr | diff_xcorr | threshold_3σ | permG | TY | **K** |
|------|:-----------:|:----------:|:------------:|:-----:|:--:|:-----:|
| entropy→d1 | ✓ (lag=+5, p=0.023) | ✓ (fdr_p=0.0004) | ✗ (ds_onset=null) | ✗ (fdr_p=0.066) | ✗ | **2** |
| entropy→d2 | ✓ (lag=+5) | ✓ | ✗ (ds_onset=null) | ✗ | ✗ | **2** |
| entropy→d3 | ✓ (lag=+5) | ✓ | ✗ (ds_onset=null) | ✗ | ✗ | **2** |
| entropy→mauve | ✓ (lag=+4) | ✗ | ✗ (ds_onset=null) | ✗ | ✗ | **1** |
| ece→d1 | ✗ (lag=**-1**) | ✓ | ✗ (ds_onset=null) | ✓ | ✗ | **2** |
| ece→d2 | ✗ (lag=**-1**) | ✓ | ✗ (ds_onset=null) | ✓ | ✗ | **2** |
| ece→d3 | ✗ (lag=**-2**) | ✓ | ✗ (ds_onset=null) | ✓ | ✗ | **2** |
| ece→mauve | ✗ (lag=**-3**) | ✗ | ✗ (ds_onset=null) | ✗ | ✗ | **0** |

### 结论

- **K≥3(3σ) = 0/8**（正确值，应用方向检查）
- **K≥4(3σ) = 0/8**
- 3sigma_recompute_v2.json 的 3/8 是 bug：naive_xcorr 未检查 peak_lag 方向，把 ECE→d1/d2/d3 的 naive 误判为通过，K 从 2 升到 3

### 差异机制对比

| | `5method_leadlag.json` consensus | `3sigma_recompute_v2.json` |
|---|---|---|
| naive_xcorr 判定 | sig=true **AND** peak_lag>0 | sig=true only（忽略方向） |
| ECE→d1/d2/d3 naive | ✗（lag<0） | ✓（只看 p<0.05） |
| ECE→d1/d2/d3 K | 2（diff+perm） | 3（naive+diff+perm） |
| K≥3(3σ) | **0/8** | **3/8** |

---

## Part 2: Table 7 抽查（D105 3σ 一致性）

### Pythia-410M s42

- 文件：`5method_leadlag.json`（无 unified 版本）
- config: `"threshold_criterion": "3x_sigma_drift"` ✓
- 每个 threshold_onset 条目：`"threshold": "3x_sigma_drift"` ✓
- **3σ 确认** ✓

### OPT-1.3B s42

- `unified_5method.json` 存在，但 **params 中无 sigma 信息**，threshold_onset 条目也无 threshold 字段
- 底层 `5method_leadlag.json` 存在，config: `"threshold_criterion": "3x_sigma_drift"` ✓
- unified 文件由不同版本脚本生成，未记录 sigma level
- **3σ 可通过源文件确认** ✓，但 unified 文件本身存在审计盲区

### 抽查结论

两个模型的 threshold_onset 均使用 3σ，D105 一致性成立。但 OPT-1.3B 的 unified_5method.json 格式缺少 sigma 标注，建议补上。

---

## 总结

1. **SmolLM3 K≥3(3σ) = 0/8**（不是 3/8）
2. 差异来源 = `3sigma_recompute_v2.json` 的 naive_xcorr **方向盲判 bug**（hypothesis (b)）
3. 没有 `unified_5method.json`（hypothesis (c) 部分成立：Worker 用了不同文件，但不是 unified vs 5method_leadlag，而是 3sigma_recompute_v2 vs 5method_leadlag consensus）
4. Table 7 的 3σ 一致性：**通过**（两个抽查模型均确认使用 3x_sigma_drift）

---
