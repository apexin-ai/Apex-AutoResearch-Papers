# diagnose 14b registry fix and qwen check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_14b-registry-fix-and-qwen-check_20260521T030610_result.json`
- **Structured JSON:** [`e8b70af53673b5fa88df.json`](../../sessions/e8/e8b70af53673b5fa88df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。

## 14B RSFT @1024 实际 metrics（已修正）
- **truncated**: 105（原 registry 值 0 → 修正为 105，rate=10.7%）
- ign_f1=0.5886, evi_f1_joint=0.4859
- Registry 已更新，增加了 evi_f1_joint、precision/recall 等完整字段

## cuda:1 状态
- **PID 70388**: alive（运行 20分34秒，status=S）
- **GPU 1 显存**: 32503 MiB（被 plan017_14b_rsft_eval_2048 占满）

## Qwen SFT with-evidence 截断率（全部 @1024，n_total=985）

| Scale | Eval ID | Seed | truncated | rate | ign_f1 |
|-------|---------|------|-----------|------|--------|
| **1.7B** | qwen3_1_7b_sft_eval | 42 | 314 | **31.9%** | 0.4786 |
| **1.7B** | plan019_1_7b_sft_s43_eval | 43 | 408 | **41.4%** | 0.4286 |
| **1.7B** | plan019_1_7b_sft_s44_eval | 44 | 473 | **48.0%** | 0.4321 |
| **4B** | d111_4b_sft_s42_reeval | 42 | 288 | **29.2%** | 0.3974 |
| **4B** | wave1_sft_4b_s43_eval_r2 | 43 | 318 | **32.3%** | 0.4365 |
| **4B** | wave1_sft_4b_s44_eval_r2 | 44 | 249 | **25.3%** | 0.4734 |
| **8B** | qwen3_8b_sft_eval | 42 | 313 | **31.8%** | 0.5051 |
| **8B** | 8b_sft_s43 | 43 | 139 | **14.1%** | 0.5324 |
| **8B** | plan019_8b_sft_s44_eval | 44 | 306 | **31.1%** | 0.4681 |

## 建议

所有 Qwen SFT evals 截断率远超 5%（14%–48%），全部需要 @2048 重跑。优先级：
1. **1.7B** 截断最严重（31–48%），但模型小、推理快
2. **4B** 截断 25–32%
3. **8B** 截断 14–31%

**cuda:1 当前被占用**（plan017_14b_rsft_eval_2048 运行中），无法立即安排新任务。cuda:0/2/3 各占 18879 MiB，也都在忙。需要等当前任务完成后再安排 @2048 重跑。

---
