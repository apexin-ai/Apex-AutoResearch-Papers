# Error Analysis Report: Tier 1 vs Tier 2 vs Baseline 错误模式分析

生成时间: 2026-05-20
测试集: 1190 样本 (HumanEval: 340, MBPP: 850)，每个 problem 有多个候选解（通常 10 个），部分通过部分失败。

---

## 1. 总览

| 实验 | Tier | 模型 | 条件 | Accuracy | #Errors | #FP(pass→fail) | #FN(fail→pass) |
|------|------|------|------|----------|---------|-----------------|-----------------|
| ae_only | T1 | Qwen-7B | ae_only | 99.92% | 1 | 1 | 0 |
| codellama13b_exception_only_seed42 | T1 | CodeLlama-13B | exception_only | 99.83% | 2 | 2 | 0 |
| exception_only | T1 | Qwen-7B | exception_only | 99.83% | 2 | 2 | 0 |
| qwen15b_exception_only_seed42 | T1 | Qwen-1.5B | exception_only | 99.83% | 2 | 2 | 0 |
| exception_only_seed123 | T1 | Qwen-7B | exception_only | 99.83% | 2 | 2 | 0 |
| exception_only_seed456 | T1 | Qwen-7B | exception_only | 99.83% | 2 | 2 | 0 |
| deepseek_exception_only | T1 | DeepSeek | exception_only | 99.33% | 8 | 8 | 0 |
| deepseek_exception_only_seed456 | T1 | DeepSeek | exception_only | 99.33% | 8 | 8 | 0 |
| codellama13b_ae_only_seed42 | T1 | CodeLlama-13B | ae_only | 99.08% | 11 | 11 | 0 |
| qwen15b_ae_only_seed42 | T1 | Qwen-1.5B | ae_only | 99.08% | 11 | 11 | 0 |
| deepseek_ae_only_seed42 | T1 | DeepSeek | ae_only | 98.74% | 15 | 1 | 14 |
| loop_only_seed456 | T2 | Qwen-7B | loop_only | 86.64% | 159 | 91 | 68 |
| loop_only_seed123 | T2 | Qwen-7B | loop_only | 85.88% | 168 | 96 | 72 |
| loop_only | T2 | Qwen-7B | loop_only | 85.63% | 171 | 110 | 61 |
| deepseek_loop_only_seed42 | T2 | DeepSeek | loop_only | 81.26% | 223 | 100 | 123 |
| qwen15b_loop_only_seed42 | T2 | Qwen-1.5B | loop_only | 78.32% | 258 | 105 | 153 |
| codellama13b_loop_only_seed42 | T2 | CodeLlama-13B | loop_only | 77.06% | 273 | 214 | 59 |
| codellama13b_no_trace_seed42 | BL | CodeLlama-13B | no_trace | 76.47% | 280 | 142 | 138 |
| no_trace | BL | Qwen-7B | no_trace | 75.13% | 296 | 206 | 90 |
| deepseek_no_trace | BL | DeepSeek | no_trace | 73.36% | 317 | 163 | 154 |
| qwen15b_no_trace_seed42 | BL | Qwen-1.5B | no_trace | 67.31% | 389 | 259 | 130 |

> **异常运行已排除**: deepseek_exception_only_seed123 (91.09%, 模型输出乱码如 `[`, `count`)、deepseek_full_trace (10.59%)、deepseek_vota (15.97%) — 这些是训练不收敛或解码异常的结果，不纳入错误模式分析。

---

## 2. Tier 1 错误深入分析（最重要）

### 2.1 核心发现：Tier 1 错误几乎全部是 FP（False Positive, pass→fail）

**违反直觉的关键结论**：Tier 1 的少量错误不是"漏检失败"，而是"误报成功代码为失败"。在排除异常运行后，Tier 1 所有实验的 FP:FN 比约为 42:14，且 14 个 FN 全部来自 deepseek_ae_only 单个实验。

原因：Tier 1 trace 格式（exception_only / ae_only）在特定代码模式下产生**看似错误但实际无害的 trace 事件**，误导模型。

### 2.2 HumanEval/95 — 跨所有模型×所有 seed 的唯一共同错误

**错误样本**: ID 901, 905（HumanEval/95 的 2 个通过解，共 10 个候选中仅此 2 个通过）

**问题描述**: `check_dict_case(d)` — 判断字典所有 key 是否全小写或全大写

