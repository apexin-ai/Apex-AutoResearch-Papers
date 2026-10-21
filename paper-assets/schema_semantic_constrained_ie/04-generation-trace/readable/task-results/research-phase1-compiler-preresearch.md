# research phase1 compiler preresearch

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_phase1_compiler_preresearch_20260513T191628_result.json`
- **Structured JSON:** [`625093d0859bd0eee633.json`](../../sessions/62/625093d0859bd0eee633.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下。

---

## Phase 1 Compiler 技术预研报告

### 1. 调研结论

#### 推荐技术路线：**HF transformers + XGrammar (standalone)**

| 方案 | Qwen3 支持 | LogitsProcessor API | 性能 | 状态 | 推荐度 |
|------|-----------|-------------------|------|------|--------|
| **HF transformers + XGrammar** | ✅ 已在用 | `LogitsProcessor.__call__(input_ids, scores)` — 简单、有状态、full sequence access | 无 continuous batching，单条推理 | **已验证可用** | ⭐⭐⭐ 首选 |
| SGLang | ✅ 支持 (≥0.4.x) | `CustomLogitProcessor.__call__(logits, custom_param_list)` — dill 序列化，batch-level | continuous batching，~40μs/token grammar overhead | 需安装，BF16 on Blackwell OK | ⭐⭐ 性能优化路径 |
| vLLM 0.18.1 | ⚠️ 模块存在但 torch.compile bug | V1 API: `apply(logits)` + `update_state(batch_update)` — 复杂 | 最佳 throughput | **当前服务器不可用** | ⭐ 暂不可用 |

**理由**：
- transformers 后端已跑通 Qwen3-8B 全流程（run_extraction.py 已在用）
- XGrammar 已安装且验证可编译 SciERC ontology schema 为 `CompiledGrammar`
- `xgr.contrib.hf.LogitsProcessor` 直接传入 `model.generate(logits_processor=[...])`，零额外基础设施
- HF LogitsProcessor 的 `input_ids` 参数给出完整生成序列，便于解析 JSON 结构位置和维护 EntityRegistry 状态
- Research prototype 阶段 throughput 不是瓶颈（SciERC 551 sentences，单条推理可接受）

#### vLLM Qwen3 支持进展
- vLLM 从 **v0.8.4** 起原生支持 Qwen3（PR #15289）
- 当前服务器 vLLM 0.18.1 已包含 `qwen3.py` 模块，但 import 时触发 `AssertionError: duplicate template name`（torch 2.10.0 的 `torch.compile` 与 vLLM 的 `TritonTemplate` 冲突）
- 修复方式：升级 torch 或 vLLM，但当前不优先

#### XGrammar-2 可用性：✅ 完全可用
- 服务器已安装（serialization v11，即 XGrammar-2 v0.2.0）
- 支持 `Grammar.from_json_schema()`, `from_ebnf()`, `from_regex()`
- 已验证：`GrammarCompiler.compile_grammar()` 成功编译 SciERC JSON schema
- `contrib.hf.LogitsProcessor` 可直接传入 `model.generate()`
- 无 CUDA 兼容性问题（grammar 计算在 CPU，bitmask apply 用 PyTorch ops）

#### 风险评估
| 风险 | 影响 | 缓解措施 |
|------|------|---------|
| Blackwell GPU (sm_120) 兼容性 | 低 — BF16 推理已验证正常 | 避免 FP8 量化 |
| `OtherScientificTerm` 是 4-token type | 中 — first-token masking 仍可行（first token "Other" = 11409 唯一） | 已验证所有 first tokens 唯一 |
| PositionDetector regex 解析开销 | 中 — 每步 O(n) 文本解析 | 后续可切换到 GrammarMatcher state-based detection |
| 多 token type 的中间 token 共享 | 低 — XGrammar enum grammar 保证一旦 first token 选定，后续 token 被 grammar 强制 | EBNF/JSON schema 的 enum 约束兜底 |

### 2. 代码骨架

#### `compiler/ontology_compiler.py` (9.5KB)
- `OntologyCompiler(constraints_path)` — 解析 `ontology_constraints.json`
- `ConstraintSpec` dataclass — entity types, relation types, `RelationConstraint` (valid_pairs + query methods)
- `compile_ebnf()` — 生成 EBNF grammar（JSON 结构 + entity/relation type enum）
- `compile_json_schema()` — 生成 JSON Schema（XGrammar 推荐方式）
- `compile_xgrammar(tokenizer)` → `CompiledGrammar` — 直接产出 XGrammar 可用的编译产物
- `compile_for_tokenizer(tokenizer)` — 建立 type string → token IDs 映射
- `compile_ontology()` — 一键接口：`(ConstraintSpec, CompiledGrammar)`

#### `compiler/type_mask_processor.py` (14.5KB)
- `TypeConstraintProcessor(LogitsProcessor)` — 解码时动态 domain/range masking
- `FieldPosition` enum — 检测当前生成位置（ENTITY_TYPE / RELATION_TYPE / HEAD_TYPE / TAIL_TYPE / FREE_TEXT）
- `PositionDetector` — 基于 regex 解析生成文本尾部，确定当前 JSON 字段
- `EntityRegistry` — 运行时维护 text→type 映射
- `GenerationState` — 跟踪当前 relation 的已知 type/head_type
- `_mask_head_type()` / `_mask_tail_type()` — 核心约束逻辑：
  - head_type: 允许 `constraint.valid_head_types()`
  - tail_type: 给定 head_type 后，允许 `constraint.valid_tail_types_for_head(head_type)` ← **最关键约束**
- `build_constrained_processors()` — 一键构建 `[grammar_processor, type_processor]`

### 3. 关键技术挑战

1. **Position Detection 准确性** — regex 解析生成文本来判断"当前在哪个 JSON 字段"，边界情况多（嵌套引号、转义字符）。优化路径：利用 XGrammar 的 `GrammarMatcher` 内部状态追踪位置，O(1) per step。

2. **Multi-token Type Masking** — `OtherScientificTerm` 编码为 4 个 token。当前方案：只 mask first token（已验证所有 first tokens 唯一）。XGrammar 的 enum constraint 保证后续 token 被 grammar 强制。如果未来增加 first token 冲突的 type，需要实现 trie-based prefix tracking。

3. **EntityRegistry 跨 section 一致性** — entities section 中注册的 entity text→type，在 relations section 中用于 cross-reference。当前实现在每步重新解析全文提取 entities——后续需优化为增量更新。

4. **Grammar 与 Semantic Mask 组合正确性** — XGrammar mask ∧ TypeConstraint mask 可能产生空集（所有 token 都被 mask），导致生成失败。需要 fallback 机制（如仅保留 grammar mask）。

### 4. 下一步

- [ ] 实现 `PositionDetector` 的单元测试（用 Qwen3 tokenizer 构造各种 partial JSON）
- [ ] 端到端集成测试：`compile_ontology()` + `build_constrained_processors()` + `model.generate()`
- [ ] 性能基线：对比 unconstrained vs grammar-only vs grammar+type-mask 的生成速度
- [ ] DocRED 适配（96 relation types，验证 XGrammar 编译性能）

---
