# code rasp rlvr prune

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rasp_rlvr_prune_20260516T095028_result.json`
- **Structured JSON:** [`6ff1efab35c198b47f87.json`](../../sessions/6f/6ff1efab35c198b47f87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

## 代码修改

`src/prune.py` 新增 `rasp-rlvr` 模式：
- `--mode` choices 添加 `"rasp-rlvr"`
- Score 公式：`importance * cka_overlap^alpha`（与 RASP 的 `importance * (1 - cka_overlap)^alpha` 相反）
- metadata 中 alpha 字段覆盖新模式

## 剪枝结果

| | RASP (α=1.0) | RASP-RLVR (α=1.0) |
|---|---|---|
| Actual sparsity | 19.09% | 19.09% |
| Attn groups pruned | 0/112 | 0/112 |
| MLP groups pruned | 200/784 | 200/784 |
| Params | 7.62B → 6.16B | 7.62B → 6.16B |

**输出路径**: `/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20/`（含 `model.safetensors`）

## Group Selection 差异

两种模式的剪枝分布明显不同：
- **RASP** 重剪前 6 层 + 后几层（19, 23-25, 27），保留中间层（6-18 大部分全保留）
- **RASP-RLVR** 同样重剪前 6 层，但中后段（16-26）也大量剪枝，而 Layer 6-7, 27 反而全保留

关键差异层：Layer 6（RASP 保留 12 vs RLVR 保留 28）、Layer 27（RASP 保留 12 vs RLVR 保留 28）、Layer 16-18（RASP 全保留 vs RLVR 剪 20-30%）。这符合预期——RLVR 模式保留高 overlap（冗余）结构，剪掉功能独特的结构。

---
