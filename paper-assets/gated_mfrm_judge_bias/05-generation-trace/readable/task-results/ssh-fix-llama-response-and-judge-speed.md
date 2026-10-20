# ssh fix llama response and judge speed

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_llama_response_and_judge_speed_20260522T065849_result.json`
- **Structured JSON:** [`69c5ee8c16510591876a.json`](../../sessions/69/69c5ee8c16510591876a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full status report:

---

## 1. Llama Response Generation — 根因 + 修复

**根因**:
- `generate_vllm_online.py` 的 `MAX_TOKENS=4096`，qwen/mistral 的 vLLM `--max-model-len=4096` → 没有空间给 input tokens → **500 条全部 ERROR**
- llama vLLM `max-model-len=8192` 可以工作，但**无并发** + judge collection 同时竞争 GPU → 极慢 (5 tok/s)

**修复措施**:
1. `MAX_TOKENS` 4096 → 2048
2. 添加 per-endpoint 并发（32 workers/ThreadPoolExecutor）
3. 暂停 judge collection，释放 GPU 给 response generation
4. 删除 qwen/mistral 的 500 条 error responses，重新生成

**当前进度** (启动 ~5 min):

| Model | Progress | Throughput | ETA |
|---|---|---|---|
| llama-3.3-70b | 25/500 | **83 tok/s** (原 5 tok/s) | ~1h |
| qwen2.5-72b | 9/500 | ~40 tok/s | ~2h |
| mistral-large-2 | 4/500 | **45 tok/s** | ~2h |
| gpt-4o-mini | 68/500 | OpenAI API | ~10h |
| Others (5 models) | 500/500 | Done | — |

## 2. Judge 并发优化

**原始设置**: `collect.py` 纯同步循环，1 request at a time。rpm=100 rate limiter 没用（瓶颈是 GPU 生成速度，不是 rate limit）

**修改后设置**: 
- 添加 `--workers N` CLI 参数 + `max_workers` config 支持
- ThreadPoolExecutor 并发执行
- Thread-safe RateLimiter（加锁）和文件写入（加锁）
- 预计使用 `--workers 8` 重启

**预期 ETA 改善**:
- 原始：~50-60h per judge（1 item/min）
- 修改后：~12-15h per judge（4-5 items/min with 8 workers）
- 提速 ~4x

## 3. vLLM 并发测试

5 concurrent × 10 max_tokens:
```
req 0: 1.6s, status=200
req 1: 1.6s, status=200
req 2: 1.6s, status=200
req 3: 1.6s, status=200
req 4: 1.6s, status=200
```
vLLM continuous batching 处理并发正常。

## 4. 全局状态快照

**Responses**:
- 5/8 完成 (500/500)，3/8 生成中（在 gen-vllm tmux session）

**Judgments**: 
| Judge | Done/3000 |
|---|---|
| gpt-5.5-proxy | 1046 (35%) |
| claude-opus-4.7 | 467 (16%) |
| claude-sonnet-4.6 | 431 (14%) |
| gemini-2.5-pro | 360 (12%) |
| qwen3-235b | 252 (8%) |
| deepseek-v4-pro | 243 (8%) |
| llama-3.3-70b | 233 (8%) ⏸️ |
| qwen2.5-72b | 144 (5%) ⏸️ |
| mistral-large-2 | 68 (2%) ⏸️ |

**GPU**: 全部 4 卡 68-100% utilization。

**Active tmux sessions**: gen-vllm, exp001-gpt55, vllm-llama, vllm-mistral

**下一步**: response gen 完成后重启 judge collection with `--workers 8`。

---
