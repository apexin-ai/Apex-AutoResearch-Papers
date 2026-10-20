# ssh check truncation rate

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-truncation-rate_20260512T233152_result.json`
- **Structured JSON:** [`60c4319bee4fcec5d34b.json`](../../sessions/60/60c4319bee4fcec5d34b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. 进度
112/985 样本（batch 14/124），约 11.4%。

### 2. 截断率分析

基于 gold output 的 token 长度分布（用实际 tokenizer 计数）：

| 指标 | 值 |
|------|-----|
| 样本数 | 985 |
| Gold 输出平均 tokens | **1138** |
| 中位数 | 907 |
| p75 | 1461 |
| p95 | 2764 |
| **gold output >= 1024 tokens** | **441/985 (44.8%)** |

**预估截断率：~44.8%**。近半数样本的 gold output 超过 1024 tokens。SFT 模型输出长度与 gold 高度相关，因此实际截断率应在这个量级。

注意：这是下界估计。模型生成可能比 gold 更冗长（你提到平均 1362 tokens vs gold 平均 1138），实际截断率可能更高。

### 3. 间接证据
- 日志无 token count 信息，无法直接从已完成样本测量
- 命令行确认 `--max_new_tokens 1024`（config.py 默认 2048，被启动参数覆盖）

### 4. 输出保存机制
**最后批量写入**。`generate_predictions()` 将所有结果收集到内存 list，全部生成完成后才进入 NLI scoring，最终写入 `outputs/posthoc_nli_v2/nli_reranking_results.json`。没有中间结果文件。

---
