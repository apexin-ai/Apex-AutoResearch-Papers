# audit cron log judgment

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_cron_log_judgment_20260527T070149_result.json`
- **Structured JSON:** [`249f47046fb15665c3f1.json`](../../sessions/24/249f47046fb15665c3f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

判定结果汇总：

| exp_id | 日志状态 | 判定 | SR值/说明 |
|--------|---------|------|----------|
| eval_pi05_baseline_goal_seed42_strict | Registry 已标记 DONE(killed)；~/runs 日志显示新进程在跑（T3 ep=20/50），autodl-tmp 路径另一实例等 GPU | **仍在运行** | 原实验被 kill，新实验未完成。无需更新 registry（killed 记录准确） |
| eval_pi05_attn_k09_long_seed42_strict | 完整完成 10/10 tasks | **success** (已录入) | SR=64.0% (320/500) |
| eval_pi05_attn_k085_long_seed42_strict | 完整完成 10/10 tasks | **success** (已修正，原误标 failed) | SR=50.0% (250/500) |

关键修正：实验 3 从 DONE(failed) → DONE(success)，补录 metrics 和 per-task SR。实验 1 有新进程在跑但尚未完成，当前 registry 的 killed 记录仍然有效。

---
