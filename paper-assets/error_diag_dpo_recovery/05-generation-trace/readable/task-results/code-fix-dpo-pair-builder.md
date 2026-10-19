# code fix dpo pair builder

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-dpo-pair-builder_20260512T163659_result.json`
- **Structured JSON:** [`8157d793418396f8c631.json`](../../sessions/81/8157d793418396f8c631.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个修复都验证通过。

## 结果汇总

### build_dpo_pairs.py 修改
- **核心变更**：`build_pair()` 不再用 LLM 报告的 `failure_step` 做切分点，改为 `find_divergence_point()` 逐步比较 expert 和 failure 的 action 序列，找到真实分歧点
- `extract_action_text()` 提取 `Action:` 行并归一化（去空格、转小写）做比较
- 共享前缀取自 expert 轨迹（同 game_file + 同 action = 同 observation，状态一致性有保证）
- 输出新增 `divergence_step` 字段

### classify_errors.py 修改
- `ICL_PREFIX_LEN=22` 硬编码替换为 `_find_task_start_index()` 动态检测（找最后一个 `"Your task is to:"` 消息）
- 实际数据中 task 在 index 12，旧硬编码 22 会跳过 10 条真实 action 消息

### dry-run 统计
- 79 pairs 构建成功（88 条 classified 中，6 条无 expert 匹配，3 条构建失败）
- **divergence 分布**：min=1, max=5, mean=1.3，69/79 在第 1 步就分歧
- **failure_step vs divergence_step**：76/79 的 divergence 早于 LLM 报告的 failure_step（平均早 5.3 步），证实了旧逻辑的状态不一致问题

---
