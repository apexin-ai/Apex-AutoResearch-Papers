# fix extract json backup logs

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_extract-json-backup-logs_20260515T064616_result.json`
- **Structured JSON:** [`b256bd9728dd85d7adbe.json`](../../sessions/b2/b256bd9728dd85d7adbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 结果

**A. argmin-r2 JSON 提取 — 成功**
- 保存到 `logs/eval_reconvla_spatial_r2.json`，6 个顶层 key
- 内容：mode=reconvla, baseline_mode=single, benchmark=spatial, n_rollouts=10
- **overall_success_rate = 0.1** (10%)，只有 1 个 task（pick_up_black_bowl → plate），1/10 成功

**B. 3 个 log 备份 — 全部成功**
- `eval-acr-spatial-v4-scalar-r2.log.bak` ✓
- `eval-acr-spatial-v4-small-r2.log.bak` ✓
- `eval-acr-spatial-v4-obs-only-r3.log.bak` ✓

**C. eval-mag-obsonly-norm03 进程状态 — 存活**
- 2 个 tmux session 在运行：`eval-mag-obsonly-norm03-r2`（14:50 创建）和 `eval-mag-obsonly-norm03-b2`（15:05 创建）
- 两个 python 进程都活跃，均使用 `--output_file logs/eval_mag_obsonly_norm03.json`，cuda:0
- 注意：有两个实例在跑同一个实验（r2 和 b2），都写同一个 output_file，可能会互相覆盖结果

---
