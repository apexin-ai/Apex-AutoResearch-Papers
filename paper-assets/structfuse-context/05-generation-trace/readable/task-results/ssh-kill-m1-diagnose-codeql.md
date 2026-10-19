# ssh kill m1 diagnose codeql

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_m1_diagnose_codeql_20260513T194339_result.json`
- **Structured JSON:** [`4b7c315504dd8bdabd8e.json`](../../sessions/4b/4b7c315504dd8bdabd8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 1. 进程清理 ✓
- `m1_reextract` tmux session 已 kill
- PID 97364/97358 已 kill
- 无残留进程（m2_full_qwen / m2_full_starcoder 训练 session 未动）

### 2. 无效文件清理
- **无需清理**：最近 2 小时内 m1_extraction 目录下 0 个新 json 文件。因为所有 CodeQL 查询都失败了，重跑没有产出任何数据。all.jsonl 未受影响。

### 3. CodeQL 诊断

| 项目 | 结果 |
|------|------|
| CodeQL 版本 | 2.25.4 |
| Python extractor | ✓ 已安装 |
| Python QL pack | **✗ 未安装** |

### 4. 根因

**`codeql/python-all` 标准库 pack 未安装。**

错误信息：
```
Pack 'codeql/python-all@7.1.0' was not found in the pack download cache.
Run 'codeql pack install' to download the dependencies.
```

`qlpack.yml` 声明了 `codeql/python-all: "*"` 依赖，但 `/root/.codeql/packages/` 目录不存在——从未执行过 `codeql pack install`。

### 5. 可在 bjb1 修复

根分区剩余 22GB，python-all pack 约 100-200MB，空间充足。修复命令：

```bash
cd /root/structfuse/extraction/codeql_queries && /opt/codeql/codeql pack install
```

要现在执行修复吗？

---
