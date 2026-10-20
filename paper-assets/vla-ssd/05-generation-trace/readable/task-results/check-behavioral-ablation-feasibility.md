# check behavioral ablation feasibility

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_behavioral_ablation_feasibility_20260524T001923_result.json`
- **Structured JSON:** [`c20c07e9c8ed40ed82b4.json`](../../sessions/c2/c20c07e9c8ed40ed82b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

## 环境检查结果

### 1. LIBERO simulator: ✅
- **conda env `libero`** (`/root/miniconda3/envs/libero`, Python 3.10) 已安装:
  - `robosuite` ✅
  - `mujoco` ✅
  - `torch 2.12.0+cu130` ✅
  - `transformers` ✅
  - `accelerate` ✅
  - `timm` ✅
  - `PIL` ✅
- **flash_attn**: ❌ 未安装（OpenVLA 加载可能需要，可 fallback 到 eager attention）
- LIBERO 源码: `/root/autodl-tmp/LIBERO/libero/`，含完整 envs/benchmark/utils
- **注意**: nora venv 不含模拟器依赖，必须用 libero conda env

### 2. OpenVLA checkpoint: ✅
- 路径: `/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-finetuned-libero-goal/`
- 4 个 safetensors shard（~14.5GB 合计），config.json 完整
- 模型架构: `OpenVLAForActionPrediction`，Llama-2-7B backbone
- 包含 libero_goal norm_stats（428 trajectories, 52042 transitions）
- 自带 `configuration_prismatic.py` + `modeling_prismatic.py`

### 3. Rendering: ✅ (EGL)
- **EGL**: ✅ 有 NVIDIA EGL (`libEGL_nvidia.so`)
- **OSMesa**: ❌ 不存在（不需要，EGL 足够）
- **Xvfb**: ❌ 不存在（不需要，用 `MUJOCO_GL=egl` 即可 headless 渲染）

### 4. GPU: ✅✅
- **2x NVIDIA RTX PRO 6000 Blackwell, 98GB VRAM each**
- cuda:0 空闲, cuda:1 空闲
- CUDA 13.0, Driver 580.82.09

### 5. LIBERO-Goal 任务定义: ✅
- `/root/autodl-tmp/LIBERO/libero/libero/bddl_files/libero_goal/` 含 10 个 `.bddl` 文件
- 完整覆盖全部 10 个 LIBERO-Goal tasks

### 6. 现有 ablation 脚本: ❌
- 已有 attention 分析脚本（probing/counterfactual/bootstrap），但**没有 rollout/behavioral evaluation 脚本**
- 需要从零编写：模型加载 → attention head ablation → LIBERO env rollout → success rate 统计

### 7. 磁盘: ⚠️
- 数据盘 250GB，已用 207GB，剩余 44GB — 够用但不富裕

---

## 可行性评估

| 项目 | 估算 |
|------|------|
| GPU 显存 | OpenVLA-7B bf16 ≈ 14-15GB VRAM，单卡 98GB 绰绰有余 |
| 单 episode 时间 | ~30-60s（300 step horizon，每步 forward pass ~0.1-0.2s） |
| 10 tasks × 10 episodes | ~50-100 min per condition |
| ablated + intact 对比 | ~2-3 小时总计 |

## 总体判断: **可行**

**需要做的搭建工作**（预计 2-3 小时开发 + 调试）:
1. **写 rollout 脚本**: 加载 OpenVLA checkpoint → hook L1 attention → ablate top-24 instruction-dominant heads → LIBERO env rollout → 记录 success rate
2. **安装 flash-attn**（可选，若 eager attention 加载失败则需要）
3. **确认 libero conda env 下 LIBERO import 正常**（源码已有但需确认 `pip install -e .` 是否已执行）
4. 设置 `MUJOCO_GL=egl` 环境变量

硬件和核心依赖全部就绪，主要工作量在编写 behavioral evaluation 脚本。

---
