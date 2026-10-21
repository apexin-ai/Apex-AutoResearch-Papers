# fix pi05 normalization

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_pi05-normalization_20260521T032653_result.json`
- **Structured JSON:** [`32e70580fb1df475ab14.json`](../../sessions/32/32e70580fb1df475ab14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job 已启动（PID 811001），正在加载模型。

总结：
- **Killed** 旧进程 802634
- **确认** stats 文件包含 `observation.state.mean/std`（shape [8]）和 `action.mean/std`（shape [7]），norm_map = MEAN_STD
- **修复** `pi05_wrapper.py`：`_load_normalizer_stats` 加载 mean/std 而非 q01/q99；`_normalize_state` 改用 `(x-mean)/(std+eps)`；`_unnormalize_action` 改用 `x*std+mean`；离散化范围 [-1,1] 不变（与 lerobot PI05 processor 一致）
- **验证** import + 方法签名检查通过
- **Registry**: `eval-pi05-baseline-object-seed42` 标记 failed；`eval-pi05-baseline-object-seed42-r2` 已创建并提交
- **New eval** 运行中：`eval-pi05-baseline-object-seed42-r2`，PID 811001，cuda:0

---
