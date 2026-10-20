# ssh fix exp001 judge errors

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_exp001_judge_errors_20260522T053339_result.json`
- **Structured JSON:** [`93352e7187a322cd0ced.json`](../../sessions/93/93352e7187a322cd0ced.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

gpt-5.5-proxy 仍正常运行 (470/3000)。

---

## 修复完成汇报

### 1. 每个 judge 的错误根因分类

| Judge | 错误率 | 根因分类 |
|-------|--------|----------|
| gemini-2.5-pro-proxy | 90% | **proxy 余额不足 (402)** + **max_tokens=1024 截断** (parse_failure) |
| deepseek-v4-pro-proxy | 69% | **proxy 余额不足 (402)** + **模型返回空内容** (empty_response) |
| qwen3-235b-proxy | 44% | **proxy 余额不足 (402)** |
| claude-opus-4.7-proxy | 28% | **proxy 余额不足 (402)** + 少量 parse_failure |
| claude-sonnet-4.6-proxy | 27% | **proxy 余额不足 (402)** |
| gpt-5.5-proxy | 5% | 偶发空响应，仍正常运行 |
| 3 local judges | 0% | 无错误 |

### 2. API 连通性
- Proxy (`http://47.94.22.126/v1`) 本身可连，但 **OpenRouter 余额已耗尽** (HTTP 402)
- 所有 proxy judges 除 gpt-5.5 外都卡在 402 重试循环，已停止
- **需要充值 OpenRouter 后才能恢复 5 个 proxy judge**

### 3. Local judge JSONL 数据完整性
- 296 行，**0 行损坏**，全部有效 JSON
- 已按 judge 拆分：llama=173, qwen=89(+4新), mistral=34

### 4. 执行的修复

**代码改动:**
- `judge_interface.py`: ProxyJudge/OpenAIJudge/AnthropicJudge/DeepSeekJudge/OpenRouterJudge 的 `max_tokens` 从 1024 → 4096（修复 Gemini 截断）；VLLMJudge 保持 1024（适配 4096 context limit）

**Config 改动:**
- `config_llama_arena.yaml`: `output_dir` → `results/llama-3.3-70b/`
- `config_qwen_arena.yaml`: `output_dir` → `results/qwen2.5-72b/`
- `config_mistral_arena.yaml`: `output_dir` → `results/mistral-large-2/`

**操作:**
- 停止 5 个 proxy sessions (402 无效重试)
- 停止 3 个 local judges + 1 个多余的 mistral 进程
- 备份共享 JSONL → `arena_hard_judgments.jsonl.bak`
- 拆分数据到 per-judge 目录
- 重启 3 个 local judges（per-judge 独立输出）

### 5. 当前各 judge 状态

| Session | 状态 | 进度 |
|---------|------|------|
| exp001-llama | **运行中** | 173/3000 |
| exp001-qwen | **运行中** | 93/3000 |
| exp001-mistral | **运行中** | 21/3000 |
| exp001-gpt55 | **运行中** | 470/3000 |
| 5 个 proxy judges | **已停止** | 等待 OpenRouter 充值 |

### 6. 待用户操作
- **充值 OpenRouter 账户** (https://openrouter.ai/settings/credits)，然后重启 5 个 proxy judge sessions
- 充值后 Gemini 的 `max_tokens=4096` 修复应能将 parse failure 率从 ~85% 降至接近 0
- DeepSeek 的空响应问题可能需要进一步调查 proxy 的 model routing

---
