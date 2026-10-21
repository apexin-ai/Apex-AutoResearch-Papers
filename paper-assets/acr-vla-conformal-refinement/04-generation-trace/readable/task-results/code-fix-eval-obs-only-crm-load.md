# code fix eval obs only crm load

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-eval-obs-only-crm-load_20260514T124633_result.json`
- **Structured JSON:** [`cd836c0a774c832b8b12.json`](../../sessions/cd/cd836c0a774c832b8b12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成：

1. **bjb1 旧进程 PID 203968** — 已 kill
2. **bjb1 + bjb2 evaluate.py** — 已修复，CRM 加载条件包含 `crm_obs_only`，`unc_dim=0` 分支正确
3. **eval-obs-only-spatial-v3** — bjb1:cuda:2, PID 211961, RUNNING
4. **CRM 加载验证** — 日志显示 `[eval] CRM loaded from .../crm_best.pt (327,198 params)`，无 TypeError，正在加载 LIBERO spatial 环境

---
