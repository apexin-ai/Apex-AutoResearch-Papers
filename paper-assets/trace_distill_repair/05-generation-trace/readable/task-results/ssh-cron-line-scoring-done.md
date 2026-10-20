# ssh cron line scoring done

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cron_line_scoring_done_20260515T014221_result.json`
- **Structured JSON:** [`98b1fd271a446e42522b.json`](../../sessions/98/98b1fd271a446e42522b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告

### 1. Line Scoring 最终状态：**SUCCESS**

| 指标 | 值 |
|------|-----|
| Instances | 38 (excluded: fastapi_3, fastapi_5) |
| Total segments | 3,922 |
| Scored | 2,256 |
| Failed | 1,666 (API errors: None content / 502) |
| **Keep** | **38** |
| **Drop** | **2,218** |
| **Error** | **1,666** |
| Keep rate | 1.7% |
| Error rate | 42.5% |
| Elapsed | 14,016s (~3.9h) |
| Output | `/root/trace_distill_repair/pipeline_output/phase2_line_scores.json` (1.83MB) |

### 2. Registry 操作
- `mvp_line_scoring_clean`: status=DONE, conclusion=success, metrics 已写入
- Cron `mvp_line_scoring_clean`: 已删除

### 3. Structural Scoring：**已启动**
- exp_id: `mvp_structural_scoring_clean`
- PID: **85831**
- 状态: RUNNING，已开始处理 `[1/38] black_14`
- Cron 监控: submit_training_job 已自动注册

> 注意：首次提交因 `.bashrc` 有 non-interactive guard (`[ -z "$PS1" ] && return`) 导致 `OPENROUTER_API_KEY` 未 export，已通过 inline export 修复。

---
