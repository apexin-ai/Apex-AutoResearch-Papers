# assess cqa1 utilization

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_assess_cqa1-utilization_20260519T141234_result.json`
- **Structured JSON:** [`ab7adc169287f54ae359.json`](../../sessions/ab/ab7adc169287f54ae359.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## cqa1-21977 可行性评估

### GPU Eval 可行性
| 项目 | 状态 |
|------|------|
| GPU | RTX 4090D 24GB, **完全空闲** (0MiB/24564MiB) |
| CUDA | 13.0, Driver 580.76.05 |
| PyTorch | 2.11.0+cu130 |
| Python | 3.12.3 (miniconda3) |
| transformers/peft | 已装 |
| evaluate.py | **旧版** (35855 bytes, v3 应为 37591) |
| 数据盘 | 818GB free (/dev/sda2) |
| 根分区 | 12GB free (overlay 30GB) |

**已有基础模型**: 0.5B, 1.5B, 3B (Qwen), Llama-3.2-3B, gemma-2-9b. **无 7B base model**（HF cache 只有 4KB 元数据）。

**已有 LoRA checkpoints**: 非常全面 —— 0.5B/1.5B/3B 全部 d000-d100 × s42/s123, 7B 全部 d000-d100 × s42/s123, Llama-3.2-3B, gemma-2-9b, 14B 部分。全部 alpha=32。

**已有 eval_results**: 覆盖面非常广（0.5B/1.5B/3B/7B/Llama/OLMo 多个 aligned/para_aligned 结果已存在）。

| 模型 | 能否 eval | 说明 |
|------|-----------|------|
| 0.5B / 1.5B / 3B | **可直接跑** | base model + adapters 都在 |
| Llama-3.2-3B | **可直接跑** | model 在 autodl-tmp/models |
| 7B | **需下载 base** (~14GB) | adapters 在，但 base model 缺失 |
| gemma-2-9b | **可跑** | 35GB model 在 |
| 14B | **不可行** | 24GB 显存不够 |

### CPU-bound 任务可行性
| 项目 | 状态 |
|------|------|
| CPU | 192 vCPUs (2× Xeon Platinum 8481C) |
| RAM | 1TB (944GB available) |
| numpy/scipy | 已装 |
| cmdstanpy | 已装 (可做 IRT fitting) |
| pymc | **未装** |

**结论: 极其适合 CPU-bound 任务。** 192 核 + 1TB RAM 跑 IRT fitting / bootstrap 统计检验绰绰有余。

### 建议

1. **立即可利用** — CPU-bound 分析（IRT 2PL+γ fitting via CmdStan, bootstrap TOST, 数据聚合）不需要任何额外配置
2. **低成本可用** — 0.5B/1.5B/3B eval 只需同步 evaluate.py 到 v3 版本
3. **7B eval** — 需先下载 Qwen2.5-7B base (~14GB), ModelScope 走国内 CDN 约 5-10 min
4. **须同步 evaluate.py** — 当前版本 35855 bytes ≠ v3 的 37591 bytes, git pull 即可
5. **14B** — 不可行 (OOM)

---
