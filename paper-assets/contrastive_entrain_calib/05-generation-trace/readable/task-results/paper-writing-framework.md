# paper writing framework

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_framework_20260520T073815_result.json`
- **Structured JSON:** [`cff6bf2fa4d6c1241e12.json`](../../sessions/cf/cff6bf2fa4d6c1241e12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

§2 `framework.tex` 已写入并注册。内容概要：

- **§2.1 Direction Extraction**: 定义 $d_{\text{syc}}$ 的 mean-difference 提取方法，362 style-controlled contrastive activations (181 pairs)，5-fold CV AUROC 0.827±0.028，best layer=19 (Qwen3-8B)
- **§2.2 GRPO Reward Formulation**: 组合奖励 $R = w_1 \cdot R_1 + w_3 \cdot R_3$，三种 R1 公式化 (F1 cosine, F2 scaled cosine, F3 binary probe)，DeBERTa NLI 作为 R3
- **§2.3 Online Recalibration**: 每 500 步重提取 $d_{\text{syc}}$，cosine similarity ≈ 0.96
- **§2.4 Evaluation Protocol**: ToF / NoF / SYCONScore (harmonic mean) 定义，NLI-based classification，模型配置 (LoRA rank=64, α=128, ZeRO-2)

所有要求的符号 (`\dsyc`, `\tof`, `\nof`, `\sycon`, `\rone`, `\rthree`) 均使用自定义命令。无 em-dash、无 -ing 结尾、无过度分段。约 730 words。

---
