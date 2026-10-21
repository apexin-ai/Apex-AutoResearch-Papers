# ops westd full status harvest

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_full_status_harvest_20260518T211029_result.json`
- **Structured JSON:** [`b3432bc7e52940b765fa.json`](../../sessions/b3/b3432bc7e52940b765fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 GPU 全部在跑，无异常。

**cuda:0 — grpo_cka_only_20_extended_300**
286/300 (95%)，ETA ~26min。训练正常推进，无需操作。完成后再提取 reward 轨迹并更新 registry。

**cuda:1 — eval_math500_grpo_standard_20_fair_v2**
192/500 (38%)，未崩溃。结果文件尚未生成。Interim acc@150 = **0.3133**。数据集加载时网络不可达，已回退到缓存版本，运行正常。ETA ~3-4h。无需操作。

**cuda:2 — math500_sft_cka_only_20_v4**
389/500 (78%)，Interim acc@350 = **0.3029**。ETA ~1-2h。无需操作。

**cuda:3 — math500_grpo_rasp_20_fair**
283/500 (57%)，Interim acc@250 = **0.2760**。ETA ~2-3h。无需操作。

**总结**：4 卡满载运行，无崩溃无卡死。cuda:0 训练最先完成（~30min），其余 3 个 eval 任务按序完成。当前无需干预。

---
