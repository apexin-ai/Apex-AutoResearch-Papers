# deploy fill w38 idle gpus

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_fill_w38_idle_gpus_20260528T110812_result.json`
- **Structured JSON:** [`8474c0e72549005a0e18.json`](../../sessions/84/8474c0e72549005a0e18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部启动成功，进程正在加载模型：

| GPU | tmux session | PID | 实验 |
|-----|-------------|-----|------|
| cuda:0 | `pi05_random_k085_long_s47` | 589824 | random k=0.85 long seed47 |
| cuda:1 | `pi05_l2norm_k05_long_s47` | 589899 | l2norm k=0.5 long seed47 |
| cuda:2 | `pi05_attn_k05_long_s47` | 590036 | attention k=0.5 long seed47 |

备注：Option A 的 3 个实验（l2norm/random k=0.9 goal s42、l2norm k=0.9 spatial s42）已在 eval_results 中存在，因此部署了 Option B（Long suite seed47 高 variance 点）。GPU 3 的 Attn k=0.95 s46 似乎刚完成（内存已释放至 0 MiB），未触碰。

---
