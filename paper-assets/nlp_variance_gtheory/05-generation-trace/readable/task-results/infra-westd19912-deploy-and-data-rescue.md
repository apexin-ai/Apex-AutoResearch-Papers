# infra westd19912 deploy and data rescue

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd19912_deploy_and_data_rescue_20260521T161922_result.json`
- **Structured JSON:** [`bf0bd032d9e799f5378e.json`](../../sessions/bf/bf0bd032d9e799f5378e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 items 文件就绪。整体状态汇总：

---

## 状态汇总

### 1. westd-19912 环境
- **GPU**: 4× NVIDIA RTX PRO 6000 Blackwell (98GB each)
- **Python**: 3.12.3 (conda base)
- **关键包**: PyTorch 2.11.0, vLLM 0.21.0, transformers 5.9.0, accelerate 1.13.0, flashinfer 0.6.8
- **代码/数据**: 全部就绪（src, scripts, data, design matrices, items files）

### 2. 从 westd-15695 抢救的 exp001 数据
| 文件 | 行数 | 状态 |
|------|------|------|
| `exp001_olmo/olmo_mmlu.jsonl` | 86,400 | ✅ 已 scp 到 westd-19912 |
| `exp001_olmo/olmo_arc.jsonl` | 86,400 | ✅ 已 scp 到 westd-19912 |
| `exp001_yi/yi_mmlu.jsonl` | 86,400 | ✅ 已 scp 到 westd-19912 |

### 3. westd-15695 auto_chain 当前进度
- **OLMo GSM8K**: 73,600/86,400 (85.2%)，预计 ~15-20 分钟完成
- **接下来**: OLMo HellaSwag → **SKIP**（items 文件缺失）→ Yi ARC → Yi HellaSwag → **SKIP** → Yi GSM8K
- Yi ARC + Yi GSM8K 预计再需 1-2 小时

### 4. westd-19912 推理状态
- **auto_chain_19912.sh** 已在运行（PID 49266），等待模型下载
- **OLMo 模型下载**: 3 个 safetensors 并行下载中 (~36%，1.5-2 MB/s)，预计 **~30 分钟**完成
- **Yi 模型下载**: 4 个 safetensors 并行下载中 (~30%，1.5-2 MB/s)，预计 **~35 分钟**完成
- 模型就绪后 auto_chain 自动开始：
  - **Phase A (OLMo)**: Round 1: MMLU+ARC+HellaSwag+GSM8K (4 GPU 并行) → Round 2: MATH (1 GPU)
  - **Phase B (Yi)**: Round 1: MMLU+ARC+HellaSwag+GSM8K (4 GPU 并行) → Round 2: MATH (1 GPU)

### 5. 模型
- 通过 ModelScope 下载到 `/root/autodl-tmp/.hf_cache/{org}/{model}`
- OLMo: `allenai/OLMo-2-1124-7B-Instruct` (~13.6 GB)
- Yi: `01ai/Yi-1___5-9B-Chat` (~16.5 GB)

### 6. exp002 设计
- 每模型 1440 条件（每 benchmark 288 条件 × 200 items = 57,600 行/benchmark）
- 5 benchmarks: MMLU, ARC, HellaSwag, GSM8K, MATH

### 7. 预计时间线
- **~00:55 (15 min)**: westd-15695 OLMo GSM8K 完成 → 追加 scp
- **~01:15 (35 min)**: westd-19912 模型下载完成 → auto_chain 自动启动 OLMo Round 1
- **~01:30 - 02:30**: westd-15695 Yi ARC + Yi GSM8K 完成 → scp
- **~03:00 - 05:00**: westd-19912 OLMo 全部完成 → Yi 开始
- **~06:00 - 08:00**: westd-19912 所有推理完成

### 待办
- OLMo GSM8K 完成后从 westd-15695 再次 scp（以及后续 Yi ARC, Yi GSM8K）
- 监控 westd-19912 auto_chain 启动和推理进度

---
