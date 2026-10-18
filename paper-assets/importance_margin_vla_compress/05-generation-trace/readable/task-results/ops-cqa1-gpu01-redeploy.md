# ops cqa1 gpu01 redeploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1_gpu01_redeploy_20260526T091233_result.json`
- **Structured JSON:** [`5291ace06dab4df1af3d.json`](../../sessions/52/5291ace06dab4df1af3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型还在 CPU 加载中（π0.5 模型大，加载需要几分钟）。两个进程都在正常运行，没有报错。关键的 offline flags 已生效——之前在这个阶段就崩溃了，现在已顺利通过。

**部署完成汇总：**

| GPU | exp_id | PID | log_path |
|-----|--------|-----|----------|
| 0 | `eval_pi05_l2norm_k075_long_seed42` | 212672 | `logs/eval_pi05_l2norm_k075_long_seed42.log` |
| 1 | `eval_pi05_attention_k075_long_seed42_v2` | 213212 | `logs/eval_pi05_attention_k075_long_seed42_v2.log` |

GPU 2/3 未受影响（10017 MiB, 23-41%）。两个新实验正在加载模型到 GPU，预计几分钟后 GPU 0/1 显存会上来。

---
