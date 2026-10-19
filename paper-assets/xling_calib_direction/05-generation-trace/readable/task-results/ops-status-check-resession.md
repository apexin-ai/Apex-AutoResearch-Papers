# ops status check resession

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status-check-resession_20260521T081427_result.json`
- **Structured JSON:** [`f6e1d5e9f7d7b9bafb72.json`](../../sessions/f6/f6e1d5e9f7d7b9bafb72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. Qwen3-235B-GPTQ-Int4 (ModelScope 下载)
- **进程**: PID 68080 存活，运行 32 分钟
- **大小**: 71G 已下载
- **safetensors**: 完成 13/32（其中 `._____temp/` 下有 8 个正在写入的临时文件）
- **日志**: 正在下载 `model-00011-of-00032.safetensors`，12% (449M/3.73G)，速度 2.18MB/s
- **预估**: 按当前速度，剩余约 19 个分片 × ~3.7GB ≈ 70GB，约 **9-10 小时**完成

### 2. Llama4-Scout-W4A16 (HF 下载)
- **进程**: PID 67791 存活，运行 34 分钟
- **大小**: 47G 已下载
- **safetensors**: 完成 8/14
- **日志**: 反复出现 **read operation timed out**（model-00011, model-00009），正在自动重试
- **状态**: 下载受 HF 网络超时影响，进度缓慢但进程仍在重试

### 3. Telugu GlobalMMLU
- **进程**: PID 67841 已结束
- **日志**: `Telugu loaded: 14042 samples` → **TE DOWNLOAD COMPLETE**
- **状态**: ✓ 完成

### 4. plan_013_v2 (probing_controls_v2)
- **进程**: PID 47972 存活，运行 **7 小时 18 分钟**，CPU 103%
- **输出**: results 目录下无 v2 文件（尚未写出最终结果）
- **日志**: 已完成 2/8 层的 probing：
  - Layer 0: CV AUROC=0.6304, Selectivity=+0.1297 (耗时 12719s ≈ 3.5h)
  - Layer 12: CV AUROC=0.6389, Selectivity=+0.1411 (耗时 9291s ≈ 2.6h)
- **预估**: 剩余 6 层，按平均速度约 **15-18 小时**完成

### 5. run_p0.sh
- **存在**: ✓ `/root/xling_calib_direction/code/run_p0.sh`，1762 字节，可执行权限

### 6. 磁盘
- **数据盘**: 350G 总量，已用 206G (59%)，剩余 **145G**
- **models 目录**: 148G
- Qwen3 完整约 130G + Llama4 完整约 80G → 两个都下完后 models 约 210G+，磁盘可能紧张（剩余 145G 可能不够 Qwen3 剩余的 ~60G + Llama4 剩余的 ~30G ≈ 90G，勉强够）

---
