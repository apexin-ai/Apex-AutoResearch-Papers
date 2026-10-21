# exp-001 Target Models 数据源调研报告

Date: 2026-05-21

---

## 1. 各 Benchmark 公开数据可用性

### MT-Bench (LMSYS)
- **Prompts**: 80 questions (multi-turn, question_id 81-160)
- **Pre-generated responses**: 34 models
- **来源**: HuggingFace Space `lmsys/mt-bench` (非 GitHub repo)
- **格式**: JSONL, 字段: `question_id`, `answer_id`, `model_id`, `choices[0].turns[]`, `tstamp`
- **覆盖模型**: GPT-4, GPT-3.5-turbo, Claude-v1, Llama-2 (7B/13B/70B), Vicuna (7B/13B/33B), WizardLM, Guanaco, MPT, etc.
- **访问**: `git clone https://huggingface.co/spaces/lmsys/mt-bench` 或 FastChat 的 `download_mt_bench_pregenerated.py`
- **License**: 未明确标注，HuggingFace Space 公开
- **局限**: 模型偏旧 (2023年中期)，无 2024+ 模型

### Arena-Hard-Auto (LMSYS)
- **Prompts**: v0.1 = 500, v2.0 = 750 (500 technical + 250 creative)
- **Pre-generated responses**: GitHub repo 仅 3-4 models; HuggingFace dataset `lmarena-ai/arena-hard-auto` 有 ~28 models (3.31 GB)
- **格式**: JSONL, 字段: `uid`, `ans_id`, `model`, `messages[]`, `tstamp`
- **覆盖模型** (HF full): GPT-4.1, o3, Claude variants, Gemini-2.5, Qwen, Llama, DeepSeek-R1, etc.
- **访问**: `git lfs clone hf.co/datasets/lmarena-ai/arena-hard-auto`
- **License**: 未明确
- **优势**: 模型覆盖较新，有 pairwise judge annotations

### WildBench V2 (AI2)
- **Prompts**: 1,024
- **Pre-generated responses**: 64 models (`allenai/WildBench-V2-Model-Outputs`)
- **格式**: Parquet (HuggingFace Datasets), 字段: `session_id`, `chat_history`, `model_input`, `output`, `generator`, `configs`
- **覆盖模型**: GPT-4o, Claude-3.x, Gemini 1.5, Llama-3, Qwen2, DeepSeek-V2, Gemma-2, Mistral, etc.
- **访问**: `load_dataset("allenai/WildBench-V2-Model-Outputs", "<model>")`
- **License**: Apache 2.0
- **优势**: 模型多样且较新 (2024 mid), Apache 许可

### AlpacaEval 2 (Stanford/tatsu-lab)
- **Prompts**: 805 instructions
- **Pre-generated responses**: 228 models
- **格式**: JSON, 字段: `dataset`, `instruction`, `output`, `generator`
- **覆盖模型**: 从 alpaca-7b 到 GPT-4o, Claude 3.5 Sonnet, Llama 3.1 405B, Qwen2-72B, etc.
- **访问**: GitHub `results/<model>/model_outputs.json` 或 HuggingFace
- **License**: CC BY-NC 4.0 (⚠️ 非商用)
- **优势**: 模型数量最多 (228)

### Chatbot Arena Conversations (LMSYS)
- **Conversations**: 33,000 pairwise
- **Models**: 20 LLMs
- **格式**: Parquet, OpenAI API JSON format
- **License**: Prompts CC BY 4.0, Outputs CC BY-NC 4.0; Gated (auto-approval)
- **局限**: Pairwise 格式不适合直接用作 target responses

---

## 2. 推荐数据获取策略

### 策略 A: 混合方案 (推荐)

**Phase 1 — 利用公开数据快速启动:**
- 用 **AlpacaEval 2** 的 805 prompts + 现有 model outputs 做初步实验
  - 优势: 228 models 覆盖广，格式简单
  - 劣势: CC BY-NC, prompts 质量中等
- 用 **Arena-Hard v0.1** 的 500 prompts 做高质量实验
  - 优势: prompts 来自真实用户，区分度高
  - 劣势: 公开 responses 仅 ~28 models

**Phase 2 — 补充生成 frontier models:**
- 对公开数据中缺失的 2025-2026 frontier models (GPT-5.5, Claude Opus 4.7, DeepSeek V4 Pro, etc.) 自行生成 responses
- Benchmark prompts 用 Arena-Hard v0.1 (500) 或 WildBench V2 (1024)

### 策略 B: 全自行生成

在 MT-Bench 80 questions + Arena-Hard 500 prompts 上，对全部 20+ target models 统一生成 responses。
- 优势: 完全一致的生成参数，可控性强
- 劣势: API 成本高，时间长

### 推荐: **策略 A**
- Primary benchmark: **Arena-Hard v0.1** (500 prompts) — 难度高，区分度好
- Secondary: **WildBench V2** (1024 prompts) — prompts 多样，已有 64 models
- 仅对缺失模型 (frontier 2025-2026) 自行生成 responses

---

## 3. Target Models 最终列表 (22 models)

### Frontier Tier (5 models)

| # | Model | ID | Params | Type | Access |
|---|-------|-----|--------|------|--------|
| 1 | GPT-4o | `gpt-4o` | ~200B (est.) | API | OpenAI API |
| 2 | GPT-5.5 | `gpt-5.5` | Undisclosed | API | OpenAI API |
| 3 | Claude Opus 4.7 | `claude-opus-4-7` | Undisclosed | API | Anthropic API |
| 4 | Gemini 2.5 Pro | `gemini-2.5-pro` | Undisclosed | API | Google API |
| 5 | DeepSeek V4 Pro | `deepseek-ai/DeepSeek-V4-Pro` | 1.6T/49B active | Open+API | HF / DeepSeek API |

