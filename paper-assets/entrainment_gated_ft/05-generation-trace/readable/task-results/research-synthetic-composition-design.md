# research synthetic composition design

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_synthetic-composition-design_20260518T053347_result.json`
- **Structured JSON:** [`1a0bc873ffb4ac4392f4.json`](../../sessions/1a/1a0bc873ffb4ac4392f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## 产出

### 1. Ye et al. 调研（`artifacts/synthetic_task_design.md` Section 1）
- **L-FuncComp** 是纯理论构造：函数 z_l: [N_{l-1}] -> [N_{l-1}]，domain size 指数增长，用于 communication complexity 下界证明
- 核心结论：(L+1)-layer full attention 可解，但 (L-1) full + 2^{3L^2} linear 不可解
- 论文无实验 protocol，需自行设计实际评估版本

### 2. 8-shot Prompt Format（Section 2）
- **Alphabet**: digits 0-9, |Sigma|=10, 每个 digit 单 token
- **两种 variant**:
  - **Direct**: 只给最终答案（对齐 Ye et al. 理论，测单 forward pass 能力）
  - **CoT**: 展示中间步骤 `f1(4)=9 f2(9)=4 f3(4)=1`
- **Token budget**: depth 5 direct ≈ 1650 tokens, CoT ≈ 1870 tokens, 均在 2048 内
- 每个 demo 使用不同随机函数，防止 shortcut

### 3. `artifacts/eval_composition.py`
- `generate_composition_task()` — 确定性种子生成 task instance
- `format_prompt()` — direct / cot 两种格式
- `evaluate_model()` — 加载 HF 模型 + batched greedy decoding + exact match
- `run_experiment()` — 主循环，先生成 JSON dataset 再逐模型评估，输出 summary table
- 支持 `--print-sample` 预览 prompt、`--generate-only` 仅生成数据集

### 4. Pipeline 建议
**推荐独立脚本**，不用 lm-eval-harness。核心原因：动态随机 lookup tables 不适合 lm-eval 的静态 dataset 模式，且需要精确控制 prompt format 和 batch size。

---
