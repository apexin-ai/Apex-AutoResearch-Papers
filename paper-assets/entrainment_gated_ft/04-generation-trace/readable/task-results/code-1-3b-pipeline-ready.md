# code 1 3b pipeline ready

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_1_3b-pipeline-ready_20260518T084744_result.json`
- **Structured JSON:** [`bfc96846ad3d9f01900f.json`](../../sessions/bf/bfc96846ad3d9f01900f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 产出汇总

### 1. 下载进度报告

| 模型 | 状态 | 已下载 | 预期总大小 | 进度 |
|------|------|--------|-----------|------|
| **transformer_1.3B_baseline** | 下载中 | 93MB | ~4.6GB | ~2% |
| **1.3B-100B-GatedDeltaNet-hybrid-3-1** | 下载中 | 215MB (2 shards) | ~5.6GB | ~4% |
| **1.3B-100B-GatedDeltaNet-pure** | 下载中 (hf cli) | 3.5MB (仅 config/tokenizer) | ~5.6GB | <1% |
| **1.3B-100B-RetNet-pure** | 下载中 | 275MB (2 shards) | ~5.2GB | ~5% |
| 其余 12 个模型 | 未开始 | 0 | - | 0% |

**活跃下载进程:**
- `hf download` 在拉 GatedDeltaNet-pure
- 多个 `wget` 并行拉 GatedDeltaNet-hybrid-3-1 shard2、RetNet-pure shard1、transformer_1.3B_baseline
- `dl_sequential.sh`、`dl_dual.sh`、`dl_hf_channel.sh` 三个下载调度脚本在运行
- `conda install aria2` 仍在安装中

**磁盘**: 22GB/250GB used (充裕)

### 2. FLA 1.3B 加载测试

**无法执行** - 目前没有任何一个模型完成下载（所有 safetensors 文件都是部分下载状态）。最早可测试的模型预计是 transformer_1.3B_baseline 或 GatedDeltaNet-hybrid-3-1。

### 3. 推荐 batch_size

- 1.3B bf16 模型: ~2.6GB VRAM
- 可用 VRAM: 94GB - 2.6GB = ~91GB
- 脚本默认 `BATCH_SIZE=32`（保守安全值）
- 如果不 OOM 可尝试 `BATCH_SIZE=48` 或 `BATCH_SIZE=64`

### 4. run_mvp_1.3b.sh 已部署

路径: `/root/entrainment_gated_ft/scripts/run_mvp_1.3b.sh`

关键特性:
- 自动跳过未下载/下载不完整的模型（检查 safetensors > 100MB）
- 模型目录名已按实际 ls 结果修正（去掉了 `New-`、`-baseline` 等任务中的不匹配后缀）
- 支持 `BATCH_SIZE`/`NUM_SAMPLES`/`DEVICE` 环境变量覆盖
- 支持传入指定模型路径只跑子集

**模型到位后一行启动:**
```bash
bash /root/entrainment_gated_ft/scripts/run_mvp_1.3b.sh
```

---
