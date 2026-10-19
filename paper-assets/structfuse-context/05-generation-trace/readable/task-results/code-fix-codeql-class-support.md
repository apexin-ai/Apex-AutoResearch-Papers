# code fix codeql class support

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_codeql_class_support_20260512T150208_result.json`
- **Structured JSON:** [`06afba2ae45c802c4764.json`](../../sessions/06/06afba2ae45c802c4764.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。修复总结：

### 修改的文件

**1. `call_graph.ql`** — 新增 Class 支持
- 添加 `isBuggyClass(Class c)` 谓词：按名称+文件匹配 Python 类
- 将 `isBuggyFunction` 泛化为 `isOrigin(Function f)`：匹配直接函数 OR 匹配类的所有方法（`f.getScope() = c`）
- 新增 `classInstantiationCaller`：捕获 `ClassName()` 调用点作为 hop1 caller
- 新增 `isSubclassMethod`：通过 `sub.getABase().(Name).getId()` 名称匹配直接子类的方法，归入 hop1 subclass

**2. `bounded_dataflow.ql`** — 同步 Class 支持
- 添加 `isBuggyClass` + `isOrigin` 谓词
- 将 `isBuggyFunction` 在 hop1/hop2/inScopeFunction 中替换为 `isOrigin`
- 数据流分析范围自动覆盖类方法

**3. `extract_dataflow.py`** — 修复 `--external` 参数
- 将 `--external=buggyFunctionName={value}` 改为写入 CSV 文件再传路径（与 batch_extract.py 一致）

### 验证结果

| 实例 | buggy_function | 修复前 | 修复后 |
|------|---------------|--------|--------|
| Client | 类 | 0 条 | 134 条（7 origin, 14 subclass, 71 caller, 42 callee） |
| ImplicitGrant | 类 | 0 条 | 95 条 |

---
