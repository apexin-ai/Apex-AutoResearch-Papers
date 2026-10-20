# ops sft retry gpu0 gpu1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_sft-retry-gpu0-gpu1_20260515T110259_result.json`
- **Structured JSON:** [`cfdd4dacff6f617fefcb.json`](../../sessions/cf/cfdd4dacff6f617fefcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 SFT 重试已提交并正常训练中：

| 实验 | exp_id | GPU | PID | 步数 | 预计时长 |
|------|--------|-----|-----|------|----------|
| 1.5B d025 s123 | `exp_001_sft_15B_d025_s123_v2` | cuda:0 | 549516 | 0/3384 | ~1h55m |
| 1.5B d005 s123 | `exp_001_sft_15B_d005_s123_v2` | cuda:1 | 549858 | 0/3177 | ~1h50m |

日志路径：`/tmp/sft_15B_d025_s123_v2.log`、`/tmp/sft_15B_d005_s123_v2.log`

---
