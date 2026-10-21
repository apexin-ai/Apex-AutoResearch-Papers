# code demo standardized rsa

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_demo_standardized_rsa_20260516T025703_result.json`
- **Structured JSON:** [`a096bbaf2569abd2ef15.json`](../../sessions/a0/a096bbaf2569abd2ef15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**标准化 RSA（10 demos, Method B）**

| Model | RSA | 95% CI |
|-------|-----|--------|
| **DINO cls** | **0.641** | [0.495, 0.775] |
| DINO patch_mean | 0.568 | [0.392, 0.734] |
| SigLIP projector | 0.565 | [0.427, 0.701] |
| CLIP patch_mean | 0.541 | [0.362, 0.710] |
| VLA untrained L9 imgmean | 0.514 | [0.367, 0.674] |
| VLA trained L9 lastpre | 0.499 | [0.343, 0.635] |
| CLIP cls | 0.482 | [0.292, 0.659] |

**Pairwise Δ 重要发现**：
- trained vs untrained 方向**因 feature type 而逆转**：`last_preaction` untrained > trained (Δ=-0.078, sig)，`image_mean` trained > untrained (Δ=+0.056, sig)。说明 training 在 token 位置间重新分配了 action information。
- DINO cls > SigLIP projector (Δ=+0.077, sig)
- SigLIP vs VLA trained: borderline (CI 下界 ≈ 0)

**Step 2 回答**：`image_mean` 聚合的是 positions 1:257（256 个 image patch tokens），不含 BOS 和 text tokens。代码见 `extract_features.py` 第 `hs_tuple[li][:, 1:1+NUM_IMAGE_TOKENS, :].mean(dim=1)` 行。

JSON 已保存到 `/root/autodl-tmp/vla-ssd/results/rsa/rsa_demo_standardized.json`，摘要在 `artifacts/demo_standardized_rsa.md`。

---
