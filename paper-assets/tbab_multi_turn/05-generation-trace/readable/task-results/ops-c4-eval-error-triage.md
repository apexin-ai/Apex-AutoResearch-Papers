# ops c4 eval error triage

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c4-eval-error-triage_20260518T162745_result.json`
- **Structured JSON:** [`554e8f7fa25772ac4c64.json`](../../sessions/55/554e8f7fa25772ac4c64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查完成。

---

## 排查结论

### 1. Sample 26 完整 traceback

Sample `[26/91]` = **sharded-HumanEval/63**（`fibfib` 问题）

```
[26/91] repeat=1 task=code id=sharded-HumanEval/63
Fatal Python error: Segmentation fault

  File "&lt;string>", line 44 in fibfib
  File "&lt;string>", line 44 in fibfib
  ... (重复 ~100 行)

Extension modules: numpy._core._multiarray_umath, ... (total: 131)
  ERROR in simulation: list index out of range
  -> wrong (score=0.0, turns=3)
```

### 2. Error 来源：simulation 框架（非 TBAB 推理代码）

**调用链**：
1. 模型生成了带无限递归的 `fibfib` 代码
2. `simulator_sharded.py:89` → `task.evaluator_function()` → `check_correctness()`
3. `eval_code.py:581-588`：sandbox 子进程执行生成代码 → 无限递归 → 栈溢出 → **segfault 杀死子进程**
4. `eval_code.py:591-594`：处理了 `result` 为空的情况，但 **`metadata_list` 为空未处理**
5. `eval_code.py:597`：`return result[0], metadata_list[0]` → **`IndexError: list index out of range`**
6. 异常传回 `run_eval.py:79-80`，被 catch 输出 `ERROR in simulation: list index out of range`

**根因**：`eval_code.py:check_correctness()` 第 597 行有 bug。子进程 segfault 后 `metadata_list` 为空，但只给 `result` 做了 fallback，没给 `metadata_list`。这是 **lost_in_conversation 框架自带的 bug**（代码来自 LiveCodeBench），与 TBAB bridge token / position_ids 逻辑完全无关。

### 3. Error 统计

- **C4_s42**：全日志仅 **1 个 ERROR**（line 173），即 sample 26（HumanEval/63）
- 无其他 error pattern，其余 sample 正常运行

### 4. C1_s42 同 sample 对比

- C1_s42 的 `[26/91]` 同样是 `sharded-HumanEval/63`
- **无 error**，正常返回 `-> wrong (score=0, turns=7)`
- C1_s42 全日志 **0 个 ERROR**

原因：C1 模型在同一 task 上生成了不同代码（没有触发无限递归），所以 sandbox 正常执行没有 segfault。

### 5. 结论

| 维度 | 判断 |
|------|------|
| 孤例 vs 系统性 | **孤例**，91 个 sample 中仅 1 个触发 |
| TBAB 引入 vs benchmark 本身 | **benchmark 本身**（`eval_code.py` 的 `metadata_list` 缺 fallback） |
| 对结果的影响 | 无影响——error 被 catch 后该 sample 已记录为 `score=0.0`，eval 继续正常运行 |
| 是否需要修复 | 非紧急。若想消除，在 `eval_code.py:597` 前加 `if not metadata_list: metadata_list.append({})` |

### 当前进度

- **C4_s42**: 33/91，正常推进中
- **C1_s137**: 25/91，正常推进中

---
