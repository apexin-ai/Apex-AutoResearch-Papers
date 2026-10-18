# code gpu status check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gpu_status_check_20260514T020239_result.json`
- **Structured JSON:** [`dbdcdc66595d4e27b498.json`](../../sessions/db/dbdcdc66595d4e27b498.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态汇总

### GPU

| GPU | 型号 | 显存占用 | 利用率 | 温度 |
|-----|------|---------|--------|------|
| cuda:0 | RTX PRO 6000 Blackwell (98GB) | 17.1GB / 98GB | 83% | 69°C |
| cuda:1 | RTX PRO 6000 Blackwell (98GB) | 0GB / 98GB | **0% (空闲)** | 35°C |

### 正在运行的进程

- **PID 168914** — `python run_llama_eval_fix.py`，在 cuda:0 上运行（`CUDA_VISIBLE_DEVICES=0`），启动于 10:01，已运行约 2 分钟
- cuda:1 上 **无任何实验进程**

### Llama Pipeline 进度

- **Phase 1 (Profiling)**: ✅ 已完成，`llama_profiling_results.json` 存在 (34KB, 09:39)
- **Phase 2 (MCKP)**: ✅ 已完成，分配方案 `{4bit: 244, 8bit: 4, 2bit: 8}`，distortion 0.2695 vs uniform 0.8085
- **Phase 3 (WikiText-2 PPL)**: ❌ **失败** — `load_dataset("wikitext")` 报 `ConnectionError: Couldn't reach 'wikitext' on the Hub`（网络/代理问题）
- 当前正在运行 `run_llama_eval_fix.py` 作为修复尝试

### 文件存在性

| 文件 | 状态 |
|------|------|
| `llama_profiling_results.json` | ✅ 34KB |
| `exp_e_hires_results.json` | ✅ 10KB (exp_e Phase 2+3 结果已生成) |
| `run_llama_phase23.py` | ✅ 存在 |
| `run_mistral_pipeline.py` | ✅ 存在 |

### 可启动的下一步

1. **cuda:1 完全空闲** — 可立即启动 `run_mistral_pipeline.py` 或其他实验
2. **等 `run_llama_eval_fix.py` 完成** — 如果修复成功，Llama Phase 3 PPL 评估将完成；如果仍然报网络错误，需要先 `source /etc/network_turbo` 解决 HF Hub 连接问题，或改为离线加载 wikitext 数据集

---
