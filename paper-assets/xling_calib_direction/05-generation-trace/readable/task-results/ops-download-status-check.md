# ops download status check

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_download-status-check_20260521T081000_result.json`
- **Structured JSON:** [`0f19598a76f748ab4a2f.json`](../../sessions/0f/0f19598a76f748ab4a2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

### 1. Qwen3-235B GPTQ-Int4 (ModelScope 下载)
- **进程**: PID 68080 **存活**，已运行 **28 分钟**
- **已下载**: **70GB**，14 个文件（共 32 个 safetensors）— 已完成 shard 1-6, 9, 13
- **当前进度**: shard 7/32 下载中 (92%, 3.42G/3.73G)，shard 10/32 刚开始 (2%)
- **下载速度**: ~2-3 MB/s
- **预估**: 还剩约 18 个 shard，按当前速度约需 **3-5 小时**

### 2. Llama4 Scout W4A16 (HF 下载)
- **进程**: PID 67791 **存活**，已运行 **30 分钟**
- **已下载**: **47GB**，8/14 个 safetensors（缺 4, 9, 11, 12, 13, 14）
- **⚠️ 问题**: 日志显示 shard 11 和 12 反复超时（`The read operation timed out`），正在自动重试
- **风险**: HF 下载无认证（未设 HF_TOKEN），限速；超时可能导致长时间卡住

### 3. Telugu GlobalMMLU 下载
- **进程**: PID 67841 **已结束**
- **状态**: ✅ **下载完成** — 日志显示 "TE DOWNLOAD COMPLETE"，Telugu 14042 samples 已加载

### 4. plan_013_v2 (probing_controls_v2)
- **进程**: PID 47972 **存活**，已运行 **7 小时 14 分钟**
- **输出**: results 目录中 **无 probing_controls_v2 文件/目录**。仅有旧的 `probing_controls_DEPRECATED.csv`
- **⚠️ 注意**: 运行超 7 小时但无输出文件，可能还在计算中或结果写到其他位置

### 5. run_p0.sh
- **状态**: ✅ **存在** — `/root/xling_calib_direction/code/run_p0.sh`
- **内容**: 完整的 P0 pipeline 脚本（extract_activations → train_probes），支持 model_name / model_path / gpu_ids 参数

### 6. 磁盘空间

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根分区 `/` | 30G | 1.4G | 29G | 5% |
| 数据盘 `/root/autodl-tmp/` | 350G | 204G | **147G** | 59% |

模型占用明细：
| 目录 | 大小 |
|------|------|
| Qwen3-235B-GPTQ-Int4 | 70G (下载中) |
| Llama4-Scout-W4A16 | 47G (下载中) |
| Qwen (旧模型) | 15G |
| LLM-Research | 15G |

Qwen3 最终约 ~130-140GB，Llama4 约 ~65GB。下载完成后数据盘预计用到 ~280G，剩余约 70G，空间足够。

### 需关注的问题
1. **Llama4 下载超时重试** — HF 无认证下载在 AutoDL 上不稳定，如果持续超时可能需要切换到 ModelScope 或设置 HF_TOKEN
2. **probing_controls_v2 运行 7h+ 无输出** — 建议查看该进程的 stdout/log 确认是否正常推进

---
