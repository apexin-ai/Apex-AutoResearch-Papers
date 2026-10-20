# prep math benchmark

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_math_benchmark_20260521T102232_result.json`
- **Structured JSON:** [`93247768d90a0ccd4ed3.json`](../../sessions/93/93247768d90a0ccd4ed3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the summary:

## 完成内容

### Step 1: MATH 数据集下载 + 采样
- 数据源: `DigitalLearningGmbH/MATH-lighteval` (5000 test, 7500 train)
- **`data/math_items_exp002.json`**: 200 items, 按 difficulty(1-5) × subject(7类) 分层抽样
  - Difficulty 分布: {1: 42, 2: 42, 3: 42, 4: 39, 5: 35}
  - Subject 覆盖: Algebra(29), Counting & Probability(29), Geometry(29), Intermediate Algebra(29), Number Theory(28), Prealgebra(28), Precalculus(28)

### Step 2: Few-shot 示例
- **`data/few_shot_math.json`**: 5 examples, 每个 difficulty level 一个, solution < 800 chars

### Step 3: 代码适配
- **`src/inference/benchmark_utils.py`** (新增): MATH_TEMPLATES (6 变体), `format_math_prompt`, `extract_math_answer` (\\boxed{} > "The answer is" > ####), `_normalize_math_answer` (\\frac→float 等), `score_math` (float comparison + normalized string match)
- max_tokens: 512, stop_seqs 与 GSM8K 一致

### Step 4: 设计矩阵更新
- **`src/design/generate_design.py`**: exp002 新增 "math" benchmark, expected_total 4608→5760 (1152 MATH conditions)

### Step 5: Runner 更新
- **`src/inference/run_experiment.py`**: `_build_prompt`, `_extract_and_score`, `DEFAULT_ITEMS`, `DEFAULT_FEW_SHOT`, argparse choices 均已添加 "math"

### 验证结果
- Answer extraction: 6/6 通过 (含 \\boxed{}, nested braces, decimals, ####)
- Scoring: 5/5 通过 (含 \\frac→float 转换)
- 6 个 prompt template 变体均正确生成
- Design matrix: 5760 conditions, MATH 1152 rows, items_file 正确

---
