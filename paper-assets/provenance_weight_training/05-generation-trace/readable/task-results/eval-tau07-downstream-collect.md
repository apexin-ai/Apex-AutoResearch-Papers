# eval tau07 downstream collect

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_tau07_downstream_collect_20260520T025914_result.json`
- **Structured JSON:** [`a1bbdf5bea8f11fd35c3.json`](../../sessions/a1/a1bbdf5bea8f11fd35c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据就绪。汇总：

## τ=0.7 Downstream Eval 结果

3 个 eval 进程均已完成。提取的指标：

| Benchmark | τ=0.7 s42 | τ=0.7 s123 | τ=0.7 s456 | τ=0.7 Mean | τ=0.8 Mean | Uni Mean | Δ(0.7−0.8) |
|-----------|-----------|------------|------------|------------|------------|----------|------------|
| ARC-E     | 0.6166 | 0.6309 | 0.6111 | 0.6195 | 0.6185 | 0.6174 | +0.0010 |
| ARC-C     | 0.3473 | 0.3481 | 0.3515 | 0.3490 | 0.3515 | 0.3476 | −0.0025 |
| HellaSwag | 0.4795 | 0.4775 | 0.4811 | 0.4794 | 0.4799 | 0.4820 | −0.0005 |
| PIQA      | 0.6861 | 0.6866 | 0.6834 | 0.6854 | 0.6831 | 0.6841 | +0.0023 |
| WinoGrande| 0.5817 | 0.5675 | 0.5722 | 0.5738 | 0.5740 | 0.5762 | −0.0002 |
| **Avg**   | 0.5422 | 0.5421 | 0.5399 | **0.5414** | 0.5414 | 0.5414 | **0.0000** |

τ=0.7 的 3-seed 均值（0.5414）与 τ=0.8（0.5414）和 Uniform（0.5414）**完全一致**（四位小数）。各 benchmark 差异均在 ±0.003 以内，无统计显著差异。

## ρ=0.6 训练状态

目录名为 `hybrid_rho06_seed42`（非 `rho06_tau07_seed42`），配置：τ=0.7, contamination_ratio=0.6, max_steps=6103。

**训练已完成**（`final/` 目录存在，step_metrics 最后一行 step=6102，共 24412 条 log，4 条/step × 6103 步）。所有 GPU 当前空闲。

---
