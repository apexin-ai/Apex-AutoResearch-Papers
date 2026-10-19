# ops emergency disk cleanup westd

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_emergency-disk-cleanup-westd_20260518T175029_result.json`
- **Structured JSON:** [`7ef80213ec4674b041a2.json`](../../sessions/7e/7ef80213ec4674b041a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**结果：**

| 指标 | 清理前 | 清理后 |
|------|--------|--------|
| 已用 | 228G (92%) | 142G (57%) |
| 可用 | 23G | **109G** |
| 释放 | — | **~86G** |

**清理内容：**
- gsweep-g050/g080/g095/g100-h5 checkpoints: 84G
- exp021_ragen_sft_v4 + qwen3 版: 6.6G
- 12 个旧 ray sessions: ~1.5G

**保留确认：**
- `factorial-h2-episode-adv/` (62G, seed1 完成)
- `factorial-h2-episodeadv-seed2/` (21G, 运行中)
- 两个活跃 ray sessions (PID 576727 + PID 34193)

109GB 可用，两个实验有充足空间继续运行。

---
