# code update writing plan

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_update_writing_plan_20260516T035057_result.json`
- **Structured JSON:** [`ee7e8c20741461313dd2.json`](../../sessions/ee/ee7e8c20741461313dd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

writing_plan.yaml 已全面更新，对齐 D042 paper_framing.md。主要变更：

**Narrative 翻转**:
- Claim 1: "VL pretraining is the source" → "Self-supervised geometry is king" (DINO cls 0.692 > Proj 0.615 > CLIP 0.557)
- Claim 2: "LLM degrades" → "LLM non-monotonic inverted-U" (L0=0.612→L12=0.628→L32=0.422)
- Claim 3: "Training invariance Δ=0.021" → "Peak shift L0→L12, best-vs-best Δ=+0.017 n.s., same-layer Δ=+0.079 p<0.0001"

**数值全换 Method B**: 清除所有 Method A 数值 (DINO 0.388, VLA ~0.50, R² 0.706/0.731 等)，替换为 unified_action_probe R² (0.634/0.630/0.587/0.671) 和 D041 RSA。

**其他修正**:
- Method 2.1: 修正 "LIBERO-10 fine-tuned" → "OXE-pretrained, NOT fine-tuned on LIBERO"
- Method 2.2: 加入 standalone encoders、branch-split (10 个 extraction source)
- Discussion: 删除 geometric-functional dissociation（已证伪），加入 branch-split insight 和 self-supervised dominance
- Figures: fig2 改为 cross-encoder 排序，fig3 改为 inverted-U 双线，fig5 改为 peak shift 可视化
- Tables: tab1 完整 10-row cross-encoder RSA 表，tab2/tab3 全换 Method B 数值

---