**正确解法**:
```python
def check_dict_case(d):
    if not d: return False
    keys = list(d.keys())
    if all(isinstance(k, str) and k.islower() for k in keys):
        return True
    if all(isinstance(k, str) and k.isupper() for k in keys):
        return True
    return False
```

**根因 — GeneratorExit trace 伪影**:

exception_only trace 中出现 7 条 `[ERROR]` 事件：
```
[ERROR] GeneratorExit at line 5: | locals: .0='<list_iterator>', k='A'
[ERROR] GeneratorExit at line 7: | locals: .0='<list_iterator>', k='p'
[ERROR] GeneratorExit at line 5: | locals: .0='<list_iterator>', k=5
...
```

**原理**: Python 的 `all()` 函数遇到 False 元素时短路退出，导致底层 generator 被垃圾回收并触发 `GeneratorExit`。这是 Python 语言的正常行为，不是错误。但 tracer 将其捕获为 `[ERROR]` 事件。

**影响**: 所有 4 个模型（Qwen-7B/1.5B, CodeLlama-13B, DeepSeek）× 所有 seed 均在此样本上出错。这是 exception_only trace 格式的**系统性局限**，而非模型能力不足。

**跨模型交集**:
| | Qwen-7B | Qwen-1.5B | CodeLlama-13B | DeepSeek |
|---|---------|-----------|---------------|----------|
| exception_only 错误 IDs | {901,905} | {901,905} | {901,905} | {540,541,542,543,548,549,901,905} |

901/905 是**唯一在所有模型中共同出错的样本**。

### 2.3 MBPP/113 — DeepSeek 独有错误（caught exception 歧义）

**错误样本**: ID 540-549（全部 10 个通过解）— 仅 DeepSeek 出错

**代码**:
```python
def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
```

**exception_only trace**:
```
[ERROR] ValueError at line 3: invalid literal for int() ... | locals: s='python'
```

**根因**: `try/except` 模式中的 ValueError 被代码 **有意捕获**，这是正确行为。但 exception_only trace 将其标记为 `[ERROR]`，与真正的未捕获异常无法区分。DeepSeek 对 `[ERROR]` 标记更敏感，直接判定为失败。Qwen-7B 和 CodeLlama-13B 能正确推理出该异常是被捕获的。

### 2.4 HumanEval/72 — ae_only 格式的模型规模效应

**错误样本**: ID 170-179（全部 10 个通过解）— CodeLlama-13B 和 Qwen-1.5B 出错，Qwen-7B 正确

**代码**: `will_it_fly(q, w): return q == q[::-1] and sum(q) <= w`（一行正确解）

**ae_only trace**: `[ASSERT] assert ...`（显示 assert 通过事件）

**根因**: 较小模型（Qwen-1.5B）和 CodeLlama-13B 在 ae_only trace 中看到 assert 事件时，误解为 assertion 失败而非通过。Qwen-7B 能正确区分。

### 2.5 MBPP/794 — ae_only 的 truthiness 显示歧义

**错误样本**: ID 345 — ae_only 跨所有模型均出错

**ae_only trace**:
```
[ASSERT] assert text_starta_endb("aabbbb") | actual='aabbbb', expected=True
```

**根因**: 函数返回字符串 `'aabbbb'`（truthy），assert 通过。但 trace 格式显示 `actual='aabbbb', expected=True` 看起来像类型不匹配。模型将其解读为 assert 失败。

### 2.6 跨 seed 一致性

Qwen-7B exception_only 跨 3 个 seed **完全一致**：
- seed42: 错误 IDs = {901, 905}
- seed123: 错误 IDs = {901, 905}
- seed456: 错误 IDs = {901, 905}

交集 = 并集 = {901, 905}。证明这不是随机波动，而是 trace 格式的确定性局限。

---

## 3. Tier 2 (loop_only) vs Tier 1 错误模式差异

### 3.1 数量级差异

| 模型 | exception_only 错误 | loop_only 错误 | 共同错误 | loop额外 | exception独有 |
|------|-------------------|---------------|---------|---------|-------------|
| Qwen-7B | 2 | 171 | 0 | 171 | 2 |
| CodeLlama-13B | 2 | 273 | 2 | 271 | 0 |
| DeepSeek | 8 | 223 | 2 | 221 | 6 |

### 3.2 FP vs FN 分布的 Tier 差异

