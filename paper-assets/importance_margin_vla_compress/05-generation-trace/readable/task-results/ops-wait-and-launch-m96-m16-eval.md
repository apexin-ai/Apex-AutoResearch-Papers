# ops wait and launch m96 m16 eval

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_wait_and_launch_m96_m16_eval_20260518T035042_result.json`
- **Structured JSON:** [`d431877721d9b22a51da.json`](../../sessions/d4/d431877721d9b22a51da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务描述中的信息与服务器实际状态不匹配：

1. **训练 PID 350781 和 352025 不存在** — 在 `westd-27271` 上找不到这两个进程
2. **`eval_smart_compress_libero.py` 脚本不存在** — 服务器上没有任何 `smart_compress` 相关脚本
3. **`checkpoints/smart_compress_m96/` 和 `smart_compress_m16/` 不存在** — 没有这些 checkpoint 目录
4. **任务提到的服务器是 `cqa1-33015`**，但项目配置的服务器是 `westd-27271`

当前 `westd-27271` 上的 GPU 状态：
- GPU 0: 正在运行 `eval_openvla_libero.py --mode random_prune --k_ratio 0.7` (PID 755671)
- GPU 1: 正在运行 `eval_openvla_libero.py --mode random_prune --k_ratio 0.3` (PID 768729)
- GPU 2-3: 空闲

需要你确认：
- M=96/M=16 训练是否在另一台服务器 (`cqa1-33015`) 上？
- 还是任务描述中的脚本名/checkpoint 路径需要更正？

---
