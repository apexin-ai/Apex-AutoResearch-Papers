# ops d017 restart v2 standard

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d017-restart-v2-standard_20260515T034219_result.json`
- **Structured JSON:** [`7b96b9e1d92a383dec73.json`](../../sessions/7b/7b96b9e1d92a383dec73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。最终状态汇总：

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| grpo_stage2_rasp_20_v2 | cuda:0 | 274156 (未中断) | RUNNING |
| grpo_stage2_standard_20_v2 | cuda:1 | 276501 (重启) | RUNNING |

- v2 rasp 未被误杀，一直在 GPU 0 正常运行（84908MiB 显存，100% 利用率）
- v2 standard 已在 GPU 1 重启，旧输出目录已清除，模型正在加载中
- Registry 两个实验均为 RUNNING 状态

---
