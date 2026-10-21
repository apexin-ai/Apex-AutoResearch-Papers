# analysis exp 007

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-007_20260519T185044_result.json`
- **Structured JSON:** [`54adb39dd7ccee656c1b.json`](../../sessions/54/54adb39dd7ccee656c1b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-007 分析完成。Registry 已更新为 DONE(success)。

## 结果汇总

### Cross-Architecture Std（340M vs 1.3B）

| Attention Ratio | 340M std | 1.3B std (ref) |
|---|---|---|
| pure (attn=0) | 0.0248 | 0.024 |
| h24-1 (attn=1) | **0.0116** | 0.016 |
| h12-1 (attn=2) | **0.0178 ↑** | 0.014 |
| h6-1 (attn=4) | **0.0110** | 0.006 |
| h3-1 (attn=8) | **0.0160 ↑** | 0.005 |

340M 呈锯齿形振荡（两次 rebound），1.3B 单调递减。

### Spearman ρ
- **340M**: ρ = −0.5, perm_p = 0.45（不显著，非单调）
- **1.3B**: ρ = −1.0, perm_p = 0.0167（显著，完美单调）

### Rebound 机制
h3-1 处 rebound 由**架构间差异响应**驱动：
- GDN: helped=422, hurt=678, **net=−256**（attention 损害 GDN）
- HGRN2: helped=575, hurt=337, **net=+238**（attention 帮助 HGRN2）
- RetNet: helped=373, hurt=479, net=−106

340M 容量不足以让 attention 统一各架构表现→ divergence 而非 convergence。

### Per-example Jaccard
340M h3-1 的 Jaccard（helped=0.094, hurt=0.090）与 1.3B exp-010 参考值（~0.096, ~0.090）高度一致，表明 sample-level 机制相似但 aggregate 结果相反。

**Hypothesis supported**: scale 是实现完全跨架构均等化的必要条件。

---
