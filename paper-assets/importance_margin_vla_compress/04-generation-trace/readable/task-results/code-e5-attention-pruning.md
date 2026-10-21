# code e5 attention pruning

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e5_attention_pruning_20260523T070916_result.json`
- **Structured JSON:** [`762e28aa1263a90bfa47.json`](../../sessions/76/762e28aa1263a90bfa47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Syntax check 通过。

## 产出

**脚本路径**: `/root/autodl-tmp/importance_margin_vla_compress/eval_xvla_attention_pruning_libero.py` (westd-27271)

**支持的 attention pruning 模式**:
| 模式 | 说明 |
|------|------|
| `attention_last` | 最后一层 encoder attention 的 column-sum（各 head 平均） |
| `attention_mean` | 所有 encoder 层 attention 的 column-sum（层+head 平均） |
| `attention_rollout` | Abnar & Zuidema 2020 的 attention rollout（考虑 residual connection 的跨层累积） |

**代码结构 — 与 L2 pruning 的关键差异**:

原始 L2 pruning 在 `_encode_image` 返回后、进入 BART encoder 之前裁剪 vision tokens。Attention pruning 的注入点不同：

1. **`compute_attention_importance()`** (新增) — 从 encoder attention weights 计算每个 vision token 的 importance score（column-sum = 该 token 从所有 position 接收的总 attention）
2. **`install_attention_pruning()`** — monkey-patch `model.forward_vlm`（而非 `model.vlm._encode_image`），流程：
   - 所有 vision tokens 正常通过 `_encode_image` 和 BART encoder（`output_attentions=True`）
   - 从 encoder attention 计算 importance
   - 在 encoder 输出上 prune：保留 top-k vision positions + 全部 text positions
   - 返回格式与原始 `forward_vlm` 完全一致

这样 attention scoring 的上下文是完整的（所有 token 都参与了 self-attention），比 L2 pruning 更符合 "informed pruning" 的语义。

---
