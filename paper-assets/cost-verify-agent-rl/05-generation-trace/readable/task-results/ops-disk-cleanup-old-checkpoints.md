# ops disk cleanup old checkpoints

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup-old-checkpoints_20260514T124418_result.json`
- **Structured JSON:** [`f1dd01f047df50a65332.json`](../../sessions/f1/f1dd01f047df50a65332.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**结果汇总：**

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 194G (78%) | 113G (45%) |
| 可用 | 57G | 138G |
| **释放空间** | — | **81G** |

**保留的 checkpoint：**
- `exp013f` — 62G（最新完成实验）
- `exp008_sft` — 23G（SFT 基线，`qwen3_sft_final` 软链接指向它）

无 Ray 临时文件需要清理。

---
