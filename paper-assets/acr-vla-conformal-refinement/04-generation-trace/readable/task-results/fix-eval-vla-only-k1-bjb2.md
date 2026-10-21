# fix eval vla only k1 bjb2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_eval-vla-only-k1-bjb2_20260514T000046_result.json`
- **Structured JSON:** [`1346dfe74454f3055d6f.json`](../../sessions/13/1346dfe74454f3055d6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

一切正常。

**修复内容**: 在 `src/evaluate.py` 第354-356行，`main()` 函数中 `parse_args()` 之后添加：
```python
if args.mode == "vla_only":
    args.K = 1
```
只影响 vla_only 模式，其他模式（acr_vla/reconvla/crm_*）的 K 值不变。

**新进程**:
- 父 bash PID: **125823**
- Python 进程 PID: **125830**
- 日志路径: `/root/autodl-tmp/eval_results/eval-object-v6.log`
- 日志已确认 `K: 1` 生效，模型加载完成，正在初始化 LIBERO object 环境

---
