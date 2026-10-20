# code openvla extract script

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openvla-extract-script_20260515T071417_result.json`
- **Structured JSON:** [`98832f1d6be76af95eb7.json`](../../sessions/98/98832f1d6be76af95eb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

语法正确，argparse 正常。Checkpoint 还在下载（缺 shard 2，shard 1 大小异常），无法 dry-run。

脚本已更新到 `/root/vla-ssd/scripts/extract_features.py`，相比原版改动：

| 新增/改动 | 说明 |
|-----------|------|
| `HDF5_USE_FILE_LOCKING=FALSE` | 顶部设置，避免 HDF5 锁问题 |
| `--layers` | 支持 `0-32` 或 `0,5,10` 选择性提取，默认全 33 层 |
| `--task_instruction` | 覆盖自动推断的 task description |
| `--max_demos` 默认 50 | 原来是 None（全部） |
| `torch.amp.autocast` | forward pass 加 autocast 节省显存 |
| `f.attrs["layers"]` | HDF5 元数据记录提取了哪些层 |
| `--data_dir` 默认路径 | 改为 `/root/autodl-tmp/vla-ssd/data/libero/libero_10/` |
| docstring | 补充了输入/输出/依赖说明 |

输出格式与 `train_probes.py` 兼容（HDF5，每个 demo 组含 `last_preaction` (T, 33, 4096) 和 `image_mean` (T, 33, 4096)，fp16 + gzip）。等 checkpoint 下载完成后可用 `--max_demos 1` dry-run 验证。

---
