# code llama probe ablation

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-probe-ablation_20260520T082413_result.json`
- **Structured JSON:** [`be6051eeba09b242a5b3.json`](../../sessions/be/be6051eeba09b242a5b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。结果已保存到 `/root/contrastive_entrain_calib/results/exp012_probe_ablation/results.json`。

## 结果

| Metric | Llama-3-8B | Qwen | 
|---|---|---|
| d_syc best layer | L16 | L19 |
| d_syc best layer AUROC | 0.778 | 0.817 |
| d_syc multi-layer AUROC | 0.813 | 0.835 |
| Random direction AUROC | 0.530 ± 0.054 | 0.727 ± 0.017 |
| **Gap (d_syc − random)** | **+0.248** | **+0.108** |

关键发现：

1. **Llama 的 probe ablation gap 比 Qwen 更大** (+0.248 vs +0.108)——d_syc 方向的信息特异性在 Llama 上更强。

2. **随机方向在 Llama 上接近 chance** (0.53)，而 Qwen 上随机方向自带较高 baseline (0.73)。这说明 Qwen 的激活空间更均匀地编码了 sycophancy 信号，而 Llama 的 sycophancy 信号更集中在特定方向上。

3. d_syc 方向本身的绝对判别力 Llama (0.778) 略低于 Qwen (0.817)，但相对于 random baseline 的优势更大。

---
