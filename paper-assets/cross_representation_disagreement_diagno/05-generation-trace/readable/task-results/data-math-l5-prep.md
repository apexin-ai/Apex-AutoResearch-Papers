# data math l5 prep

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_math_l5_prep_20260515T060623_result.json`
- **Structured JSON:** [`6fd7915c749a54a1608e.json`](../../sessions/6f/6fd7915c749a54a1608e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有输出均已确认。以下是完整总结。

---

## 完成情况

### 1. 数据集下载 ✓
- 路径：`/root/autodl-tmp/crdd/data/math_l5/math_level5.jsonl`
- **1324 道 Level 5 题目**（MATH test set 共 5000 题，Level 5 占 26.5%）
- 7 个 subject 全部覆盖

| Subject | Count |
|---------|-------|
| algebra | 307 |
| intermediate_algebra | 280 |
| prealgebra | 193 |
| number_theory | 154 |
| precalculus | 135 |
| geometry | 132 |
| counting_and_probability | 123 |

### 2. 数据格式
- 字段：`problem`（LaTeX 题目）、`solution`（LaTeX 逐步解答，含 `\boxed{answer}`）、`level`、`subject`
- 答案提取率：**100%**（所有 solution 都有 `\boxed{}`）
- 答案类型多样：整数、分数（`\frac{1}{8}`）、复数（`i`）、区间（`[0,\infty)`）、矩阵等

### 3. 适配代码 ✓
- 文件：`/root/autodl-tmp/crdd/src/math_adapter.py`
- 包含：数据加载、答案提取/标准化/比较、prompt 模板、verdict 映射

### 4. 双表征推荐方案

**推荐：CoT（自然语言推理链）+ SymPy Code（符号计算代码）**

| 维度 | 表征 A: CoT | 表征 B: SymPy Code |
|------|------------|-------------------|
| 对应 FOLIO | FOL（形式推理） | Python Code（可执行验证） |
| 本质 | 推理逻辑 | 符号计算 |
| 输出 | `\boxed{answer}` | `print(answer)` |
| 失败模式 | 算术错误、逻辑跳步、幻觉 | 建模错误、crash、超时 |
| crash 率 | 0%（纯文本） | ~10-30%（可执行代码） |
| LLM 生成难度 | 低 | 中 |

**为什么这个组合最优：**

1. **互补性强**：CoT 擅长逻辑推理但易犯算术错误；SymPy 精确计算但可能建模错误。两者失败模式正交，分歧信号有诊断价值
2. **与 FOLIO 方法论一致**：FOL→CoT（形式化推理路径），Python Code→SymPy Code（可执行验证），pipeline 结构可复用
3. **crash 作为诊断信号**：SymPy crash（类似 Z3 crash）提供额外错误定位信息，与 FOLIO 的 `SINGLE_ERROR` 类型直接对应
4. **文献支持**：SymCode (EACL 2026) 证明 SymPy 在 MATH 上有效；CSV (ICLR 2024) 证明 code self-verification 与 CoT 互补

**排除的方案及理由：**
- **Lean4 形式化证明**：LLM 生成质量差，crash 率 >50%，大规模实验不可行
- **纯数值 Python (PAL)**：与 CoT 都是"计算"，失败模式重叠，分歧信号弱
- **Wolfram Alpha**：需要外部 API，不可本地执行，不可控

### 5. Prompt 模板草案

**CoT prompt** 要求：逐步推理 → `\boxed{answer}`，不输出代码

**SymPy prompt** 要求：`import sympy as sp`，符号定义，方程建模，求解，验证（回代检查），`print(answer)`。关键约束：禁止 `float()`，用 `sp.Rational` 保持精确分数

Sources:
- [PAL: Program-aided Language Models (ICML 2023)](https://arxiv.org/abs/2211.10435)
- [SymCode: Neurosymbolic Math Reasoning via SymPy (EACL 2026)](https://arxiv.org/abs/2510.25975)
- [Code-based Self-Verification for Math (ICLR 2024)](https://arxiv.org/abs/2308.07921)
- [Design of Chain-of-Thought in Math Problem Solving](https://arxiv.org/abs/2309.11054)

---
