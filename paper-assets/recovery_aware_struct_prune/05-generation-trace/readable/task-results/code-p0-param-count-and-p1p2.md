# code p0 param count and p1p2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_p0-param-count-and-p1p2_20260515T054804_result.json`
- **Structured JSON:** [`ed5e88ac1b4360ff854c.json`](../../sessions/ed/ed5e88ac1b4360ff854c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。以下是三项任务的结果。

---

## Task 1 (P0): 总移除参数量验证

**结论：论文 "395,232 parameters are removed" 是错误的。实际移除 ~1.454B 参数。**

### 来源数据

| 项目 | 值 |
|------|-----|
| hidden_size | 3,584 |
| intermediate_size | 18,944 |
| num_attention_heads | 28 |
| num_key_value_heads | 4 |
| num_hidden_layers | 28 |
| head_dim | 128 |

### 计算

**MLP groups:**
- n_mlp_groups = 28/layer, total = 28 × 28 = 784
- group_size = 18944 // 28 = **676 channels**
- params_per_mlp_group = 676 × 3584 × 3 (gate + up + down) = **7,268,352**
- 200 groups pruned → 200 × 7,268,352 = **1,453,670,400**

**Attention groups:**
- 0 groups pruned → 0 params

**总移除参数 = 1,453,670,400 ≈ 1.45B**

### 与 pruning_metadata.pt 交叉验证
- original_params = 7,615,616,512
- pruned_params = 6,161,946,112
- 差值 = **1,453,670,400** ✓

### "395,232" 的真实含义
这是**所有层保留的 MLP intermediate 维度之和**，不是参数量：
- 原始总 intermediate = 28 layers × 18,944 = 530,432
- 移除 channels = 200 groups × 676 = 135,200
- 保留 intermediate = 530,432 − 135,200 = **395,232** ✓

experiments.tex L29 需修正为 ~1.45B (或精确值 1,453,670,400)。

---

## Task 2 (P1): run_full_eval.sh L35-36

**已检查，路径已全部正确。** 当前文件内容：

- L32: `GRPO_RASP_20="/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v2"` ✓
- L33: `GRPO_STANDARD_20="/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v2"` ✓
- L35-41: `ALL_MODELS` 数组引用 `$GRPO_RASP_20` / `$GRPO_STANDARD_20` 变量（间接引用，自动继承 `_v2`）✓

无需修改。

---

## Task 3 (P2): 剪枝参数一致性

| 参数 | 论文值 | 代码值 | 一致？ |
|------|--------|--------|--------|
| Sparsity | 20% (L27) | CLI default=**0.35** (L165)，但 metadata 显示实际运行用 **0.2** | ⚠️ 代码默认值不一致，实际运行正确 |
| MLP groups/layer | 28 (L28) | `n_mlp_groups = n_heads = 28` (L222) | ✓ |
| MLP group size | 676 (L28) | `18944 // 28 = 676` (L223) | ✓ |
| Capacity floor | ≥40%, ≥12/28 groups (L44) | 初选: `max(4, int(28*0.4))=11` (L252)；后校正: `ceil(18944*0.4/676)=12` (L277) | ✓ 有效值=12 |
| Calibration samples | 512 (L32, L36) | `default=512` (cka_overlap L202, importance_score L174) | ✓ |
| α (alpha) | 1.0 (L40) | `default=1.0` (L166) | ✓ |
| Attn groups pruned | 0/112 (L27) | metadata: `n_attn_groups_pruned=0` | ✓ |

**唯一问题**: `prune.py` L165 默认 sparsity=0.35，但论文和实际实验均用 0.20。建议将代码默认值改为 0.2 以保持一致，或在论文中明确说明 CLI 参数 `--sparsity 0.2`。

---
