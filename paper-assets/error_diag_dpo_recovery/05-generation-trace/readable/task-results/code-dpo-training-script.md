# code dpo training script

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dpo-training-script_20260512T234612_result.json`
- **Structured JSON:** [`790a4248a066de4e7573.json`](../../sessions/79/790a4248a066de4e7573.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。产出汇总：

| 文件 | 说明 |
|------|------|
| `src/train_dpo.py` | 训练脚本，支持 `--mode single_gamma` 和 `--mode etadn` |
| `configs/dpo_single_gamma.yaml` | Baseline 配置：固定 γ=0.92 |
| `configs/dpo_etadn.yaml` | ETADN 配置：γ_min=0.85, γ_max=0.97 |
| `scripts/run_training.sh` | 一键脚本：3 seeds × 2 modes，双 GPU 并行 |

核心设计：
- `compute_gamma_d(div_step, expert_steps, γ_min, γ_max)` 实现连续 γ(d) = γ_min + (γ_max - γ_min) × d
- 数据加载时从 JSONL 的 `divergence_step` 和 `metadata.expert_steps` 计算 d，算出每个 pair 的 γ
- `single_gamma` 模式映射到 ETADNTrainer 的 `dmpo` mode（全局 γ），`etadn` 映射到 `etadn` mode（per-sample γ from data）
- 复用已有的 `ETADNTrainer`、`phi_weighted_logps`、`ETADNDataCollator`、`add_turn_ids_to_dataset`，零重复代码
- `--help` 和 γ(d) 单元测试均通过

---
