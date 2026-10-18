# gpu yi15 hires constrained mckp

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_yi15_hires_constrained_mckp_20260514T201826_result.json`
- **Structured JSON:** [`b46ecf9fe0306b719d77.json`](../../sessions/b4/b46ecf9fe0306b719d77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇报：

---

## Yi-1.5-9B Hires Constrained MCKP — 结果

| Method | PPL | Delta vs uniform |
|---|---|---|
| Baseline (bf16) | 7.0157 | — |
| **Hires MCKP (k=2)** | **7.2181** | **-0.0009** |
| Uniform 4-bit | 7.2171 | — |
| Std MCKP (k=2, ref) | 7.2209 | -0.0038 |
| Std MCKP (k=8, ref) | 7.3129 | -0.0958 |

**Verdict: FAIL**

**Bit distribution:** 4-bit=189, 8-bit=1, 2-bit=2
- 2-bit heads: L22H1, L24H3（最不敏感的 heads）
- 8-bit heads: L6H2
- **L4H3 保持 4-bit**（未升到 8-bit）

**Concentration:** hires=0.7139 vs standard=0.4934

**对比 standard profiling：** Hires 数据将 k=2 的 gap 从 -0.0038 缩窄到 -0.0009，但仍然无法翻盘。

**根因分析：** L4H3 的 outlier 极端集中在 2-bit 层级（delta=13.12），但其 4-bit delta=0.0048、8-bit delta=0.0040 几乎为零。这意味着：
1. Solver 已经通过避免将 L4H3 降到 2-bit 来规避了最大损失
2. 将 L4H3 从 4-bit 升到 8-bit 几乎无收益（delta 差仅 0.0008）
3. Yi-1.5-9B 的 heterogeneity 是 **spike pattern**（单点极端但窄带），不是 **spread pattern**（多 head 在多 bitwidth 下有差异），solver 在 4-bit/8-bit 层级没有优化空间

---
