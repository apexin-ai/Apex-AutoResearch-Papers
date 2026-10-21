# prep exp008 binary probe

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_exp008-binary-probe_20260518T163308_result.json`
- **Structured JSON:** [`d2845398167e78b9a0d0.json`](../../sessions/d2/d2845398167e78b9a0d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

就绪状态评估完成。

## exp-008 就绪状态清单

| 项目 | 状态 | 详情 |
|------|------|------|
| **代码** | **不存在** | 无 `run_exp008_*` 或 `*binary_probe*` 相关文件 |
| **数据** | 就绪 | `directions.pt` 存在 (`d_syc: [36,2,4096]`, `d_gen: [36,2,4096]`)；`calibration_v2_1_expanded.jsonl` 和 `calibration_v2.jsonl` 都在 |
| **基础模型** | 就绪 | Qwen3-8B 已缓存 (`/root/autodl-tmp/.hf_cache/models--Qwen--Qwen3-8B`) |
| **DeBERTa NLI** | 就绪 | `cross-encoder/nli-deberta-v3-base` 已缓存 |
| **依赖** | 就绪 | trl 1.4.0, peft 0.19.1, transformers 4.57.6 |
| **GPU 3** | 空闲 | RTX 5090, 2MiB/32607MiB, 0% util |

## GPU 使用情况 (westd-28034)

- **GPU 0**: 21612/32607 MiB, 42% util (运行 python3 进程，可能是 exp-004)
- **GPU 1**: 空闲
- **GPU 2**: 空闲
- **GPU 3**: 空闲 ← 目标卡，可用

## 缺少内容

**唯一缺少的是 exp-008 训练脚本。** 需要创建：

1. **`training/run_exp008_binary_probe_penalty.py`** — 核心训练脚本，公式 `R_hat = R3 - lambda * S(t)`，其中 S(t) 是二元线性探针的 sycophancy 分数
2. **`training/launch_exp008.sh`** — 启动脚本 (参考 `launch_exp004.sh`，改为 `CUDA_VISIBLE_DEVICES=3`)

### 参考材料

- `training/run_exp004_act_baseline.py` (11240 bytes) — 类似 baseline 结构：LoRA + 自定义 loss，使用同样的 paired calibration 数据、同样的模型加载方式、同样的 `dcgrpo_trainer.py` 中的 `_resolve_transformer_layers`
- `training/dcgrpo_trainer.py` (29994 bytes) — 主 DC-GRPO trainer，包含方向投影等核心逻辑
- `data/directions.pt` — 包含 `d_syc` (sycophancy 方向) 和 `d_gen` (generalization 方向)，36 层 x 2 方向 x 4096 维

**不自行编写训练代码，等待 Agent 安排。**

---
