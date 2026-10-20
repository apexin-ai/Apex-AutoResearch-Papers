# analysis d32 moment cascade gpu

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d32_moment_cascade_gpu_20260520T165922_result.json`
- **Structured JSON:** [`3de1e4d83e5d03efa1a5.json`](../../sessions/3d/3de1e4d83e5d03efa1a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。所有产出已保存到 `artifacts/moment_cascade/`。

## 核心发现

### Cascade 时序确认（α≥0.50, 两个 seed 一致）

| 阶段 | Onset | 指标 |
|------|-------|------|
| Phase 1 | Gen 1 | Token Entropy↓, ECE↑, Effective Rank↑ |
| Phase 2 | Gen 2 | Distinct-1/2/3↓, Perplexity↑ |
| Phase 3 | Gen 3-5 | MAUVE↓ (lagging indicator) |

**Entropy→Diversity→Calibration cascade**: 在 α=0.50 和 α=0.75 的 s42/s43 全部 4 个实验中 CONFIRMED。

### 两个 collapse 机制域

- **低 α (≤0.10)**: 只有 diversity 崩塌（gen 2 onset），entropy/ECE 维持在 baseline 2σ 内。纯 model collapse 效应。
- **高 α (≥0.50)**: Entropy 先崩（gen 1），一个 generation 后 diversity 跟进（gen 2）。额外叠加 calibration 爆炸（ECE +800-1800%）。

### PermG 方向性解释（FLAG）

α=0.50 两个 seed 均确认 Entropy(gen 1) → Diversity(gen 2) 单向因果链：
- **PermG fwd=6/8 rev=0/8** — directed test 正确检测到 forward causation
- **DiffXCorr fwd=6/8 rev=6/8** — undirected test 无法区分方向，因此双向显著

Moment cascade 提供了 mechanistic explanation：entropy loss 驱动 diversity collapse，而非反向。

### S(α) 反直觉发现

Diversity 降幅在低 α 反而更大（α=0.10: Distinct-2 −56% vs α=0.75: −41%），因为高 α 的 entropy collapse 改变了退化机制——从纯多样性丧失转为分布集中+校准崩溃。

### 输出文件

- `artifacts/moment_cascade/moment_cascade_analysis.json` — 完整数值结果
- `artifacts/moment_cascade/fig_moment_cascade.pdf/png` — 4-metric trajectory 图
- `artifacts/moment_cascade/fig_cascade_onset_heatmap.pdf/png` — onset 热力图
- `artifacts/moment_cascade/fig_decomposition.pdf/png` — S(α)×R(α) 分解

---
