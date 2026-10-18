# code c4ext fix pathB westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c4ext_fix_pathB_westd41074_20260519T182128_result.json`
- **Structured JSON:** [`269d72a58814e28135f7.json`](../../sessions/26/269d72a58814e28135f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-27271 上 Path A 正在运行 dry-run（`--dry-run` 模式），还不是正式训练。GPU 内存未被占用（仅 3 MiB）。

## 汇报

**westd-41074 状态：**
- 训练进程已死，4x 97GB GPU 全部空闲
- 崩溃原因确认：`httpx.ConnectError: Network is unreachable`（lerobot 的 `get_safe_version` 调用 HF Hub API）
- **网络已修复**：通过 `source /etc/network_turbo` + SSL 证书配置，HF Hub 已可达（HTTP 200）
- 代码和配置文件完好：`train_openvla_smart_compress.py` 和 `configs/openvla_smart_compress_m128.yaml` 均在

**westd-27271 (Path A) 状态：**
- 正在执行 dry-run（PID 836910），尚未开始正式训练
- 2x 97GB GPU 空闲

**问题：`submit_training_job` 工具不可用。** 当前 MCP 工具集中没有此工具，无法按规范提交训练任务。需要你提供该工具，或授权使用 `ssh_execute` + tmux 方式启动训练。

**重启命令已就绪，待授权后可执行：**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/autodl-tmp/importance_margin_vla_compress && \
export HF_HUB_OFFLINE=1 && \
export HF_HOME=/root/autodl-tmp/.hf_cache && \
python train_openvla_smart_compress.py --config configs/openvla_smart_compress_m128.yaml --seed 42
```

---
