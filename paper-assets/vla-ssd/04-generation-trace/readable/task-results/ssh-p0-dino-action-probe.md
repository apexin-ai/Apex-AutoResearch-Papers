# ssh p0 dino action probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p0-dino-action-probe_20260515T234230_result.json`
- **Structured JSON:** [`8c88b481dfe3678817c4.json`](../../sessions/8c/8c88b481dfe3678817c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三方对比结果：

| 特征源 | mean_R² | overall_R² | grip_acc |
|--------|---------|------------|----------|
| **DINO cls_token** | 0.7116 | 0.7188 | 0.9259 |
| DINO patch_mean | 0.7082 | 0.7166 | 0.9205 |
| SigLIP+Projector | 0.7063 | 0.7169 | 0.9221 |
| LLM trained L19 | 0.7309 | — | — |
| LLM trained im_mean L19 | 0.6832 | — | — |

- **DINO ≈ Projector**：delta=+0.0054，95% CI=[-0.008, 0.019]，p=0.22，差异不显著
- **Action-delta probe** 很低（mean_R²=0.10），DINO 单帧特征几乎不编码动作变化量
- 结果保存在 `/root/autodl-tmp/vla-ssd/results/functional_validation/dino_action_probe.json`

---
