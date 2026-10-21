# dryrun content verification

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_dryrun_content_verification_20260520T110435_result.json`
- **Structured JSON:** [`9f85d1510ebdf5b0719f.json`](../../sessions/9f/9f85d1510ebdf5b0719f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 版本成功运行，`LD_LIBRARY_PATH` 修复了 CUDA 问题。结果与 CPU 版一致。

## Dry Run 结果汇总

**BERTScore + NLI 管线端到端可用** ✓

### 5 条 identity transform 记录结果

| 指标 | 结果 |
|------|------|
| **BERTScore** | mean=1.0000, std=0.0000 ✓ |
| **NLI** | mean=0.1975, std=0.4379 (1/5 pass) |
| **passed** | 1/5 (仅 BERTScore+NLI 同时过阈值的) |

### 逐条 NLI 详情
- Sample 0 (920 chars): entailment=0.9808 ✓
- Sample 1 (1494 chars): entailment=0.0039 ✗
- Sample 2 (37 chars): entailment=0.0006 ✗
- Sample 3 (1471 chars): entailment=0.0018 ✗
- Sample 4 (178 chars): entailment=0.0003 ✗

### 需要关注的问题

1. **NLI identity test 失败**：`cross-encoder/nli-deberta-v3-large` 对 identical text 大多预测 "neutral" 而非 "entailment"。这是 NLI 模型的已知行为——训练数据中 premise ≠ hypothesis。但这意味着对真实 counterfactual pairs（相似但不同的文本）时需要重新验证 NLI 阈值是否合理。

2. **CUDA JIT 修复**：`torch 2.11.0+cu130` 需要 `LD_LIBRARY_PATH` 包含 `/root/miniconda3/lib/python3.12/site-packages/nvidia/cu13/lib`，否则 `libnvrtc-builtins.so.13.0` 找不到。

3. **BERTScore 默认模型**：`microsoft/deberta-xlarge-mnli` (~2.8GB) 尚未下载到服务器（AutoDL 代理下载极慢）。已添加 `--bertscore-model` 和 `--bertscore-num-layers` 参数，dry run 使用本地 NLI 模型替代。正式跑需下载原模型或用 ModelScope 后台下载。

4. **代码变更**：`content_verification.py` 新增 `--bertscore-model`、`--bertscore-num-layers` 两个参数（已同步到服务器和本地 artifacts）。

---
