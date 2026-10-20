# gpu autodl5090 batch

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_autodl5090_batch_20260514T143208_result.json`
- **Structured JSON:** [`b2fff96675bc370de547.json`](../../sessions/b2/b2fff96675bc370de547.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部成功启动并确认推理进行中。

| 实验 | GPU | tmux session | PID | 任务 | 进度 |
|------|-----|-------------|-----|------|------|
| `exp_001_seed42_v2` | cuda:1 (29GB) | exp_001_seed42_v2 | 78728 | NER N=16 seed=42 | ~10% (848/8816 prompts) |
| `exp_001_seed123_v2` | cuda:2 (29GB) | exp_001_seed123_v2 | 78733 | NER N=16 seed=123 | 运行中 |
| `exp_008_re_n16_v2` | cuda:3 (29GB) | exp_008_re_n16_v2 | 78737 | RE N=16 seed=42 | 运行中 |

关键确认：
- 全部使用 `--collect_logprobs`，满足 exp-012 前置要求
- 模型 `qwen3-8b-scierc-merged-v2` (ft_002_v2)
- cuda:0 未动
- 推理速度 ~2900 toks/s，8816 prompts (551 instances × 16 samples)，预计 ~15-20 分钟完成
- 已设置每 7 分钟自动监控 cron

---
