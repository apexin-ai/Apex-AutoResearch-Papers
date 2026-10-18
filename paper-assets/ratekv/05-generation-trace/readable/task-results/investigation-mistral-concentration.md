# investigation mistral concentration

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigation_mistral_concentration_20260514T211724_result.json`
- **Structured JSON:** [`1a97535dd62c9f4f569d.json`](../../sessions/1a/1a97535dd62c9f4f569d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Root cause confirmed. Here's the full finding:

## Mistral Concentration 溯源结果

| 数据源 | 文件 | 分辨率 | 零值头数/总头数 | Concentration |
|--------|------|--------|----------------|---------------|
| Standard profiling | `mistral_profiling_results.json` | 低（无记录） | 221/256 (86%) | **0.4220** |
| Hires profiling | `mistral_ppl_profiles_hires.json` | 64 samples, 2048 seq_len | 43/256 (17%) | **0.2307** |
| C4 cross-dataset | `mistral_c4_eval_results.json` | C4 calibration | — | 0.1363 |

**0.42 是低分辨率 profiling 的伪影。** 标准 profiling 中 256 个 head 有 221 个（86%）的 2-bit delta 为 0.0，不是因为这些 head 真的不敏感，而是因为 calibration 样本太少导致测量精度不够。少数非零 head 占了总 delta 的大部分 → 虚高的 concentration。

Hires profiling 将零值 head 降到 43/256（17%），分辨率足以检测到大多数 head 的微小 delta，分布变得更均匀 → concentration = 0.23。

**结论：**
- **0.42**（paper_framing.md）：来自 standard profiling，**错误**，是低分辨率伪影
- **0.22**（analysis.tex Table 3）：来自 hires profiling（实际计算值 0.2307，四舍五入），**正确**
- paper_framing.md 应更新为 0.22–0.23

需要我直接修正 paper_framing.md 中的值吗？

---
