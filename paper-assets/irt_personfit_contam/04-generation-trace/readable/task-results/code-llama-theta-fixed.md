# code llama theta fixed

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-theta-fixed_20260520T231635_result.json`
- **Structured JSON:** [`a262f92cccbe59a415d8.json`](../../sessions/a2/a262f92cccbe59a415d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**Llama θ_fixed lz\* 分析 (Snijders 2001)**

| 条件 | θ_free | lz\*_free | lz\*_fixed | Δlz\*_fixed |
|------|--------|----------|-----------|-------------|
| clean | -0.666 | 0.845 | 0.845 | — |
| contam_15 | -0.276 | -2.992 | 0.959 | +0.114 |
| contam_50 | -0.149 | -3.331 | 1.172 | +0.327 |

- **验证通过**：clean lz\*_free = lz\*_fixed = 0.8446（θ_fixed = clean θ_free，完全一致）
- **Dose-response ratio (fixed)**: 2.87（|Δ50|/|Δ15| = 0.327/0.114）
- **单调性**：✓（|Δcontam_50| > |Δcontam_15|）
- **对比 free theta ratio**: 1.09 → fixed 后增强至 2.87，θ_fixed 显著恢复了单调 dose-response

与 Qwen 结果类似（ratio 3.12），θ_fixed 方法在 Llama 上同样有效地将 dose-response 从几乎平坦（1.09）恢复为清晰的单调关系（2.87）。

注意 lz\*_fixed 方向：contam 条件下 lz\* 为正值（0.96, 1.17），说明在固定 θ=-0.666 下 contam 模型的 response pattern 比 IRT 预期"更好"（更像高能力者），但 lz\* 并未达到显著异常阈值（<1.96）。关键是 **Δlz\* 的单调递增** 才是 dose-response 的核心证据。

---
