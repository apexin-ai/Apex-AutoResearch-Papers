# code fix answer normalization

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-answer-normalization_20260518T113208_result.json`
- **Structured JSON:** [`a30f76204a0479d5f359.json`](../../sessions/a3/a30f76204a0479d5f359.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

## 修改总结

### 新增函数
- **`sica/pipeline.py:117-132`** — `normalize_logic_answer(ans)`: 先用 regex `^\\+text\{...\}$` 剥离 LaTeX `\text{...}` 包装，再通过 `_LOGIC_CANONICAL` 字典做大小写归一化映射

### 修改点

| 文件 | 行 | 修改内容 |
|------|-----|---------|
| `sica/pipeline.py:10` | 新增 `import re` |
| `sica/pipeline.py:67-71` | `run_single()` scoring 前，对 logic 数据集 trace answers 调用 `normalize_logic_answer()` |
| `sica/pipeline.py:135-141` | `_group_logic_answers()` 改用 `normalize_logic_answer()` 替代原始 `.strip().lower()` lookup |
| `run_case_study.py:16` | import 增加 `normalize_logic_answer` |
| `run_case_study.py:104-108` | scoring 前对所有 trace answers 归一化 |
| `scripts/cross_model_extract.py:17` | 新增 `from sica.pipeline import normalize_logic_answer` |
| `scripts/cross_model_extract.py:105-109` | scoring 前对 logic 数据集 trace answers 归一化 |

### 归一化在 pipeline 中的调用点

1. **SC voting** — `_group_logic_answers()` 内部调用 `normalize_logic_answer()` (被 `self_consistency.py` 和 `run_case_study.py` 使用)
2. **SICA scoring** — `SICAPipeline.run_single()` 在构建 candidates/answer_counts 前归一化 trace answers，确保 scorer 读取的也是归一化后的值
3. **Cross-model extraction** — `cross_model_extract.py` 在独立 scoring 流程前归一化

### 覆盖的变体 (23 test cases 全部通过)
- 大小写: `true/TRUE/True`, `false/FALSE/False`, `unknown/UNKNOWN/Unknown`
- 同义词: `yes→True`, `no→False`, `uncertain→Unknown`, `undetermined→Unknown`
- LaTeX: `\text{True}`, `\text{false}`, `\\text{Unknown}`, `\text{uncertain}` 等

---
