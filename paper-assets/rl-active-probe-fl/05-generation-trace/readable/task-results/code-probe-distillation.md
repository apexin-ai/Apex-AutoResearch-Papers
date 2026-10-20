# code probe distillation

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_probe-distillation_20260514T061239_result.json`
- **Structured JSON:** [`0bb95a15df27ac01ab03.json`](../../sessions/0b/0bb95a15df27ac01ab03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完美，294/294 全部 1:1 匹配。

## 结果

- **方案 A（API）**，全量成功，无需方案 B
- **294/294** 条 distill 成功，0 失败
- **API 用量**: 261,483 input tokens + 91,919 output tokens（295 requests，含测试 3 条）
- 产出文件: `data/probes_train.jsonl`

**样例 1** (`card-flipping-game`):
- good_probe: `print(type(fronts), type(backs)); print(fronts - backs)` — 直接触发 TypeError 暴露 list 减法 bug
- bad_probe: `print('bad set:', bad); print('fronts:', fronts)` — 检查无关变量

**样例 2** (`count-equal-and-divisible-pairs-in-an-array`):
- good_probe: 用 `ast.parse` 尝试解析源码，暴露多余括号导致的 SyntaxError
- bad_probe: 打印 dict 内容，完全无法发现语法错误

---
