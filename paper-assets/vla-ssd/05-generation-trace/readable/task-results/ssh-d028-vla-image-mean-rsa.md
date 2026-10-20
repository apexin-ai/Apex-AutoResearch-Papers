# ssh d028 vla image mean rsa

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d028-vla-image-mean-rsa_20260515T223122_result.json`
- **Structured JSON:** [`fcbe9998282577f28c5a.json`](../../sessions/fc/fcbe9998282577f28c5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果总结：

### image_mean RSA 结果

|  | last_preaction | image_mean | delta |
|---|---|---|---|
| **Trained** peak | 0.4876 | **0.5014** (L23) | +0.014 |
| **Untrained** peak | 0.4846 | **0.4847** (L23) | +0.000 |
| **SigLIP projector** | — | 0.6153 | — |

### 解读

1. **image_mean RSA ≈ 0.50，远低于 SigLIP 的 0.615**：聚合方式差异不能解释 gap。LLM self-attention 确实降解了 image token 中的 action-relevant 结构。

2. **Trained vs Untrained 分离更清晰**：image_mean 下 trained-untrained delta = +0.017（peak layer 23），比 last_preaction 的 +0.003 明显更大。训练增强了 image token 表征的 action 相关性，但这个信号在 last_preaction（序列末位 token）中被稀释了。

3. **Layer 0 一致性验证**：trained 和 untrained 在 layer 0 完全相同（0.4509），符合预期（LLM 处理之前）。

4. **Trained 呈现 inverted-U 曲线**：RSA 从 layer 0（0.45）升至 layer 23（0.50）再降到 layer 32（0.44）。Untrained 几乎平坦（0.47-0.48）。

结果已保存到 `/root/autodl-tmp/vla-ssd/results/rsa/rsa_image_mean.json`。

---
