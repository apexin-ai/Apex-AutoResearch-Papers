# analysis depth extension gpt2xl d4d5 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_depth_extension_gpt2xl_d4d5_001_20260515T114406_result.json`
- **Structured JSON:** [`eac4ad4b5c5e9a3fe9ec.json`](../../sessions/ea/eac4ad4b5c5e9a3fe9ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。

## 结果摘要

- **EDD: 4**（d3v4=0.7501 刚好踩线 ≥0.75，d4v5=0.6805 < 0.75）
- **Binary Pairwise AUC:**
  - d1v2: 0.9657 [0.9588, 0.9725]
  - d2v3: 0.9190 [0.9074, 0.9304]
  - d3v4: 0.7501 [0.7281, 0.7710] ⚠️ 极度边界
  - d4v5: 0.6805 [0.6572, 0.7025]
- **6-class acc (RF):** 0.679 [0.667, 0.691]
- **6-class acc (LR):** 0.631 [0.618, 0.643]
- **Finetune train_loss:** d3→d4 = 1.133, d4→d5 = 0.992
- **样本数:** d0-d5 各 5000，共 30000 ✓

## 对比 Pythia

| 深度对 | Pythia-1.4B | GPT-2 XL | 差异 |
|--------|-------------|----------|------|
| d1v2 | 0.925 | 0.966 | +0.041 |
| d2v3 | 0.823 | 0.919 | +0.096 |
| d3v4 | 0.784 | 0.750 | **-0.034** |
| d4v5 | 0.683 | 0.681 | -0.002 |
| EDD | 4 | 4 | 相同 |

趋势：GPT-2 XL 在浅层（d1v2, d2v3）区分能力显著强于 Pythia（+4~10%），但在深层（d3v4, d4v5）反而略低。两个模型 EDD 一致 = 4。

值得注意的是 GPT-2 XL 的 d3v4 AUC = 0.7501，95% CI 下界 = 0.7281 < 0.75。这意味着如果阈值定义稍严格（如要求 CI 下界 > 0.75），EDD 会降为 3。

## Pipeline 执行情况

8 步全部完成，EXIT_CODE=0，无 OOM/Error：
| Step | 内容 | 耗时 |
|------|------|------|
| 1 | LoRA finetune d3 | ~12 min |
| 2 | Generate d4 (5000) | ~58 min |
| 3 | LoRA finetune d4 | ~12 min |
| 4 | Generate d5 (5000) | ~59 min |
| 5 | Feature extraction d0-d5 | ~7 min |
| 6 | 6-class classifier | <1 min |
| 7 | Binary pairwise eval | <1 min |
| 8 | Data summary | <1 min |

总耗时约 2.5 小时（17:12 → 19:41）。

## 异常/注意事项

1. **d3v4 AUC 极度边界**：0.7501 距阈值 0.75 仅 +0.0001，统计上不稳健（CI 下界 0.728）
2. **无 contamination check**：日志中未见 code contamination 检查步骤
3. **6-class confusion matrix 显示 d3/d4/d5 互混严重**：d4 precision=0.40, recall=0.32（RF），符合 d3v4 边界性和 d4v5 不可区分

## Checkpoint/Data Paths

- d4 data: `/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_4.jsonl`
- d5 data: `/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/depth_5.jsonl`
- d3 LoRA: `checkpoints/gpt2xl/lora_depth_3/checkpoint-939`
- d4 LoRA: `checkpoints/gpt2xl/lora_depth_4/checkpoint-939`
- Features: `results/gpt2xl_depth_extension/features_6class.jsonl`
- Binary results: `results/gpt2xl_depth_extension/binary_pairwise/binary_pairwise_results.json`

---
