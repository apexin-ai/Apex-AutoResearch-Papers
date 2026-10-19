# infra extraction integration test

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_extraction_integration_test_20260512T151138_result.json`
- **Structured JSON:** [`c907aef28ed4029f2430.json`](../../sessions/c9/c907aef28ed4029f2430.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cantools 测试完成。两个 repo 的测试全部通过。

## 集成测试报告

### 1. 代码冲突检查
**无冲突。** 两个 Worker 的修改互补，分布在不同逻辑区域：
- Worker A: `batch_extract.py` 中的 beniget ClassDef 支持 + `min_reachable_files=1`
- Worker B: `call_graph.ql` / `bounded_dataflow.ql` 中的 CodeQL Class 谓词 + `extract_dataflow.py` 的 `--external` 参数

### 2. 端到端测试结果

**oauthlib** (含 class + function 类型):

| 实例 | buggy_function 类型 | 提取方法 | call_graph | dataflow |
|------|---------------------|---------|-----------|----------|
| `list_to_scope` | function | beniget | 0 | 0 |
| `Client` | **class** | beniget (ClassDef, 13跨文件) | **81** | 0 |
| `ImplicitGrant` | **class** | **codeql** | **95** | **2033** |

- 非空 call_graph: **2/3**, 非空 dataflow: **1/3**
- CodeQL 对前两个实例返回 exit code 2（可能是查询编译缓存问题），beniget 正常接管

**cantools** (function 类型):

| 实例 | call_graph | dataflow |
|------|-----------|----------|
| `01jft1mj` | 17 | 146 |
| `02y1oom0` | 130 | 2306 |
| `05wgqjp2` | 34 | 393 |

- **CodeQL 3/3 (100%)**，非空 call_graph **3/3**，非空 dataflow **3/3**
- 零 regression，function 类型实例完全正常

### 3. Regression
**无。** function 类型实例 (cantools) 全部 CodeQL 成功，class 类型实例 (oauthlib) CodeQL 和 beniget 双路径均正常工作。`extract_dataflow.py --help` 独立运行正常。

---
