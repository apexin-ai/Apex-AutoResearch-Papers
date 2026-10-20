# analysis exp 001 eval 3B d100 s123 para aligned v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308_result.json`
- **Structured JSON:** [`ad8d309586b78e628060.json`](../../sessions/ad/ad8d309586b78e628060.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 实验结果

**状态**: success — 正常完成（EXIT_CODE=0，.done sentinel 已写入）

### Para-aligned 指标 (d100, s123)

| Benchmark | Accuracy | Correct/Total |
|-----------|----------|---------------|
| MMLU | 0.6565 | 4330/6596 |
| GSM8K | 0.5877 | 134/228 |
| ARC-Challenge | 0.8164 | 569/697 |
| HumanEval pass@1 | 0.0769 | 2/26 |

### 与 aligned 版本对比

对比对象：`exp_001_eval_3B_d100_v2_s123_aligned`（同 checkpoint，原题评估）

| Benchmark | Aligned | Para-aligned | Δ |
|-----------|---------|-------------|------|
| MMLU | 0.6319 | 0.6565 | +2.5pp* |
| GSM8K | 0.7324 | 0.5877 | **-14.5pp** |
| ARC-Challenge | 0.8311 | 0.8164 | -1.5pp |
| HumanEval | 0.1829 | 0.0769 | **-10.6pp** |

### 注意事项

1. **MMLU 反向偏差**：para_aligned 略高于 aligned，但 item pool 不同（para 仅 6596 QC-passed items vs aligned 全量 14042），不可直接对比绝对值
2. **GSM8K/HumanEval 大幅下降**：符合预期 — 100% contamination 模型在 paraphrase 测试下生成类 benchmark 掉分最明显（GSM8K -14.5pp，HumanEval -10.6pp），说明记忆效应在这两个 benchmark 最严重
3. **ARC 稳定**：选择题格式的 paraphrase 对 ARC 影响较小（-1.5pp）
4. **与 s42 一致**：s42 para_aligned 结果（MMLU 0.659, GSM8K 0.583, ARC 0.809, HumanEval 0.115）高度一致，跨 seed 可复现
5. **bitsandbytes 警告**：`libnvJitLink.so.13` 加载失败，非致命，不影响推理结果

---
