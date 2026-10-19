# analysis perlayer sparsity distribution

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_sparsity_distribution_20260522T102032_result.json`
- **Structured JSON:** [`24aaaa97b00b50cf2dad.json`](../../sessions/24/24aaaa97b00b50cf2dad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果分析——**原始假说（KL 在 middle layers 更激进剪枝）不成立**。实际模式更有趣：

### 按区域平均（KL natural vs Magnitude greedy，总体均为 32.3%）

| Region | KL Sparsity | Mag Sparsity | Δ |
|--------|------------|-------------|------|
| Early (L0-L7) | 0.2806 | 0.2752 | +0.005 |
| Middle (L8-L23) | 0.2815 | 0.2728 | +0.009 |
| Late (L24-L31) | 0.4489 | 0.4717 | −0.023 |

三个区域的均值差异都极小。但 **middle layers 内部** 有显著的非均匀分布：

### 关键发现：KL 在 middle layers 内形成"保护谷"

- **L8-L12**: KL 高剪枝 (0.32–0.36)，比 magnitude 多 +7~10pp
- **L14-L18**: KL **极低**剪枝 (0.14–0.25)，比 magnitude **少** −8~16pp ← **保护区**
- **L22-L23**: KL 再次高剪枝 (0.38–0.41)

KL predictor 在 L14-L18 主动保留了更多 neuron（sparsity 仅 14-18%，远低于全局均值 32%）。这几层恰好对应 factual knowledge retrieval 的核心区域（Geva et al. 2023）。

### 另一个显著模式：tail layers 行为完全相反

- KL 在 L24-L28 激进剪枝（48-57%），但在 L30-L31 急剧保留（18-23%）
- Magnitude 在 L30-L31 激进剪枝（70-73%），在 L24-L26 保留较多（24-30%）

### 对 MMLU/GSM8K regression 的叙事

原始假说需要修正。更准确的解释：KL 的 mode-covering 特性让它学会了**保护** L14-L18 知识层，但代价是将 sparsity budget 推到 L8-L12（early-middle, 可能影响 contextual encoding）和 L22-L28（late layers）。MMLU/GSM8K regression 更可能源于 L22-L28 的过度剪枝影响 output projection quality，而非 knowledge storage 层被破坏。

---
