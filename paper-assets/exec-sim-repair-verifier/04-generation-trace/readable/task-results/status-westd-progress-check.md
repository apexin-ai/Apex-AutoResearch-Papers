# status westd progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_westd-progress-check_20260514T082849_result.json`
- **Structured JSON:** [`1b35ee6ac936ad99bf51.json`](../../sessions/1b/1b35ee6ac936ad99bf51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `memory.md`。

**摘要：4 个进程全部正常运行。**

| GPU | 任务 | 进度 | 关键指标 | 预计完成 |
|-----|------|------|----------|----------|
| cuda:0 | CWM seed123 eval | 42.7% (4176/9784) | acc=57.9% | ~10h 后 |
| cuda:1 | CWM v12 eval | 43.2% (4224/9784) | acc=57.8% | ~10h 后 |
| cuda:2 | 8B CWM 训练 | 6.0% (step ~400/6633) | loss=4.27, eval_loss=0.29 | ~21.5h 后 |
| cuda:3 | 8B CLS seed123 训练 | 12.1% (step ~800/6633) | loss=1.12, eval_loss=0.11 | ~13.5h 后 |

**Checkpoints**:
- CWM 8B: checkpoint-100/200/300 (`/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/`)
- CLS 8B seed123: checkpoint-200/400/600 (`/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/`)

**注意**: repo-level-cwm-v12.log 显示 CWM v12 训练之前在 step 756 被 kill (EXIT_CODE=137)，当前 cuda:1 跑的是 v12 eval 而非训练。两个 eval 的 accuracy 非常接近 (~57.8-57.9%)。

---
