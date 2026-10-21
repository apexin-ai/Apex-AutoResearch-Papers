# diagnose eval obs only object norm02 seed51

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-object-norm02-seed51_20260520T193400_result.json`
- **Structured JSON:** [`8e818798bdf6952718c6.json`](../../sessions/8e/8e818798bdf6952718c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**两个实验都已正常完成，非真正失败。**

### eval-obs-only-object-norm02-seed51
- **根因**：Cron false positive — eval 脚本不写 sentinel/W&B，进程正常退出后 cron 5 次检测均无标记 → 自动标记 failed
- **实际状态**：正常完成，JSON 已写入（05-21 03:20）
- **结果**：crm_obs_only / object / norm=0.2 / seed=51 → **SR = 17.0% (17/100)**

### eval-perdof-object-norm02-seed50（同服务器同期）
- **根因**：同上
- **实际状态**：正常完成，JSON 已写入（05-21 03:22）
- **结果**：crm_perdof / object / norm=0.2 / seed=50 → **SR = 10.0% (10/100)**

memory.md 中已有这两个实验的诊断记录和结果数据（在"失败模式 Cron false positive 批量"条目和"2026-05-20 新增 eval 结果"表格中），无需重复追加。

**结论**：均无需重跑，需手动修正 conclusion=success 并补录 metrics。

---
