# code proofwriter prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_proofwriter-prep_20260515T183539_result.json`
- **Structured JSON:** [`f79dea1d4a207654f5f0.json`](../../sessions/f7/f79dea1d4a207654f5f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇报：

### 1. ProofWriter 数据来源
- **已有本地数据**: `/root/symb_invariant_consensus/data/proofwriter_subset.json`（10 题 D5）
- 原始来源: CRD 项目 `/root/autodl-tmp/crdd/data/proofwriter/proofwriter-OWA-D5-validation.jsonl`
- 已有 `prepare_proofwriter.py` 可从 CRD 数据重新生成
- 答案分布: True×4, False×3, Unknown×3

### 2. 关键设计决策
- **数据加载器** (`data/proofwriter_loader.py`):
  - `load_proofwriter()` → 返回 `{id, context, question, answer, depth}` 格式（标准化接口）
  - `load_proofwriter_pipeline_format()` → 返回与 `run_full_mvp.py` 兼容的格式（直接喂给 `SICAPipeline`）
  - 自动从合并的 `problem` 字段解析 context/question
- **评估脚本** (`eval_proofwriter.py`):
  - 直接调用 `SICAPipeline.run_single()` + `SelfConsistency` baseline
  - 答案比较用 case-insensitive 精确匹配（`match_answer()`），不走 `is_equiv` 的 sympy 路径
  - 每题做 checkpoint，支持 `--dry-run` 验证数据

### 3. 后续步骤
1. **Trace generator prompt 需要适配**（已标 TODO）: 当前 `SOLVE_PROMPT` 是数学导向（"Solve the following math problem... put answer in `\boxed{}`"），ProofWriter 应使用逻辑推理 prompt，要求输出 True/False/Unknown。现有答案提取 (`extract_answer`) 的 fallback 模式对 "True"/"False" 文本匹配可能不稳定
2. **v3 完成后直接执行**: `python eval_proofwriter.py --k 12 --temperature 0.7`
3. 也可用已有的 `run_proofwriter.sh`（调用 `run_full_mvp.py`），两种方式都能跑

---
