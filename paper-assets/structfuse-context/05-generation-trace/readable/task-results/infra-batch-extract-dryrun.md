# infra batch extract dryrun

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_batch_extract_dryrun_20260512T143141_result.json`
- **Structured JSON:** [`01321b2cac2d03727388.json`](../../sessions/01/01321b2cac2d03727388.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 总结

### 修复的 bug（2 个）

1. **`--format=csv` 不是 `codeql query run` 的有效参数**（`batch_extract.py` + `extract_dataflow.py`）
   - 修复：分两步执行 — `codeql query run` 输出 BQRS → `codeql bqrs decode --format=csv` 转 CSV

2. **`--external` 参数接受 CSV 文件路径，不是直接值**
   - 修复：将 buggyFunctionName/buggyFileName 写入临时 CSV 文件，再用文件路径传参

3. **CSV header 解析**（已修复）
   - `parse_call_graph_csv`: `bqrs decode` 输出 header 带引号 `"target_func"`, 原始检测 `line.startswith("target_func")` 失败
   - `parse_dataflow_csv`: header 以 `"col0"` 开头 + 列映射错位（path-problem 查询前 3 列是 CodeQL 内部列）

### 运行结果

| 指标 | 值 |
|------|-----|
| 总 instances | 5 |
| CodeQL 成功 | 0 (阈值=5) / 1 (阈值=1) |
| Beniget fallback | 5 / 4 |
| 失败 | 0 |
| 平均耗时 | 6.4s/instance（含 CodeQL query ~5s + Beniget ~1s） |
| 全量预估 | 50869 × 6.4s ÷ workers |

### CodeQL 命中率低的原因

- 4/5 instance 的 `buggy_function` 是 **class 名**（Client, ImplicitGrant 等），但 `call_graph.ql` 用 `Function f` 匹配，不匹配 Python class
- 1/5 的 `list_to_scope` 是函数，CodeQL 找到 3 entries / 2 files，但 < `min_reachable_files=5` 阈值

### JSONL 输出格式

字段完整：`instance_id, repo, github_repo, base_commit, buggy_file, buggy_function, gold_patch_files, call_graph, dataflow_paths, inter_procedural, extraction_method, extraction_time_s, error`

### 待改进

- `call_graph.ql` 应支持 Python class（`Class` 类型），否则大量 class 级 buggy function 永远无法走 CodeQL 路径
- dataflow parser 列映射已修复，但仅在服务器端；本地 `extract_dataflow.py` 也需同步修复

---
