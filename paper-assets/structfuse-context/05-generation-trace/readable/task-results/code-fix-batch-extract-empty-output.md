# code fix batch extract empty output

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_batch_extract_empty_output_20260512T150049_result.json`
- **Structured JSON:** [`b231cf1c0d156037453b.json`](../../sessions/b2/b231cf1c0d156037453b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。验证结果汇总：

## V1: oauthlib (5 实例)

| 实例 | buggy_function | method | call_graph | dataflow |
|------|---------------|--------|-----------|----------|
| 09vlzwgc | list_to_scope | beniget | 0 | 0 |
| 0fceycuu | **Client** (ClassDef) | beniget | **81** | 0 |
| 0fukhdzk | **ImplicitGrant** (ClassDef) | beniget | **9** | 0 |
| 0hkl0pea | **GrantTypeBase** (ClassDef) | beniget | **10** | 0 |
| 0mvyid7d | **DeviceAuthorizationEndpoint** (ClassDef) | beniget | **3** | 0 |

**4/5 非空 call_graph**（修复前 0/5）。sanity check 通过。

## V3: 跨 repo 验证

| repo | 实例数 | 非空 call_graph | 非空 dataflow | 方法 |
|------|-------|----------------|--------------|------|
| **paramiko** | 3 | **3/3** | 0/3 | beniget (ClassDef: SSHClient 等) |
| **jinja** | 3 | **2/3** | 1/3 | beniget + codeql |
| **deepdiff** | 3 | **3/3** | 0/3 | beniget (ClassDef: AnySet 等) |
| **cantools** | 3 | **3/3** | **3/3** | codeql (17/130/34 entries) |

所有 4 个 repo 的 sanity check 均通过（非空 call_graph > 0）。cantools 尤其出色：3/3 全部 CodeQL 成功，dataflow 分别有 146/2306/393 条路径 — Bug 2 修复让 4-reachable-files 不再被丢弃。

## 修改内容

1. **Bug 1** (`beniget_extract`): 增加 `ast.ClassDef` 匹配 + 新增 `_search_class_refs_in_file()` 做跨文件搜索（继承/实例化/方法调用）
2. **Bug 2** (`query_instance`): `min_reachable_files` 从 5 改为 1
3. **CLI**: 新增 `--repo`（按 repo 过滤）、`--limit`（限制实例数）、`--dryrun`（不写文件，打印结果）
4. **V2 sanity check**: dryrun 结束时统计非空 call_graph 占比，全空则 WARNING + exit(1)

---
