# debug grpo health check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_grpo-health-check_20260514T073123_result.json`
- **Structured JSON:** [`8ce3690d375ecf9c483c.json`](../../sessions/8c/8ce3690d375ecf9c483c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

| 项目 | 状态 |
|------|------|
| **PID 166574** | DEAD |
| **tmux session** | 不存在 |
| **GPU 状态** | cuda:0 — 0% util, 0 MiB / 97887 MiB; cuda:1 — 0% util, 0 MiB / 97887 MiB |
| **训练进程** | 无任何 Python 训练进程 |

### Step 3.5 结果
**未通过** — 两个 eval（standard 和 rasp）都在 `eval_gsm8k.py:59` 崩溃。

### 错误原因
`eval_gsm8k.py` 第 59 行 `normalize_answer()` 函数：
```python
if val == int(val):  # line 59
```
模型生成了无法解析为有效数字的输出，被解析为 `float('inf')`，`int(inf)` 抛出 `OverflowError: cannot convert float infinity to integer`。

- **standard 模型**：第 1 个样本就崩了（1/1319）
- **rasp 模型**：第 7 个样本崩了（7/1319）

### `results/` 目录
只有 `importance_scores.pt` 和 `cka_scores.pt`（Step 1-2 的产物），**无 eval 结果文件**。

### 修复方案

在 `normalize_answer()` 中加 `inf`/`nan` 防护：
```python
def normalize_answer(text):
    ...
    if not math.isfinite(val):
        return text  # 或 return None 标记为错误
    if val == int(val):
        return str(int(val))
    ...
```

修复后重新从 Step 3.5 resume 即可，无需重跑 Step 1-3（pruned 模型已存在）。

---
