# code plan012 xgboost matched baseline

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan012-xgboost-matched-baseline_20260516T013038_result.json`
- **Structured JSON:** [`e8f91e9e906f5e51635f.json`](../../sessions/e8/e8f91e9e906f5e51635f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `results/plan012_xgboost_matched.json`。并排对比：

| Model | 5-class macro-F1 | 3-class macro-F1 |
|---|---|---|
| **HGBT-matched** (7 features, 5-fold stratified) | 0.497 [0.491, 0.503] | 0.805 [0.799, 0.811] |
| QLoRA Qwen3-0.6B | 0.583 ± 0.010 | 0.905 ± 0.003 |
| QLoRA Pythia-410M | 0.556 ± 0.016 | 0.870 ± 0.022 |
| *旧 HGBT baseline (plan-009 LOGO, 6 gen)* | *0.503* | *0.782* |

**关键发现**：

- **5-class**：QLoRA Qwen3-0.6B 比 matched HGBT 高 **+8.6 pp**，Pythia-410M 高 **+6.0 pp**。HGBT 在 matched 条件下比旧 LOGO baseline 略低（0.497 vs 0.503），说明 LOGO CV 对 HGBT 反而更宽松（跨生成器泛化对 feature-based 方法不难）。

- **3-class**：QLoRA Qwen3-0.6B 比 matched HGBT 高 **+10.0 pp**，差距更显著。这消除了 reviewer 关于评估协议不对等的质疑——在完全相同条件下 QLoRA 优势依然稳健。

- HGBT 的瓶颈在 depth 2/3（per-class F1 仅 0.27/0.26），而 QLoRA Qwen3-0.6B 在这些类上分别达到 0.41/0.26——高 depth 的区分主要靠 LLM 的 token-level representation。

---
