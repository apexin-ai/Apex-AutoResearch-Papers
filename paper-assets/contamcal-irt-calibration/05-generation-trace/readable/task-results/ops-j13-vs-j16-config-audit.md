# ops j13 vs j16 config audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_j13_vs_j16_config_audit_20260517T164448_result.json`
- **Structured JSON:** [`e16c7432bd179e6fa71b.json`](../../sessions/e1/e16c7432bd179e6fa71b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已收集完毕，汇报如下：

---

## 汇报

### 1. `pooled_irt_2pl_gamma_n16_fixed/` 模型列表

| Benchmark | J | Scales | 模型组成 |
|-----------|---|--------|---------|
| MMLU | **16** | 1.5B + 3B | 8×1.5B (d000/d005/d025/d100 × s42/s123) + 8×3B (同) |
| ARC | **16** | 1.5B + 3B | 同上 |
| GSM8K | **24** | 0.5B + 1.5B + 3B | 8×0.5B + 8×1.5B + 8×3B |

0.5B 被排除出 MMLU 和 ARC（D045 exclusion: position bias），GSM8K 保留 0.5B。

### 2. `pooled_irt_all_scales/` 模型列表

| Benchmark | J | 说明 |
|-----------|---|------|
| MMLU | **15** | 比 n16_fixed 少 `3B_d000_s123` |
| ARC | **13** | 少 `1.5B_d025_s123`, `1.5B_d100_s123`, `3B_d000_s123` |
| GSM8K | **20** | 少 `0.5B_d100_s123`, `1.5B_d025_s123`, `1.5B_d100_s123`, `3B_d000_s123` |

`all_scales` 是 s123 信号计算完成之前的**不完整快照**，不是有意设计的 J=13 配置。缺失的全是 s123 seed 的模型。

### 3. J=13 的定义

J=13 并非一个刻意设计的配置。它只是 `pooled_irt_all_scales/arc_challenge` 中恰好有 13 个模型数据可用时的状态。

### 4. Table 4 实际配置

**Table 4 使用 `pooled_irt_2pl_gamma_n16_fixed/`，实际 J=16（MMLU & ARC）/ J=24（GSM8K）。**

论文 caption 写 "J=13 configuration" 是错的，需要修正为 J=16（或注明 GSM8K 为 J=24 因包含 0.5B）。

---
