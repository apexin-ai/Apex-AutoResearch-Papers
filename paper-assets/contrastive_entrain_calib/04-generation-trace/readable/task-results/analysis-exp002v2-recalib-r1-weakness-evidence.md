# analysis exp002v2 recalib r1 weakness evidence

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp002v2-recalib-r1-weakness-evidence_20260519T133726_result.json`
- **Structured JSON:** [`9b104dc08ab9a0eb54ca.json`](../../sessions/9b/9b104dc08ab9a0eb54ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存到 `artifacts/research/exp002v2_recalib_r1_weakness_analysis.md`。

---

## 核心发现

### Cosine R1 (exp002v2-recalib) — 信号持续为负

| 指标 | 早期 (steps 510–539) | 晚期 (steps 1675–1705) |
|------|---------------------|----------------------|
| R1 mean | **−0.048** | **−0.080** |
| R1 range | [−0.098, +0.017] | [−0.189, +0.034] |
| 正值比例 | 3.3% (1/30) | 6.7% (2/30) |
| R3 mean | 0.495 | 0.823 |

**R1 加权贡献 = −0.02（负拖累），R3 加权贡献 = +0.62。模型学习 100% 由 R3 驱动。**

### Recalibration 无法解决问题

- Recalib 1 (step ~999): auroc=0.815, cosine_sim=0.670
- Recalib 2 (step ~1499): auroc=0.855, cosine_sim=0.860
- 方向质量提升了，但 R1 在 recalib 前后均为负值，无系统性改善

### 对比: Binary Probe R1 (exp008v3) 远优于 Cosine R1

| 指标 | Cosine R1 (002v2) | Binary Probe R1 (008v3) |
|------|--------------------|-------------------------|
| R1 mean (early) | **−0.048** | **+0.591** |
| R1 mean (late) | **−0.080** | **+0.349** |
| R1 正值率 | 5% | **100%** |
| 梯度方向 | 负 (惩罚) | 正 (奖励) |

### 论文可用总结 (English)

> In exp-002v2 (cosine-based directional reward with periodic recalibration), the R1 signal remained persistently negative throughout 1,700+ training steps (mean = −0.064, positive rate = 5%, max = +0.034), contributing a −0.02 drag on the combined reward while R3 (NLI faithfulness) dominated at +0.62. Despite recalibration improving direction quality (AUROC: 0.82 → 0.86), the cosine similarity formulation was structurally unable to produce positive R1 rewards during RL generation. In contrast, the binary probe baseline (exp-008v3) maintained a positive R1 signal throughout (mean = 0.46, range [0.06, 0.75]), confirming that the representation-level sycophancy signal exists but requires a thresholded reward formulation to be actionable during RL training.

---
