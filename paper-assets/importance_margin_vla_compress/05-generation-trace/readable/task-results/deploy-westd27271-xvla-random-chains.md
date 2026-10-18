# deploy westd27271 xvla random chains

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd27271_xvla_random_chains_20260522T184535_result.json`
- **Structured JSON:** [`90d49fbc60c711de0187.json`](../../sessions/90/90d49fbc60c711de0187.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两条链都正常运行中。

**汇报：**

| 项目 | 状态 |
|------|------|
| Wait loop | 已杀掉 |
| 链式实验 | 两条均已启动并在跑 episode |
| X-VLA 实际参数名 | `--mode random`（非 `--prune_mode`），`--num_episodes`（非 `--n_episodes`），需额外指定 `--model_path /root/autodl-tmp/X-VLA-Libero` |
| GPU 0 | 4778 MiB，xvla_random_goal k=0.95 正在跑（Task 0 Ep 1 SUCCESS） |
| GPU 1 | 加载中，xvla_random_spatial k=0.95 已开始 Task 0 |
| Registry | `eval_xvla_random_k095_goal_seed42` / `eval_xvla_random_k095_spatial_seed42` → RUNNING |
| tmux sessions | `xvla_random_goal`、`xvla_random_spatial` |

---
