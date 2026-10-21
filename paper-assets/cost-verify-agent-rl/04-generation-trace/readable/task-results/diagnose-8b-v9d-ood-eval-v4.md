# diagnose 8b v9d ood eval v4

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_8b_v9d_ood_eval_v4_20260520T101923_result.json`
- **Structured JSON:** [`d85c54d1e1a4e7aed816.json`](../../sessions/d8/d85c54d1e1a4e7aed816.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。4次失败的完整分析：

| 版本 | 错误 | 原因 |
|------|------|------|
| **v1** | `AssertionError: sum([1]) != 2` on `train_es_manager` | train 的 `n_groups: [1]` 与 `env_groups: 2` 不匹配 |
| **v2** | `python3: command not found` (56 bytes log) | 启动脚本未激活 conda 环境 |
| **v3** | `python3: command not found` (55 bytes log) | 同 v2 |
| **v4** | `AssertionError: sum([134]) != 234` on `val_es_manager` | val 的 `n_groups: [134]` 与 `env_groups: 234` 不匹配 |

**v4 的具体问题**：config `_alfworld_8b_v9d_ood_eval.yaml` 中：
```yaml
es_manager:
  val:
    env_groups: 234   # ← 错！应该是 134
    group_size: 1
    env_configs:
      tags: ["AlfworldSG_OOD"]
      n_groups: [134]  # ← 134 个 OOD 任务，正确
```

`es_manager.py:65` 断言 `sum(n_groups) == env_groups`，即 `134 != 234` 失败。234 = 134 + 100，可能是把 OOD 任务数和原 val set 大小加在了一起。

v1→v4 的修复只修了 train 侧（`n_groups: [1]→[2]`），val 侧的 `env_groups: 234` 始终错误但 v1 在 train 侧就崩了没暴露。

```json
{"root_cause":"AssertionError: Sum of n_groups must equal env_groups. Got sum([134]) != 234 (es_manager.py:65)","error_type":"hyperparameter","fix_steps":["将 _alfworld_8b_v9d_ood_eval.yaml 中 es_manager.val.env_groups 从 234 改为 134"],"can_auto_fix":true,"all_four_same_cause":false,"pattern":"4次全是 config 错误：v1 train n_groups/env_groups 不匹配，v2-v3 启动脚本未激活 conda，v4 val n_groups/env_groups 不匹配（234应为134）。核心断言 sum(n_groups)==env_groups 在 es_manager.py:65，每次只修了上一个错误暴露下一个。"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "AssertionError: Sum of n_groups must equal env_groups. Got sum([134]) != 234 (es_manager.py:65)",
    "error_type": "hyperparameter",
    "fix_steps": [
      "将 _alfworld_8b_v9d_ood_eval.yaml 中 es_manager.val.env_groups 从 234 改为 134"
    ],
    "can_auto_fix": true,
    "all_four_same_cause": false,
    "pattern": "4次全是 config 错误：v1 train n_groups/env_groups 不匹配，v2-v3 启动脚本未激活 conda，v4 val n_groups/env_groups 不匹配（234应为134）。核心断言 sum(n_groups)==env_groups 在 es_manager.py:65，每次只修了上一个错误暴露下一个。"
  }
}
```

</details>

---
