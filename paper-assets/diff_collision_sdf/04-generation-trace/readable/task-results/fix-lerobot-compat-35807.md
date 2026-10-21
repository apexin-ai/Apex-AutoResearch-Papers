# fix lerobot compat 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_lerobot-compat-35807_20260529T034201_result.json`
- **Structured JSON:** [`3dd119ee87195e8a68b0.json`](../../sessions/3d/3dd119ee87195e8a68b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常运行。

## 总结

**1. LeRobot 版本**：两台都是 0.1.0，版本相同。

**2. 根因**：westd-45947 之前已手动 patch 了 3 处 LeRobot 代码以兼容新版 HF datasets API，但 westd-35807 没有这些 patch：
- `lerobot_dataset.py:508-509` — `torch.stack(hf_dataset["timestamp"])` 改为 `np.array(to_dict()["timestamp"])`
- `lerobot_dataset.py:511` — `check_timestamps_sync` 用 try/except 包裹（object_pudding 数据集 timestamp 不符合严格校验）
- `utils.py:272` — `hf_transform_to_torch` 增加 `dict` + `"bytes"` 类型处理（图像以 bytes dict 存储）
- `lerobot_dataset.py:698` — `_query_hf_dataset` 整个方法重写，处理多种数据类型

**3. 修复方案**：方案 B — 把 westd-45947 上的 4 处 patch 逐一移植到 westd-35807。

**4. 训练状态**：
- PID: 93395，运行 1 分 50 秒，状态 S（正常）
- GPU 0: 利用率 100%，显存 19061 MiB / 97887 MiB
- 已完成 step 0-8，loss ~0.10-0.15，速度 ~1.5s/it，预计 ~12.5h 完成 30000 steps

---