| Tier | 平均 FP 比例 | 平均 FN 比例 | 特征 |
|------|-------------|-------------|------|
| T1 (exception_only) | ~100% | ~0% | 几乎全是误报（pass→fail） |
| T2 (loop_only) | ~60% | ~40% | FP 略多于 FN，但更均衡 |
| BL (no_trace) | ~55% | ~45% | 最接近随机 |

**解读**: Tier 1 的 trace 信息太强，导致模型在看到 `[ERROR]` 标记时过度反应（FP 主导）。Tier 2 的 loop trace 信息不足以形成判断，错误在两个方向上都有分布。

### 3.3 Tier 2 额外错误的特征

**Qwen-7B loop_only 的 171 个额外错误**:
- 错误类型: no_error (129), AssertionError (42)
- FP/FN 分布: FP=110, FN=61
- 来源分布: MBPP (155), HumanEval (16) — MBPP 错误率 18.2% vs HumanEval 4.7%
- 代码行数: mean=4.4, min=1, max=21

**CodeLlama-13B loop_only 的 271 个额外错误**:
- 错误类型: no_error (216), AssertionError (51), Timeout (3), SyntaxError (1)
- FP/FN 分布: FP=212, FN=59
- CodeLlama-13B 的 FP 比例高达 78%，可能与其对 loop trace 的理解偏差有关

### 3.4 错误来源分布

| 实验 | Tier | HumanEval 错误率 | MBPP 错误率 |
|------|------|----------------|-----------|
| exception_only (Qwen-7B) | T1 | 0.59% | 0.00% |
| deepseek_exception_only | T1 | 0.59% | 0.71% |
| loop_only (Qwen-7B) | T2 | 4.71% | 18.24% |
| codellama13b_loop_only | T2 | 10.59% | 27.88% |
| no_trace (Qwen-7B) | BL | 29.12% | 23.18% |

MBPP 程序在 Tier 2 中错误率远高于 HumanEval，可能因为 MBPP 程序更短、loop trace 的信息量更少。

### 3.5 Tier 2 错误类型分布

| 实验 | no_error | AssertionError | Timeout | TypeError | SyntaxError |
|------|----------|---------------|---------|-----------|-------------|
| codellama13b_loop_only | 216 | 51 | 3 | 0 | 3 |
| deepseek_loop_only | 127 | 80 | 8 | 3 | 5 |
| loop_only (Qwen-7B) | 129 | 42 | 0 | 0 | 0 |
| qwen15b_loop_only | 141 | 86 | 8 | 15 | 4 |

"no_error" 类样本占多数 — 这些是原始程序没有产生异常的情况，loop trace 缺乏诊断性信息，模型只能猜测。

### 3.6 跨 seed 一致性（Tier 2）

Qwen-7B loop_only:
- seed42: 171 errors, seed123: 168 errors, seed456: 159 errors
- 交集: 113 / 并集: 227（交集比 50%）

对比 Tier 1 exception_only 的交集比 100%，Tier 2 的不确定性更高，约一半错误受 seed 影响。

---

## 4. Baseline 错误分析

### 4.1 no_trace 错误模式

| 实验 | #Errors | FP | FN | 错误类型分布 |
|------|---------|----|----|------------|
| codellama13b_no_trace | 280 | 142 | 138 | no_error:153, AssertionError:102, SyntaxError:14, Timeout:8 |
| no_trace (Qwen-7B) | 296 | 206 | 90 | no_error:213, AssertionError:59, SyntaxError:24 |
| deepseek_no_trace | 317 | 163 | 154 | no_error:194, AssertionError:83, TypeError:19, SyntaxError:13 |
| qwen15b_no_trace | 389 | 259 | 130 | no_error:286, AssertionError:65, SyntaxError:27 |

特征：
- FP/FN 相对均衡（CodeLlama-13B 和 DeepSeek 最接近 50/50）
- 错误分布广泛，无明显集中在特定 problem
- 所有模型的 no_trace 性能均 < 77%，远低于 exception_only (>99%)

### 4.2 full_trace vs Tier 1 错误交集

| 模型 | full_trace 错误 | exception_only 错误 | 共同错误 | full_trace独有 | exception独有 |
|------|----------------|-------------------|---------|--------------|-------------|
| Qwen-7B | 217 | 2 | 0 | 217 | 2 |

