# ops check pi05 download

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_pi05_download_20260522T135051_result.json`
- **Structured JSON:** [`36ca13b5403fa57b9d6c.json`](../../sessions/36/36ca13b5403fa57b9d6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果汇总

### 1. pi0.5 下载进度
- **状态**：正在下载中（gsutil -m 多进程并行）
- **进度**：10/16 files, 5.9 GiB / 11.6 GiB (51%)
- **速度**：~400 KiB/s（波动大，176~671 KiB/s）
- **ETA**：约 3-5 小时（按当前速度估算）
- **路径**：`/root/autodl-tmp/openpi_weights/pi05_libero/`

### 2. LIBERO assets
- **已就绪** ✓
- 位置：`/root/miniconda3/lib/python3.12/site-packages/libero/libero/assets/`
- 包含：`articulated_objects/`, `scenes/`, `textures/`, `turbosquid_objects/` 等完整资源
- 另有副本在 `/root/colliforce-vla/LIBERO/libero/libero/`

### 3. openpi serve_policy.py
- **已就绪** ✓
- `serve_policy.py`: `/root/autodl-tmp/openpi/scripts/serve_policy.py`
- `examples/libero/main.py`: `/root/autodl-tmp/openpi/examples/libero/main.py`

### 4. tmux sessions
- `a3_spatial` — 运行中（创建于 May 22 01:12）

### 5. GPU 状态
| GPU | 利用率 | 显存使用 | 总显存 |
|-----|--------|----------|--------|
| 0 | 100% | 23935 MiB | 97887 MiB |
| 1 | **0%** | **0 MiB** | 97887 MiB |

### 阻塞项
- **pi0.5 权重下载速度极慢**（~400KB/s），目前仅 51%，预计还需 3-5 小时完成。下载完成前无法启动 eval。GPU 1 空闲可用，不是瓶颈。

---
