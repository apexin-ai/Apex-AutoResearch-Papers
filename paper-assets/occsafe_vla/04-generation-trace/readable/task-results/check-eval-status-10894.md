# check eval status 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_status_10894_20260526T113521_result.json`
- **Structured JSON:** [`834da4ddfe6bb126b0ef.json`](../../sessions/83/834da4ddfe6bb126b0ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 进程全部存活且正常运行：

| exp_id | 状态 | 已运行 | GPU | GPU利用率 | 日志进度 |
|--------|------|--------|-----|-----------|----------|
| mvp_occ_s3_v2_eval (PID 186624) | **running** | 24:12 | cuda:1 | 0% (瞬时) | T5: 28/50 (56%) |
| full_occ_ln_s3_v2_eval (PID 186832) | **running** | 24:10 | cuda:2 | 53% | T5: 27/50 (54%) |
| ablation_occ_detach_s3_v2_eval (PID 189896) | **running** | 23:22 | cuda:3 | 37% | T5: 34/50 (68%) |

三个进程都在评估 libero_spatial 的 Task 5，各跑了约 24 分钟。ablation_occ_detach 进度最快（68%），另外两个在 54-56%。cuda:0 被其他任务占用（99% 利用率，62GB 显存），不影响这三个 eval。一切正常。

---