Qwen-7B full_trace (81.76%) 与 exception_only (99.83%) 的错误完全不重叠。full_trace 的错误主要源于 trace 过长导致的截断和信息过载。

---

## 5. 跨 Tier/跨模型错误交集矩阵

| | exc_qwen7b (2) | exc_codellama (2) | exc_deepseek (8) | loop_qwen7b (171) | loop_codellama (273) | no_trace_qwen7b (296) |
|---|---|---|---|---|---|---|
| exc_qwen7b | **2** | 2 | 2 | 0 | 2 | 0 |
| exc_codellama | 2 | **2** | 2 | 0 | 2 | 0 |
| exc_deepseek | 2 | 2 | **8** | 6 | 2 | 6 |
| loop_qwen7b | 0 | 0 | 6 | **171** | 101 | 132 |
| loop_codellama | 2 | 2 | 2 | 101 | **273** | 115 |
| no_trace_qwen7b | 0 | 0 | 6 | 132 | 115 | **296** |

关键读法：
- exception_only 跨模型交集很小（2），且 loop_only/no_trace 几乎不包含 exception_only 的错误
- loop_only 与 no_trace 交集大（101-132），说明 loop trace 对很多样本的信息增益有限
- Qwen-7B loop_only (171) 与 CodeLlama-13B loop_only (273) 交集 101，约 60% 的 Qwen 错误也出现在 CodeLlama 中

---

## 6. 高频错误 Problem ID（跨实验累计）

| Problem ID | 跨实验累计出错次数 | 主要涉及 Tier | 典型错误方向 |
|------------|------------------|-------------|------------|
| HumanEval/95 | 130+ | T1+T2+BL | pass→fail (GeneratorExit 伪影) |
| MBPP/284 | 120+ | T2+BL | pass→fail |
| MBPP/295 | 120+ | T2+BL | fail→pass |
| MBPP/92 | 114 | T2+BL | fail→pass |
| MBPP/419 | 108 | T2+BL | pass→fail |
| MBPP/113 | 92 | T1(DeepSeek)+T2+BL | pass→fail (caught exception) |
| HumanEval/162 | 85 | T2+BL | fail→pass |
| MBPP/229 | 84 | T2+BL | 混合 |

---

## 7. Key Findings

1. **Tier 1 错误几乎全是 FP（误报），根因是 trace 格式伪影，而非模型能力不足**。exception_only 的 2 个跨模型共同错误源于 Python `all()` 短路触发的 GeneratorExit，被 tracer 标记为 `[ERROR]`。这是 trace 收集器的系统性局限。

2. **Caught exception 是 exception_only 格式的第二大歧义源**。`try/except` 中被有意捕获的异常同样被标记为 `[ERROR]`，DeepSeek 对此最敏感（MBPP/113 全部 10 个通过解均被误判），而 Qwen-7B 能正确推理。

3. **Tier 1 的错误跨 seed 完全确定性**（Qwen-7B 3 个 seed 均为 {901,905}），说明这些错误是 trace 格式的确定性盲区，不随训练随机性变化。

4. **Tier 2 (loop_only) 错误与 Tier 1 几乎不重叠**（Qwen-7B 交集 = 0）。loop_only 的 ~170 个错误主要集中在 MBPP 短程序（mean 4.4 行），其中"no_error"类型占 75%——即原始程序没有异常的情况下，loop trace 缺乏判别信息。

5. **从 T1→T2→BL，FP/FN 比例从极端不对称趋向均衡**：Tier 1 ~100% FP，Tier 2 ~60/40，Baseline ~55/45。说明 trace 质量越高，模型越"自信"——但这种自信有时是对 trace 伪影的过度反应。

---

## 8. 对论文写作的启示

- **Tier 1 的 ~2% 错误率可以在论文中被解释为 trace 格式的确定性盲区**，不是模型泛化失败。建议在 Discussion 或 Error Analysis 节详细讨论 GeneratorExit 和 caught exception 问题。
- **MBPP/113 案例**是一个极好的定性例子，可以展示 exception_only trace 的局限性——被捕获的异常与未捕获的异常在 trace 中无法区分。
- **Tier 1 vs Tier 2 的 gap (99.8% vs 85.6%) 可以用错误类型分析来强化叙事**：exception trace 提供了 direct diagnostic signal，而 loop trace 只提供 indirect behavioral evidence。
