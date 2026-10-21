# code v8b fixed schedsampling

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v8b_fixed_schedsampling_20260519T174233_result.json`
- **Structured JSON:** [`0f204637f1919433ac21.json`](../../sessions/0f/0f204637f1919433ac21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修复已就位。总结验证结果：

**创建的文件：**
- `/root/turn_residual_gating/src/train_phase2_v8b.py` — 基于 v8 修改
- `/root/turn_residual_gating/scripts/run_v8b.sh` — 启动脚本

**修复点确认：**

| 修复项 | 位置 | 状态 |
|--------|------|------|
| `compute_gar_loss` len==1 分支 | L401-402: `if len(gar_per_turn) == 1 and mode == "mse_target"` → `(gar_per_turn[0] - target)**2` | OK — grad 从 `gar_per_turn[0]` 继承，device 正确 |
| SS generation `model.eval()` + `torch.no_grad()` | L356 eval, L367 train, L369 empty_cache | OK |
| `max_new_tokens` 256→128 | argparse default=128 + run script `--ss-gen-max-tokens 128` | OK |
| `lambda_gar` 2.0→1.0 | run script `--lambda-gar 1.0` | OK |
| 超参对齐 v7/v9 | init-bias=1.5, gate-lr-multiplier=10, gar-target=0.5, min-gate-std=0.05 | OK |
| SS/TF L_GAR 分别追踪 | L286-289 计数器, L409/L489 累加, L513-521 输出 | OK |
| 文件头注释说明 v8b | docstring 开头 `v8b fixes three issues in v8` | OK |

---
