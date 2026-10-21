# diagnose norm005 seed67 and norm01 seed67

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_norm005-seed67-and-norm01-seed67_20260521T044713_result.json`
- **Structured JSON:** [`104d08eb3110e59aa7e0.json`](../../sessions/10/104d08eb3110e59aa7e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**两个实验都是监控误报，实际已正常完成，不需要重跑。**

| 实验 | 服务器 | 状态 | SR | JSON 路径 |
|------|--------|------|-----|-----------|
| norm005-seed67 | bjb1-32546 | 已完成 | **10.0%** (10/100) | `/root/logs/eval_object_crm_obs_only_norm0.05_seed67.json` |
| norm01-seed67 | bjb1-18228 | 已完成 | **14.0%** (14/100) | `/root/logs/eval_object_crm_obs_only_norm0.1_seed67.json` |

**根因**：
- norm005-seed67：registry 之前被错误标记为 `conclusion=failed`，日志实际完整跑完全部 10 tasks × 10 rollouts
- norm01-seed67：进程正常跑完后自然退出（PID 666593 不再存在），监控检测到进程消失误判为异常。registry 之前一直是 RUNNING 状态未更新

**已修正**：
- norm005-seed67：`conclusion` 已从 `failed` 改为 `success`，补充了 notes
- norm01-seed67：已更新为 `DONE/success`，补充了 `log_path` 和 notes

**注意**：两个实验的 JSON 都保存在 `/root/logs/` 而非 `/root/acr-vla-conformal-refinement/logs/`，是因为启动命令的工作目录是 `/root/` 而非项目目录。后续实验建议用绝对路径 `--output_file /root/acr-vla-conformal-refinement/logs/...` 避免此问题。

---
