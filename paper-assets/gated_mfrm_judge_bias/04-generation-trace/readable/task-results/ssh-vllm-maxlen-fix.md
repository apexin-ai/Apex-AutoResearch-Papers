# ssh vllm maxlen fix

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_vllm_maxlen_fix_20260523T212401_result.json`
- **Structured JSON:** [`e0835c21a9fdaa3b9fbc.json`](../../sessions/e0/e0835c21a9fdaa3b9fbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。产出报告：

---

## 产出报告

### 1. vLLM 参数对比

| 参数 | 旧值 | 新值 |
|------|------|------|
| max-model-len | **4096** | **8192** |
| 其他参数 | 不变 | 不变 |

三个 vLLM 实例共享参数：`--quantization awq --gpu-memory-utilization 0.90 --attention-backend FLASH_ATTN`  
新增环境变量：`VLLM_USE_FLASHINFER_SAMPLER=0`

| 模型 | GPU | 端口 | 旧 PID | 新 PID |
|------|-----|------|--------|--------|
| LLaMA-3.3-70B-AWQ | 0 | 8001 | 656336 | 662563 |
| Qwen2.5-72B-AWQ | 1 | 8002 | 656337 | 663361 |
| Mistral-Large-AWQ | 2 | 8003 | 656338 | 664095 |

### 2. vLLM 健康检查
三个 endpoint 全部返回 200，`max_model_len: 8192` 已确认生效。

### 3. collect.py 重启后的 PID

| Judge | 类型 | PID | workers |
|-------|------|-----|---------|
| llama_arena_n17 | local | 665441 | 10 |
| qwen_arena_n17 | local | 665509 | 10 |
| mistral_arena_n17 | local | 665583 | 10 |

### 4. JSONL Baseline 行数（重启时刻）

| 目录 | 行数 |
|------|------|
| llama-3.3-70b | 7,128 |
| qwen2.5-72b | 9,922 |
| mistral-large-2 | 9,425 |
| llama-3.3-70b-shard2 | 5,943 |

### 5. API judge 进程状态：正常运行

| Judge | PID | 状态 |
|-------|-----|------|
| claude-sonnet-4.6-proxy | 653489 | ✓ |
| gemini-2.5-pro-proxy | 653490 | ✓ |
| deepseek-v4-pro-proxy | 653491 | ✓ |
| qwen3-235b-proxy | 653492 | ✓ |
| gpt-5.5-proxy (partial) | 659566 | ✓ |
| claude-opus-4.7-proxy (partial) | 659677 | ✓ |

### 6. 10 分钟验证
已调度后台脚本（PID 665662），结果将写入 `/tmp/final_check.txt`，可稍后用 `cat /tmp/final_check.txt` 查看 400 error 数量和 throughput 增长。

---
