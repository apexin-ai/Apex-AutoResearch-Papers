# code bug doc and semantic only check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bug_doc_and_semantic_only_check_20260514T043417_result.json`
- **Structured JSON:** [`63b14f61bb3190d5dfa0.json`](../../sessions/63/63b14f61bb3190d5dfa0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个任务全部完成，结果如下：

---

## Task 1: Bug 文档化 ✅

注释已插入 `compiler/type_mask_processor.py:336`，替换了原有的 2 行简短注释。完整的 Grammar-First Invariant 注释块现在位于 `_GRAMMAR_MASK_THRESHOLD` 定义之前。模块导入验证通过，代码逻辑未受影响。

---

## Task 2: DocRED semantic_only 兼容性 ✅ 完全兼容

- `semantic_only` 模式是 dataset-agnostic 的，mode 选择逻辑（line 425: `if mode in ("semantic_only", "full_s1")`）与 dataset 参数无关
- `build_messages()` 函数（line 152）根据 dataset 分支构建 prompt，与 mode 独立
- **Dry-run 结果**：1 sample 成功，15 entities / 14 relations，耗时 29.5s（含 CUDA 首次 warmup）
- **预估 998 docs 耗时**：~18-25s/doc（warmup 后），约 **5-7 小时**
- **无需代码修改**

---

## Task 3: Phase 0 vs Phase 2 评估一致性 ❌ 不可直接复用

| 维度 | Phase 0 (`raw_outputs_docred.jsonl`) | Phase 2 (`docred_grammar_only.jsonl`) |
|------|------|------|
| JSONL 字段名 | `document`, `model_output`, `elapsed_seconds` | `input_text`, `raw_output`, `inference_time_seconds`, `mode` |
| 报告字段 | `total_documents`, `parse_failures` | `total_samples`, `json_parse_failures` |
| 样本数 | 998 | 998 |
| JSON 解析率 | 96.4%（36 parse failures） | 100% (grammar_only) |
| Phase 2 DocRED unconstrained | **不存在** | — |

**关键差异**：
1. **输出格式不同** — 字段名变了，说明是不同版本的 `run_constrained_extraction.py` 生成
2. **Checker 版本不同** — 报告 schema 不一致（`total_documents` vs `total_samples`）
3. **Phase 2 没有 DocRED unconstrained 跑** — `violation_report_phase2_unconstrained.json` 是 SciERC 的（551 samples）
4. **无法确认 prompt template 一致** — Phase 0 可能用了旧版 prompt

**结论**：需要用当前 Phase 2 pipeline 补跑 `--mode unconstrained --dataset docred`，不能直接复用 Phase 0 数据作为消融表的 unconstrained 行。

---
