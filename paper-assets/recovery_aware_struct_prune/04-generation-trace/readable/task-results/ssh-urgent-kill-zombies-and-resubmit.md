# ssh urgent kill zombies and resubmit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_kill_zombies_and_resubmit_20260523T211441_result.json`
- **Structured JSON:** [`ab2d62ea164fa67a8ba3.json`](../../sessions/ab/ab2d62ea164fa67a8ba3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程均已启动，正在加载模型。

## Kill 结果
- westd: 142647 161700 165259 165865 159074 全部 DEAD
- westb: 322091 327023 全部 DEAD

## GPU 验证
| GPU | 状态 |
|-----|------|
| westd GPU 0 | sft_standard_25_fixed_v2 已在运行 (PID 166245) — 不碰 |
| westd GPU 1 | grpo_rasp (PID 145176) — 不碰 |
| westd GPU 2 | grpo_standard (PID 142486) — 不碰 |
| westd GPU 3 | 已清空，新任务加载中 |
| westb GPU 0 | grpo_cka_only (PID 321428) — 不碰 |
| westb GPU 1 | 已清空，新任务加载中 |

## 重新提交
| 任务 | GPU | PID |
|------|-----|-----|
| westd:0 sft_standard_25_fixed_v2 | 跳过（已在运行 PID 166245） | — |
| westd:3 sft_standard_20_fixed_v3 | ✓ 已提交 | 167047 |
| westb:1 sft_random_20_fixed_v2 | ✓ 已提交 | 327972 |

---
