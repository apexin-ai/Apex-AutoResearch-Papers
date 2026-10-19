# data download 4090x4

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_download-4090x4_20260513T043525_result.json`
- **Structured JSON:** [`9374c7ffd9b1155b83eb.json`](../../sessions/93/9374c7ffd9b1155b83eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载速度缓慢但在推进（3.8→4.0GB）。94GB 预计需要 1-2 小时。

**当前状态报告：**

### Part 1: SmolVLA 模型 ✅ 完成
- **路径**：`/root/autodl-tmp/models/SmolVLA/lerobot/smolvla_base/`
- **大小**：873MB
- **文件**：config.json, model.safetensors, policy_preprocessor/postprocessor 等齐全
- **格式**：LeRobot 专用格式（type: smolvla），底层 VLM 为 `SmolVLM2-500M-Video-Instruct`
- **注意**：需要 `lerobot` 库加载，不能用 `AutoModelForVision2Seq`

### Part 2: LIBERO 数据集 ⏳ 下载中
- **仓库**：`yifengzhu-hf/LIBERO-datasets`（原 `openvla/libero_data` 不存在/需认证）
- **路径**：`/root/autodl-tmp/libero_data/`
- **进度**：~4GB / ~94GB（5 个 suite，130 个 hdf5 文件）
- **PID**：3159
- **预计时间**：1-2 小时

### 轮询命令
```bash
# 进度
du -sh /root/autodl-tmp/libero_data/
# 已完成的 hdf5 文件数
find /root/autodl-tmp/libero_data/ -name "*.hdf5" -type f | wc -l
# 进程状态
ps -p 3159 -o pid= 2>/dev/null && echo "RUNNING" || echo "DONE"
# 日志最后几行
tail -3 /tmp/libero_download.log
```

### 遇到的问题
1. **`openvla/libero_data` 401 错误**：该 repo 不存在或需认证，改用 `yifengzhu-hf/LIBERO-datasets`
2. **SmolVLA 加载**：非标准 HF 模型，需 lerobot 库
3. **下载速度**：AutoDL 代理下载 HF 大文件偏慢（~10-30MB/s），但稳定推进

---
