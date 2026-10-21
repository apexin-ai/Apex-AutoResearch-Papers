# eval fullft 50k libero goal

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_fullft_50k_libero_goal_20260516T204037_result.json`
- **Structured JSON:** [`4a13ae88d62663e07b6f.json`](../../sessions/4a/4a13ae88d62663e07b6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== Full FT 50K libero_goal EVAL ===
Overall SR: 42/100 (42%)
95% Wilson CI: [32.8%, 51.8%]

Per-task:
  Task 0: 20% (2/10) -- open the middle drawer of the cabinet
  Task 1: 70% (7/10) -- put the bowl on the stove
  Task 2: 50% (5/10) -- put the wine bottle on top of the cabinet
  Task 3: 10% (1/10) -- open the top drawer and put the bowl inside
  Task 4: 60% (6/10) -- put the bowl on top of the cabinet
  Task 5: 50% (5/10) -- push the plate to the front of the stove
  Task 6: 20% (2/10) -- put the cream cheese in the bowl
  Task 7: 80% (8/10) -- turn on the stove
  Task 8: 50% (5/10) -- put the bowl on the plate
  Task 9: 10% (1/10) -- put the wine bottle on the rack

Per-task array: [2, 7, 5, 1, 6, 5, 2, 8, 5, 1]

Comparison:
  libero_object  = 33%
  libero_spatial = 34%
  libero_goal    = 42%  ← highest of the three
```

**Observations:**
- `libero_goal` 表现最好 (42% vs object 33% / spatial 34%)
- Task 7 "turn on the stove" 表现最佳 (80%)，Task 3 和 Task 9 最差 (各 10%)
- 所有 FAIL episodes 均 timeout 到 max_steps=300，无 crash
- 日志末尾显示又启动了一次模型加载（可能是脚本内部第二阶段），进程可能仍在运行

---
