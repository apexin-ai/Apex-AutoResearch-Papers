# code v6 pipeline prep

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v6-pipeline-prep_20260512T230459_result.json`
- **Structured JSON:** [`38d53930211935c8231e.json`](../../sessions/38/38d53930211935c8231e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已部署到服务器，语法验证和 smoke test 均通过。

### 产出

**1. `scripts/run_v6_pipeline.sh`** — 一键执行 v6 后处理
```bash
bash scripts/run_v6_pipeline.sh [GPU_ID]   # 默认 GPU 0
```
流程：合并双卡 → CSF 后处理 → 4 版分类（LLM / LLM-nospan / LLM-fewshot / RuleBased） → 对比分析报告。输出到 `outputs/v6_pipeline_&lt;timestamp>/`。

**2. `src/compare_classifiers.py`** — 多分类器对比分析
```bash
python src/compare_classifiers.py \
    --files f1.jsonl f2.jsonl ... \
    --labels "Name1" "Name2" ... \
    --output comparison.json
```
输出：分布对比表、Cohen's κ agreement 矩阵、per-method P1 分析（KW test + ordinal check）、majority vote 共识、per-task 明细。

### 预计耗时
- Step 1-2（合并 + 后处理）：< 1 min
- Step 3（4 版 LLM 分类）：~30-60 min（取决于 failure 数量和模型推理速度），rulebased < 1 min
- Step 4（对比分析）：< 30 sec

### 注意
- `--few_shot` 运行前会自动检测是否已实现，未实现则跳过
- cuda0/cuda1 的 game_file 不重叠（各处理不同 task），所以 agreement 矩阵需要在同一输入上的不同分类方法间才有意义（pipeline 已正确处理）

---
