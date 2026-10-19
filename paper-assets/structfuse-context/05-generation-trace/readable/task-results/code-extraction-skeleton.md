# code extraction skeleton

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_extraction_skeleton_20260512T100103_result.json`
- **Structured JSON:** [`bc5a2dfbf0b46e543033.json`](../../sessions/bc/bc5a2dfbf0b46e543033.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个文件已创建并注册。文件结构：

```
artifacts/code/extraction/
├── codeql_queries/
│   ├── call_graph.ql          # Phase 1a: 2-hop call graph (caller+callee 双向)
│   └── bounded_dataflow.ql    # Phase 1b: scope-bounded inter-procedural data-flow
├── extract_dataflow.py        # 主 pipeline: CodeQL → Beniget fallback → JSONL
└── build_training_data.py     # 对比训练数据: (query, pos, negatives) + 特征向量
```

各文件要点：

**call_graph.ql** — 通过 external predicate 接收 buggy function 位置，用 points-to 分析解析调用关系，手动展开 2 层（`hop1`/`hop2` predicates），输出函数名、hop distance、方向、文件路径和行号。

**bounded_dataflow.ql** — 使用 module-based `DataFlow::ConfigSig` 配置，sources 限制为 `inScopeFunction` 的 parameters 和 return values，sinks 限制为同范围函数的 variable reads。`@timeout 300` / `@ram 8192` pragma 控制资源。`@kind path-problem` 获取完整路径。

**extract_dataflow.py** — `multiprocessing.Pool` 并行处理 repos；每个 repo 依次创建 CodeQL DB → 运行 call_graph.ql → 检查 reachable files ≥ min_reachable_files → 运行 bounded_dataflow.ql；失败时 fallback 到 `beniget` 做 intra-file def-use；输出带 `inter_procedural` 标记的 JSONL。

**build_training_data.py** — 按 repo 分组构建 BM25 索引；hard negatives = BM25 高分但 data-flow 不可达；特征向量含 dataflow_distance / path_count / dependency_type / bm25_score / inter_procedural；全局 min-max 归一化；输出 HuggingFace datasets 兼容格式。

---
