# code next pipeline prep and download check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_next_pipeline_prep_and_download_check_20260521T025805_result.json`
- **Structured JSON:** [`2616a723d5918091806c.json`](../../sessions/26/2616a723d5918091806c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有脚本验证通过。汇总报告：

---

## 汇总报告

### Part A: 下载进度

| 项目 | 状态 | 详情 |
|------|------|------|
| **Phi-3-Vision base** | ~60% 下载中 | PID 524060 已结束。两个并行下载在跑：HF (PID 521338, 52% 但频繁超时) + **ModelScope (PID 521488, 58%, 8.5GB)**。ModelScope 是主力 |
| **OpenVLA-OFT checkpoint** | ~75% 下载中 | aria2c (PID 522184) 下载 `openvla-7b-oft-finetuned-libero-10` 到 14GB/~19GB。3 个 .safetensors 文件有 .aria2 标记（未完成），model-00004 尚未出现 |
| **NORA Goal checkpoint** | ~70% 下载中 | aria2c (PID 523735) 下载 model-00002-of-00002.safetensors，当前 2.4G。model-00001 (4.7G) 已完成。总计 7.1GB |
| **LIBERO-Long demo data** | **已有（以 libero_10 命名）** | `/root/autodl-tmp/vla-ssd/data/libero/libero_10/` 已有 10 个 hdf5 文件，即 LIBERO-Long。`libero_long/` 目录不存在但不需要下载，libero_10 = libero_long |

### NORA Goal Pipeline 状态

**已崩溃（EXIT_CODE=2）**。日志显示：
```
nora_goal_full_pipeline.py: error: unrecognized arguments: untrained
```
启动命令传了位置参数 `untrained`，但脚本期望 `--conditions trained,untrained` 格式。需要用正确参数重启。

### 当前活跃任务
- **OpenVLA Object pipeline** (tmux `libero_object_full_pipeline`, GPU:0)
- **TraceVLA Spatial trained** (PID 521842, GPU:1)

### Part B: 新建脚本

| 脚本 | 路径 | 基于 | 关键修改 |
|------|------|------|----------|
| NORA Spatial | `/root/autodl-tmp/vla-ssd/scripts/nora_spatial_full_pipeline.py` | nora_goal | DATA→libero_spatial, CKPT→nora-libero-spatial, spatial tasks/paraphrases |
| TraceVLA Object | `/root/autodl-tmp/vla-ssd/scripts/tracvla_object_full_pipeline.py` | tracvla_spatial | DATA→libero_object, object tasks/paraphrases, 同 checkpoint |
| OpenVLA Long | `/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py` | libero_object | CKPT→openvla-7b-oft-finetuned-libero-10, DATA→libero_10, 手写 INSTRUCTIONS（剥离 scene 前缀） |

### 注意事项

1. **NORA Spatial checkpoint `nora-libero-spatial/` 尚不存在**，需要从 HuggingFace 下载（`declare-lab/nora-long-finetuned-libero-spatial` 或类似名称）
2. **OpenVLA Long 脚本可能需要调整模型加载逻辑**：OFT 模型有 LoRA adapter + 独立 action_head，与标准 OpenVLA 加载方式不同。`UNNORM = "libero_10"` 键名需等 `dataset_statistics.json` 确认
3. **NORA Goal pipeline 需要用正确参数重启**：`python nora_goal_full_pipeline.py --conditions trained,untrained`

---
