# code fix openvla attention rotary v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-openvla-attention-rotary-v2_20260524T064354_result.json`
- **Structured JSON:** [`8373c170d2d93f92ca19.json`](../../sessions/83/8373c170d2d93f92ca19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. rotary_emb 实际位置
- transformers 4.40.1（openvla_deps 版本）：`rotary_emb` 在 `LlamaAttention`（即 `layer.self_attn.rotary_emb`）
- `LlamaModel` 顶层 **没有** `rotary_emb`
- 代码已修正为 `layer.self_attn.rotary_emb(v, position_ids)`，shape 验证通过（cos/sin [1,256,128] 与 q/k [1,32,256,128] 兼容）

### 2. 代码修改
代码磁盘上已是正确版本（line 210: `layer.self_attn.rotary_emb`）。原始失败的实验应该是用了 `lm.rotary_emb`（LlamaModel 级别），之后已有人修过。

### 3. 额外修复
Object 实验首次启动时因 `--unnorm_key` 缺失崩溃（模型 `openvla-7b-finetuned-libero-10` 的 stats key 是 `libero_10`，非默认 `libero_object`）。已加 `--unnorm_key libero_10` 重新启动。

### 4. 部署状态

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| `eval_openvla_attn_k05_object_seed42_v2` | GPU 0 (16GB/98GB) | 676486 | RUNNING, Task 1/10 进行中 |
| `eval_openvla_attn_k05_goal_seed42` | GPU 1 (16GB/98GB) | 675516 | RUNNING, Task 1/10 进行中 |

两个实验均已成功通过 Attention Pruning hook（256→128 tokens），无 rotary_emb 错误。

---
