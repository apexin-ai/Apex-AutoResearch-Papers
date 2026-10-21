# analysis plan006 cross benchmark v2

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan006-cross-benchmark-v2_20260524T102005_result.json`
- **Structured JSON:** [`e1a5feee31962709acc3.json`](../../sessions/e1/e1a5feee31962709acc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。验证结果文件已保存。

## 结果

**V2 Cross-Benchmark Sign Consistency: 17/18**（论文旧数据 V1: 14/18）

按 K 分解：
- K=3: **5/6** sign consistent（唯一不一致：`position_bias`，boot_rate=0.218）
- K=5: **6/6** sign consistent
- K=7: **6/6** sign consistent

唯一不一致的条件是 **K3×position_bias**：MMLU β_keff=+0.0837（显著 p=0.007），ARC β_keff=−0.0500（不显著 p=0.43）。Bootstrap sign rate 仅 21.8%，说明 ARC 侧系数方向在 bootstrap 中不稳定。

V2 数据修正后结果比 V1 更强（17/18 vs 14/18），β(K_eff) 在几乎所有条件下方向一致为正，且 K≥5 时 100% 一致。

结果已保存至 `/root/cert_manip_resist_eval/artifacts/results/plan001/cross_benchmark_v2.json`。

---
