# ops gpu2 openvla fix attempt

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu2_openvla_fix_attempt_20260525T231108_result.json`
- **Structured JSON:** [`30d31a9083fa86418c98.json`](../../sessions/30/30d31a9083fa86418c98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报结果：

## OpenVLA Eval 诊断结果: **NO** — 30 分钟内无法跑起来

### 1. 模型文件：不完整，无法加载
- **safetensors 下载未完成**：3 个 shard 文件均有 `.aria2` 控制文件残留，说明 aria2 下载中断，文件很可能是截断/损坏的
- **缺少关键文件**：`configuration_prismatic.py`、`modeling_prismatic.py`、tokenizer 系列文件全部缺失
- 目录中仅有：`config.json`、`generation_config.json`、3 个 safetensors shard、`model.safetensors.index.json`

### 2. Eval 脚本：不存在
- `eval_safelibero_openvla.py` 不存在
- 现有 `eval_safelibero.py` 仅支持 `baseline`/`a1`/`a3` 三种模型类型，全部基于 pi0 (openpi)，不支持 OpenVLA
- 代码库中无任何 openvla 或 prismatic 相关文件

### 3. 具体阻塞点
1. **模型需重新下载** — safetensors 损坏 + 缺少 6 个必要文件（约 15GB 总量，下载时间不可控）
2. **需从零写 eval 脚本** — OpenVLA 的推理接口（`AutoModelForVision2Seq` + `AutoProcessor`）与现有 pi0 架构完全不同，无法复用现有脚本，需要编写完整的 OpenVLA 推理 + SafeLIBERO 环境交互逻辑

---
