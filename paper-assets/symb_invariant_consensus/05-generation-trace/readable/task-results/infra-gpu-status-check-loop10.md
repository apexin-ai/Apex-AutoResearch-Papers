# infra gpu status check loop10

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-check-loop10_20260519T111823_result.json`
- **Structured JSON:** [`dd55d7ee3d9ca8b43264.json`](../../sessions/dd/dd55d7ee3d9ca8b43264.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

## 两台服务器状态

**westd-25068**: GPU 0/1/3 满载运行 exp-065/066/062，**GPU 2 空闲**（exp-067 已完成）

**westd-16639**: GPU 1/2/3 满载运行 exp-068/064/048，**GPU 0 空闲**（exp-063 已完成）

## 新完成的实验

| 实验 | 模型 | SC | SICA | Delta |
|------|------|----|------|-------|
| **exp-063** | LLaMA-3.1-8B FOLIO-204 | 66.2% | 61.8% | **-4.4pp** |
| **exp-067** | Mistral-7B FOLIO s789 | 54.4% | 53.9% | **-0.49pp** |

- exp-063: 确认低能力模型 SICA 无增益，与 exp-020 一致
- exp-067: Mistral 4-seed 汇总 mean delta=+1.47pp，variance 很大（+3.43, +2.94, 0.00, -0.49）

两个实验注册表已更新为 DONE。空闲 GPU：westd-25068 cuda:2、westd-16639 cuda:0。

---
