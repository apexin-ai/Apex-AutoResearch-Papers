# check exp001 and models

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp001-and-models_20260516T184531_result.json`
- **Structured JSON:** [`ef02149a3cd08428a4d7.json`](../../sessions/ef/ef02149a3cd08428a4d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. exp-001 状态：**进行中，97.5% 完成**

| 指标 | 值 |
|------|-----|
| PID | 181491（存活，已运行 13h30m） |
| 命令 | `python run_full_mvp.py --mode vllm --k 12 --temperature 0.7 ...` |
| 进度 | **784/804 题 (97.5%)** |
| ProofWriter | 600/600 ✅ 完成 |
| FOLIO | 184/204（剩余 20 题） |
| 预计完成 | 按当前速率，约 20-30 分钟内完成 |

分析脚本 `scripts/analyze_expanded.py` 存在，待实验完成后运行。

### 2. 模型下载状态：**三个模型全部完整** ✅

| 模型 | 路径 | Shards | 状态 |
|------|------|--------|------|
| Mistral-7B-Instruct-v0.3 | `/root/autodl-tmp/models/Mistral-7B-Instruct-v0.3/mistralai/Mistral-7B-Instruct-v0___3/` | 3 shards (3.5G+4.2G+3.5G) | ✅ 完整 |
| LLaMA-3.1-8B-Instruct | `/root/autodl-tmp/models/Llama-3.1-8B-Instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct/` | 4 shards (4.7G+3.7G+4.6G+1.1G) | ✅ 完整 |
| DeepSeek-R1-Distill-LLaMA-8B | `/root/autodl-tmp/models/DeepSeek-R1-Distill-Llama-8B/` | 2 shards (8.1G+6.9G) | ✅ 完整 |

无 temp/incomplete 残留文件。

### 3. vLLM 脚本路径验证：**全部正确** ✅

| 脚本 | MODEL 路径 | config.json |
|------|-----------|-------------|
| `start_vllm_deepseek_r1_8b.sh` | `/root/autodl-tmp/models/DeepSeek-R1-Distill-Llama-8B` | ✅ OK |
| `start_vllm_llama_8b.sh` | `.../Meta-Llama-3___1-8B-Instruct` | ✅ OK |
| `start_vllm_mistral_7b.sh` | `.../Mistral-7B-Instruct-v0___3` | ✅ OK |

### 总结

exp-001 还剩 20 道 FOLIO 题即将完成。三个模型下载完整，vLLM 启动脚本路径全部正确，可直接用于后续 cross-model 实验。

---
