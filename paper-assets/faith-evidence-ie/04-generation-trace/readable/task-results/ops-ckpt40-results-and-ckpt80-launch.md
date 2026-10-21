# ops ckpt40 results and ckpt80 launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_ckpt40-results-and-ckpt80-launch_20260514T231059_result.json`
- **Structured JSON:** [`74cab1228b2947029651.json`](../../sessions/74/74cab1228b2947029651.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

### ckpt-40 eval 结果

| 指标 | 值 |
|------|-----|
| **rel_f1** | **0.0071** (FAIL, 阈值 0.30) |
| precision | 0.0066 |
| recall | 0.0078 |
| tp / pred / gold | 95 / 14434 / 12151 |
| evi_f1 | 0.7584 |
| evi_precision | 0.9113 |
| evi_recall | 0.6494 |
| edcr | 0.9942 |
| format_ok_rate | 0.9939 |
| field_compliance_rate | 0.5675 |
| n_truncated | 424 / 985 (43%) |
| inference_time | 6152s (~102min) |

**结论**：negative。模型预测了 14434 个关系但仅 95 个 TP，precision/recall 均极低。evidence 质量尚可（evi_f1=0.76），但关系抽取本身几乎失败。43% 截断率也是问题。

### ckpt-80 eval

- **PID**: 111731
- **GPU**: cuda:2
- **Log**: `/tmp/eval_lr5e6_ckpt80.log`
- **Cron 监控**: 已注册，120s 轮询
- **预计耗时**: ~100min（参考 ckpt-40）

### 异常

无异常。ckpt-40 日志显示有两次 eval 运行（一次成功写入 `lr5e6_r1_ckpt40/`，另一次写入 `grpo_ced_lr5e6/` 但被 SIGTERM kill），最终结果来自成功的那次。

---
