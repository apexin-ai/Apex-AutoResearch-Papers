# analysis deepseek tail1024

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_tail1024_20260517T231140_result.json`
- **Structured JSON:** [`2f7973fc2645ba6b58ba.json`](../../sessions/2f/2f7973fc2645ba6b58ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验分析完成，registry 已更新为 DONE(success)。

## 结果摘要

**Accuracy: 96.47%** (CI: [95.38%, 97.48%])，n=1190

**假设判定: FALSIFIED**（tail-1024 并未低于 tail-512）
- tail-1024 (96.47%) 显著高于 tail-512 (93.9%)，CI 无重叠

**意外发现: 1024→2048 出现 non-monotonicity**
- DeepSeek tail 系列: 256 (76.4%) → 512 (93.9%) → **1024 (96.5%)** → 2048 (95.0%)
- 峰值在 1024，2048 反而下降 1.5pp（CI 略有重叠，接近显著）
- Qwen-7B 全程 monotonic: 256→512→1024→2048 持续上升

**跨模型关键对比**: 两个模型在 tail-1024 达到完全相同的 96.47%，但在 2048 分道扬镳（Qwen 97.3% vs DeepSeek 95.0%），说明 DeepSeek 对 noisy prefix context 更敏感。

---
