# analysis 19828 wiki m035 verify

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_19828_wiki_m035_verify_20260520T035427_result.json`
- **Structured JSON:** [`8ac577b91046bad05853.json`](../../sessions/8a/8ac577b91046bad05853.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 19828 WikiText 验证结果

### a075_s43
- **config.json data_dir**: `data/wikitext103_5k` (WikiText 确认)
- **5method_leadlag.json**: 存在但为 pre-M035 版本，已用 M035 脚本重跑
- **M035 兼容**: 重跑（旧版 consensus 用 `peak_lag > 0`，计入了 positive lag 的 naive，K≥3 虚高 4/8→2/8）
- **PermG_fwd (FDR)**: 5/8
- **naive_fwd (M035 peak_lag<0)**: 1/8（仅 ece→distinct_1, lag=-1）
- **diff_fwd (FDR)**: 8/8
- **ThreshOnset**: 0/8
- **TY**: 1/8
- **K≥3 (M035 consensus)**: 2/8（ece→distinct_1: 3/5, ece→distinct_3: 3/5）
- **K≥3(3σ)**: 2/8（threshold_onset=0/8，3sigma 也是 0/8，不影响投票）

### a050_s43
- **config.json data_dir**: `data/wikitext103_5k` (WikiText 确认)
- **5method_leadlag.json**: 存在但为 pre-M035 版本，已用 M035 脚本重跑
- **M035 兼容**: 重跑（旧版 naive 方向反转导致 K≥3=1/8，修正后 ece pairs 被正确计入）
- **PermG_fwd (FDR)**: 6/8
- **naive_fwd (M035 peak_lag<0)**: 4/8（ece 全部 4 pair: lag=-1/-5/-5/-1）
- **diff_fwd (FDR)**: 6/8
- **ThreshOnset**: 0/8
- **TY**: 0/8
- **K≥3 (M035 consensus)**: 3/8（ece→distinct_1: 3/5, ece→distinct_2: 3/5, ece→perplexity: 3/5）
- **K≥3(3σ)**: 3/8

### M035 修正前后对比

| 实验 | K≥3 旧 (pre-M035) | K≥3 新 (M035) | 变化原因 |
|------|-------------------|---------------|---------|
| a075_s43 | 4/8 | 2/8 | token_entropy 4 pair 的 naive_lag 全为正(3-5)，旧版错误计入 |
| a050_s43 | 1/8 | 3/8 | ece 4 pair 的 naive_lag 全为负(-1/-5)，旧版错误排除 |

### Registry 更新需求

两个实验（`alpha_sweep_a075_s43`、`alpha_sweep_a050_s43`）当前 registry 无 5method 分析指标，需更新：

**alpha_sweep_a075_s43**:
- `metrics.perm_granger_fdr_forward_sig`: "5/8"
- `metrics.diff_xcorr_fdr_forward_sig`: "8/8"
- `metrics.naive_fwd_m035`: "1/8"
- `metrics.threshold_onset_forward_sig`: "0/8"
- `metrics.threshold_onset_3sigma`: "0/8"
- `metrics.ty_forward_sig`: "1/8"
- `metrics.K_ge3_m035`: "2/8"
- `metrics.dataset`: "wikitext"
- `notes`: 追加 M035 re-run 信息

**alpha_sweep_a050_s43**:
- `metrics.perm_granger_fdr_forward_sig`: "6/8"
- `metrics.diff_xcorr_fdr_forward_sig`: "6/8"
- `metrics.naive_fwd_m035`: "4/8"
- `metrics.threshold_onset_forward_sig`: "0/8"
- `metrics.threshold_onset_3sigma`: "0/8"
- `metrics.ty_forward_sig`: "0/8"
- `metrics.K_ge3_m035`: "3/8"
- `metrics.dataset`: "wikitext"

注：`alpha_sweep_a050_s43_fp32` 是 17855 上的独立 fp32 重跑，与 19828 上的原始 `a050_s43` 是不同实验。

---