### Mid Tier (5 models)

| # | Model | ID | Params | Type | Access |
|---|-------|-----|--------|------|--------|
| 6 | Claude Sonnet 4.6 | `claude-sonnet-4-6` | Undisclosed | API | Anthropic API |
| 7 | GPT-4o-mini | `gpt-4o-mini` | Undisclosed | API | OpenAI API |
| 8 | Gemini 2.5 Flash | `gemini-2.5-flash` | Undisclosed | API | Google API |
| 9 | Qwen3-235B-A22B | `Qwen/Qwen3-235B-A22B-Instruct` | 235B/22B active | Open | HF (Apache 2.0) |
| 10 | Mistral Large 3 | `mistral-large-2512` | 675B/41B active | Open+API | HF / Mistral API |

### Open-Source Strong (4 models)

| # | Model | ID | Params | Type | License |
|---|-------|-----|--------|------|---------|
| 11 | Llama-3.3-70B | `meta-llama/Llama-3.3-70B-Instruct` | 70B | Open | Llama 3.3 CL |
| 12 | Qwen2.5-72B | `Qwen/Qwen2.5-72B-Instruct` | 72B | Open | Qwen License |
| 13 | DeepSeek-V3 | `deepseek-ai/DeepSeek-V3` | 671B/37B active | Open | MIT |
| 14 | Mistral Medium 3.5 | `mistralai/Mistral-Medium-3.5-128B` | 128B | Open | Mistral License |

### Open-Source Mid/Weak (8 models)

| # | Model | ID | Params | Type | License |
|---|-------|-----|--------|------|---------|
| 15 | Llama-3.1-8B | `meta-llama/Llama-3.1-8B-Instruct` | 8B | Open | Llama 3.1 CL |
| 16 | Qwen2.5-7B | `Qwen/Qwen2.5-7B-Instruct` | 7B | Open | Qwen License |
| 17 | Mistral-7B | `mistralai/Mistral-7B-Instruct-v0.3` | 7B | Open | Apache 2.0 |
| 18 | Phi-4 | `microsoft/phi-4` | 14B | Open | MIT |
| 19 | Gemma-2-27B | `google/gemma-2-27b-it` | 27B | Open | Gemma ToU |
| 20 | Llama-3.1-70B | `meta-llama/Llama-3.1-70B-Instruct` | 70B | Open | Llama 3.1 CL |
| 21 | Qwen2.5-14B | `Qwen/Qwen2.5-14B-Instruct` | 14B | Open | Qwen License |
| 22 | Gemma-2-9B | `google/gemma-2-9b-it` | 9B | Open | Gemma ToU |

---

## 4. 成本估算 (自行生成 responses)

### 假设
- Benchmark: Arena-Hard v0.1 (500 prompts)
- 每个 prompt 平均输入 ~200 tokens, 输出 ~500 tokens
- 需要生成: ~10 API-only models × 500 prompts = 5,000 API calls

### API 成本估算

| Model | Input $/1M tok | Output $/1M tok | Est. Cost (500 prompts) |
|-------|---------------|-----------------|------------------------|
| GPT-5.5 | ~$15 | ~$60 | ~$0.93 |
| Claude Opus 4.7 | ~$15 | ~$75 | ~$1.05 |
| Gemini 2.5 Pro | ~$2.50 | ~$15 | ~$0.24 |
| GPT-4o | ~$2.50 | ~$10 | ~$0.16 |
| GPT-4o-mini | ~$0.15 | ~$0.60 | ~$0.01 |
| Claude Sonnet 4.6 | ~$3 | ~$15 | ~$0.24 |
| Gemini 2.5 Flash | ~$0.15 | ~$0.60 | ~$0.01 |
| DeepSeek V4 Pro API | ~$2 | ~$8 | ~$0.13 |
| Mistral Large | ~$2 | ~$6 | ~$0.10 |

**API-only models 总计: ~$3-5 (500 prompts)**

### 开源模型 (本地推理)
- 12 open-source models × 500 prompts
- 使用 vLLM 在 4×RTX6000 上推理
- 70B models: ~5 min/model (batch inference)
- 7-14B models: ~1-2 min/model
- **总推理时间: ~1-2 小时 (无额外成本)**

### 总预算
- **API 成本**: ~$5 (Arena-Hard 500 prompts, 10 API models)
- **本地推理**: 0 (用项目服务器)
- **总计**: < $10

---

## 5. 关键决策点

1. **Primary benchmark 选择**: Arena-Hard v0.1 (500 prompts) vs WildBench V2 (1024 prompts)
   - Arena-Hard: 更难，区分度高，LMSYS 标准
   - WildBench: prompts 更多样，已有 64 models outputs

2. **是否需要 multi-turn**: MT-Bench 是 multi-turn，Arena-Hard/WildBench 是 single-turn
   - 建议: 主实验用 single-turn (Arena-Hard), 补充实验探索 multi-turn (MT-Bench 80Q)

3. **CC BY-NC 限制**: AlpacaEval 数据有非商用限制
   - 建议: 如果计划商用/开源数据集，避免用 AlpacaEval 的 model outputs

4. **公开数据 vs 自行生成**: 公开数据中的 model outputs 生成参数不一致 (温度、max_tokens 等)
   - 如果需要严格控制实验变量，建议全部自行生成
   - 如果关注 ecological validity，用公开数据更好
