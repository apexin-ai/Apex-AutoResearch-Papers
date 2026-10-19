# code v6 conditioned fix train

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v6-conditioned-fix-train_20260516T062301_result.json`
- **Structured JSON:** [`6f8768e92ff87712f2aa.json`](../../sessions/6f/6f8768e92ff87712f2aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已完成。总结：

**代码修复已到位**：`acib_policy.py` 中 `_compute_lang_condition()` 在 `forward()` 中预计算 language embedding（masked mean pooling），`_connector_hook()` 通过 `_get_condition()` 分支选择 condition source。`config.py` 默认 `condition_source="language"`。

**v6 训练已在运行**：
- PID 866194，GPU 0，westb-13953
- 当前 step ~200/20000，速度 ~1 step/s（预计 ~5.5h 完成）
- scorer 输出 mean=0.512, std=0.266，非退化
- β warmup 前 1000 步 β=0，之后线性升至 0.01
- Registry 已更新为 RUNNING

**早期验证计划**（registry notes 已记录）：step 500-1000 后重跑 Probe A（同图不同 instruction），cos < 0.95 = conditioning 生效。

---
