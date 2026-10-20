# code prepare exp 022 untrained dt emb gate

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-exp-022-untrained-dt-emb-gate_20260517T041745_result.json`
- **Structured JSON:** [`3728503d132cf0c75cf9.json`](../../sessions/37/3728503d132cf0c75cf9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**最终参数列表**：
| 参数 | 值 | 说明 |
|------|------|------|
| `--gate_enabled` | True | 启用 gate 网络 |
| `--gate_dt_embed_dim` | 32 | 创建 dt embedding（RSSM 内） |
| `--dt_emb_freeze` | True | 冻结 dt_emb（随机初始化后不接收梯度） |
| `--gate_subsample_min_dt` | 1 | subsample ON |
| `--gate_subsample_max_dt` | 2 | subsample ON |
| `--imag_horizon` | 8 | 想象 horizon |
| `--compile` | True | 正式运行开启编译 |
| `--steps` | 105000 | |
| `--seed` | 0 | |
| `--checkpoint_every` | 10000 | |

**Dry-run 结果**：成功，无报错。Gate 模块正确激活（metrics 中 `gate_loss`、`gate_dt_mean`、`gate_dt_*_frac`、`gate_entropy_bonus` 全部正常记录）。Step 5000 时 gate_scale=0（curriculum phase1=50000 未到），所有 dt=1，符合预期。

**脚本路径**：`artifacts/scripts/exp_022_untrained_dt_emb_learned_gate.sh`

**无需代码修改**：`dt_emb_freeze=True` + `gate_enabled=True` 组合在现有代码中已完全支持（models.py:97-98 冻结 embedding，同时 EventGate 网络独立接收梯度学习）。

---
