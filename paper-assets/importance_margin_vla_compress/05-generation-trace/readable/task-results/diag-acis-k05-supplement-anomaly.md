# diag acis k05 supplement anomaly

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_acis_k05_supplement_anomaly_20260518T150543_result.json`
- **Structured JSON:** [`3d065c5a3b41f8f0bf86.json`](../../sessions/3d/3d065c5a3b41f8f0bf86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**Pruning 未实际执行。** 原因已确认。

### 根因

cqa1-33015 上的 `eval_success_rate_libero.py` 是**旧版本**，`register_acis_hook` 的实现有 bug：

**cqa1（旧版，有 bug）：**
```python
def hook_fn(module, input, output):
    tokens = output[0] if isinstance(output, tuple) else output
    if tokens.dim() != 3 or tokens.shape[1] != mask.shape[1]:
        return output  # ← 直接跳过！
```

**westd（新版，正确）：**
```python
state = {"offset": 0}
def hook_fn(module, input, output):
    ...
    n = tokens.shape[1]
    cam_mask = mask[:, offset:offset + n]  # ← 按 camera 分段切片
    state["offset"] = offset + n
```

模型使用 2 个 camera（`image`, `image2`），connector 被调用多次，每次输出一个 camera 的 token 子集。`mask` 是所有 camera token 拼接的总长度。旧版直接比较 `tokens.shape[1]`（单 camera）vs `mask.shape[1]`（全部 camera），必然不等，hook **每次都 return output 不做任何修改**。

### 佐证

| 实验 | 服务器 | hook 版本 | Tasks 6-9 SR |
|------|--------|-----------|-------------|
| eval_stage1only_object_v2_fixed | westd（offset 版） | 正确执行 pruning | **0%** |
| eval_acis_k05_supplement_200eps | cqa1（shape 比较版） | pruning 被跳过 | **47.5%** |

westd 同一 checkpoint 对 tasks 6-9 也是 0%，排除 task 差异。cqa1 的 47.5% 就是未 pruning 的 baseline 性能。

### 其他差异（非根因但需注意）

1. **脚本版本差异**：cqa1 缺少 `--k_ratio` CLI 参数、`random_prune` mode、offset-based hook
2. **Checkpoint 一致**：两边 size 均为 1,211,985,753 bytes
3. **Config 一致**：k_ratio=0.5，其余参数相同

### 修复

将 westd 上最新的 `eval_success_rate_libero.py` 同步到 cqa1，重跑 supplement 实验即可。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "offset": 0
  }
}
```

</details>

---
