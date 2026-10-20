# code fix grammar semantic interaction

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_grammar_semantic_interaction_20260514T025632_result.json`
- **Structured JSON:** [`b214ef8a30abcc9a41d0.json`](../../sessions/b2/b214ef8a30abcc9a41d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动并在处理中：
- GPU 1: 16689 MiB, 84% 利用率
- 输出文件: 89 行（从 87 行 resume，已处理 2 个新文档）
- 崩溃点 doc 88 已安全通过

---

## 汇报

### 1. 崩溃根因

**文件**: `compiler/type_mask_processor.py` → `_apply_type_mask` 方法

**机制**: `full_s1` 模式下两层 LogitsProcessor 按序运行：
1. **XGrammar** 先执行，将 grammar-invalid tokens 设为**有限负值**（如 -1e10），而非 `-inf`
2. **TypeConstraintProcessor** 后执行，将 semantically-disallowed type tokens 设为 `-inf`

当 semantic 约束的 `allowed_types` 与 grammar 当前位置允许的 type tokens 无交集时（如 `valid_tail_types_for_head(head_type)` 返回空集），**所有 grammar-valid type tokens 被设为 -inf**，而 grammar-invalid tokens 仍为有限负值 (-1e10 > -inf)。`argmax` 选中 grammar-invalid token → 下一步 XGrammar 的 `accept_token` assertion 失败。

### 2. 修复内容

**文件 1**: `compiler/type_mask_processor.py` (方案 B — 根治)
- 新增类属性 `_GRAMMAR_MASK_THRESHOLD = -1e8`
- `_apply_type_mask` 增加安全检查：应用 semantic mask 前验证至少一个 semantically-allowed type 有非 grammar-masked logit（> threshold）。若全部已被 grammar mask，跳过 semantic masking，交由 grammar 控制

**文件 2**: `run_constrained_extraction.py` (方案 A — 已存在)
- try-except `AssertionError` fallback 到 grammar-only 已存在（之前手动添加的）

### 3. Dry-run 验证

从 doc 88 (原崩溃点) 起连续 8 个文档全部 OK：
```
[88] Riksakten: OK E=40 R=38 42.8s  ← 原崩溃文档
[89] Dan Sterling: OK E=19 R=14 15.8s
[90] Guillermo Endara: OK E=31 R=31 36.0s
[91-95] 全部 OK
```

### 4. 重启状态

- **PID**: 157042
- **tmux session**: `phase2_docred_full_s1`
- **GPU**: cuda:1 (CUDA_VISIBLE_DEVICES=1)
- **Resume**: 从 87 行处继续，当前已 89 行
- **日志**: `~/runs/schema_semantic_constrained_ie/phase2_docred_full_s1.log`

---
