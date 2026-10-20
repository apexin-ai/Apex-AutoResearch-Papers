# ssh check gpu conflict

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-gpu-conflict_20260512T232341_result.json`
- **Structured JSON:** [`79438eaa35918ac757e0.json`](../../sessions/79/79438eaa35918ac757e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### GPU 占用情况

| GPU | 显存占用 | 利用率 | 进程 |
|-----|---------|--------|------|
| cuda:0 | 29,993 / 97,887 MiB (31%) | 94% | PID 40397 — sft_eval_v2 (evaluate.py) |
| cuda:1 | **58,061 / 97,887 MiB (59%)** | **100%** | **3 个进程**（不是 2 个） |

**cuda:1 上的 3 个进程：**

| PID | 进程 | 显存 | 启动时间 |
|-----|------|------|---------|
| 64374 | **grpo_pilot_v1** (train_grpo.py) | 21,374 MiB | 07:17 |
| 64955 | posthoc_nli_v2 (rerank_nli.py) | 19,878 MiB | 07:18 |
| 65730 | **test_gen.py**（未知来源） | 16,790 MiB | 07:22 |

### OOM 风险

当前 58 GB / 96 GB，还有 ~40 GB 余量。**暂无 OOM 风险**，但 3 个进程抢占 GPU 计算资源（利用率已 100%），互相拖慢速度。

### GRPO Pilot 训练状态 — 有严重问题

进度 4/20 steps (20%)，但训练信号异常：

- **Steps 1-3: loss=0.0, reward=0.0, grad_norm=0.0** — 完全没有梯度
- Step 4: reward=0.183, grad_norm=0.053 — 刚出现微弱信号
- **completions/clipped_ratio=1.0** — 所有生成都打满 max_completion_length=1024
- **completions/mean_terminated_length=0.0** — 没有任何生成正常终止（生成了 EOS）
- **frac_reward_zero_std=1.0**（steps 1-3）— 同一 prompt 的多个 generation 得到完全相同的 reward，GRPO 无法学习

这说明模型当前无法在 1024 token 内生成有效输出，导致几乎所有 reward 为 0，训练基本失效。

### posthoc_nli_v2 状态

正常推理中，4/124 batches (32/985 samples)，进度约 3%。

### 建议

1. **Kill posthoc_nli_v2 和 test_gen.py** — 释放 cuda:1 上 ~37 GB 显存和计算资源，保障 GRPO pilot
2. **但 GRPO pilot 本身有根本性问题**：reward 全 0 + clipped_ratio=1.0 意味着即使独占 GPU 也不会有效训练。需要排查：
   - `max_completion_length=1024` 太短，模型无法在该长度内完成任务
   - reward function 实现可能有 bug（前 3 步全 0）
   - 可能需要增大 `max_completion_length` 或调整 reward function

是否要我先 kill posthoc_nli_v2 和 test_gen.py？

---
