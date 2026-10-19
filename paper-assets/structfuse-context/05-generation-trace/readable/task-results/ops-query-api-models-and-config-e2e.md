# ops query api models and config e2e

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_query-api-models-and-config-e2e_20260515T190349_result.json`
- **Structured JSON:** [`9ae112da6f42349c1d6b.json`](../../sessions/9a/9ae112da6f42349c1d6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Confirmed — results.jsonl has only 1 line despite 5 instances evaluated. This is a file write bug in the eval script (instances 2-5 results lost from disk, but metrics are correct from in-memory computation).

---

## E2E Dry-Run 报告

### 1. 可用模型列表

API endpoint `http://47.94.22.126/v1` 返回 5 个 Qwen 模型：

| Model ID | Provider |
|----------|----------|
| `qwen/qwen3-235b-a22b` | Alibaba |
| `qwen/qwen3-30b-a3b` | Alibaba |
| `qwen/qwen3.6-plus` (实际: qwen3.6-plus-04-02) | Alibaba |
| `qwen/qwq-32b` | Alibaba |
| `qwen/qwen2.5-vl-72b-instruct` | Alibaba |

### 2. 推荐模型 ID

**`qwen/qwen3.6-plus`** — 参数量最大的文本模型，reasoning/thinking 默认开启。

### 3. API 测试结果

测试成功。模型返回了包含 312 reasoning tokens 的 hello world 响应，确认 API 可用。

### 4. Dry-Run 结果

| Metric | Value |
|--------|-------|
| Strategy | random |
| Instances | 5 |
| **Resolve rate** | **0.0000 (0/5)** |
| 95% Bootstrap CI | [0.0000, 0.0000] |
| Total time | 7m36s (~91s/instance) |
| Retriever | m2_full_qwen/random_s42/best_by_recall_at_1 |
| LLM | qwen/qwen3.6-plus |

### 5. 问题分析

**0% resolve rate 原因：**

- `results.jsonl` 仅写入 1/5 条记录（文件写入 bug），但该条记录 `patch_preview` 为空字符串，说明 LLM 未能生成有效 patch
- Qwen3.6-plus 默认开启 thinking mode，`temperature=0.0` 下可能与 thinking tokens 交互异常
- 单轮 Agentless prompt 方案对 patch 生成要求较高，0/5 在小样本下并不意外

**修复建议：**

1. **results.jsonl 写入 bug**：检查 `eval_swebench_e2e.py` 中 `fout.write` + `fout.flush` 在 tqdm stderr 输出并行时是否存在 fd 竞争；考虑在循环外用 `os.fsync(fout.fileno())` 确保落盘
2. **patch 为空**：查看 `generate_patch()` 函数（line ~293）中 API 返回的 raw response，确认 LLM 是否返回了 thinking tokens 但没有 content，或者 patch 解析正则未匹配
3. **thinking mode**：尝试在 API 请求中设 `extra_body={"enable_thinking": False}` 或换用 `qwen/qwq-32b`
4. **更大样本**：5 instances 不具统计意义，full run (300 instances) 才能评估真实性能

---
