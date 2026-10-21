# code text window ablation r1 8b

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_text_window_ablation_r1_8b_20260517T001923_result.json`
- **Structured JSON:** [`28bcb32535213220a832.json`](../../sessions/28/28bcb32535213220a832.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果支持 "method-agnostic" claim。

**核心发现**: Text probe 和 HS probe 在 W 增大时表现出完全一致的趋势方向:
- accuracy↑, coverage↓, FPR↓, precision↑

**对比亮点**:
- Text probe 从 windowing 获得更大相对收益 (bal_acc +18.6% vs HS +4.0%)，因为单步 text embeddings 本身较弱
- HS probe 在所有 W 下绝对值均优于 text (bal_acc 高 10-13pp, FPR �� 6-15pp)
- Text coverage 在 W≥15 后饱和 (0.5814)，而 HS 继续下降

**输出位置**:
- `artifacts/text_window_ablation_r1_8b/results.json`
- `artifacts/text_window_ablation_r1_8b/report.md`

---
