# harvest eval pi05 attention k05 spatial seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_pi05_attention_k05_spatial_seed42_20260523T230413_result.json`
- **Structured JSON:** [`012b0401acfb4f1daed6.json`](../../sessions/01/012b0401acfb4f1daed6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已被删除或未创建）。Registry 已更新为 DONE。

## 结果报告

**eval_pi05_attention_k05_spatial_seed42** — DONE (negative)

| 指标 | 值 |
|------|-----|
| Attention k=0.5 Spatial SR | **72.6%** (363/500) |
| Random k=0.5 Spatial SR | 71.6% (358/500) |
| Delta | **+1.0pp** (noise) |

**Per-task breakdown:**
- 高 SR: T2 table center (96%), T1 next to ramekin (92%), T7 stove (88%), T9 wooden cabinet (88%), T6 next to cookie box (86%)
- 低 SR: T4 top drawer (28%), T5 on ramekin (32%)

**D185 narrative 影响:**

π0.5 attention importance 跨 3 个 suite 的 k=0.5 表现：

| Suite | Attention | Random | Delta |
|-------|-----------|--------|-------|
| Goal seed42 | 70.2% | 73.6% | **-3.4pp** |
| Goal seed43 | 72.2% | 73.6% | **-1.4pp** |
| Spatial seed42 | 72.6% | 71.6% | **+1.0pp** |

Attention 在 MLP connector (π0.5) 上跨 suite 表现 ≈ Random，无系统性优势。Spatial 的 +1.0pp 在统计噪声内，不改变 Goal 双 seed 确认的结论：**attention importance 在 MLP connector 架构上失效**。与 X-VLA (BART connector) attention k=0.5 Goal=98.2% 形成鲜明对比，支持 architecture-dependent importance 的 claim。

**westd-41074 GPU 2 现已空闲可用。**

---
