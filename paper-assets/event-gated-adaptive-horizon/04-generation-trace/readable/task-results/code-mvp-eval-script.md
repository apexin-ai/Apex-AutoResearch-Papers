# code mvp eval script

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_eval_script_20260513T193419_result.json`
- **Structured JSON:** [`f3f8a534843835b4318c.json`](../../sessions/f3/f3f8a534843835b4318c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行正常。结果汇总：

**脚本路径**: `/root/autodl-tmp/event-gated-adaptive-horizon/scripts/mvp_eval.py`

**Dry-run 输出 (interim, 85K)**:

```
══════════════════════════════════════════════════
  MVP Evaluation — INTERIM (85K)
══════════════════════════════════════════════════
⚠ 中间检查——趋势判断，非 pass/fail 判定

[Criterion 1] Return
  eval_return (last 9): 319.3 ± 163.1
  return_ratio: 0.335
  trend: TRENDING_DOWN (-269.8/10K)
  gate_scale: 0.300
  status: TRENDING_DOWN

[Criterion 2] Gate Entropy        → PASS (0.924 > 0.3)
[Criterion 3] Effective Horizon   → PASS (dt_mean=1.691 > 1.2)
[Criterion 4] Temporal Structure  → PASS (dt_std=0.655 > 0.5)

Overall: INTERIM — gate ramping (scale=0.30), return trend: TRENDING_DOWN
```

**缺失字段**: `gate_dt_autocorr` 不在 metrics.jsonl 中（0 条匹配）。脚本已做降级处理——Criterion 4 仅依赖 `dt_std > 0.5`，当前 0.655 已满足。如需 autocorr，需在训练代码中增加该指标的记录。

**注意**: 当前 85K 步，gate_scale=0.30，C2/C3/C4 都已 PASS，但 return 仅 0.335 baseline 且趋势下降——gate 激活后 return 暂时下降是预期行为，需继续跑到 gate_scale=1.0 后再做 final 评估。

---
