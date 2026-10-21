# fix westd 41074 tokenizer redeploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd-41074-tokenizer-redeploy_20260524T014920_result.json`
- **Structured JSON:** [`0f041c3a7ef4f08aada8.json`](../../sessions/0f/0f041c3a7ef4f08aada8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认成功。4 个 GPU 状态：

| GPU | 显存占用 | 实验 | 状态 |
|-----|---------|------|------|
| 0 | 10063 MiB | `eval_pi05_random_k095_goal_seed43` | 刚启动，random pruning 243/256 tokens |
| 1 | 10490 MiB | `eval_pi05_l2norm_k07_goal_seed43_v2` | 运行中，Task 1 进行中 |
| 2 | 10670 MiB | `eval_pi05_l2norm_k05_long_seed43` | 刚启动，l2norm pruning 128/256 tokens |
| 3 | 10532 MiB | `eval_pi05_random_k085_goal_seed43` | 运行中，Task 5 进行中 |

**根因**：原始 3 个实验缺少 `TRANSFORMERS_OFFLINE=1` 环境变量，tokenizer 尝试从 HuggingFace Hub 下载但网络不可达。修复方法是同时设置 `HF_HUB_OFFLINE=1` 和 `TRANSFORMERS_OFFLINE=1`，使 tokenizer 从本地 cache (`/root/autodl-tmp/.hf_cache`) 加载。

---
