# diagnose recovery vanilla s1

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_recovery-vanilla-s1_20260516T083711_result.json`
- **Structured JSON:** [`7a0bdbc7e17e8e99a874.json`](../../sessions/7a/7a0bdbc7e17e8e99a874.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成，cron 误报。结果明确：

```
ACTUAL_STATUS: success
REASON: cron 误报——eval 脚本不写 sentinel 文件，cron 轮询无信号后误判为 failed。实际 eval 已于 2026-05-16 16:22 正常完成，47/47 tasks 全部跑完，结果已写入 JSON。
METRICS:
- recovery_rate: 0.66 (66%)
- recovery_count: 31/47
- detection_rate: 0.0
- C1_context_truncation: 8/12 (0.667)
- C4_observation_masking: 6/11 (0.545)
- P1_step_order_swap: 8/12 (0.667)
- P2_sub_goal_deletion: 9/12 (0.75)
LOG_PATH: /tmp/eval_recovery_vanilla_s1.log
OUTPUT_PATH: /root/autodl-tmp/tax_error_inject_agent/eval_results/v4_vanilla_recovery_eval_s1.json
```

注意：cron 没找到日志是因为它找的路径是 `~/runs/tax_error_inject_agent/recovery-vanilla-s1.log`（不存在），实际日志在 `/tmp/eval_recovery_vanilla_s1.log`。这个 eval 是通过 tmux 直接启动的，不走 cron 的 job wrapper，所以没有 sentinel 文件和标准化日志路径。

---
