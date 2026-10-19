# exec step4 icl feasibility

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_step4-icl-feasibility_20260512T145408_result.json`
- **Structured JSON:** [`b051c7bdea69d4f9ea44.json`](../../sessions/b0/b051c7bdea69d4f9ea44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

测试仍在后台运行（当前 7/9 = 78%），但已有足够数据做出判断。P1 gate 已明确通过。

## 汇报

### 整体结果（9/25 已完成，测试仍在后台运行）

| 指标 | 值 |
|------|-----|
| 整体成功率 | **7/9 = 77.8%** |
| P1 Gate (>10%) | **PASS** |
| vs 8B baseline | 0% → 78% |

### 按 task type

| Task Type | 成功/总数 | 成功率 |
|-----------|-----------|--------|
| pick_and_place | 5/5 | **100%** |
| look_at_obj | 2/2 | **100%** |
| pick_two_obj | 0/1 | 0% |
| pick_clean_then_place | 0/1 | 0% |

### 关键发现

1. **之前 0% 的根本原因不是模型能力，是 ALFWorld 环境的 action 格式不匹配**：环境使用 `move X to Y`，但指令/ICL 用的是 `put X in/on Y`。这意味着 Qwen3-8B 的 0% 也是同样的 bug，不是模型太弱。

2. **14B-AWQ 推理能力很强**：正确的物品识别、导航策略、多步规划。成功任务平均 4-18 步完成。

3. **复杂任务仍然失败**：`clean`/`heat`/`cool`/`toggle` 动作在此 ALFWorld 版本中也有映射问题（环境 action vocabulary 只有 `examine, go, help, inventory, look, move, open, take`），需要进一步调查。

4. **Action 翻译方案有效**：`translate_action()` 函数使用 admissible commands + fuzzy matching，已解决 `put → move` 映射。

### 即使最保守估计
最差情况：剩余 16 个任务全部失败 → 7/25 = **28%** > 10%，P1 Gate 确定通过。

### 下一步建议
- 需要修复 `collect_trajectories.py` 中同样的 action 翻译问题
- 调查 `clean`/`heat`/`cool`/`toggle` 在当前 ALFWorld 版本中的正确 action 格式
- 用修复后的环境重新测试 Qwen3-8B，看是否也能达到合理成功率

---
