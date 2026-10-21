# viz rsa perlayer curve

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_rsa_perlayer_curve_20260517T200801_result.json`
- **Structured JSON:** [`7ae0609b99338b5dd3a3.json`](../../sessions/7a/7ae0609b99338b5dd3a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已生成并保存。

**输出文件：**
- 服务器：`/root/autodl-tmp/vla-ssd/results/figures/fig_rsa_perlayer_curve.{pdf,png}`
- 本地：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/fig_rsa_perlayer_curve.{pdf,png}`

**关键数字摘要：**

| Condition | Peak Layer | Peak RSA ρ |
|---|---|---|
| Trained, image mean | L12 | 0.6282 |
| Trained, last pre-action | L12 | 0.6425 |
| Untrained, image mean | L0 | 0.6117 |
| Untrained, last pre-action | L1 | 0.6262 |

- **Crossing point:** trained image_mean 和 trained last_preaction 在 ~L11.6 (ρ ≈ 0.623) 交叉。L12 之后 last_preaction 持续高于 image_mean，在深层（L22-32）优势明显（last_preaction 衰减更缓慢）。
- **Trained vs Untrained:** trained model 在 L12 附近形成明显的 peak（尤其 last_preaction），而 untrained model 两条线几乎平坦（image_mean ~0.55，last_preaction 从 0.626 缓慢单调下降至 0.587），无 mid-layer peak 结构。
- **Image mean 深层崩塌:** trained image_mean 从 L12 (0.628) 急剧下降至 L32 (0.422)，而 last_preaction 仅从 0.642 降至 0.584，说明深层 token-level 表征保留了更多 action-relevant 信息。

---
