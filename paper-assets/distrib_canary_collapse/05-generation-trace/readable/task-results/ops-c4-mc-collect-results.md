# ops c4 mc collect results

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c4_mc_collect_results_20260521T041249_result.json`
- **Structured JSON:** [`183fd4efcec4f4e96771.json`](../../sessions/18/183fd4efcec4f4e96771.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MC 已完成（2000 reps × 1000 perms，52 min）。结果保存至本地 `artifacts/c4_first_diff_montecarlo.json`。

## 关键结果

### Size Control (β=0.0, α=0.05)

| Condition | Raw Perm FPR | Diff Perm FPR |
|-----------|-------------|---------------|
| T=11, φ=0.5 | 0.074 | 0.066 |
| T=11, φ=0.87 | **0.103** | 0.058 |
| T=21, φ=0.5 | 0.059 | 0.053 |
| T=21, φ=0.87 | **0.118** | 0.053 |

**Raw permutation 在 near-unit-root (φ=0.87) 下严重 inflate**——FPR 达 10-12%，是名义 5% 的 2 倍多。First-differencing 修复了这个问题，所有条件下 diff FPR ≈ 0.05-0.07，size control 良好。

### Power (Raw vs Diff Permutation)

| Condition | Raw Perm | Diff Perm | Power Loss |
|-----------|----------|-----------|------------|
| T=11, φ=0.5, β=0.46 | 0.266 | 0.144 | **45.8%** |
| T=11, φ=0.5, β=0.92 | 0.622 | 0.349 | **44.0%** |
| T=11, φ=0.87, β=0.46 | 0.306 | 0.100 | **67.4%** |
| T=11, φ=0.87, β=0.92 | 0.642 | 0.261 | **59.3%** |
| T=21, φ=0.5, β=0.46 | 0.540 | 0.300 | **44.5%** |
| T=21, φ=0.5, β=0.92 | 0.944 | 0.745 | **21.1%** |
| T=21, φ=0.87, β=0.46 | 0.705 | 0.233 | **67.0%** |
| T=21, φ=0.87, β=0.92 | 0.972 | 0.667 | **31.4%** |

### 核心发现

1. **Size-power tradeoff 明确**：Raw perm 在 φ=0.87 下 FPR inflated（10-12%），所以其 "power" 部分是虚高的。Diff perm 修正了 size 但代价是 power loss 21-67%。

2. **φ 对 power loss 影响显著**：φ=0.87 时 power loss 59-67%（T=11）和 31-67%（T=21），远大于 φ=0.5 时的 44-46%（T=11）和 21-45%（T=21）。Near-unit-root 过程的信号被 differencing 消除得更多。

3. **T=21 vs T=11 的 power gain**：T 翻倍使 raw power 几乎翻倍（如 φ=0.5 β=0.46: 0.27→0.54），diff power 也翻倍（0.14→0.30）。强信号 (β=0.92) + T=21 下 diff perm 仍能达到 0.67-0.74 的 power。

4. **实用含义**：对于 T=11 的实验（我们的实际 setting），diff perm 在 φ=0.87 β=0.46 下 power 仅 10%——几乎无检测力。这解释了为什么某些实验在 differencing 后信号消失。

---
