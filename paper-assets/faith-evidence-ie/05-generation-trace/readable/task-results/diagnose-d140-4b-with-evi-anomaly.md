# diagnose d140 4b with evi anomaly

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_d140_4b_with_evi_anomaly_20260521T113755_result.json`
- **Structured JSON:** [`57ca3b43edf207c9d749.json`](../../sessions/57/57ca3b43edf207c9d749.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐了。汇总诊断如下：

## 诊断结果

### 核心对比表

| 配置 | ign_f1 | ign_prec | ign_rec | pred_count | n_predictions | truncated |
|------|--------|----------|---------|------------|---------------|-----------|
| **4B s42 with-evi@1024** | 0.3974 | 0.3936 | 0.4013 | 11626 | 16880 | 288/985 |
| **4B s43 with-evi@1024** | 0.4365 | 0.4431 | 0.4302 | 11118 | 17055 | 318/985 |
| **4B s44 with-evi@1024** | 0.4734 | 0.4676 | 0.4794 | 11859 | 16143 | 249/985 |
| **4B s42 with-evi@2048** | **0.3946** | 0.3748 | 0.4167 | 12645 | **24682** | 243/985 |
| 4B s42 no-evi@2048 | 0.4016 | 0.3859 | 0.4185 | 12349 | 25638 | 178/985 |
| 1.7B s42 with-evi@2048 | 0.4806 | 0.4759 | 0.4854 | 11891 | 25534 | 267/985 |

### 结论：**不是 bug，是两个因素叠加**

**1. s42 本身就是最弱 seed（主因）**

4B @1024 三 seed ign_f1 分别为 0.3974 / 0.4365 / 0.4734，方差极大（std≈0.038）。s42 在 @1024 就已经只有 0.3974，比 3-seed 均值 0.4358 低了 0.038。所以 @2048 的 0.3946 看起来"异常低"，主要是因为在跟 3-seed 均值比，而不是跟 s42 自身比。

**2. @2048 引发 over-generation（次因）**

@2048 对 s42 的影响：
- n_predictions 从 16880 暴增到 **24682**（+46%），模型利用额外 token 空间生成了大量冗余 triple
- TP 仅从 4814 增加到 5000（+3.9%），额外预测几乎全是 FP
- Recall 提升 +0.015（0.4013→0.4167），但 precision 下降 -0.019（0.3936→0.3748）
- 净效果：ign_f1 从 0.3974 微降到 0.3946（-0.003）

**3. 与 1.7B 的差距是模型质量差异，非配置错误**

1.7B with-evi@2048 精度远高于 4B（0.4759 vs 0.3748），说明 1.7B adapter 在 RE 任务上质量更好（可能更易 fine-tune）。这不是 4B 的 bug。

### 排除项
- Adapter 路径：正确（`/root/autodl-tmp/sft_output`）
- Format 合规：99.8%，正常
- Truncation：243/985（24.7%），比 @1024 的 288 还少，不是瓶颈
- Evidence field compliance：75.2%，与 1.7B 的 72.9% 相当

**建议**：如果要做 @2048 的公平对比，应跑 s43 和 s44 的 @2048 eval，预期它们会比 s42 好很多。s42 本身就不具代表性。

---
