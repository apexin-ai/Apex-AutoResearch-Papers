# analysis p7 diag and extraction fail

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_p7-diag-and-extraction-fail_20260515T174029_result.json`
- **Structured JSON:** [`2af8ee5731292912d496.json`](../../sessions/2a/2af8ee5731292912d496.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。现在我有所有证据，可以输出完整诊断报告。

---

## 任务 1：P7 诊断脚本完整输出

### Part 1: Parse success/failure (31 个约束)
- **24/31 OK, 7 FAIL**
- 失败的都是 Python 代码(`N = a*1000 + ...`)、自然语言(`N is a 4-digit number`)或函数调用(`replace_digit(...)`)

### Part 2: Pairwise equivalence
- 只发现 1 对等价：两个 `x > 0`

### Part 3: Full dedup simulation
- 3 traces, 10 raw → 6 unique（正确去重）

### Part 4: Bug-specific tests（核心发现）

**4c/4d/4e: Int vs Real sort 不匹配** — 这是 P7 去重不充分的根因：
- 含 `%` 运算的约束 → Z3 自动用 `Int` sort（如 `N%7 == 0`, N 是 Int）
- 不含 `%` 的约束 → Z3 用 `Real` sort（如 `N >= 1000`, N 是 Real）
- `z3.Int('N') ≠ z3.Real('N')` — 同名变量在不同 sort 下是**不同的 Z3 对象**
- `check_equivalence` 在比较 Int-mode 和 Real-mode 公式时无法正确判断等价

4e 直接演示了后果：4 个约束（2 Int + 2 Real）去重后仍是 4 个，本应合并为 2 个。

### Part 5: Realistic P7 parse rate
- **19/24 = 79%**
- 混合 sort 清晰可见：`N == a*1000 + ...` → Real, `(1000 + b*100 + ...) % 7 == 0` → Int
- 解析成功的约束中，sort 不一致会导致去重失败

---

## 任务 2：P2/P8/P9/P11 逐题诊断

### 全局证据：trace_gen_s 与 SC 投票强相关

| trace_gen_s | 问题 | SC 投票 |
|------------|------|--------|
| 351-435s | II_01, II_04, II_06 | 12/12 |
| 568s | II_03 | 11/12 |
| 566-678s | II_10, II_12, II_13 | 7-10/12 |
| 731-748s | II_05, II_07 | 1/12 |
| **740-811s** | **II_08, II_09, II_11** | **0/12** |

### P2 (II_02, GT=236) — Category C: 错误处理 bug 导致 traces 丢失

**根因链**：
1. Trace 生成成功（日志有 12 个 HTTP 200 响应）
2. Z3 MaxSAT 崩溃：`"Value cannot be converted into a Z3 Boolean value"`（某个约束无法转为布尔表达式）
3. 异常从 `pipeline.py:83` 传播到 `run_full_mvp.py:235`（当时 pipeline.py 没有 try/except）
4. run_full_mvp.py 的 error handler 设置 `sica_result = {"traces": [], ...}`
5. SC baseline 收到 0 条 trace → 0 投票

**注意**：当前版本的 pipeline.py 已有 try/except 保留 cached_traces（修复已存在于代码中），但 P2 的结果需要重跑才能更新。

### P8 (II_08, GT=127) — Category B: max_tokens 截断

- 26 raw constraints, 8/12 traces 有约束 → 模型确实在推理
- trace_gen=740s（属于高截断风险区间）
- MaxSAT: 4 sat, 2 excl → SICA 管道正常运行
- 但 `sica_scores={}` → 没有候选答案可供评分（所有 trace 的 `\boxed{}` extraction 都失败）
- **结论**：12 条 trace 全部在 10240 tokens 处被截断，模型未来得及输出 `\boxed{}`

### P9 (II_09, GT=902) — Category B: max_tokens 截断

- 35 raw constraints, 6/12 traces 有约束
- trace_gen=732s
- MaxSAT: 14 sat, 0 excl
- SC 0/12
- 与 P8 相同模式

### P11 (II_11, GT=601) — Category B: max_tokens 截断

- 60 raw constraints, 11/12 traces 有约束（约束提取非常成功！）
- trace_gen=811s（最长的）
- MaxSAT: 0 sat, 12 excl, solve_time=10003ms（超时）
- SC 0/12
- 同样是截断问题，且 MaxSAT 还触发了超时

---

## 修复建议

### 1. max_tokens 截断（P8/P9/P11 及 P5/P7 的部分 trace）

**方案 A**：提高 `--max-tokens` 到 16384 或 32768（QwQ-32B 支持 32K 上下文）
- 简单直接
- 代价：推理时间和 VRAM 增加

**方案 B**：添加 fallback answer extraction
```python
def extract_answer_fallback(text: str) -> str:
    # 1. 先尝试 \boxed{}
    ans = extract_boxed_answer(text)
    if ans: return ans
    # 2. "The answer is X" / "the answer is X"
    m = re.search(r'[Tt]he\s+(?:final\s+)?answer\s+is\s+[:\s]*(\d+)', text)
    if m: return m.group(1)
    # 3. "= X" at the end
    m = re.search(r'=\s*(\d+)\s*$', text.strip())
    if m: return m.group(1)
    return ""
```

**方案 C（推荐）**：两者都做 — 提高 max_tokens + 添加 fallback extraction

### 2. finish_reason 日志（通用改进）

在 `_generate_n_batch` 中记录 `choice.finish_reason`：
```python
for i, choice in enumerate(response.choices):
    text = choice.message.content or ""
    if choice.finish_reason == "length":
        logger.warning("Trace %d truncated (hit max_tokens)", batch_start + i)
    answer = extract_boxed_answer(text)
```

### 3. P2 的 Z3 错误

当前 pipeline.py 的 try/except 已修复 traces 丢失问题，P2 只需重跑。Z3 错误本身（某约束无法转布尔值）需要检查约束去重/MaxSAT 对非布尔表达式的处理。

---
