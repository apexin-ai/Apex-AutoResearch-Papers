# code test gen pilot

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_test-gen-pilot_20260514T052144_result.json`
- **Structured JSON:** [`0f1050343e6a3b3fdc04.json`](../../sessions/0f/0f1050343e6a3b3fdc04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个失败都是 LLM 生成的测试用例中的**期望值错误**（不是代码结构问题），这是正常的 LLM 测试生成噪声。

## 结果汇报

### 1. API 连通性
- `claude-sonnet-4-20250514` — **不可用**（503 model_not_found）
- `claude-haiku-4-5` — **可用**，5/5 请求全部成功，响应约 2-3 秒/条
- 可用的 Anthropic 模型（openai 端点）：`claude-haiku-4-5`、`anthropic/claude-opus-4.7`、`anthropic/claude-opus-4.7-fast`

### 2. 生成质量
- 5 条全部生成成功（0 失败）
- 结构正确：每条 test_code 包含 3-7 个 `test_*` 函数，使用 `assert` 断言
- **已发现并修复的问题**：
  - LLM 输出包含 markdown fence（```python / ```）→ 已在 `clean_test_code()` 中添加清理
  - LLM 输出包含 `from solution import Solution`（无效导入）→ 已添加清理
  - 部分样本包含 Solution 类定义 → 已有的 `strip_solution_class` 逻辑处理

### 3. 验证结果

| 指标 | 数量 | 比例 |
|------|------|------|
| Solution pass | 3/5 | 60% |
| Buggy fail | 3/3 | 100%（在 solution pass 的基础上） |
| Both correct | 3/5 | 60% |

- 2 条 solution 失败原因：LLM 生成的**期望值算错了**（不是代码格式问题）
  - `moving-stones-until-consecutive-ii`：期望 `[1,2]`，实际 `[2,8]`
  - `largest-number-after-mutating-substring`：期望 `"54921"`，实际 `"54932"`

### 4. 建议

- solution pass rate 60% 低于目标 80%。原因是 haiku 模型能力较弱，容易算错测试期望值。正式生成建议换用 `anthropic/claude-opus-4.7-fast`（API 上支持 openai 端点）
- `validate_tests.py` 的 `clean_test_code()` 已修复，可以处理 markdown fence 和无效 import
- 可用模型名记录为 `claude-haiku-4-5`

---
