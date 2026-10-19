# code swebench bm25 retriever

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_swebench-bm25-retriever_20260515T190400_result.json`
- **Structured JSON:** [`c3c762583524afbf96e9.json`](../../sessions/c3/c3c762583524afbf96e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

---

## 产出报告

### 1. 代码修改 diff 摘要（554行 → 597行，+43行）

- **新增 `--retriever-type` CLI 参数**：`neural`（默认）/ `bm25`，bm25 模式下 `--checkpoint-path` 变为 optional
- **新增 `BM25Retriever` 类**（L223-242）：使用 `rank_bm25.BM25Okapi`，tokenization 为 `re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*", text.lower())`，文件内容截断 12000 字符（与 neural retriever 一致），接口与 `StructFuseRetriever.rank()` 完全相同
- **`evaluate()` 函数**：新增 bm25 分支，跳过模型加载，直接用 BM25 排序
- **`_write_summary()`**：config 中新增 `retriever_type` 字段
- **模块 docstring**：补充 BM25 用法示例

### 2. 5-instance dry-run 结果

| Metric | Value |
|--------|-------|
| R@1 | 0.6000 |
| R@5 | 0.6000 |
| R@10 | 0.6000 |
| R@20 | 0.6000 |
| MRR | 0.6045 |
| 耗时 | ~3s |

### 3. 100 instances eval 结果（已完成）

| Metric | Value |
|--------|-------|
| R@1 | **0.2800** |
| R@5 | **0.5100** |
| R@10 | **0.5800** |
| R@20 | **0.6300** |
| MRR | **0.3768** |
| Gold coverage | 1.0000 |
| Errors | 0 |
| 总耗时 | ~83s（CPU only） |

- 日志：`/root/autodl-tmp/structfuse/logs/swebench_bm25_100.log`
- 结果目录：`/root/autodl-tmp/structfuse/artifacts/swebench_retrieval_eval/bm25_100/`

---
