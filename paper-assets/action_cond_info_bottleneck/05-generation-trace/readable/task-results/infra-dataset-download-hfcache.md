# infra dataset download hfcache

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_dataset-download-hfcache_20260515T210203_result.json`
- **Structured JSON:** [`9a083a3a5d8d6dab2e0f.json`](../../sessions/9a/9a083a3a5d8d6dab2e0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。

**结果汇总：**

1. **LeRobotDataset 支持 `root` 参数** — v0.5.1 支持，`train_acib_libero.py` 已使用
2. **方案：symlink + 删 legacy cache**
   - 创建 symlink：`/root/autodl-tmp/.hf_cache/lerobot/lerobot/libero/ → /root/autodl-tmp/libero_dataset/`
   - 删除了 `.cache/huggingface/download/` 目录（legacy hub metadata 触发强制 re-fetch）
3. **无需下载** — 数据已完整在本地（v3.0 格式，1693 episodes，273,465 frames）
4. **验证结果**：
   - `LeRobotDataset('lerobot/libero')` 无参加载 ✓
   - `LeRobotDataset('lerobot/libero', root=...)` 显式路径 ✓
   - DataLoader 输出 shapes 正确：images `[B,3,256,256]`、state `[B,8]`、action `[B,7]`、task 为 string list ✓

`train_acib.py` 可直接使用 `LeRobotDataset("lerobot/libero")` 加载，无需代码修改。

---
