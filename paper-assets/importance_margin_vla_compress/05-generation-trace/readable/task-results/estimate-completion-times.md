# estimate completion times

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_estimate_completion-times_20260527T200327_result.json`
- **Structured JSON:** [`bc9c3d79fce1270d7779.json`](../../sessions/bc/bc9c3d79fce1270d7779.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the summary. All times are in log timezone (appears to be UTC). Current log time: ~04:03.

---

## cqa1-33015

| 实验 | GPU | 进度 (task/ep) | 已用时间 | 预估剩余 | 预估完成 |
|------|-----|---------------|---------|---------|---------|
| pi05_l2norm_k05_seed43 | cuda:0 | T5/20 (270/500) | ~130 min | ~111 min | ~05:51 |
| pi05_l2norm_k09_seed44 | cuda:1 | T2/40 (140/500) | ~53 min | ~136 min | ~06:18 |
| pi05_attn_k09_seed43 | cuda:2 | T9/10 (460/500) | ~220 min | ~19 min | **~04:21** |
| pi05_attn_k075_seed43 | cuda:3 | T4/20 (220/500) | ~106 min | ~135 min | ~06:16 |

## westd-41074

| 实验 | GPU | 进度 (task/ep) | 已用时间 | 预估剩余 | 预估完成 |
|------|-----|---------------|---------|---------|---------|
| pi05_attn_k085_seed43 | cuda:0 | T7/30 (380/500) | ~122 min | ~39 min | **~04:42** |
| pi05_attn_k07_seed43 | cuda:1 | T8/10 (410/500) | ~129 min | ~28 min | **~04:28** |
| pi05_random_k09_seed44 | cuda:2 | T2 done (150/500) | ~54 min | ~127 min | ~06:10 |
| pi05_attn_k05_seed43 | cuda:3 | T3/30 (180/500) | ~52 min | ~104 min | ~05:45 |

## westd-27271 (2 experiments/GPU, concurrent)

| 实验 | GPU | 进度 (task/ep) | 已用时间 | 预估剩余 | 预估完成 |
|------|-----|---------------|---------|---------|---------|
| pi05_random_k05_seed43 | cuda:0 | T7/20 (370/500) | ~118 min | ~42 min | **~04:43** |
| pi05_attn_k085_seed43_v2 | cuda:0 | T5/40 (290/500) | ~99 min | ~80 min | ~05:22 |
| pi05_l2norm_k07_seed43 | cuda:1 | T7/30 (380/500) | ~116 min | ~39 min | **~04:41** |
| pi05_attn_k075_seed43_v2 | cuda:1 | T5 done (300/500) | ~106 min | ~70 min | ~05:12 |

## westd-38929

| 实验 | GPU | 进度 (task/ep) | 已用时间 | 预估剩余 | 预估完成 |
|------|-----|---------------|---------|---------|---------|
| OV random_k085_v3 | cuda:0 | **已完成** ✅ | 559.8 min | — | SR=45.0% |
| OV attn_k085_v3 | cuda:1 | **已完成** ✅ | 548.6 min | — | SR=45.8% |
| pi05_l2norm_k05_seed44 | cuda:2 | T3/10 (160/500) | ~51 min | ~108 min | ~05:49 |
| pi05_attn_k05_seed43 | cuda:3 | T4/30 (230/500) | ~73 min | ~93 min | ~05:35 |

---

**关键发现：**

1. **westd-38929 cuda:0/1 已空闲** — 两个 OV 实验均已完成（EXIT_CODE=0），GPU 可用于新任务
2. **即将完成（<45min）：** cqa1 cuda:2 (attn_k09), westd-41074 cuda:0/1 (attn_k085/k07), westd-27271 cuda:0/1 的第一个实验 (random_k05, l2norm_k07)
3. **最晚完成：** ~06:18 UTC — cqa1 cuda:1 (l2norm_k09_seed44) 和 westd-41074 cuda:2 (random_k09_seed44)
4. **所有 π0.5 实验预计在 06:20 UTC 前全部完成**，远在 C002 截止时间 (05-28 12:00 UTC) 之前

注：westd-38929 上的 OV 实验实际名称是 random_k085 和 attn_k085（非用户清单中的 k095/k075），且已完成。

---
