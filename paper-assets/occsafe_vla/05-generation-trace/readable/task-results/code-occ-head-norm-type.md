# code occ head norm type

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_occ_head_norm_type_20260523T052405_result.json`
- **Structured JSON:** [`cd6b74d6cdd39548c210.json`](../../sessions/cd/cd6b74d6cdd39548c210.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。修改验证通过：

**改动汇总：**

1. **`prismatic/models/occ_head.py`** — `BEVOccupancyHead.__init__` 新增 `norm_type: str = "bn"` 参数。内部用 `_norm(channels)` 工厂函数：`"bn"` → `BatchNorm2d`，`"ln"` → `GroupNorm(1, channels)`（等价 LayerNorm）。

2. **`vla-scripts/finetune.py`** — `FinetuneConfig` 新增 `occ_norm_type: str = "bn"`（第96行），OccHead 实例化处传入 `"norm_type": cfg.occ_norm_type`（第1016行）。

**使用方式：** 训练时加 `--occ_norm_type ln` 即可启用 LayerNorm。默认行为不变。

---
