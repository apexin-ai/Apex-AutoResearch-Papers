# fix gpu1 eval 25 restart

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gpu1_eval_25_restart_20260514T171754_result.json`
- **Structured JSON:** [`3051573eeed152e0af11.json`](../../sessions/30/3051573eeed152e0af11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**情况与预期不同，两块 GPU 都在跑 GRPO 训练：**

| GPU | PID | 运行时间 | 任务 |
|-----|-----|---------|------|
| 0 | 221271 | 10 min | `train_grpo.py` pruned_rasp_20 → recovered_rasp_20 |
| 1 | 221911 | 7 min | `train_grpo.py` pruned_standard_20 → recovered_standard_20 |

**其他发现：**
- Qwen3.5-9B：未找到，可能已删除或不在 autodl-tmp 内
- 25% eval 结果：无任何已有结果
- pruned 模型目录：`pruned_standard_25` 和 `pruned_rasp_25` 都存在

**GPU 1 正在跑 grpo_standard_20（刚启动 7 分钟），不是空转。** 25% eval 现在无法在 GPU 1 上运行。

需要你决定：
1. **等 grpo_standard_20 跑完**再启动 25% eval
2. **杀掉 grpo_standard_20** 腾出 GPU 1 立即跑 eval（GRPO 才跑 7 分钟，杀了可以之后重启）

---
