# code edge pruning hf v2

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_edge_pruning_hf_v2_20260512T191451_result.json`
- **Structured JSON:** [`0fea512b0e07f7d1b54b.json`](../../sessions/0f/0fea512b0e07f7d1b54b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 与 v1 的核心架构差异

| | v1 | v2 |
|---|---|---|
| Hook 策略 | 1 个 `layer.register_forward_pre_hook` 构建单一 masked residual | 4 个 submodule pre-hook：`q_proj`、`k_proj`、`v_proj`、`mlp` 各自独立构建 masked input |
| MLP mask | 参数存在、参与 backward，但 forward 无 hook 应用 → score 全不可信 | `_mlp_pre_hook` 从 source cache 按 MLP edge mask 加权构建输入 |
| Q/K/V 粒度 | L328-329 对 (src, layer) 的所有 Q/K/V mask 取 `mean()` → 单标量 | 每个 hook 独立使用 `masks[idx_tensor].view(1,1,n_heads,1)` 向量化广播，per-head 独立 |
| Source cache | `_ActivationCache` class (embed/head_out/mlp_out 分离) | 统一 `Dict[str, Tensor]`，key = canonical node name |
| 模型冻结 | `model.eval()` 仅切 BN/Dropout | 追加 `model.requires_grad_(False)` 省 backward 内存 |
| 新增模块 | — | `_build_hook_mask_indices`（预计算向量化索引）、`_build_masked_input_qkv`、`_build_masked_input_mlp`、`_src_nodes_before_layer`（提升为模块级共享） |
| 删除 | — | `_ActivationCache`、`_build_dst_mask_table`、`_get_module` |

### 2. Mask 参数总数

**完全相同**。`_build_edge_topology` 未修改，拓扑结构和 mask 数量不变。

- Qwen-2.5 0.5B (24L/14H/2KV): 179,388 edges → 79,452 independent masks (0.30 MB)
- GPT-2 small (12L/12H/12KV): 32,334 edges → 32,334 masks (0.12 MB)

### 3. 各 edge 类型 mask 独立性验证

| 类型 | 验证结果 |
|------|---------|
| Q | n_heads 个独立 mask per (src, layer) ✓ |
| K | n_kv_heads 个独立 mask，同 KV group 内共享 ✓ |
| V | 同 K，但 K≠V（同 group 内也独立）✓ |
| MLP | 每个 (src, layer) 1 个独立 mask ✓ |
| 全覆盖 | hook indices 覆盖所有 n_masks 个参数 ✓ |

### 4. Smoke test 结果

12/12 no-torch tests 全部通过（torch-dependent tests 因本机无 torch 跳过）：

```
[PASS] AST syntax check (v2)
[PASS] Function signature (AST)
[PASS] Edge topology non-GQA: 99 edges, 99 masks
[PASS] Edge topology GQA: 759 edges, 351 masks
[PASS] Destination mask table
[PASS] Qwen-2.5 0.5B: 179388 edges, 79452 masks, 0.30 MB
[PASS] GPT-2 small: 32334 edges, 32334 masks, 0.12 MB
[PASS] Q masks independent per head
[PASS] K/V GQA sharing correct
[PASS] MLP sources include same-layer attention
[PASS] Q/K/V sources exclude same-layer
[PASS] All 71 mask parameters covered by hooks
```

---
