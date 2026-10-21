# ops deploy k5 argmin spatial

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-k5-argmin-spatial_20260519T040524_result.json`
- **Structured JSON:** [`7da233b9e30795cba772.json`](../../sessions/7d/7da233b9e30795cba772.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部提交成功。

| 优先级 | exp_id | 服务器 | GPU | 预估完成 |
|--------|--------|--------|-----|----------|
| P1 | `eval-argmin-object-k5-seed42` | bjb2-28827 | cuda:4 | ~8-12h（5/20 凌晨） |
| P1 | `eval-argmin-object-k5-seed43` | bjb1-18228 | cuda:2 | ~8-12h（5/20 凌晨） |
| P2 | `eval-obs-only-spatial-norm02-k5-seed42` | bjb2-28827 | cuda:5 | ~8-12h（5/20 凌晨） |
| P2 | `eval-obs-only-spatial-norm02-k5-seed43` | bjb1-32546 | cuda:1 | ~8-12h（5/20 凌晨） |

说明：
- **argmin mode = `reconvla`**：K 个 VLA samples → 计算均值 → L2 argmin 选最近的，无 CRM correction
- 所有 GPU 与现有 eval 共享（eval VRAM ~3.5-6GB，24GB 卡空间充足）
- 输出文件分别在各服务器 `/root/acr-vla-conformal-refinement/logs/` 下

---
