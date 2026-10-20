# research literature gc pertimestep

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-gc-pertimestep_20260515T190611_result.json`
- **Structured JSON:** [`36bc36ae5a3bb9f39b7a.json`](../../sessions/36/36bc36ae5a3bb9f39b7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/literature_map.yaml`。汇总如下：

## 搜索结果概览

**共收录 17 篇论文，分三个类别：**

### 1. Probe Methodology (7 篇)
- **Hewitt & Liang 2019** — control task + selectivity，直接解释 random projection 也 100% 的现象
- **Voita & Titov 2020** — MDL probing，用描述长度替代 accuracy，能区分 pretrained vs random
- **Pimentel et al. 2020** — Pareto probing，accuracy-complexity tradeoff
- **Belinkov 2022** — 综述，统一参考
- **Gorban & Tyukin 2018** + **Grechuk et al. 2021** — stochastic separation theorems，数学解释 4096-dim 10-class 为什么 trivially separable
- **Prabhu et al. 2024 (RanDumb, NeurIPS)** — random projection 在 continual learning 超过学到的表征

### 2. VLA Representation Probing & Temporal Analysis (5 篇)
- **Grant et al. 2026** (arXiv:2603.19233) — 最接近的竞争者，task structure determines language sensitivity，但用 injection+SAE 而非 per-timestep probe
- **Lu et al. 2025** (arXiv:2502.04558) — OpenVLA 在 LIBERO 上的 layer-wise symbolic state probing，无 temporal 分析
- **Buurmeijer et al. 2026** (arXiv:2603.05487) — VLA feature observability/controllability，linear intervention
- **Luo et al. 2026** (arXiv:2603.15618) — 深层 visual token sensitivity 衰减
- **Jiang et al. 2025** (ICLR) — manipulation-centric representation probing

### 3. Instruction Encoding & Language Sensitivity (5 篇)
- **LIBERO-Plus** (2025) — VLA 完全忽略 language instruction
- **VLM4VLA** (2026) — vision module 是瓶颈，非 language
- **Fang et al. 2026** — counterfactual failure，LIBERO-CF benchmark
- **Zhan et al. 2026** — modality collapse，visual prior 压倒 language
- **Zhang et al. 2026** — linguistic blindness + IGAR attention recalibration

## Novelty 评估

**Per-timestep goal classification 作为 trained/untrained discriminator 是全新的。** 具体空白：

1. **没有人做过 per-timestep goal classification** — Lu 2025 只做 layer-wise，Grant 2026 做 injection，Buurmeijer 2026 做 observability
2. **VLA 领域没有 trained vs random-projection probe 对比** — Hewitt/Voita 的框架仅在 NLP 中应用
3. **Task structure 作为 moderator 未被量化** — Grant 2026 定性提及，我们用 LIBERO-10 vs LIBERO-Goal 量化
4. **t=0 instruction encoding 信号（+56.7pp gap）是全新发现**

---
