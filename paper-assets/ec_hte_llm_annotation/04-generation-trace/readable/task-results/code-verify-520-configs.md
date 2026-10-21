# code verify 520 configs

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-520-configs_20260522T095244_result.json`
- **Structured JSON:** [`48b6da57f5028aacac35.json`](../../sessions/48/48b6da57f5028aacac35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. 520 的精确来源

**520 = 26 × 20**，来自 `exp002_bias_heatmap.csv`（K=2 解析热力图网格）：

| 维度 | 值 | 数量 |
|------|------|------|
| `delta_misclass` (Δπ) | 0.00, 0.01, ..., 0.25 | 26 |
| `delta_cate` (Δτ) | 0.025, 0.05, ..., 0.50 (排除 0.0) | 20 |
| **总计** | | **520** |

排除了 Δτ=0 的 26 行（此时 bias 恒为零），546 - 26 = 520。

260/520 = 50.0% 验证通过 — 恰好一半的 (Δπ, Δτ) 配置中 global correction 对至少一个子群造成了更大偏差。

### 2. 论文描述有误

论文写的是：
> "520 configurations spanning K∈{2,4}, two misclassification regimes, and six expert budget levels"

**实际情况**：
- 仅 K=2（K=4 有独立的 55 点网格）
- 不是"两个 misclassification regime"，而是连续的 Δπ 扫描（0.00 到 0.25）
- 不涉及"六个 expert budget levels"（exp002 没有 `n_expert` 参数）

这段描述混淆了两个实验：exp002（解析/MC 参数网格验证）和 exp001（主实验，确实有 K∈{2,4}、regimes、budget levels）。

### 3. R² 值正确

- K=2: R² = 0.994 ✓（来自 `exp002_bias_bound.csv`，2000 个非零偏差数据点）
- K=4: R² = 0.974 ✓（来自 `exp002_k4_validation.csv`，320 个非零偏差数据点）

### 4. 84.6% 无法复现

论文声称 "global correction increases bias in 84.6% of cases (π_s < π̄)"，但从现有数据无法得到 84.6%：
- `exp005_diagnostic_subgroups.csv`：52/60 = **86.7%**
- `exp001` MC 数据（全部）：54/72 = **75.0%**
- `exp001` 仅 extreme：30/36 = **83.3%**
- `exp002` 热力图：260/500 = **52.0%**

### 5. 建议修正

1. **必须修正**：将 "spanning K∈{2,4}, two misclassification regimes, and six expert budget levels" 改为准确描述，如 "spanning 26 misclassification heterogeneity levels (Δπ ∈ [0, 0.25]) and 20 CATE heterogeneity levels (Δτ ∈ [0.025, 0.50]) in a K=2 parameter grid"
2. **应当核实**：84.6% 的来源 — 当前数据给出 86.7%（exp005）或 83.3%（exp001 extreme）。如果来自 exp005，应更新为 86.7%；如果来自 exp001 extreme regime，应更新为 83.3%

---
