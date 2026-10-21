# infra bjb1 exploration

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_bjb1_exploration_20260521T211104_result.json`
- **Structured JSON:** [`4704bd027366df21d473.json`](../../sessions/47/4704bd027366df21d473.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

探查完成。汇总如下：

---

## bjb1-17606 资源探查报告

### 1. GPU 状态
| GPU | 型号 | 显存 | 已用 | 利用率 |
|-----|------|------|------|--------|
| cuda:0 | RTX PRO 6000 Blackwell | 96GB | **0 MiB** | **0%** |
| cuda:1 | RTX PRO 6000 Blackwell | 96GB | **0 MiB** | **0%** |

两块 GPU 完全空闲。

### 2. 磁盘
| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| 根分区 `/root` | 30GB | 8.4GB | 22GB | 28% |
| 数据盘 `/root/autodl-tmp` | 250GB | 171GB | 80GB | 69% |

### 3. 异常进程
- **zombie ray::TaskRunner** (PID 337402): CPU 66.5%，RAM 8.4GB，**无 GPU 占用**。来自 exp029 训练崩溃（CUDA OOM at `loss.backward()`）。
- **defunct wandb-core** (PID 337879): 僵尸进程。
- **checkpoint_watchdog.sh**: 仍在运行，监控已结束的 exp029-seed4。
- 这些都是可清理的孤儿进程。

### 4. 可用 Checkpoint 列表

| Checkpoint | 路径 | 大小 | 格式 | 可直接推理? |
|---|---|---|---|---|
| exp021_ragen_sft_v4/final | `.../exp021_ragen_sft_v4/final/` | ~8GB | HF safetensors | **是** |
| exp021_ragen_sft_v4/checkpoint-160 | `.../exp021_ragen_sft_v4/checkpoint-160/` | ~8GB | HF safetensors | **是** |
| exp021_ragen_sft_v4/checkpoint-320 | `.../exp021_ragen_sft_v4/checkpoint-320/` | ~8GB | HF safetensors | **是** |
| **exp029-seed4/global_step_15_hf** | `.../exp029-seed4/global_step_15_hf/` | ~4GB | **HF safetensors** | **是** |
| exp029-seed4/global_step_15/actor | `.../exp029-seed4/global_step_15/actor/` | ~12GB | FSDP sharded .pt | 否，需转换 |
| exp029-seed7-high-kl/global_step_5/actor | `.../exp029-seed7-high-kl/global_step_5/actor/` | 21GB | FSDP sharded .pt | **否，需转换** |
| exp029-seed7-high-kl/global_step_7/actor | `.../exp029-seed7-high-kl/global_step_7/actor/` | 21GB | FSDP sharded .pt | **否，需转换** |
| scienceworld_sft/huggingface | `.../scienceworld_sft/huggingface/` | 7.6GB | HF safetensors (2-shard) | **是** |

注意：exp029-seed7-high-kl 的 huggingface 子目录只有 tokenizer 文件，**缺少 model weights**，HF 转换未完成。

### 5. 评估脚本和数据
- **ScienceWorld eval 脚本**: `eval_scienceworld.py`, `eval_scienceworld_info_loss.py`, `eval_per_task_type.py` ✅
- **通用 checkpoint eval**: `scripts/eval_checkpoint.py`, `scripts/eval_checkpoint_full_context.py` ✅
- **FSDP→HF 转换工具**: `scripts/convert_fsdp_to_hf.py`（CPU-only，不需 GPU）✅
- **ALFWorld valid_unseen 数据**: `/root/autodl-tmp/alfworld/json_2.1.1/valid_unseen/` (~2.2GB, 约70+个task) ✅
- **最近评估结果**: scienceworld_sft 已完成 ScienceWorld dev 评估（full context: 34.83%, h=2: 4.49%）

### 6. 建议：可立即执行的任务

**优先级排序：**

1. **清理孤儿进程** — kill PID 337402 (ray) 和 337879 (wandb)，释放 8.4GB RAM
2. **转换 exp029-seed7-high-kl 的 FSDP checkpoint 到 HF 格式** — 用 `convert_fsdp_to_hf.py`，CPU-only 无需 GPU，两个 step (5, 7) 都转
3. **跑 OOD eval** — exp029-seed4/global_step_15_hf 已经是 HF 格式，可立即用于评估。但需确认是用 ALFWorld OOD eval 还是 ScienceWorld eval（当前脚本是 ScienceWorld 的）
4. **exp029-seed7-high-kl 转换完成后也跑 eval** — 对比不同 seed/KL 设置的效果

**关键疑问（需要你确认）：**
- 目标 OOD eval 是 ALFWorld 还是 ScienceWorld？当前服务器上只有 ScienceWorld eval 脚本，没看到 ALFWorld 专用 eval 脚本
- exp029-seed4 step 15 是否已经完成过 eval？如果没有，这是最快能跑起来的任务

---
