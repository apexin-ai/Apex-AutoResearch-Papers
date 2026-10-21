# code check h5 key compat

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check-h5-key-compat_20260515T175420_result.json`
- **Structured JSON:** [`e94d5f791cccb70c1128.json`](../../sessions/e9/e94d5f791cccb70c1128.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**兼容，无需修改。**

`scan_features` (第 78 行) 的关键逻辑在第 87 行：

```python
keys = sorted(f.keys(), key=lambda x: int(x.split("_")[-1]))
```

它遍历 h5 文件的**所有顶层 key**，不依赖任何固定前缀。排序用 `split("_")[-1]` 提取末尾数字，对 `demo_0` 和 `traj_0` 都有效（分别提取出 `0`）。

每个 trajectory key 存入 `traj_metas` 时记录的是实际的 `h5_key` 值（第 98 行 `h5_key=hk`），后续 `load_layer_features`（第 128 行）通过 `f[m["h5_key"]][m["feat_key"]]` 访问数据，完全按存储的实际 key 加载，不做任何前缀假设。

实际验证：
- VLA h5 key: `demo_0, demo_1, ...`
- DINO h5 key: `traj_0, traj_1, ...`

两种格式都能被 `scan_features` 正确枚举和加载。

---
