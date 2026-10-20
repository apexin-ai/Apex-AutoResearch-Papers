# fix sft standard offline resubmit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_sft_standard_offline_resubmit_20260519T212343_result.json`
- **Structured JSON:** [`503e657abd9fcc00c22b.json`](../../sessions/50/503e657abd9fcc00c22b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

**已完成：**
- PID 141113 已 kill，tmux session `mbpp_sft_std_clean` 已清理
- `eval_mbpp_sft_standard_20_clean` → DONE(failed), failure_reason: westd network unreachable
- `eval_mbpp_sft_standard_20_v4` 已在 tmux `eval_mbpp_sft_standard_20_v4` 中启动（HF_DATASETS_OFFLINE=1 + HF_HUB_OFFLINE=1）
  - 模型已加载到 GPU 0（12903 MiB）
  - MBPP 数据集从离线缓存成功加载 374 题
  - 评估进行中，~10s/题，预计约 1 小时完成
  - Registry 状态: RUNNING

**其他实验健康状态：**
- `eval_mbpp_grpo_standard_20_v4`: ALIVE（GPU 1, 17277 MiB）
- `eval_mbpp_grpo_rasp_20`: ALIVE（GPU 2, 16767 MiB）
- GPU 3: 空闲

---
