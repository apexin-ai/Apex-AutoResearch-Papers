# code instruction conditional probe

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_instruction_conditional_probe_20260516T225829_result.json`
- **Structured JSON:** [`1ffaf767b2836c229d0e.json`](../../sessions/1f/1ffaf767b2836c229d0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本写好，dry-run 通过。

**脚本**: `/root/vla-ssd/scripts/instruction_conditional_probe.py`
**结果**: `/root/autodl-tmp/vla-ssd/results/qa_probe/instruction_conditional_results.json`

**Dry-run 结果（2 tasks, L0, trained only）**:
| 条件 | acc | f1 |
|---|---|---|
| trained_image_mean L0 | 0.9951 | 0.9949 |
| trained_last_preaction L0 | 0.5924 | 0.3720 |
| dino_cls | 0.9974 | 0.9973 |

**初步观察**: L0 层 image_mean 远高于 last_preaction（0.995 vs 0.592）。这说明在 L0 层，image_mean 已经包含足够的视觉差异来区分 2 个 tasks（不同场景），而 last_preaction token 在 L0 还没有充分编码视觉信息。DINOv2 也接近 1.0，进一步佐证这两个 task 的视觉场景差异很大。

完整实验（10 tasks × 9 layers × 2 条件 × 2 聚合 + DINOv2）等 Director 确认后再跑。

---
