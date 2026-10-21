# ops cleanup bjb2 cuda2 orphan and check bjb1 cuda5

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-bjb2-cuda2-orphan-and-check-bjb1-cuda5_20260515T183116_result.json`
- **Structured JSON:** [`ec86913d016f130c0017.json`](../../sessions/ec/ec86913d016f130c0017.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 部分 A：bjb2-28827 — cuda:2 孤儿清理 ✓

**PID 115384 已 kill。** cuda:2 显存从 11324MiB → 5664MiB，GPU util 从 92% → 18%。

cuda:2 上仍保留 PID 117278 — 这是 **eval-mag-perdof-norm0p3-object**（`--mode crm_perdof --benchmark object --max_correction_norm 0.3`），是合法进程。

**bjb2-28827 GPU 占用（kill 后）：**

| GPU | PID | 显存 | Util | 说明 |
|-----|-----|------|------|------|
| cuda:0 | 105947 | 5182MiB / 24564MiB | 18% | 运行中 |
| cuda:1 | 109655 | 5645MiB / 24564MiB | 18% | 运行中 |
| cuda:2 | 117278 | 5645MiB / 24564MiB | 18% | eval-mag-perdof-norm0p3-object |
| cuda:3 | 118886 | 5645MiB / 24564MiB | 19% | eval-mag-perdof-norm03-object (P1修复版) |
| cuda:4 | 101616 | 5200MiB / 24564MiB | 18% | 运行中 |
| cuda:5 | 103034 | 5200MiB / 24564MiB | 18% | 运行中 |

**6/6 GPU 全部在用，无空闲卡。**

---

### 部分 B：bjb1-32546 — cuda:5 **不空闲**

cuda:5 有 PID 127741 在跑：`--mode crm_perdof --benchmark object --max_correction_norm 0.2 --output_file logs/eval_object_perdof_norm02.json`（eval-mag-perdof-norm02-object），5182MiB，23% util，正常运行中。

**bjb1-32546 GPU 占用：**

| GPU | PID(s) | 显存 | Util | 说明 |
|-----|--------|------|------|------|
| cuda:0 | 121334 + 123062 | 7103MiB / 24564MiB | 86% | 2个进程，util 高 |
| cuda:1 | 111718 | 5146MiB / 24564MiB | 22% | 运行中 |
| cuda:2 | 114673 | 5182MiB / 24564MiB | 22% | 运行中 |
| cuda:3 | 118214 | 5182MiB / 24564MiB | 22% | 运行中 |
| cuda:4 | 134103 | 5645MiB / 24564MiB | 22% | 运行中 |
| cuda:5 | 127741 | 5182MiB / 24564MiB | 23% | eval-mag-perdof-norm02-object |

**6/6 GPU 全部在用，无空闲卡。** cuda:0 有两个进程值得注意（可能有类似的孤儿问题）。

---

**Registry 待部署实验（PREPARING，未 failed/killed）：**
- `eval-acr-object-obs-only-default` — obs_only CRM v3-norm, default max_correction_norm, object benchmark
- `eval-mag-perdof-norm0p3-object` — 已在 bjb2-28827:cuda:2 运行（PID 117278）

两台服务器 12 张卡全满，目前无可用 GPU 部署新实验。

---
