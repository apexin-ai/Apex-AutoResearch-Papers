# analysis t20 a060 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_t20_a060_s42_fp32_20260520T174009_result.json`
- **Structured JSON:** [`585649342aa692bb84a5.json`](../../sessions/58/585649342aa692bb84a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## T=20 α=0.60 验证结果

**Verdict: PASS** — 预测 PermG 0/8，观测 PermG 0/8。

### 核心发现

| Method | Fwd Sig | Rev Sig |
|--------|---------|---------|
| PermG (FDR) | 0/8 | 0/8 |
| Diff XCorr (FDR) | 6/8 | 6/8 |
| Threshold Onset | 6/8 | — |
| TY Granger | 3/8 | — |
| **Robust (K≥3)** | **3/8** | — |

### Sync-dip 结论

**α=0.60 sync dip 是结构性的，不是功效问题。** T=10→T=20 数据量翻倍后 PermG 仍为 0/8。

关键证据：
- Lead-lag 结构存在（Diff XCorr 6/8, Threshold 6/8），但 Granger 检验无法捕捉
- token_entropy→distinct_1 的 PermG raw p=0.048（名义显著），FDR 修正后 p=0.064（near-miss）
- 3 个 robust pairs 全部是 ece-based（ece→distinct_1/2/3），token_entropy 在此 α 值下只达 2/5 consensus

### 方向性

Diff XCorr fwd/rev 对称（6/6）——α=0.60 regime 下无法分辨因果方向，与 sync dip 的同步耦合机制一致。

### 产出

`artifacts/t20_a060_verify.json` 已注册（art_20260520_7356b6）。

---
