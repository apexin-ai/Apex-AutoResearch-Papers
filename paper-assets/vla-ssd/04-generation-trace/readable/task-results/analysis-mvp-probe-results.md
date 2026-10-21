# analysis mvp probe results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp-probe-results_20260515T134750_result.json`
- **Structured JSON:** [`8cdaaec938d3e84a153d.json`](../../sessions/8c/8cdaaec938d3e84a153d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 和 artifact 已更新。以下是完整分析报告：

---

## MVP Probe 结果分析

### Gate 评估

| Gate | 指标 | 实测值 | 阈值 | 结果 |
|------|------|--------|------|------|
| G1 | best_layer ρ > 0.5 | **0.9562** (L3) | 0.5 | **PASS** |
| G2 | max Δρ > 0.1 (非坍塌层) | **0.0427** (L4) | 0.1 | **FAIL** |
| G3 | VLA ρ ≥ DINO-V2 | **0.9562** vs 0.901 | 0.901 | **PASS** |

### **Overall: FAIL** (Gate 2 未通过)

### 关键数据

**Trained Top-5**: L3=0.956, L4=0.955, L2=0.955, L5=0.950, L6=0.950
**Untrained Top-5**: L1=0.933, L13=0.932, L5=0.931, L8=0.928, L2=0.928

**Δρ Top-5** (17 个两端都未坍塌的层):
- L4: +0.043, L7: +0.040, L11: +0.037, L19: +0.035, L29: +0.035
- Mean Δρ = +0.019, 16/17 正向（仅 L13 为 -0.029）

**Layer Collapse**: 33 层中 16 层在至少一端坍塌（ρ=0.0），其中训练导致 7 层额外坍塌。

### 核心结论

1. **LLM 训练贡献可忽略**: max Δρ=0.043，远低于 0.1 阈值，与 ROADMAP 预判精确吻合
2. **信号来自 vision encoder**: untrained 模型已达 ρ=0.933，说明 SigLIP ViT-SO400M 预训练特征主导 temporal distance 信号
3. **VLA > DINO-V2 但归因于更强的 vision backbone**: SigLIP（0.933 untrained）> DINO-V2（0.901），不是 LLM 的功劳
4. **项目定位: Negative Result** — VLA LLM 层不编码显著额外的 scene structure 信息

---
