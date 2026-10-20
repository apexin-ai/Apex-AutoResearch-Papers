# diag occ warning investigation

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_occ_warning_investigation_20260520T161310_result.json`
- **Structured JSON:** [`7b66c16039660d821bd4.json`](../../sessions/7b/7b66c16039660d821bd4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 根因

**`occ_index.json` schema 与 `datasets.py` 代码不匹配。**

代码 `datasets.py:199` 执行 `demos = task_info["demos"]`，期望一个 `{demo_key: original_len}` 字典。

但 `occ_index.json` 的实际结构是：
```json
{
  "task_name": {
    "file": "...",
    "num_demos": 50,
    "demo_ids": ["demo_0", "demo_1", ...]   // ← 列表，且没有 "demos" 键
  }
}
```

**每次**调用 `_load_occ_label` 都在第 199 行抛 `KeyError: 'demos'`，被第 253 行的通用 `except Exception as e` 捕获，打印 `Failed to load occ label: 'demos'`，然后返回全零 fallback。

### 数量和比例

| 指标 | 值 |
|------|-----|
| 总警告数 | 2516（"Failed to load occ label: 'demos'"） |
| "No occ index entry" 警告 | 1（`pick_up_the_black_bowl_on_the_wooden_c...` 不在 index 中） |
| 当前训练进度 | step 402/50005, ~1.08 it/s |
| occ 加载失败率 | **100%**（每个 sample 都失败，每 step 约 6-8 条警告 = batch_size） |

### 模式

**固定失败，非随机。** 所有有 occ index entry 的 task 都因 `KeyError: 'demos'` 失败，与具体 demo/timestep 无关。

### 影响

训练没有 crash，但 occ head 在全零 label 上训练：
- `occ_loss=0.0054` — 看起来很低，实际是因为 target 全零，模型只要输出接近零就行
- **occ safety head 没有学到任何有意义的东西**
- `action_loss=0.3730` — action head 不受影响，正常训练

### 是否需要修复

**必须修复。** 当前 occ head 完全没有收到有效标签，等于没训练。需要：

1. 重建 `occ_index.json`，把 `demo_ids` 列表改为 `demos` 字典，格式 `{"demo_0": original_traj_len, ...}`（从 HDF5 文件中读取每个 demo 的 trajectory 长度）
2. 或者修改 `datasets.py:199` 适配当前的 `demo_ids` 列表格式（但仍需要补充 `original_len` 信息供 demo matching 使用）

**建议方案 1**（改 JSON），因为代码的 demo matching 逻辑依赖 `original_len` 来匹配最合适的 demo，这个信息必须有。修复后需要重启训练。

---
