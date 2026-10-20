# analysis code unknown diagnosis

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_code_unknown_diagnosis_20260514T125432_result.json`
- **Structured JSON:** [`ba08b4bc8765934e0d13.json`](../../sessions/ba/ba08b4bc8765934e0d13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐了。以下是完整诊断报告。

---

## Code Unknown 诊断报告

### 1. 统计分布

| Code Verdict | 数量 | 占比 |
|---|---|---|
| **Unknown** | **19** | **46.3%** |
| True | 12 | 29.3% |
| False | 8 | 19.5% |
| Error | 2 | 4.9% |
| **Total** | **41** | |

Unknown 按 agreement_type 细分：

| agreement_type | Unknown 数量 |
|---|---|
| agree_correct | 11 |
| **disagree** | **6** |
| agree_wrong | 2 |
| single_error | 1 |

6 个 disagree 样本（核心诊断场景）全部被 Unknown 污染。

### 2. 根因判定：**#2 — LLM 生成的代码主动 print("Unknown")**

全部 19 个 Unknown 样本的 `code_exec` 均为：
- `error: null`（无运行时错误）
- `timed_out: false`（无超时）
- `output: "Unknown\n"`（代码正常执行，输出了 Unknown）

**不是**代码执行出错、代码解析失败、或 LLM 拒绝生成代码。是代码本身 print 了 "Unknown"。

### 3. Unknown 代码的两种模式

**模式 A — 硬编码 Unknown（推理后放弃）**：LLM 在注释里用自然语言推理，得出"无法确定"的结论，然后直接 `print("Unknown")`，不做任何实际计算。

```python
# folio_validation_0 尾部：
# Therefore, the conclusion does not necessarily follow from the premises
print("Unknown")

# folio_validation_4 尾部：
# we cannot determine definitively whether James has lunch in the company.
print("Unknown")
```

**模式 B — 条件分支 fallback**：代码有 if/else 逻辑，但 else 分支用 `print("Unknown")` 代替了 `print("False")`。

```python
# folio_validation_2：
if antecedent:
    if consequent: print("True")
    else: print("False")
else:
    print("Unknown")   # ← 这里应该是 False

# folio_validation_3：
if conclusion: print("True")
else: print("Unknown")  # ← 用 Unknown 代替 False
```

### 4. 对比成功样本

**folio_validation_5**（Code=True，正确）：
- 同样用 set-based Python 方法
- 代码为具体实体 "James" 做了完整赋值和 case-based reasoning
- 最终到达 `print("True")`，**没有 Unknown 分支**

关键差异：成功样本中 LLM **决定给出判断**，Unknown 样本中 LLM **选择不判断**。

### 5. 诊断结论

**这是 prompt 问题，可修复。** 理由：

1. 成功样本证明模型有能力生成正确的逻辑推理代码
2. Unknown 样本中 LLM 不是"算错了"，而是"不敢算"——它把自己的推理不确定性编码进了代码输出
3. 模式 B 尤其明显：代码逻辑本应输出 False，但 LLM 用 Unknown 做了"安全"替代

**次要因素**：set-based 方法本身对 open-world 推理有固有缺陷（空集 for 循环 = 空操作），LLM 意识到这一点时倾向于放弃而非冒险给错误答案。

---
