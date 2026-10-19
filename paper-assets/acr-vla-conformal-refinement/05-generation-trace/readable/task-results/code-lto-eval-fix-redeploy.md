# code lto eval fix redeploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lto-eval-fix-redeploy_20260519T045247_result.json`
- **Structured JSON:** [`2e57d28e38e32c0c951f.json`](../../sessions/2e/2e57d28e38e32c0c951f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

### 验证清单
1. ✅ evaluate.py 中 `.replace("_", " ")` 已删除
2. ✅ dry-run 确认 5/5 held-out tasks 匹配 (salad_dressing, ketchup, tomato_sauce, milk, orange_juice)
3. ✅ CRM eval 已启动，日志确认 `[eval] LTO: evaluating 5 tasks`
4. ✅ VLA-only baseline 已启动，日志确认 `[eval] LTO: evaluating 5 tasks`
5. ✅ 6 个 killed experiments 已更新 registry (conclusion=killed, status=DONE)

### 产出

**Bug fix diff:**
```diff
- if any(substr.replace("_", " ") in te["task_name"] for substr in requested):
+ if any(substr in te["task_name"] for substr in requested):
```

**新部署 eval:**
| exp_id | mode | GPU | server |
|---|---|---|---|
| `eval-lto-splitA-heldout-r2` | crm_obs_only (K=5, ε=0.2) | cuda:1 | bjb1-18228 |
| `eval-lto-splitA-vla-only-r2` | vla_only | cuda:2 | bjb1-18228 |

**6 个 killed experiments:**
1. `eval-obs-only-object-norm003-seed49` (magnitude sweep)
2. `eval-perdof-object-norm03-seed48` (magnitude sweep)
3. `eval-obs-only-object-norm005-seed46` (magnitude sweep)
4. `eval-obs-only-object-norm003-seed46` (magnitude sweep)
5. `eval-lto-splitA-heldout` (buggy LTO eval)
6. `eval-lto-splitA-vla-only` (buggy LTO eval)

---
