# code fix unify metrics bugs

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-unify-metrics-bugs_20260518T172223_result.json`
- **Structured JSON:** [`7a87d964b4052a849853.json`](../../sessions/7a/7a87d964b4052a849853.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Ground truth 交叉校验结果：

| 条件 | 脚本输出 | Ground Truth | 状态 |
|------|----------|-------------|------|
| Reflexion N=3 FINAL DR | **34.00%** (68/200) | 34.0% | **PASS** |
| Reflexion N=4 FINAL DR | **36.50%** (73/200) | 36.5% | **PASS** |

N=5 数据有 179 个 episodes（非 200），FINAL DR=36.31%（65/179）。

---

## 修复汇报

### Bug 1: JSON 字段名不匹配
- `data.get("task", "")` → `data.get("task_name", "")`
- `data.get("episode", -1)` → `data.get("variation_idx", -1)`
- `t["trial"]` → `t["trial_idx"]` (排序 key)
- `trial_k.get("score", 0) == -100` → `trial_k.get("is_death", ...)` (死亡判定)
- JSONL 格式同步修复

### Bug 2: DEATH_PRONE_TASKS 虚构列表
- 从 `["freeze", "burn", "drown", "poison", ...]` 替换为真实 10 个任务

### Bug 3: `--test` 模式污染
- `--test` 模式输出改写到 `_test` 后缀文件，不再覆盖主输出

### 额外修复
- **允许单独运行 retry 或 reflexion**：原脚本要求两者都传入，改为至少传一个
- **自动发现 N 条件子目录**：传入父目录时自动发现 `reflexion_n3/`, `reflexion_n4/` 等子目录，分别处理
- **新增 final death rate 计算**：原始 DR(k) 只计入到达第 k 次试验的 episode 作为分母，新增以全部 episodes 为分母的 final DR，与 ground truth 定义一致
- **N=5 数据不完整**：只有 179/200 episodes，可能还在跑

---
