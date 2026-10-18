# code openvla vtc m64 prep 41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openvla_vtc_m64_prep_41074_20260519T212958_result.json`
- **Structured JSON:** [`b1176fe4f580c9386ef9.json`](../../sessions/b1/b1176fe4f580c9386ef9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

file-048 已到。4:30 经过，48/383 = 12.5%。时间线：
- 05:35:48 开始
- 05:40:14 到 file-048
- 速度: 48 文件 / 4.5 分 = ~10.7 文件/分
- 剩余 335 文件 ≈ 31 分钟
- 预计完成: ~06:11

数据集下载预计还需约 30 分钟。进程后台运行正常。让我先汇报当前状态，然后在数据下载完成后继续检查。

---

**当前进度汇总：**

### 已完成
1. **配置文件已创建**：
   - `configs/openvla_smart_compress_m64.yaml` (num_queries=64)
   - `configs/openvla_smart_compress_m32.yaml` (num_queries=32)
   - 以 M=128 为模板，无 lora 配置，output_dir 分别设为 `openvla_sc_m64` / `openvla_sc_m32`

2. **模型加载验证通过**：
   - OpenVLA loaded: 7,541,237,184 params
   - Freeze config: trainable=403,046,400 / total=7,944,283,584 (5.07%)
   - Compressor params: 403,046,400
   - VisionTokenCompressor 正确初始化

### 进行中
3. **数据集下载** (PID=49844, GPU 3)：
   - `HuggingFaceVLA/libero` 共 383 个 parquet 文件
   - 当前进度: ~48/383 (12.5%)
   - 预计完成时间: ~06:11 UTC
   - `source /etc/network_turbo` + `HF_HUB_DISABLE_XET=1` 已启用

### 待完成（数据集下载后）
- 确认训练 step 有 loss 输出
- kill dry-run 进程释放 GPU 3
- 输出正式启动命令

### 注意
- 脚本不接受 `--seed` 和 `--gpu` 参数（与任务描述中的命令不同）
- 需要 `--dry-run --max-steps N` 代替
- 不能设 `HF_HUB_OFFLINE=1`（数据集未缓存）
- **正式训练首次启动也不能 `HF_HUB_OFFLINE=1`**，缓存完毕后才可以

是否要等数据集下载完成后继续验证 dry-run，还是先做其他事情？

---
