# analysis openvla entropy real libero

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_openvla_entropy_real_libero_20260518T051251_result.json`
- **Structured JSON:** [`799510c473043b0213a5.json`](../../sessions/79/799510c473043b0213a5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**服务器 `westd-27271` 无法连接**（端口 27271 不可达）。实例可能已关机。

**脚本已写好**，保存在本地 `measure_openvla_entropy_real.py`。与之前 20 张随机噪声图的版本相比，关键改进：

1. **真实 LIBERO-Object 图像**：从 HDF5 文件中加载 `agentview_rgb`，每个 task 采样 25 帧，覆盖全部 10 个 task = ~250 张
2. **任务相关 prompt**：根据 task 名匹配真实任务描述（而非固定 prompt）
3. **输出格式**：按你要求的 JSON schema，包含 per-layer entropy ratio/std、vision attention fraction、对比数据

**需要你做的**：
1. 在 AutoDL/SeetaCloud 控制台启动 `westd-27271` 实例
2. 告诉我服务器已上线，我会立即部署脚本并运行

部署后执行命令：
```bash
source /root/miniconda3/bin/activate
cd /root/autodl-tmp/importance_margin_vla_compress
HF_HOME=/root/autodl-tmp/.hf_cache CUDA_VISIBLE_DEVICES=0 python measure_openvla_entropy_real.py
```

预计耗时：模型加载 ~2 分钟 + 250 张图前向传播（含 attention 输出） ~15-25 分钟。

---
