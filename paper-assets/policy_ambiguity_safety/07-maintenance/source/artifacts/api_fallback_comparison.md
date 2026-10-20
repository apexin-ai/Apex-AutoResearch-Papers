# API Endpoint Fallback 方案比较

> 调研日期: 2026-05-20
> 实验规模: 360 episodes × ~4K tokens/episode ≈ 1.44M tokens per model
> 成本假设: 75% input / 25% output token split (1.08M input + 0.36M output per model)
> 当前代码: 统一 OpenRouter 端点 + openai SDK，两个模型交叉调用（agent + judge）

## 比较表

| 方案 | 支持模型 | 估算成本 (360 episodes, 双模型) | 代码改动量 | 优缺点 |
|------|----------|-------------------------------|-----------|--------|
| **1. 直连 Anthropic API** | Claude Sonnet 4.5 (`claude-sonnet-4-5-20250514`), $3/$15 per 1M | Claude 部分 ~$8.64; GPT 需另走 OpenAI | **大** — 需引入 `anthropic` SDK, 重写调用逻辑为 `client.messages.create()`, 维护两套 client | (+) 官方端点最稳定, 无中间商; (-) 需同时维护 anthropic + openai 两套 SDK, 代码改动最大 |
| **2. 直连 OpenAI API** | GPT-5.4 (`gpt-5.4`), $2.50/$15 per 1M | GPT 部分 ~$8.10; Claude 需另走 Anthropic | **中** — 已用 openai SDK, 改 `base_url` 即可; Claude 部分仍需方案 1 | (+) GPT 调用零改动(去掉自定义 base_url 即可); (-) 只解决一半问题 |
| **3. OpenRouter 官方** | 两者均支持: `anthropic/claude-sonnet-4.5`, `openai/gpt-5.4` | ~$17.66 (含 5.5% credit fee) | **最小** — 仅改 `base_url` 为 `https://openrouter.ai/api/v1` + 换 API key | (+) 代码改动最小, 一个端点覆盖两个模型, model_id 格式兼容; (-) 有 5.5% 加价, 依赖第三方, 新账户仅 $1 免费额度 |
| **4. Together / Fireworks** | 仅开源模型 (Llama, DeepSeek, Qwen 等), **不支持 Claude/GPT** | N/A | N/A | (-) **不可行** — 不提供 Claude 和 GPT 闭源模型 |

## 各方案详情

### 方案 1: 直连 Anthropic API

- **Endpoint**: `https://api.anthropic.com`
- **Model ID**: `claude-sonnet-4-5-20250514` (Sonnet 4.5); 最新版为 `claude-sonnet-4-6-20250514` (Sonnet 4.6, 同价)
- **定价**: $3.00/M input, $15.00/M output
- **单模型成本**: 1.08M × $3 + 0.36M × $15 = **$8.64**
- **SDK**: 需要 `anthropic` 库, 接口为 `client.messages.create()`, 与 openai SDK 不兼容
- **改动**:
  - `requirements.txt` 加 `anthropic>=0.40.0`
  - `harness.py` / `judge.py` 需为 Claude 调用编写独立的 client 和请求逻辑
  - 参考: `_project/intermediate/` 目录已有双 SDK 实现可复用

### 方案 2: 直连 OpenAI API

- **Endpoint**: `https://api.openai.com/v1`
- **Model ID**: `gpt-5.4`
- **定价**: $2.50/M input, $15.00/M output
- **单模型成本**: 1.08M × $2.5 + 0.36M × $15 = **$8.10**
- **SDK**: 当前已用 `openai` SDK, 去掉自定义 `base_url` 即可直连
- **改动**: 仅 GPT 部分改动极小; Claude 部分仍需方案 1

### 方案 3: OpenRouter 官方 (推荐调研)

- **Endpoint**: `https://openrouter.ai/api/v1`
- **Model IDs**: 与当前 config.py 格式一致 (`anthropic/claude-sonnet-4-5-...`, `openai/gpt-5.4`)
- **定价**: 透传原价 + 充值时 5.5% 手续费
- **双模型总成本**: ($8.64 + $8.10) × 1.055 ≈ **$17.66**
- **免费额度**: 新账户 $1 (约够 ~100 次 GPT-4o-mini 调用, 不够本实验)
- **改动**:
  - `config.py` 中 `OPENROUTER_BASE_URL` 改为 `https://openrouter.ai/api/v1`
  - 环境变量 `OPENROUTER_API_KEY` 换为 OpenRouter 官方 key
  - 其余代码无需修改

### 方案 4: Together.ai / Fireworks.ai

- **结论: 不可行**
- 仅托管开源模型 (Llama, DeepSeek, Mistral, Qwen 等)
- 不提供 Claude 或 GPT 系列模型
- 如果实验可以接受替代模型 (如 Llama 3.3 70B), 成本会大幅降低 (~$0.88/M), 但需要验证实验效果

## 混合方案 (补充)

| 组合 | 成本 | 改动量 |
|------|------|--------|
| Anthropic 直连 + OpenAI 直连 | ~$16.74 (无加价) | 大 (双 SDK) |
| OpenRouter 统一 | ~$17.66 | 最小 |
| OpenAI 直连 + OpenRouter (仅 Claude) | ~$8.10 + ~$9.12 = ~$17.22 | 中 |

## 待 Director 决策

1. 选择哪个方案 (改动量 vs 成本 tradeoff)
2. 是否接受 OpenRouter 5.5% 加价换取最小改动
3. 是否需要升级到 Claude Sonnet 4.6 (同价, 更强)
4. API key 获取渠道
