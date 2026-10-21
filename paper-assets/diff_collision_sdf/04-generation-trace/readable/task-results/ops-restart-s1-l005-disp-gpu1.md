# ops restart s1 l005 disp gpu1

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart_s1_l005_disp_gpu1_20260525T195912_result.json`
- **Structured JSON:** [`c7345dd65da95c3055ba.json`](../../sessions/c7/c7345dd65da95c3055ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动完成。

| 项目 | 值 |
|------|-----|
| tmux session | `eval_pi05_a1_30k_s1_l005_disp` |
| PID | 142394 |
| GPU | 1 (RTX PRO 6000) |
| 显存占用 | ~9 GB |
| 日志 | `~/runs/diff_collision_sdf/eval_pi05_a1_30k_s1_l005_disp.log` |

注意：实际启动命令根据 GPU 3 正在跑的 eval 做了修正——脚本路径 `scripts/eval_safelibero.py`、参数名 `--checkpoint`、增加了 `--suite safelibero_object --pi05`。

---
