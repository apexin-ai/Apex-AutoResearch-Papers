# search 008d checkpoint

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_search_008d_checkpoint_20260522T093758_result.json`
- **Structured JSON:** [`de01e793e137b6a36fde.json`](../../sessions/de/de01e793e137b6a36fde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### bjb1-40020: 无任何 008d/008a/008f checkpoint
该服务器 logdir 下没有 008d、008a 的目录。仅有一个 `exp_043_008f_walker_s1/latest.pt`（221MB，May 22）。

---

### bjb1-45299: 008d checkpoint 详情

| 目录 | Checkpoint 文件 | 大小 | 日期 | 最后 step |
|------|----------------|------|------|-----------|
| `exp_008d_subsample_on_h8` | latest.pt | 221MB | May 14 | **55,000** |
| `exp_008d_civo_trigger_s1` | latest.pt | 221MB | May 17 | **52,000** |
| | checkpoint_25000.pt | 221MB | May 17 | 25,000 |
| `exp_008d_civo_trigger_s3` | latest.pt | 221MB | May 17 | **112,000** |
| | checkpoint_25000.pt | 221MB | May 17 | 25,000 |
| | checkpoint_75000.pt | 221MB | May 17 | 75,000 |
| `exp_008d_civo_trigger_s4` | latest.pt | 221MB | May 18 | **112,000** |
| | checkpoint_25000.pt | 221MB | May 18 | 25,000 |
| | checkpoint_75000.pt | 221MB | May 18 | 75,000 |

**最佳 resume 候选**: `exp_008d_civo_trigger_s3` 或 `exp_008d_civo_trigger_s4`，均在 step 112,000，都在 **bjb1-45299** 上。

### 备选：008a / 008f（同在 bjb1-45299）

- **008a**: 5 个目录有 latest.pt，包括 `exp_008a_unexposed_s1/s2`（step 未查，有 checkpoint_25000/75000）、`exp_008a_cheetah_unexposed_s0/s1`
- **008f**: 5 个目录有 latest.pt，包括 `exp_008f_s3_no_dt_embed_walker`（有 checkpoint_25000/75000）、`exp_008f_no_dt_emb_s2/s4`

---
