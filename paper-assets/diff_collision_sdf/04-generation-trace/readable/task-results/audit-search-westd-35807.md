# audit search westd 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_search-westd-35807_20260529T054016_result.json`
- **Structured JSON:** [`a2cc56314793e9eff4cb.json`](../../sessions/a2/a2cc56314793e9eff4cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Search complete. Here's the full report:

---

## 搜索结果汇报

### 搜索目标 1: Pi0.5 baseline (TSR=71.5%, CAR=28.5%, per-task TSR: 74/80/66/66)

**未找到。** westd-35807 上仅有 3 个 Pi0.5 pretrained baseline eval 文件，均不匹配：

| 文件 | Seed | TSR | CAR | Per-task TSR (OJ/CP/Milk/BBQ) |
|------|------|-----|-----|------|
| `reeval_baseline_pertask.json` | 7 | 75.0% | 30.0% | 74/74/72/80 |
| `pi05_safelibero_object_v11_s1.json` | 1 | 76.0% | 25.0% | 72/86/68/78 |
| `pi05_safelibero_object_v11_s2.json` | 2 | 75.0% | 27.5% | 76/86/64/74 |

论文目标 (74+80+66+66)/4 = 71.5% 内部自洽，但服务器上没有任何文件含有 per-task TSR [74, 80, 66, 66]。全量扫描了 `/root/autodl-tmp/eval_results/` 下 57 个 JSON 文件，无一匹配。

### 搜索目标 2: LoRA s2 (CAR=55.0%, per-task CAR: 56/76/62/26)

**未找到。** 

**LoRA baseline checkpoint 目录实际 seed：**
| Checkpoint | 状态 |
|------------|------|
| `pi05_lora_baseline_object_pudding_seed0` | 完成 (30000 steps) |
| `pi05_lora_baseline_object_pudding_seed1` | 空目录 (无 checkpoint) |
| `pi05_lora_baseline_object_pudding_seed3` | 训练中 (仅 4000 steps, best=2000) |

**没有 seed2。** seed3 的训练尚未完成，**也没有任何 eval 结果**。

仅 seed0 的 LoRA baseline 被评估过（5 个 eval seed），avg CAR 在 51.9%~57.5% 之间，但 per-task 均不匹配 [56, 76, 62, 26]。

全量扫描中最接近的文件：
- `eval_s1_l1_22k_seed7.json`: CAR=[56, 76, 72, 22] — OJ 和 CP 匹配，但这是 **SDF 模型** (seed1, λ=1.0)，不是 LoRA baseline
- `eval_safelibero_object_all_levelII_10000_lora_baseline_seed2.json`: CAR=[56, 74, 74, 26] — OJ 和 BBQ 匹配，但 CP=74≠76, Milk=74≠62

### 结论

1. **Pi0.5 baseline (71.5/28.5)**: 源 JSON 在 westd-35807 上不存在。可能在 westd-45947 上（已知有 `pi05_safelibero_object_v11.json` 但 TSR=73%≠71.5%），或已被删除/覆盖
2. **LoRA s2 (CAR=55.0%)**: 源 JSON 不存在。seed3 checkpoint 仍在训练（4000/30000 steps），尚未产生 eval。seed1 checkpoint 为空。**论文中报告的 "s2" 数据目前无法复现**——需要等 seed3 训练完成后运行 eval
3. **无 git 历史** 记录 eval JSON 文件的变更，无法追溯是否有文件被删除

---
