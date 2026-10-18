# code gpt2xl ref model a2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpt2xl_ref_model_a2_20260516T174038_result.json`
- **Structured JSON:** [`f9b2f81aec19a6abd1c3.json`](../../sessions/f9/f9b2f81aec19a6abd1c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已提交并注册为 RUNNING。

**实验 `gpt2xl_ref_ablation_001`**：
- 脚本：`src/gpt2xl_ref_ablation.py`
- GPU：cuda:1 on gpu-6000pro-2
- 流程：GPT-2 XL 对 20000 条 Pythia nucleus 文本提取 surprisal features → RF 4-class 5-fold CV → 与 Pythia-as-ref baseline 对比
- 产出：`results/gpt2xl_ref_model/summary.json`
- 预计 20000 samples × batch_size=16 ≈ 1250 batches，约 30-60 分钟完成特征提取，加评估共 ~1h

---
