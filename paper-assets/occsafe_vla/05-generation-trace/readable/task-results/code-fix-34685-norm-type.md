# code fix 34685 norm type

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_34685_norm_type_20260525T134505_result.json`
- **Structured JSON:** [`76bacd68f9eb68195ba1.json`](../../sessions/76/76bacd68f9eb68195ba1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。汇报：

### 34685 代码版本
**v2**（已有 `occ_detach`、`DepthHead`、`clean_cutoff` 等 v2 特性），仅缺 `occ_norm_type` 一个字段。`occ_head.py` 已支持 `norm_type` 参数（line 15, 23），无需同步。

### 修改内容（finetune.py 两处）
1. **line 98**：在 `occ_detach` 和 `occ_resolution` 之间添加配置定义：
   ```python
   occ_norm_type: str = "bn"  # Norm type for occ head: "bn" (BatchNorm) or "ln" (GroupNorm-1 = LayerNorm)
   ```
2. **line 1018**：BEVOccupancyHead 实例化 dict 中添加：
   ```python
   "norm_type": cfg.occ_norm_type,
   ```

### 验证结果
- draccus 可正确解析 `--occ_norm_type ln` 和 `--occ_detach true`
- 两处修改与 10894 完全一致
- `occ_head.py` 无需同步（34685 已有 `norm_type` 支持）
- `--help` 的 `ValueError` 是两台服务器共有的预存 bug（与本次修改无关）

---
