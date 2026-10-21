# code d146 gpu emergency

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d146-gpu-emergency_20260519T234845_result.json`
- **Structured JSON:** [`41c378988e0b6be6cd48.json`](../../sessions/41/41c378988e0b6be6cd48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**诊断结果：Pipeline 正常运行，无需恢复。**

| 实验 | 状态 | 进度 |
|------|------|------|
| d146_pf_exec_s42 | ✅ 完成 | 500/500 |
| d146_pf_exec_s43 | ✅ 完成 | 500/500 |
| d146_pf_exec_s44 | ✅ 完成 | 500/500 |
| d146_pf_isr_s42 | ✅ 完成 | 500/500 |
| d146_pf_isr_s43 | 🔄 训练中 | 472/500 (94%) |
| d146_pf_isr_s44 | ⏳ 未开始 | 目录不存在 |

当前状态：
- **PID 599223** 正在 GPU 0 上训练 `isr_s43`，GPU 利用率 91%，显存 85GB/98GB
- `isr_s43` 已跑到 step 472/500，预计很快完成
- 之后还剩 `isr_s44` 一个实验

你看到的 0% 利用率可能是瞬时采样（checkpoint 写盘或 batch 间隙），现在已恢复到 91%。不需要任何干预。

---
