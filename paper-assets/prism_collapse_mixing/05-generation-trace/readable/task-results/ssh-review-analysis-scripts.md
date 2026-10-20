# ssh review analysis scripts

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_review-analysis-scripts_20260515T230452_result.json`
- **Structured JSON:** [`80d690078c6fcc4a0b95.json`](../../sessions/80/80d690078c6fcc4a0b95.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项数据已全部拉取。以下是汇报。

---

## 1. Gen 0 完整指标

| 字段 | Seed 42 | Seed 137 |
|------|---------|----------|
| **rho_loss_entropy** | 0.9292 (p=0.0) | 0.9292 (p=0.0) |
| **rho_loss_spectral_rank** | -0.211 (p=0.0) | -0.211 (p=0.0) |
| loss_mean | 3.1565 | 3.1565 |
| loss_std | 0.5186 | 0.5186 |
| entropy_mean | 3.1564 | 3.1564 |
| entropy_std | 0.4432 | 0.4432 |
| spectral_rank_mean | 163.72 | 163.72 |
| spectral_rank_std | 8.65 | 8.65 |
| sigma_spectral_rank | 4.42 | 4.42 |
| **distinct_1** | 0.0387 | 0.0386 |
| **distinct_2** | 0.3412 | 0.3414 |
| **distinct_3** | 0.6871 | 0.6870 |
| num_probe_samples | 5000 | 5000 |

两个 seed 的 Gen 0 指标几乎相同（仅 distinct-n 有微小差异），符合预期——Gen 0 是同一基座模型，差异仅来自采样随机性。

---

## 2. analyze_correlation.py Bug 列表

### BUG-1（逻辑错误，严重）：Condition 2 检查了错误的量

**预注册标准**：该信号的 |ρ| 从 Gen 0→Gen 3 单调退化 ≥15%。

**代码实现**：检查的是 `aggregated mean`（`entropy_mean` / `spectral_rank_mean`）是否单调下降 ≥15%。

```python
# Condition 2: mean monotonically decreases, drop >= 15%
means = [data[s].get(g, {}).get("aggregated", {}).get(mean_key, ...) for g in gens]
monotonic_decrease = all(valid[i] >= valid[i + 1] for i in range(len(valid) - 1))
pct_drop = (valid[0] - valid[-1]) / abs(valid[0]) * 100
```

这里 `valid` 来自 `means`（如 entropy_mean），不是来自 `rhos`。应该改为检查 `|ρ|` 的单调退化。

**修复建议**：

```python
# Condition 2: |rho| monotonically degrades >= 15%
abs_rhos = [abs(r) for r in rhos if not np.isnan(r)]
if len(abs_rhos) == len(gens) and abs_rhos[0] != 0:
    monotonic_decrease = all(abs_rhos[i] >= abs_rhos[i + 1] for i in range(len(abs_rhos) - 1))
    pct_drop = (abs_rhos[0] - abs_rhos[-1]) / abs_rhos[0] * 100
    cond2 = monotonic_decrease and pct_drop >= 15
```

同时删除 `mean_key` 参数和 `means` 变量（不再需要）。

### 无其他 bug

- 文件读取 glob 模式正确 ✓
- Condition 1 逻辑正确（`last |ρ| < 0.5 AND early max |ρ| > 0.7`）✓
- `early_rhos` 取 `range(min(2, len(rhos)))`，覆盖 Gen 0-1 ✓
- 双 seed 判定逻辑（all pass → PASS, any pass → WEAK_PASS）✓
- 无 off-by-one ✓

---

## 3. plot_results.py Bug 列表

### BUG-1（遗漏）：rho decay 图只画了 entropy，缺 spectral_rank

`plot_rho_decay` 只画 `rho_loss_entropy`，但 Pass/Fail 同时评估 `rho_loss_spectral_rank`。两个信号都应可视化。

**修复建议**：画两条线，或拆为两个 subplot。注意 `rho_loss_spectral_rank` 是负值（Gen 0 = -0.211），需要用 |ρ| 或调整 y 轴范围。

### BUG-2（小问题）：y 轴 `set_ylim(0, 1.05)` 会裁切负 ρ

当前只画 entropy（正值）不受影响，但如果加上 spectral_rank（负值），会被裁掉。

### BUG-3（小问题）：分布图只画 seed 42

`plot_signal_distributions(data, gens, seeds[0], args.output_dir)` 只对第一个 seed 画图。建议对所有 seed 都生成。

### 无其他 bug

- 数据加载动态，不依赖硬编码的代数 ✓
- 阈值线 0.7 和 0.5 均存在 ✓
- Legend 齐全 ✓
- Gen 数量从数据推断，无 hardcode ✓

---
