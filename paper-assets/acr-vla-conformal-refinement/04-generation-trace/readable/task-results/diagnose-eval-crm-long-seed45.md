# diagnose eval crm long seed45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-crm-long-seed45_20260519T220714_result.json`
- **Structured JSON:** [`ed731f6d9a84390d0026.json`](../../sessions/ed/ed731f6d9a84390d0026.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写到 `artifacts/diagnose_crm_long_seed45.md`。

**结论：实验成功完成，是监控误报。**

原因：实验未通过标准 job 提交系统启动，日志和哨兵文件不在 `~/runs/` 和 `/tmp/agent-ml-exit/` 标准路径下，cron 找不到就误判为 dead。实际上输出 JSON 完整存在（`logs/eval_long_obs_only_norm02_seed45.json`），overall success rate 18.0%（18/100），日志正常结束无报错。不需要重试。

---
