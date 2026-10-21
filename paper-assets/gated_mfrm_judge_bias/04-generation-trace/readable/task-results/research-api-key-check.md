# research api key check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_api_key_check_20260522T025924_result.json`
- **Structured JSON:** [`0ee9b33eec78f037fc18.json`](../../sessions/0e/0ee9b33eec78f037fc18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结论明确了。服务器上 **没有任何 proprietary API key** 配置。

从 `judge_interface.py` 可以确认代码期望的环境变量名：

## API Key 状态

| Judge | Model ID | 环境变量 | 状态 |
|-------|----------|----------|------|
| **GPT-5.5** (OpenAI) | `gpt-5.5` | `OPENAI_API_KEY` | ❌ 不存在 |
| **Claude Opus 4.7** (Anthropic) | `claude-opus-4-7-20250219` | `ANTHROPIC_API_KEY` | ❌ 不存在 |
| **Claude Sonnet 4.6** (Anthropic) | `claude-sonnet-4-6-20250514` | `ANTHROPIC_API_KEY` | ❌ 不存在 |
| **DeepSeek-V4-Pro** (DeepSeek) | `deepseek-v4-pro` | `DEEPSEEK_API_KEY` | ❌ 不存在 |
| **Qwen3-235B-A22B** (OpenRouter) | `qwen3-235b-a22b` | `OPENROUTER_API_KEY` | ❌ 不存在 |
| **Gemini 2.5 Pro** (Google) | `gemini-2.5-pro` | `GOOGLE_API_KEY` | ❌ 不存在 |

## 需要的操作

需要申请/配置 **5 个 API key**（Anthropic 两个模型共用一个 key）：

1. **`OPENAI_API_KEY`** — [platform.openai.com/api-keys](https://platform.openai.com/api-keys) 创建，需确认账户有 `gpt-5.5` 模型访问权限
2. **`ANTHROPIC_API_KEY`** — [console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys) 创建，覆盖 Opus 4.7 和 Sonnet 4.6
3. **`DEEPSEEK_API_KEY`** — [platform.deepseek.com](https://platform.deepseek.com) 创建
4. **`GOOGLE_API_KEY`** — [aistudio.google.com/apikey](https://aistudio.google.com/apikey) 创建，用于 Gemini 2.5 Pro
5. **`OPENROUTER_API_KEY`** — [openrouter.ai/keys](https://openrouter.ai/keys) 创建，用于 Qwen3-235B-A22B

获取 key 后，建议写入 `/root/gated_mfrm_judge_bias/.env` 并在实验脚本中 `source` 或用 `python-dotenv` 加载，避免写入 `.bashrc` 泄露到其他用途。

---
