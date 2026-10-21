# ssh check eval progress all

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_eval_progress_all_20260524T005336_result.json`
- **Structured JSON:** [`6b9cdefdc82ba5337316.json`](../../sessions/6b/6b9cdefdc82ba5337316.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐了。汇总：

当前时间约 **08:54 UTC** (May 24)

| 实验 | Server:GPU | 进度 | 平均速度 | tqdm 瞬时 | ETA (UTC) |
|------|-----------|------|---------|----------|-----------|
| sft_standard_25_fixed_v2 | westd:0 | **213/500** (43%) | 62s/it | 55s/it | ~13:50 |
| grpo_rasp_alpha2p0_20_fixed | westd:1 | **323/500** (65%) | 38s/it | 8.9s/it | ~09:20 – 10:45 |
| sft_rasp_alpha2p0_20_fixed | westd:2 | **286/500** (57%) | 34s/it | 58s/it | ~11:00 – 12:22 |
| grpo_cka_only_25_fixed | westd:3 | **401/500** (80%) | 30s/it | 3.5s/it | ~09:00 – 09:44 |
| sft_random_20_fixed_v3 | westb:0 | **83/500** (17%) | 68s/it | 71s/it | ~16:46 |
| grpo_random_20_fixed | westb:1 | **154/500** (31%) | 71s/it | 81s/it | ~15:44 |

**关键发现：**

1. **westd:2 (sft_rasp_alpha2p0_20_fixed) 没有快完成。** 预期 ~14.6s/it，实际平均 34s/it、瞬时 58s/it。仅完成 57%，还需 2-3.5 小时。与预期的 00:14 UTC 完成差距很大。

2. **最快完成的两个**是 westd:3 (grpo_cka_only_25, 80%) 和 westd:1 (grpo_rasp_alpha2p0, 65%)——两个 GRPO 模型的 eval 速度变化剧烈（瞬时速度极快可能因为某些问题生成很短的回答就停了）。

3. **最慢的两个**是 westb 上的两个：sft_random (17%, ~16:46 UTC) 和 grpo_random (31%, ~15:44 UTC)。

4. westd:0 (sft_standard_25) 稳定但慢，预计 ~13:50 UTC。

---
