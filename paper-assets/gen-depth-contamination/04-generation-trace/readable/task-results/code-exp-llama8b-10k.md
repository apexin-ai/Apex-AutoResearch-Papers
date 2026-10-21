# code exp llama8b 10k

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_llama8b_10k_20260522T092313_result.json`
- **Structured JSON:** [`982dc822a9c8d0f2489c.json`](../../sessions/98/982dc822a9c8d0f2489c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**汇总：**

| 项目 | 值 |
|------|-----|
| 原始数据路径 | `data/exp_018_llama8b/` (5000 samples) |
| LLaMA-8B 模型 | `/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B` |
| Qwen Scorer | `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-1___5B-Instruct` |
| 新数据目录 | `data/exp_llama8b_10k/depth_0.jsonl` = **10,000 行** ✓ |
| GPU | cuda:2 (RTX PRO 6000, 98GB), 占用 18GB |
| PID | **23232** (父进程), 子 python3 进程已启动 |
| 当前进度 | Phase 1 - depth 1 生成中, ~5.3s/batch, 1250 batches |
| 日志 | `/tmp/exp_llama8b_10k.log` |

**问题记录：** C4 `datasets` 库走 fallback 路径时在 AutoDL 代理上陷入无限分页循环，已改用 `requests` 直接下载 shard 并手工创建 depth_0.jsonl。

**预估时间：** 每个 depth ~110 min 生成，5 个 depth 生成 ~9h，加上两次 feature extraction，总计 ~12-14h。由于 nohup 无硬超时，可以跑完。

---
