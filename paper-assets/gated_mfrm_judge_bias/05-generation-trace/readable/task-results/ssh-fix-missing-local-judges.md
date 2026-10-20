# ssh fix missing local judges

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_missing_local_judges_20260522T121209_result.json`
- **Structured JSON:** [`0c2d765fe2165069cff4.json`](../../sessions/0c/0c2d765fe2165069cff4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**汇总：**

**Judge collect.py — 9/9 全部在运行，无需修复：**
| Judge | Config | Workers | Status |
|-------|--------|---------|--------|
| llama-3.3-70b | config_llama_arena.yaml | 8 | ✓ running |
| qwen2.5-72b | config_qwen_arena.yaml | 8 | ✓ running |
| mistral | config_mistral_arena.yaml | 8 | ✓ running |
| gpt-5.5 | config_gpt-5.5-proxy_arena.yaml | 4 | ✓ running |
| claude-opus-4.7 | config_claude-opus-4.7-proxy_arena.yaml | 4 | ✓ running |
| claude-sonnet-4.6 | config_claude-sonnet-4.6-proxy_arena.yaml | 4 | ✓ running |
| deepseek-v4-pro | config_deepseek-v4-pro-proxy_arena.yaml | 4 | ✓ running |
| gemini-2.5-pro | config_gemini-2.5-pro-proxy_arena.yaml | 4 | ✓ running |
| qwen3-235b | config_qwen3-235b-proxy_arena.yaml | 4 | ✓ running |

**vLLM 服务 — 均在线：**
- Port 8001: `llama-3.3-70b-instruct` (max_model_len=8192)
- Port 8002: `qwen2.5-72b-instruct` (max_model_len=4096)

**Response 生成进程 — 3 个在运行（非暂停）：**
| Session | 进程 | 详情 |
|---------|------|------|
| gen-vllm | `generate_vllm_online.py --all --workers 32` | 在 tmux pts/2 |
| gen-api | `generate_responses.py --group proxy_nocredit --workers 3 --rate-delay 1.0` | 在 tmux pts/5 |
| (background) | `generate_responses.py --group openai --workers 3 --rate-delay 0.3` | nohup 后台进程 |

llama 和 qwen 的 judge sessions 已经存在并且 collect.py 正在运行，看起来是之前已经启动好了。

---
