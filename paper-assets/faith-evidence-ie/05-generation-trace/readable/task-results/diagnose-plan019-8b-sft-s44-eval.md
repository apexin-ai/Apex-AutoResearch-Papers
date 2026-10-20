# diagnose plan019 8b sft s44 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan019_8b_sft_s44_eval_20260518T234138_result.json`
- **Structured JSON:** [`4aa6709244ce04fcdbb8.json`](../../sessions/4a/4aa6709244ce04fcdbb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**实验实际成功完成了**，不是失败。

日志路径与 Cron 监控配置不一致导致误报：
- Cron 监控查找：`~/runs/faith-evidence-ie/plan019_8b_sft_s44_eval.log`
- 实际日志位置：`/root/autodl-tmp/eval_results/plan019_8b_sft_s44_eval.log`

### 实验结果

| 指标 | 值 |
|---|---|
| F1 | 0.4841 |
| **Ign-F1** | **0.4681** |
| Evi-F1(DREEAM) | 0.3839 |
| Evi-F1(TP) | 0.8361 |
| EDCR | 0.6697 |
| Format OK | 985/985 (100%) |
| Truncated | 306/985 |
| Predictions | 16690 |

推理耗时约 1h56m，于 2026-05-19 07:33 正常结束。metrics.json 和 predictions.json 均已写入 `/root/autodl-tmp/eval_results/plan019_8b_sft_s44_eval/`。

### 根因

Cron 监控的 `log_path` 配置指向 `~/runs/faith-evidence-ie/`，但这次 eval 的日志实际写到了 `/root/autodl-tmp/eval_results/`。监控找不到日志文件，判定为 "Process exited without valid W&B metrics"，auto-resolved as failed。

### 行动建议

1. **无需重跑** — 实验已成功，结果完整
2. 需要将 Ign-F1=0.4681 录入实验记录，与 canonical s42 (Ign-F1=0.5051) 配对计算 2-seed mean±std
3. 修正 Cron 监控的 log_path 配置，或统一 eval 日志输出目录，避免后续类似误报

---
