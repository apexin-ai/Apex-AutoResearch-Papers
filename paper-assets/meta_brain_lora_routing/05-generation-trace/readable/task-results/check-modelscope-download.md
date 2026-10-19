# check modelscope download

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_modelscope_download_20260516T141435_result.json`
- **Structured JSON:** [`5eeb0ef1cfd612e1e526.json`](../../sessions/5e/5eeb0ef1cfd612e1e526.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 1. ModelScope 下载状态

**进程 637101** — `modelscope snapshot_download('lerobot/pi0_libero')` 正在运行中：
- 目标：`/root/autodl-tmp/.ms_cache/`
- 日志显示 `model.safetensors`: **92% (6.01G/6.53G)**，速度 ~390 KB/s
- 已跑 4h19m，剩余约 **23-25 分钟**完成

**进程 713512** — `huggingface_hub snapshot_download('lerobot/pi0_libero_finetuned')` 也在运行：
- 目标：`/root/autodl-tmp/checkpoints/pi0_libero_finetuned/`
- `model.safetensors` 已有 6.6G，看起来已下载完成（文件时间戳 21:13 已停止增长）
- 还包含 preprocessor 和 postprocessor safetensors 文件

### 2. wget hf-mirror 进程

**已清理。** 无任何 wget 进程在运行。

### 3. 已下载 checkpoint 汇总

| 模型 | 路径 | 大小 | 状态 |
|------|------|------|------|
| `lerobot/pi0_base` | `/root/autodl-tmp/.ms_cache/lerobot/pi0_base/` | 14G (model.safetensors) | ✅ 完成 |
| `lerobot/pi0_libero` | `/root/autodl-tmp/.ms_cache/lerobot/pi0_libero/` | 6.01G/6.53G | ⏳ 92%, ~25min 剩余 |
| `lerobot/pi0_libero_finetuned` | `/root/autodl-tmp/checkpoints/pi0_libero_finetuned/` | 6.6G + preprocessors | ✅ 完成 |

---
