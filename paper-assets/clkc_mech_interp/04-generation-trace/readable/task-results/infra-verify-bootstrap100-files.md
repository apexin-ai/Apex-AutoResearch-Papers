# infra verify bootstrap100 files

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify_bootstrap100_files_20260521T234207_result.json`
- **Structured JSON:** [`578e34e0eeb8a904e664.json`](../../sessions/57/578e34e0eeb8a904e664.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**n=100 bootstrap 没有成功完成。** 所有现存 JSON 文件中 `n_bootstrap` 均为 **20**。

### 详细状况

| 模型 | n=100 运行状态 | 问题 |
|------|---------------|------|
| **Qwen** | 迭代全部跑完（日志 404 个 Bootstrap 匹配 = 4方向×101） | **保存时崩溃**：路径拼接 bug 导致 `data/qwen3/data/qwen3/probe_results_bootstrap.json`（重复），FileNotFoundError，结果丢失 |
| **Llama** | 只跑到第4个方向 ZH→EN 的 Bootstrap 12 就停了（日志 318/404） | **未完成**，进程已终止 |

### 文件现状（全部是 n=20 的旧结果）

| 文件 | n_bootstrap |
|------|-------------|
| `data/llama31/probe_results_bootstrap.json` | 20 |
| `data/llama31/probe_results_bootstrap_n20.json` | 20 |
| `data/qwen3/probe_results_bootstrap.json` | 20 |
| `data/qwen3/probe_results_bootstrap_n20.json` | 20 |

### 需要修复

1. `train_probe.py` 第335行的保存路径有 bug：相对路径 `data/qwen3/` 被拼接了两次
2. 修复后需要重新跑 n=100（两个模型都要重跑）

---
