# ssh westd phi4 eval and gemma plan

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-phi4-eval-and-gemma-plan_20260519T083848_result.json`
- **Structured JSON:** [`586d9a245be91c57a151.json`](../../sessions/58/586d9a245be91c57a151.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

## Phi-4 Eval 结果（全部完成）

| Condition | MMLU | ARC-Challenge |
|-----------|------|---------------|
| d000 (clean) | 77.47% (10879/14042) | 93.94% (1101/1172) |
| d005 | 78.09% (10966/14042) | 93.94% (1101/1172) |
| d025 | 78.39% (11007/14042) | 94.03% (1102/1172) |
| d050 | 78.67% (11047/14042) | 93.69% (1098/1172) |

d050 刚完成（16:09 CST），四个 dosage 全部 DONE with `.done` sentinel。

## GPU 状态

- **cuda:0**: phi-4_d100_s42 SFT 训练中（55.8GB/97.9GB）
- **cuda:1/2/3**: 全部空闲（0MB）

cuda:3 已释放，可以立即用于 Gemma eval。

## Checkpoint 就绪情况

- **Gemma-2-9B**: d000/d005/d025/d050 四个 adapter 全部就绪（`lora_adapter/` 子目录），base model OK
- **OLMo-2-7B d050**: adapter 就绪（`lora_adapter/` 子目录）

---
