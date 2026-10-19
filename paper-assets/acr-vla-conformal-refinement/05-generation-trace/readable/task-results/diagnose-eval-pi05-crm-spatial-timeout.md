# diagnose eval pi05 crm spatial timeout

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-pi05-crm-spatial-timeout_20260522T132405_result.json`
- **Structured JSON:** [`8300ff5db20df30e1e30.json`](../../sessions/83/8300ff5db20df30e1e30.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据清晰了。所有 3 个文件 Birth→Modify 恰好 12 小时（09:17 → 21:17），timeout=43200s。

**汇总：**
- seed42: 7/10 tasks 完成（140 rollouts），SR: 90/95/100/100/95/50/100
- seed43: 7/10 tasks 完成（140 rollouts），SR: 85/95/95/90/90/45/100
- seed44: 6/10 tasks + task7 进行到 rollout 10/20（~130 rollouts），SR: 85/90/95/90/95/30/partial

每 rollout 耗时：12h / ~140 rollouts ≈ **5.1 min/rollout**。总需 200 rollouts × 5.1min ≈ **17-18 小时**，12h timeout 差 ~6h。

```json
{"root_cause":"timeout 43200s (12h) 不够——旧版 n_action_steps=50 导致单 rollout ~5.1min，10 tasks×20 rollouts=200 rollouts 需 ~17-18h，12h 只够跑 ~140 rollouts (7/10 tasks)","error_type":"timeout_config","progress":"seed42: 7/10 tasks (140/200 rollouts); seed43: 7/10 tasks (140/200); seed44: 6.5/10 tasks (~130/200)","per_rollout_time":"~5.1 min/rollout (含 PI0.5 inference + CRM + 300 max_steps × 50 action_steps)","partial_results":"seed42: [90,95,100,100,95,50,100,?,?,?]; seed43: [85,95,95,90,90,45,100,?,?,?]; seed44: [85,90,95,90,95,30,partial,?,?,?]","fix_steps":["将 timeout 提高到 64800s (18h) 或 72000s (20h)","或改用新版 eval (n_action_steps < 50) 减少每 rollout 耗时","或拆成两批 5 tasks 分别跑，每批 ~9h 可完成"],"can_auto_fix":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "timeout 43200s (12h) 不够——旧版 n_action_steps=50 导致单 rollout ~5.1min，10 tasks×20 rollouts=200 rollouts 需 ~17-18h，12h 只够跑 ~140 rollouts (7/10 tasks)",
    "error_type": "timeout_config",
    "progress": "seed42: 7/10 tasks (140/200 rollouts); seed43: 7/10 tasks (140/200); seed44: 6.5/10 tasks (~130/200)",
    "per_rollout_time": "~5.1 min/rollout (含 PI0.5 inference + CRM + 300 max_steps × 50 action_steps)",
    "partial_results": "seed42: [90,95,100,100,95,50,100,?,?,?]; seed43: [85,95,95,90,90,45,100,?,?,?]; seed44: [85,90,95,90,95,30,partial,?,?,?]",
    "fix_steps": [
      "将 timeout 提高到 64800s (18h) 或 72000s (20h)",
      "或改用新版 eval (n_action_steps < 50) 减少每 rollout 耗时",
      "或拆成两批 5 tasks 分别跑，每批 ~9h 可完成"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
