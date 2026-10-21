# code trace optim data

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_trace-optim-data_20260515T093902_result.json`
- **Structured JSON:** [`2a18dae3b73fbe1dcc7e.json`](../../sessions/2a/2a18dae3b73fbe1dcc7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

### 1. trace_generator.py — n=K 改动

- `VLLMGenerator.generate()` 优先使用 `n=k` 参数一次请求生成 K 条 completion（`_generate_n_batch`），vLLM 内部 batch 处理比多次请求高效得多
- 如果 API 不支持 `n` 参数（抛异常），自动 fallback 到原来的 asyncio 并发模式（`_generate_async_fallback`）
- `APIGenerator.generate()` 也加了 retry

### 2. 重试逻辑添加位置

| 位置 | 重试方式 |
|------|---------|
| `VLLMGenerator._generate_n_batch()` | 3 次 exponential backoff（API 调用） |
| `APIGenerator.generate()` 每次循环 | 3 次 exponential backoff（API 调用） |
| `VLLMBackend.call()` | 3 次 exponential backoff（API 调用） |
| `APIBasedLLM.call()` | 3 次 exponential backoff（API 调用） |
| `ConstraintExtractor.extract()` | JSON 解析失败时重新提取，最多 2 次 |
| `ConstraintExtractor.extract_batch()` | 批量结果中解析失败的条目 fallback 到单条 extract（含重试） |

### 3. ProofWriter 数据

- 来源：CRD 项目已有的 `/root/autodl-tmp/crdd/data/proofwriter/proofwriter-OWA-D5-validation.jsonl`（600 条）
- 分布：True 4 题、False 3 题、Unknown 3 题（原始数据集均匀分布 200/200/200）
- 保存：`data/proofwriter_subset.json`，格式与 math500_subset.json 一致

### 4. Mock 端到端测试

通过。50 题 k=3 正常运行，extraction rate 100%，pipeline 各阶段无报错。

---
