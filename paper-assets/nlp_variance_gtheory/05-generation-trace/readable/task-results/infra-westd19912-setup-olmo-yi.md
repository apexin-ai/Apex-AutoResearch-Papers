# infra westd19912 setup olmo yi

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd19912_setup_olmo_yi_20260521T155931_result.json`
- **Structured JSON:** [`c400052a309f38ce34f5.json`](../../sessions/c4/c400052a309f38ce34f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-19912 环境搭建 + 推理部署完成

### 环境确认
| 组件 | 版本 |
|------|------|
| Python | 3.12.3 (miniconda3) |
| PyTorch | 2.11.0+cu130 |
| CUDA | 12.8 |
| vllm | 0.21.0 |
| transformers | 5.9.0 |
| flashinfer | 0.6.8.post1 (sm120 warning only, non-blocking) |
| GPU | 4× RTX PRO 6000 Blackwell 94GB |

### 代码同步
通过 westd-32570 → westd-19912 SSH key SCP 完成。所有 src/、data/、scripts/ 已就位。

### 设计矩阵
生成 `design_matrix_olmo.csv` 和 `design_matrix_yi.csv`，各 1440 conditions（288/benchmark × 5 benchmarks），condition_id 从 5761 开始。

### 模型下载（进行中）
- **OLMo-2-1124-7B-Instruct**: shard 3/3 @ 11%，~3.3MB/s，预计 ~20 min
- **Yi-1.5-9B-Chat**: shard 1/4 @ 6%，~1.4MB/s，预计 ~3.5h

### 自动接力脚本（PID 49261，已启动）
```
Phase A: 等待 OLMo 下载 → 4 GPU 并行 (mmlu/arc/hellaswag/gsm8k) → MATH
Phase B: 等待 Yi 下载 → 4 GPU 并行 (mmlu/arc/hellaswag/gsm8k) → MATH
```
`VLLM_USE_FLASHINFER_SAMPLER=0` 已设置，规避 Blackwell sm120 flashinfer 兼容性问题。

### 预计时间线
- OLMo 推理开始：~00:50（下载完成后）
- OLMo 5 benchmarks 完成：~01:05（按 ~7 min/benchmark × 2 rounds）
- Yi 推理开始：~04:00（下载完成后）
- **全部完成：~04:20**

### 监控命令
```bash
# 链式脚本日志
tail -20 /root/nlp_variance_gtheory/results/auto_chain_19912.log

# 模型下载进度
tail -3 /tmp/download_olmo.log; tail -3 /tmp/download_yi.log

# GPU 使用
nvidia-smi
```

注：`update_registry` 工具不在可用 MCP 工具列表中，registry 更新需要另行处理。

---
