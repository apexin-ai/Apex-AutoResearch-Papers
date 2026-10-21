# ssh fix sdf gt naming

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_sdf_gt_naming_20260521T072247_result.json`
- **Structured JSON:** [`e0d8963858f3b21719be.json`](../../sessions/e0/e0d8963858f3b21719be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部确认完毕。报告如下：

---

### 1. SDF GT 引用逻辑

代码使用 **显式映射表**（`SCENE_CONFIG` 字典），不是按场景名拼接路径。`object_pudding` 场景直接映射到 `sdf_gt_object_chocolate.npz`：

```python
# train_a3_hook.py:61-65, train_a1_sdf_aux.py:42-45
"object_pudding": {
    "sdf_gt": "/root/colliforce-vla/data/sdf_gt_object_chocolate.npz",
    ...
}
```

`eval_safelibero.py` 通过 `--sdf_gt_path` CLI 参数传入，不走映射表。

### 2. 命名修复

**不需要修复。** 不存在 `sdf_gt_object_pudding.npz` 也没关系——代码从不引用这个文件名。无需 symlink 或 rename。

### 3. 文件状态

**两台服务器已有完全一致的文件，无需传输：**

| 文件 | westd-35807 | westd-45947 |
|------|------------|------------|
| `sdf_gt_object_chocolate.npz` | 114882 bytes | 114882 bytes |
| `sdf_gt_spatial_bowl.npz` | 114658 bytes | 114658 bytes |

### 4. 验证结果

两台服务器均可正常加载 `sdf_gt_object_chocolate.npz`：
- Keys: `['query_points', 'sdf_values']`
- Shapes: `query_points (4084, 3)`, `sdf_values (4084,)`

**结论：问题不存在。** 之前猜测 westd-35807 缺少 object_pudding 的 SDF GT 是误判——该文件名为 `sdf_gt_object_chocolate.npz`，两台服务器都有。

---
