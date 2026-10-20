# ops full status check 0515

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full_status_check_0515_20260514T224859_result.json`
- **Structured JSON:** [`dc94586b4048673bc4d7.json`](../../sessions/dc/dc94586b4048673bc4d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 全面状态检查报告

| 实验 | GPU | PID | 状态 | 进度 | ETA (UTC) |
|------|-----|-----|------|------|-----------|
| **训练** mvp2_grpo_ced_lr5e6_r1 | cuda:0 | 90080 | ALIVE | 104/200 steps (52%) | ~09:30 (~2.7h) |
| **ckpt-60 eval** mvp2_eval_lr5e6_r1_ckpt60_r2 | cuda:1 | 108185 | ALIVE | 13/62 batches (21%) | ~08:05 (~75min) |
| **ckpt-40 eval** mvp2_eval_lr5e6_r1_ckpt40_r2 | cuda:2 | 101842 | ALIVE | ~55/62 (89%) 估算 | ~07:00 (~10min) |
| **SFT baseline eval** mvp2_eval_sft_baseline | cuda:3 | 104979 | ALIVE | 34/62 batches (55%) | ~07:35 (~44min) |

### ckpt-60 eval 修复

- PID 108185 正常运行，tmux `eval_ckpt60_r2` 存活
- Registry 中 `conclusion` 被 cron 误标为 `"killed"`，但 `status` 仍为 `RUNNING`
- 无法将 conclusion 清空（API 不支持空值）。已在 notes 中标注"忽略 conclusion 字段，以 status=RUNNING 为准"
- 进程完成后 cron 会重新设置正确的 conclusion

### 训练关注点

- Step 104/200，reward 趋势：format 0.249, f1 0.016, ced 0.018, total 0.283
- KL 偶发飙升（step 85: 1.39e7）但自动恢复，训练未中断
- checkpoint-100 已保存

### 预计结果交付顺序

1. ckpt-40 eval → ~10 min
2. SFT baseline eval → ~44 min
3. ckpt-60 eval → ~75 min
4. 训练完成 → ~2.7h

---
