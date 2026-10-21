# exp token level lp aggregator

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_token_level_lp_aggregator_20260518T103351_result.json`
- **Structured JSON:** [`4d57cb44f2bc5628eb35.json`](../../sessions/4d/4d57cb44f2bc5628eb35.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

所有实验完成，输出保存在 `output/token_lp_aggregator/`。

### SciERC (10-epoch model, 529 instances)

| Aggregator | Spearman ρ | Selection F1 | Gap Closure |
|------------|-----------|-------------|-------------|
| Random | — | 0.6476±0.015 | 0.0% |
| Mean LP (baseline) | 0.158±0.064 | 0.6566±0.018 | 10.6% |
| Attention | -0.049±0.167 | 0.6366±0.020 | -12.8% |
| 1D-CNN | **0.173±0.087** | 0.6552±0.017 | 8.9% |
| Oracle | — | 0.7331 | 100.0% |

### SciERC (3-epoch model, 529 instances)

| Aggregator | Spearman ρ | Selection F1 | Gap Closure |
|------------|-----------|-------------|-------------|
| Random | — | 0.5459±0.014 | 0.0% |
| Mean LP (baseline) | 0.354±0.022 | **0.6383±0.017** | **36.4%** |
| Attention | -0.039±0.251 | 0.5136±0.044 | -12.7% |
| 1D-CNN | **0.387±0.021** | 0.6238±0.022 | 30.7% |
| Oracle | — | 0.7998 | 100.0% |

### Few-NERD (2000 instances subsampled)

| Aggregator | Spearman ρ | Selection F1 | Gap Closure |
|------------|-----------|-------------|-------------|
| Random | — | 0.6357±0.010 | 0.0% |
| Mean LP (baseline) | 0.604±0.019 | 0.7633±0.011 | 55.8% |
| Attention | 0.387±0.316 | 0.7134±0.068 | 34.0% |
| 1D-CNN | **0.642±0.014** | **0.7647±0.009** | **56.4%** |
| Oracle | — | 0.8646 | 100.0% |

### 关键发现

1. **Attention aggregator 全面失败**：在所有数据集上都低于 mean LP baseline。训练不稳定（std 极大），多个 fold 出现负 ρ。不适合这个任务。

2. **1D-CNN 在 ρ 上略优于 mean LP**：
   - SciERC-10ep: 0.173 vs 0.158 (+9.5% relative)
   - SciERC-3ep: 0.387 vs 0.354 (+9.3% relative)
   - Few-NERD: 0.642 vs 0.604 (+6.3% relative)
   
3. **但 Selection F1 上 CNN ≈ Mean LP，未形成有意义差距**：
   - SciERC-10ep: 0.6552 vs 0.6566 (CNN 反而略低)
   - SciERC-3ep: 0.6238 vs 0.6383 (CNN 低 -2.3%)
   - Few-NERD: 0.7647 vs 0.7633 (CNN +0.2%, 在 std 范围内)

4. **结论：Token-level LP 信息本身不足，aggregation 不是瓶颈**。CNN 虽然在 ranking 相关性上微弱改善，但这个改善无法转化为实际选择性能的提升。Mean-pool 已经近乎最优地利用了 token-level LP 中的信号。更强的 negative evidence 支持"LP 信号上限本身有限"这一判断。

---
