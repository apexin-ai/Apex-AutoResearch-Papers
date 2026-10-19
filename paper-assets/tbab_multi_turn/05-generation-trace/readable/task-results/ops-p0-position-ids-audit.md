# ops p0 position ids audit

**tbab multi turn** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0-position-ids-audit_20260518T181243_result.json`
- **Structured JSON:** [`148105af545fe360ad4b.json`](../../sessions/14/148105af545fe360ad4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。以下是完整结论。

---

## Position_ids 审计结果

### 1. 训练侧 — tbab_utils.py `build_position_ids`

```python
# 核心逻辑 (tbab_utils.py:60-79)
if not use_reset:
    return list(range(seq_len))  # 标准连续递增

# use_reset=True 时:
for turn_idx, (start, end) in enumerate(turn_boundaries):
    has_bridge = (turn_idx > 0 and num_bridge > 0)
    if has_bridge:
        # bridge: [0, 1, ..., K-1]
        # content: [K, K+1, ...]
    else:
        # 从 0 开始: [0, 1, 2, ...]
```

**验证脚本实际输出 (C2, 训练数据 sample 0):**
```
EOS@232: pos=[..., 229, 230, 231, 232, 0, 1, 2, 3, ...]  ← reset ✓
EOS@575: pos=[..., 339, 340, 341, 342, 0, 1, 2, 3, ...]  ← reset ✓
Position resets: 5 个 (每个 turn boundary 都 reset)
```

**验证脚本实际输出 (C4, 训练数据 sample 0):**
```
EOS@232: pos=[..., 231, 232, 0, 1, 2, 3, 4, 5, ...]  ← bridge[0,1,2,3] + content[4,5,...] ✓
Bridge tokens [32000-32003] 在 EOS 后正确插入
Position resets: 4 个 (每个 turn boundary)
```

Batch 确认:
- `'position_ids' in batch: True`
- 4D attention mask: shape `(2, 1, N, N)`, dtype `bfloat16` — 标准 causal mask, 允许跨 turn attention
- `remove_unused_columns=False` + 自定义 `TBABTrainer.compute_loss` — `position_ids` 确实传入 `model.forward()`

### 2. 推理侧 — tbab_inference.py `build_position_ids`

```python
# 核心逻辑 (tbab_inference.py:53-87)
# boundaries = content_start positions (after bridge)
# K = bridge token count
for t_idx, content_start in enumerate(boundaries):
    bridge_start = content_start - K
    # bridge: [0, 1, ..., K-1]
    # content: [K, K+1, ...]
```

**验证脚本实际输出 (C2-infer):**
```
EOS@23: pos=[..., 21, 22, 23, 0, 1, 2, 3, ...]  ← reset ✓
EOS@46: pos=[..., 20, 21, 22, 0, 1, 2, 3, ...]  ← reset ✓
current_turn_pos=14 (生成续写从 pos=14 开始) ✓
```

**验证脚本实际输出 (C4-infer):**
```
EOS@23: pos=[..., 22, 23, 0, 1, 2, 3, 4, 5, ...]  ← bridge[0,1,2,3] + content[4,5,...] ✓
Bridge at [24-27, 51-54] → pos [0,1,2,3]
current_turn_pos=18 ✓
```

推理 routing 正确: `model_local.py` 对 C2/C4 使用 `_generate_tbab()` → `generate_tbab()` → 逐 token 解码, 每步 position 递增, 4D causal mask 覆盖 Mistral sliding window。

### 3. 一致性判断

| 维度 | 训练 | 推理 | 一致? |
|------|------|------|------|
| position reset at turn boundary | ✓ (每个 EOS 后 reset 到 0) | ✓ (每个 EOS 后 reset 到 0) | ✓ |
| bridge token positions [0..K-1] | ✓ | ✓ | ✓ |
| content starts at pos=K | ✓ | ✓ | ✓ |
| 4D causal mask (bypass packed-seq detection) | ✓ | ✓ | ✓ |
| position_ids 传入 model.forward() | ✓ (batch key + Trainer pass-through) | ✓ (显式参数) | ✓ |
| generation 阶段 pos 递增 | N/A | ✓ (current_turn_pos + 1 each step) | ✓ |

### 4. 结论: **情况 D — 训练和推理都有 position reset, 逻辑一致, 实现正确**

position_ids 不是 C4 eval 低分的原因。两侧实现干净、一致:
- 数据结构不同 (训练用 `(start, end)` tuple, 推理用 `content_start` list) 但语义等价
- bridge token 归属下一个 turn, 训练/推理一致
- 4D causal mask 正确 bypass 了 transformers 对非单调 position_ids 的 packed-sequence 检测

**如果 C4 eval 低分, 需要从其他方向排查** — 比如 bridge token embedding 初始化/训练充分性、eval 时 generation 超参、或 eval metric 本身的特性。

---
