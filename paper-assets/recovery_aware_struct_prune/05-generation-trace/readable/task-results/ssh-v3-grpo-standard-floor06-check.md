# ssh v3 grpo standard floor06 check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_v3_grpo_standard_floor06_check_20260523T125543_result.json`
- **Structured JSON:** [`fff21efc82d2d7004c64.json`](../../sessions/ff/fff21efc82d2d7004c64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
v3 MATH-500: 运行中, PID=alive (7h14m+), 进度=493/500 (99%)
  输出文件: /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_2048_v3.json（尚未写入）
  日志: /tmp/eval_math500_sft_standard_20_2048_v3.log
  预计数分钟内完成

GRPO Standard MATH-500:
  文件: /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_standard_20_fair_v2.json
  accuracy=26.4% (132/500) ← 不是 21.0%
  模型: grpo_stage2_standard_20_fair
  eval script: NEW（dict 格式，含 accuracy/n_correct/n_total）
  EOS: 55.6% natural, 44.4% truncated, avg_len=1128
  ⚠️ 21.0% 来源待查，此文件记录为 26.4%

Floor 0.6 v2: 运行中（GSM8K eval 阶段），GPU 0
  进度=344/1319 (26%), acc=64.67% (at 300/1319)
  速度: ~3s/sample, 预计还需 ~50 min
  注: 282→283 有 6 min 停顿，已恢复
```

补充：GPU 1 上刚启动了一个新的 GRPO Standard MATH-500 v3 eval（21:16 开始，日志 `eval_math500_grpo_standard_20_fair_2048_v3.log`）。

---
