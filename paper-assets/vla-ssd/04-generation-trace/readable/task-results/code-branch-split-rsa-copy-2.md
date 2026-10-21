# code branch split rsa

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_branch_split_rsa_20260516T024941_result.json`
- **Structured JSON:** [`681b169efac4db9cd4b7.json`](../../sessions/68/681b169efac4db9cd4b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

## Branch-Split RSA 结果

| 表征 | RSA |
|---|---|
| Standalone DINO cls | 0.692 |
| **Fused 2176d (pre-projector)** | **0.634** |
| Standalone DINO patch_mean | 0.631 |
| **SigLIP branch** (1152d) | **0.621** |
| **DINOv2 branch** (1024d) | **0.619** |
| Fused+Projector 4096d | 0.615 |
| Standalone CLIP patch_mean | 0.557 |

核心发现：
1. **DINOv2 和 SigLIP 两个 branch RSA 几乎相同**（0.619 vs 0.621），无显著差异
2. Fused 2176d (0.634) > 两个单独 branch，拼接有互补收益
3. Pre-projector (0.634) > post-projector (0.615)，projector MLP 略微压缩了 action-relevant 信息
4. SigLIP branch (0.621) >> standalone CLIP (0.557)，验证了 Prismatic 选择 SigLIP 的合理性

所有产出：
- JSON: 服务器 `/root/autodl-tmp/vla-ssd/results/rsa/rsa_branch_split.json`
- 分析摘要: 本地 `artifacts/branch_split_rsa_results.md`
- Features: `/root/autodl-tmp/vla-ssd/features/fused_backbone_libero_goal/` (10 tasks × 50 demos × 2176d)
- 脚本: 服务器 `/root/vla-ssd/scripts/rsa_branch_split.py` + `extract_fused_backbone.py`

---
