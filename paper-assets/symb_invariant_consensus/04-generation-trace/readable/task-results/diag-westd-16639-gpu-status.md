# diag westd 16639 gpu status

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd-16639-gpu-status_20260519T121536_result.json`
- **Structured JSON:** [`0dfe0410902a5e34bfdb.json`](../../sessions/0d/0dfe0410902a5e34bfdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-16639 诊断结果

### GPU 使用状态（4× NVIDIA RTX PRO 6000 Blackwell, 98GB）

| GPU | PID | 实验 | 模型 | 端口 | 显存 | 利用率 |
|-----|-----|------|------|------|------|--------|
| **cuda:0** | 152729 | **exp-064** | DeepSeek-R1-0528-Qwen3-8B | 8002 | 88244/97887 MiB | 96% |
| cuda:1 | 142896 | exp-068 | Qwen3-14B (non-thinking) | 8001 | 88278/97887 MiB | 97% |
| cuda:2 | 151829 | exp-069 | Meta-Llama-3.1-8B-Instruct | 8012 | 88254/97887 MiB | 96% |
| cuda:3 | 76474 | exp-048 | Meta-Llama-3.1-8B-Instruct | 8003 | 88254/97887 MiB | 97% |

全部 4 张 GPU 满载运行 vLLM EngineCore。

### Tmux Sessions（7 个）

| Session | 创建时间 | 用途 |
|---------|---------|------|
| `exp-069-llama8b-logiqa200` | 20:05 | exp-069 run |
| `exp064_vllm` | 20:05 | exp-064 vLLM |
| `exp064_run` | 20:06 | exp-064 run |
| `exp068_vllm` | 19:08 | exp-068 vLLM |
| `exp068_run` | 19:13 | exp-068 run |
| `exp048_vllm` | 10:19 | exp-048 vLLM |
| `exp048_run` | 10:20 | exp-048 run |

注：exp-069 的 vLLM 通过 nohup 启动（非 tmux），日志在 `/tmp/vllm_exp069_llama8b.log`。

### 实验进度

| 实验 | 数据集 | 进度 | 百分比 | 状态 |
|------|--------|------|--------|------|
| **exp-048** LLaMA-8B PW-600 | ProofWriter-600 | 457/600 | **76%** | 运行正常，自 10:20 启动 |
| **exp-064** DeepSeek-R1-Qwen3-8B FOLIO | FOLIO-204 | 74/204 | **36%** | 运行中（--resume），有 retry |
| **exp-068** Qwen3-14B LogiQA | LogiQA-200 | 121/200 | **60.5%** | 运行中，有 retry |
| **exp-069** LLaMA-8B LogiQA | LogiQA-200 | 12/200 | **6%** | 刚启动 ~12 分钟 |

### cuda:0 详情

**DeepSeek-R1-0528-Qwen3-8B** 的 vLLM 实例（exp-064），`max-model-len=16384`，端口 8002。exp-064 和 exp-069 的 vLLM 均在 20:05 左右重新启动（之前可能有重启/重部署）。

Registry 已为 exp-069-llama8b-logiqa200 更新 notes 字段，包含 tmux_session、PID、GPU 映射等信息。

---
