# code fix xgrammar assertion

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_xgrammar_assertion_20260514T025531_result.json`
- **Structured JSON:** [`a44c9a6b52c8d8d7d3e2.json`](../../sessions/a4/a44c9a6b52c8d8d7d3e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复已完成并验证。以下是报告：

---

## 诊断报告

### 1. 根因分析

**问题所在**：`TypeConstraintProcessor._apply_type_mask()` 在 `allowed_types` 为空集时，会将 grammar 允许的所有 6 个 entity type first tokens 全部 mask 为 -inf。

**触发路径**：在 `_mask_tail_type` 中，`constraint.valid_tail_types_for_head(head_type)` 返回空集。这发生在以下场景：
- 模型生成了一个 relation type（如 "country of citizenship"），其 valid_pairs 只允许 `(PER, LOC)` 
- `_mask_head_type` 将 head_type 强制为 PER（按 domain/range 约束）
- 但如果 PositionDetector 状态跟踪出现偏差（跨 relation 对象时 state 未重置），`head_type` 可能保留前一个 relation 的值
- `valid_tail_types_for_head(前一个relation的head_type)` 对当前 relation 返回空集

**后果**：grammar 只允许 6 个 type token，semantic 把 6 个全 mask 为 -inf → 交集为空 → `argmax` 选中 grammar 不允许的 token → 下一步 XGrammar `accept_token()` assertion 失败。

### 2. 修复内容

**Fix B（根治）** — `compiler/type_mask_processor.py`：
- `_mask_head_type` / `_mask_tail_type`：`allowed_dr` 为空时跳过 masking（`if allowed_dr is not None and allowed_dr:`）
- `_apply_type_mask`：三层防护：
  1. `allowed_types` 为空 → 跳过
  2. 无需 mask 的 token → 跳过  
  3. 验证至少一个 allowed type 有非 grammar-masked 的 logit（`_GRAMMAR_MASK_THRESHOLD = -1e8`），否则跳过

**Fix A（安全网）** — `run_constrained_extraction.py`：
- `run_single_pass`：`try/except AssertionError` 捕获 XGrammar assertion failure，fallback 到 grammar-only 重新生成
- `run_s2_two_pass` Pass 1 和 Pass 2：同样的 try/except 安全网

### 3. Dry-run 结果

**测试 1**（从头跑 5 个样本）：5/5 OK, 0 fail
```
[1/5] Skai TV: OK E=15 R=14 45.2s
[2/5] Washington Place: OK E=18 R=18 55.8s
[3/5] IBM Research – Brazil: OK E=27 R=19 47.4s
[4/5] Lookin Ass: OK E=21 R=19 41.3s
[5/5] Conrad O. Johnson: OK E=20 R=19 42.1s
```

**测试 2**（从崩溃点 resume，跑 3 个新样本）：3/3 OK, 0 fail
```
[88/90] Riksakten: OK E=40 R=38 83.8s
[89/90] Dan Sterling: OK E=19 R=14 31.4s  ← 原崩溃文档
[90/90] Guillermo Endara: OK E=31 R=31 72.0s
```

输出文件 `docred_full_s1.jsonl` 现有 90 行（87 原有 + 3 新增）。

### 4. Resume 可行性

**可以直接 `--resume` 从 90 继续到 998**。命令：
```bash
python3 run_constrained_extraction.py \
  --dataset docred --mode full_s1 \
  --data_path data/docred/dev.json \
  --constraints_path data/docred/ontology_constraints_docred.json \
  --output_path outputs/docred_full_s1.jsonl \
  --device cuda:0 --max_new_tokens 4096 --resume
```

---
