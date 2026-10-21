# ops full status and downstream pipeline

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_status_and_downstream_pipeline_20260517T004956_result.json`
- **Structured JSON:** [`f51732b12a3f6fc51a4f.json`](../../sessions/f5/f51732b12a3f6fc51a4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CED scoring 正常 - 500/24216 scored，预计 ~80 min 完成。

---

## 状态总结

| 实验 | GPU | 状态 | 进度/结果 |
|------|-----|------|-----------|
| **plan_007_r5** Re-DocRED eval | - | ✅ DONE | F1=0.4234, ign_F1=0.4145, evi_F1=0.8182, EDCR=0.621 |
| **plan_002** test eval | 1 | ▶️ running | 85/250 batches (~34%), ETA ~2h |
| **plan_006** 1.7B candidates | - | ✅ DONE | 3027/3027 docs, 24216 gens, 11h |
| **plan_006** 1.7B CED scoring | 0 | ▶️ running | 500/24216, PID 395619, ETA ~80min |
| **plan_006** 8B candidates | 3 | ▶️ running | 2503/3027 (83%) |
| **plan_016** LLaMA candidates | 2 | ▶️ running | 2743/3027 (91%) |

## 已完成操作
1. Registry 更新：plan_007_r5 → DONE (with metrics)
2. Registry 更新：plan_006_qwen3_1_7b_rsft_candidates → DONE
3. **已启动 CED scoring** (GPU 0, PID 395619) for 1.7B candidates

## 待 pipeline（无法立即启动）
- 8B CED scoring: 等 8B candidate gen 完成 + GPU 空闲
- LLaMA CED scoring: 等 LLaMA candidate gen 完成 + GPU 空闲
- 8B 预计再跑 ~3-4h，LLaMA ~2-3h

---
