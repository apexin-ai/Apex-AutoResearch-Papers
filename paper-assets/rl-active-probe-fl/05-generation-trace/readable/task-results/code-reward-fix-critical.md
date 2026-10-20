# code reward fix critical

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_reward-fix-critical_20260514T045658_result.json`
- **Structured JSON:** [`57c680c14bf5a82a0084.json`](../../sessions/57/57c680c14bf5a82a0084.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 项验证全部通过。

---

## 修改文件清单

| 文件 | 变更 |
|---|---|
| `src/reward_funcs.py` | 完全重写 — fix-based reward 架构 |
| `src/prompts.py` | 新增 `FIX_GENERATION_PROMPT` |
| `src/validate_tests.py` | 新增 `strip_solution_class`，`build_test_file` 简化，`run_pytest` 改用 `build_test_file` |
| `src/train_grpo.py` | 导入新 reward 函数，`set_policy_model` 注册，dataset 加 `test_code` |
| `src/generate_tests.py` | SYSTEM_PROMPT 加 "不要包含 Solution 类"，USER_PROMPT_TEMPLATE 同步更新 |

## fix_based_reward 完整伪代码

```
对每个 (prompt, completion) pair:
  1. extract_probe(completion) → probe  (正则匹配 ```probe``` fence)
     若 probe 为 None → reward = 0.0, continue
  2. clean_test = strip_solution_class(test_code)
  3. execute_probe(buggy_code, probe) → probe_result
     probe_output = stdout if success else ""
  4. _get_failing_output(buggy_code, clean_test) → failing_output  (LRU cached)
  5. _generate_fix(buggy_code, failing_output, probe_output) → fix_code
     (policy model, torch.no_grad, greedy decode, 提取 ```python``` fence)
     若 fix_code 为 None → reward = 0.0, continue
  6. run_tests(fix_code, clean_test) → test_result
     reward = 1.0 if test_result.passed else 0.0
```

**probe_execution_bonus**: probe 无错执行 → +0.1

**probe_dependence_reward** (随机 20%):
```
  real_fix = generate_fix(buggy_code, failing_output, probe_output)
  null_fix = generate_fix(buggy_code, failing_output, "")
  if real_fix != null_fix → +0.1
```

## strip_solution_class 正则逻辑

不用正则，用逐行解析器：
1. 遍历 test_code 每一行
2. 遇到 `class Solution:` 或 `class Solution(` 开头 → 进入 `in_solution=True`，跳过该行
3. `in_solution=True` 时：空行或缩进行（首字符为空格/tab）→ 跳过（属于类体）
4. 遇到非空且无缩进的行 → `in_solution=False`，保留该行（类体结束）
5. 输出所有保留行

---
