# experiment r deberta mirror download

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_r-deberta-mirror-download_20260520T103156_result.json`
- **Structured JSON:** [`9fc3ee4d5b5837e0941b.json`](../../sessions/9f/9fc3ee4d5b5837e0941b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 下载方式
**aria2c 多线程 + ModelScope CDN** 成功。HF mirror 和 ModelScope Python SDK 都在大文件下载时卡住（xet bridge 限速 / 连接中断），最终用 `aria2c -x 16` 直接从 ModelScope CDN 下载 pytorch_model.bin，17 MB/s，约 90 秒完成。小文件（config/tokenizer/vocab）由 HF mirror 的 `snapshot_download` 先行下载成功。

模型存放在根分区 `/root/models/deberta-large-mnli/`（数据盘 `/root/autodl-tmp` 仅剩 1.7GB 不够用）。

### 模型大小
**406.2M 参数**，pytorch_model.bin = 1.51 GB

### 实验结果

| 方法 | Accuracy | Correct/Total | Delta vs SC |
|------|----------|---------------|-------------|
| SC baseline | 54.41% | 111/204 | — |
| SICA baseline | 59.31% | 121/204 | +4.90pp |
| **NLI standalone** | **49.51%** | 101/204 | **-4.90pp** |
| NLI as SC verifier (abstain on disagree) | 68.48% (coverage 45.1%) | 63/92 | — |
| **NLI + SC combo (w=1)** | **57.84%** | 118/204 | **+3.43pp** |
| **NLI + SC combo (w=3)** | **58.82%** | 120/204 | **+4.41pp** |

### 关键发现
- DeBERTa-large-mnli 单独做 NLI 只有 49.51%，严重低估 "Unknown"（预测 22 个 vs 真实 69 个），偏向 True/False
- 但作为投票成员加入 SC（weight=3），达到 58.82%，比 SC 提高 +4.41pp，接近 SICA（59.31%）
- DeBERTa 与 SC 一致时（45.1% 的问题）准确率高达 68.48%，说明在确定性高的子集上有互补价值

---
