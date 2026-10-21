# deploy westd 41074 v2 retry

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd-41074-v2-retry_20260523T165927_result.json`
- **Structured JSON:** [`67a3e8d4d7b814f80178.json`](../../sessions/67/67a3e8d4d7b814f80178.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 python 进程都在运行（状态 Rl），正在 CPU 加载模型（各占 ~0.5-0.7% 内存）。π0.5 模型较大，CPU 加载到 GPU 通常需要 3-5 分钟。

全部完成：

| GPU | exp_id | 状态 |
|-----|--------|------|
| cuda:0 | eval_pi05_l2norm_k0925_goal_seed42_v2 | 运行中，加载模型 |
| cuda:1 | eval_pi05_random_k0925_goal_seed42_v2 | 运行中，加载模型 |
| cuda:2 | eval_pi05_random_k085_spatial_seed42_v2 | 运行中，加载模型 |
| cuda:3 | eval_pi05_l2norm_k085_spatial_seed42_v2 | 运行中，加载模型 |

- tokenizer 缓存验证通过
- 4 个旧 v3 session 已清理（含残留 GPU 进程）
- 4 个 v2 实验已提交，hypothesis 已设置
- Python 进程状态正常，等待模型加载完成后会占用 GPU

---
