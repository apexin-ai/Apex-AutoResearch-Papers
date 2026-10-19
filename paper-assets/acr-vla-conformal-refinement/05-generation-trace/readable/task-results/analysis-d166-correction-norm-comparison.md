# analysis d166 correction norm comparison

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d166-correction-norm-comparison_20260526T173127_result.json`
- **Structured JSON:** [`1f96b68bec532e51b6fb.json`](../../sessions/1f/1f96b68bec532e51b6fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整结果。

---

## 表 1：correction_norm 对比

| Model | Suite | mean_correction_norm | Saturated (=0.200)? | trigger_rate | mean_uncertainty |
|-------|-------|---------------------|---------------------|-------------|-----------------|
| **SmolVLA K2** | Spatial s42 | 0.1924 | **No** | 19.2% | 0.183 |
| **SmolVLA K2** | Spatial s46 | 0.1918 | **No** | 19.2% | 0.183 |
| **SmolVLA K2** | Spatial s48 | 0.1917 | **No** | 19.8% | 0.185 |
| **SmolVLA K2** | Goal s42 | 0.1771 | **No** | 8.8% | 0.147 |
| **SmolVLA K2** | Goal s48 | 0.1760 | **No** | 8.5% | 0.144 |
| SmolVLA (non-K2) | Spatial/Goal/Object/Long | *字段缺失* | — | — | — |
| **π0.5** | Spatial s42 | 0.20000000**48** | **Yes** | 4.8% | 0.106 |
| **π0.5** | Spatial s43 | 0.20000000**39** | **Yes** | 4.4% | 0.106 |
| **π0.5** | Spatial s44 | 0.20000000**39** | **Yes** | 3.9% | 0.098 |
| **π0.5** | Goal s42 (cqa1) | 0.20000000**40** | **Yes** | 8.1% | 0.115 |
| **π0.5** | Goal s43 (bjb1) | 0.20000000**38** | **Yes** | 8.7% | 0.119 |
| **π0.5** | Goal s44 (bjb1-18228) | 0.20000000**45** | **Yes** | 10.0% | 0.127 |
| **π0.5** | Object s42 | 0.20000000**35** | **Yes** | 3.7% | 0.084 |
| **π0.5** | Object s43 | 0.20000000**38** | **Yes** | 4.0% | 0.085 |
| **π0.5** | Object s44 | 0.20000000**41** | **Yes** | 3.5% | 0.082 |
| **π0.5** | Long s42 | 0.20000000**41** | **Yes** | 3.9% | 0.087 |

---

## 表 2：π0.5 Spatial Adaptive JSON 文件状态

| 服务器 | 文件存在? | 有 adaptive_stats? | trigger_rate | mean_correction_norm |
|--------|----------|-------------------|-------------|---------------------|
| **bjb2-28827** | **3 个 JSON (s42/s43/s44)** | **Yes** | 3.9%–4.8% | 0.200 (saturated) |
| bjb1-32546 | 无 pi05 spatial adaptive | — | — | — |
| bjb1-18228 | 仅 .log 文件，无 JSON | — | — | — |
| cqa1-32758 | 无 spatial 文件 | — | — | — |

Director 提到的 π0.5 Adaptive Spatial = 97.2±0.8% 数据来源确认在 **bjb2-28827**，三个 seed 的 JSON 都在。

---

## 关键发现：强叙事点

**π0.5 的 correction_norm 在所有 10 个实验中恒定 saturated 在 norm cap = 0.200**，精确到小数点后 8 位（0.20000000xx）。这意味着 CRM 的每一次修正都打满了上限——CRM 认为 π0.5 的每一步都需要最大幅度修正，但被 norm cap 截断。

**SmolVLA（K2 版本）的 correction_norm 在 0.176–0.192 之间变化**，低于 0.200 cap。Spatial 约 0.192（接近但未饱和），Goal 约 0.177（明显低于 cap）。CRM 对 SmolVLA 输出的修正幅度是 *自适应调节* 的，不同 task suite 有不同修正强度。

**解读**：CRM 是为 SmolVLA 训练的，对 SmolVLA 的不确定性做出 *校准的、分级的* 修正；迁移到 π0.5 时，两个模型的 action space 分布差异导致 CRM 总是输出超大修正量，被 norm cap 强制截断。这佐证了 "cross-backbone CRM transfer 需要 recalibration" 的论点，也解释了为什么 π0.5 + ACR-VLA 的提升幅度小于 SmolVLA——CRM 在 π0.5 上处于 *饱和修正* 状态，失去了细粒度调节能力。

---
