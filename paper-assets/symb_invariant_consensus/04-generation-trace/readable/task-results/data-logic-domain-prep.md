# data logic domain prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_logic_domain_prep_20260515T220240_result.json`
- **Structured JSON:** [`3becf7172a8ccb7220e2.json`](../../sessions/3b/3becf7172a8ccb7220e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个数据文件已就位。以下是完整报告。

---

## 产出文件

| 文件 | 数量 | 答案分布 | 说明 |
|------|------|----------|------|
| `data/proofwriter_30.json` | 30 | T:10 F:10 U:10 | 全 D5（D3 数据 HF Hub 不可用，本地仅有 D5） |
| `data/folio_30.json` | 30 | T:10 F:10 U:10 | 含 FOL 标注（premises_fol, conclusion_fol） |

格式均兼容 `run_full_mvp.py`：`{id, problem, solution, answer, level, dataset}`。

## 代码适配需求清单

### 已有支持（无需改动）
- **Pipeline 域检测**：`sica/pipeline.py:59` 从 `dataset` 字段自动识别 folio/proofwriter/math
- **独立 Prompt 模板**：`trace_generator.py` 有 `LOGIC_PROMPT`、`FOLIO_PROMPT`，都要求 `\boxed{True/False/Unknown}`
- **答案规范化**：`normalize_logic_answer()` 映射 "yes"→True, "uncertain"→Unknown 等变体
- **逻辑答案分组**：`_group_logic_answers()` 用大小写无关精确匹配（不走 math 等价判断）
- **约束提取**：`LOGIC_EXTRACTION_PROMPT` 使用布尔断言格式（`kind_anne == True`）
- **数据 Loader**：`proofwriter_loader.py` / `folio_loader.py` 都有 pipeline 格式函数

### 需要修改（4 处）

1. **`run_full_mvp.py` — 缺 FOLIO 加载入口**
   - `load_all_problems()` (L32) 只接收 math_path + pw_path，无 folio_path
   - 需新增 `--folio-data` 参数 + FOLIO 加载逻辑

2. **`run_full_mvp.py` — 正确率判定用 `is_equiv()`**
   - L~250: `sica_correct = is_equiv(sica_answer, prob["answer"])`
   - `is_equiv()` (`utils/math_equiv.py`) 是纯数学比较器（LaTeX normalize → sympy → numeric）
   - 逻辑域碰巧能工作（"True"=="True"），但若模型输出 "true"（小写）就会判错
   - 需加逻辑域分支：对 proofwriter/folio 先调 `normalize_logic_answer()` 再比较

3. **`baselines/self_consistency.py` — 分组用 math 等价**
   - `group_equivalent_answers()` 做数学等价检查
   - 逻辑域应该用 `_group_logic_answers()`（大小写无关精确匹配）
   - 当前因答案已规范化而碰巧正确，但不健壮

4. **`--no-proofwriter` 语义需调整**
   - L229: `pw_path = None if args.no_proofwriter else args.pw_data`
   - 如果同时跑 FOLIO + ProofWriter，需要独立的 `--no-folio` 开关

---
