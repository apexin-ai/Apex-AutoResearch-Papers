# analysis training dynamics

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_training-dynamics_20260515T014320_result.json`
- **Structured JSON:** [`07043cd208d88d21dcfe.json`](../../sessions/07/07043cd208d88d21dcfe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CSV 格式正确。

## 结果

**产出文件**: `/root/autodl-tmp/tax_error_inject_agent/analysis/training_dynamics.csv`（1640 行，5 个实验 × 328 步）

### Training Dynamics 汇总

| Experiment | Init Loss (avg10) | Final Loss (avg10) | Min Loss | Final Acc (avg10) | Max Acc |
|---|---|---|---|---|---|
| vanilla_0pct | 1.3425 | 0.2937 | 0.2461 | 0.8936 | 0.9119 |
| random_10pct | 1.4128 | 0.2907 | 0.2369 | 0.8959 | 0.9212 |
| random_25pct | 1.4255 | 0.2635 | 0.2178 | 0.9074 | 0.9202 |
| random_50pct | 1.4772 | 0.2600 | 0.1901 | 0.9076 | 0.9307 |
| taxei_50pct | 1.4780 | 0.2601 | 0.1873 | 0.9088 | 0.9330 |

### 分析

1. **收敛速度**：所有实验初始 loss 相近（1.34–1.48），injection ratio 越高初始 loss 略高（注入样本增加了任务多样性）。但最终 loss 反而更低——50% injection（taxei 和 random 均为 ~0.26）优于 vanilla（0.29）。

2. **最终性能**：injection 不仅没有损害训练，反而**改善了 final loss 和 token accuracy**。taxei_50pct 达到了最低 min loss（0.1873）和最高 max acc（0.9330），vanilla baseline 最差（0.2461 / 0.9119）。

3. **训练稳定性**：无 injection 导致训练不稳定的迹象。所有曲线单调收敛，gradient norm 均正常。

4. **taxei vs random**：50% injection 下两者几乎相同（final loss 0.2601 vs 0.2600），说明在训练 dynamics 层面两种 injection 策略无显著差异——差异需要在下游 eval（如 error detection accuracy）上体现。

5. **缺失实验**：taxei-fixed-inject10 和 taxei-fixed-inject25 因 OOM 失败（GPU 被其他进程占用）。如需补跑，需确保 GPU 空闲。

---
