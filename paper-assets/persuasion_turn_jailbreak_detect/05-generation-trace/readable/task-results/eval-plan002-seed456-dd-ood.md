# eval plan002 seed456 dd ood

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan002-seed456-dd-ood_20260518T070820_result.json`
- **Structured JSON:** [`ec7dc6843039d9dddef1.json`](../../sessions/ec/ec7dc6843039d9dddef1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**结果汇总 — plan_002 9-class persuasion treatment DD OOD (2 seeds)**:

| K | seed=42 | seed=456 |
|---|---------|----------|
| k=1 | 1.0000 | 0.9715 |
| k=2 | 0.9904 | 0.9622 |
| k=3 | 0.9904 | 0.9350 |
| k=5 | 1.0000 | 0.9904 |
| full | 1.0000 | 0.9904 |

**核心发现**：
- seed=456 DD OOD F1 全面 >0.93，precision=1.0（无误报），仅有少量漏检
- 与 seed=42 的 F1=1.0 相比确实存在方差，但幅度远小于 control variants（MLM std=0.115, Topic std=0.207）
- 2-seed 的 DD OOD Full F1 均值 = 0.9952，最差 K=3 也有 0.935
- **核心 claim 安全**：9-class treatment 的跨攻击泛化优势在多 seed 下稳定，不像 control 那样出现大幅波动

---
