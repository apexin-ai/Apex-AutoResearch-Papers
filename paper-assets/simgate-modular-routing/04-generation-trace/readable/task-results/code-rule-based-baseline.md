# code rule based baseline

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rule-based-baseline_20260513T183202_result.json`
- **Structured JSON:** [`27a0fd804064dae6857f.json`](../../sessions/27/27a0fd804064dae6857f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已写入 `/root/autodl-tmp/simgate-modular-routing/src/rule_based_routing.py` 并通过 `--help` 验证。

核心逻辑：
- `route_by_keywords()` 检查 observation + valid_actions 中是否匹配预注册关键词，返回路由决策和匹配到的关键词
- deterministic 路由复用 phase1 的 fork-based 评估（含 death filter）
- internal 路由调用 `agent.select_action_react()`
- 每步记录 `route_decision` 和 `keyword_matched`
- 脚本启动时打印 keyword file MD5 hash
- 输出 JSONL + summary JSON，格式与设计规范一致

---
