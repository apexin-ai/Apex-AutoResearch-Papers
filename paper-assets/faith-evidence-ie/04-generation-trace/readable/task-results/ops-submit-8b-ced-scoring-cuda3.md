# ops submit 8b ced scoring cuda3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_8b_ced_scoring_cuda3_20260517T034726_result.json`
- **Structured JSON:** [`4af24490acd4d8c6e800.json`](../../sessions/4a/4af24490acd4d8c6e800.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**状态总结：**
- `plan_006_qwen3_8b_ced_scoring` 已在 cuda:3 启动，PID 411027
- NLI 模型（DeBERTa-v3-base）加载成功，显存占用 ~1.4GB
- 24216 条 candidates（3027 docs）正在 CED scoring
- Registry 已更新为 RUNNING

首次尝试因 `HF_HUB_OFFLINE=1` 导致无法定位缓存中的模型，第二次改用本地快照绝对路径解决。

---
