# research model freshness check

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_model-freshness-check_20260522T152247_result.json`
- **Structured JSON:** [`f509db8e904ba03f24fd.json`](../../sessions/f5/f509db8e904ba03f24fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

搜索完成。以下是综合分析。

## 模型时效性审计结果

### 已完成/在跑（不换）的确认

| 模型 | 发布 | 当前状态 | 备注 |
|---|---|---|---|
| claude-3-haiku | 2024-03 | **已过时 2 代**（→3.5-haiku→haiku-4.5） | 已跑完，无法换。论文中说明为 legacy weak-tier 即可 |
| claude-sonnet-4 | 2025-05 | **过时 1 代**（当前 sonnet-4.6, 2026-02） | 已跑完 |
| claude-opus-4 | 2025-01 | **过时 2 代**（当前 opus-4.7, 2026-04） | 在跑中 |

这三个都已锁定，虽然版本不是最新但代理上只有这些 ID，可以接受。

---

### 未跑模型逐一评估

| 当前模型 | 发布日期 | 过时程度 | 代理可用 | 推荐 | 理由 |
|---|---|---|---|---|---|
| **gpt-4o** | 2024-05 | **过时** — 2026-02 已从 ChatGPT 下线，被 gpt-4.1 系列取代 | ✅ 可用 | **替换为 `gpt-4.1-mini`** | gpt-4.1-mini 性能≈gpt-4o 但更新（2025-04），$0.4/M 更便宜，代理已验证可用。gpt-4o 在 2026 论文中 reviewer 会觉得旧 |
| **gpt-4o-mini** | 2024-07 | **过时** — 被 gpt-4.1-nano 取代 | ✅ 可用 | **替换为 `gpt-4.1-nano`** | gpt-4.1-nano 是当前最轻量 OpenAI 模型（2025-04），$0.1/M，代理已验证可用。同 weak tier 定位 |
| **gpt-4.1** | 2025-04 | **当前** — 仍是主流开发者模型 | ✅ 可用 | **保留** | 不到 1 年，EMNLP 2026 审稿时仍当前 |
| **gpt-5.5** | 2026-04-23 | **最新** — OpenAI 旗舰 | ✅ 可用 | **保留** | 刚发布 1 个月，frontier 级 |
| **gemini-2.5-pro** | 2025-03 GA | **略旧** — Gemini 3.1 Pro 已出（2026-02），但代理没有 3.x | ✅ 可用 | **保留** | 代理上 Google 最强可用模型，无更新替代 |
| **gemini-2.5-flash** | 2026-02 GA | **当前** | ✅ 可用 | **保留** | Gemini 3 Flash 仅 preview，2.5-flash 是稳定版 |

---

### 推荐替换方案

替换 2 个，保留 4 个：

```
gpt-4o       →  gpt-4.1-mini    (mid tier, 2025-04)
gpt-4o-mini  →  gpt-4.1-nano    (weak tier, 2025-04)
gpt-4.1      →  保留
gpt-5.5      →  保留
gemini-2.5-pro   →  保留
gemini-2.5-flash →  保留
```

### 替换后完整 9 API 模型 + Tier 分配

| Tier | Anthropic | OpenAI | Google |
|---|---|---|---|
| **Strong** | claude-opus-4 | gpt-5.5 | gemini-2.5-pro |
| **Mid** | claude-sonnet-4 | gpt-4.1 | gemini-2.5-flash |
| **Weak** | claude-3-haiku | gpt-4.1-mini, gpt-4.1-nano | — |

优点：
1. **OpenAI 形成 gpt-4.1 家族梯度**（nano → mini → full）+ gpt-5.5 旗舰，比 gpt-4o/4o-mini 混搭更干净
2. **所有 6 个未跑模型都在代理上已验证可用**（`api_model_availability.json` 确认）
3. **最旧模型不超过 2025-04**（排除已锁定的 claude-3-haiku），EMNLP 2026 审稿时不会被视为过时
4. 三家厂商各 3/4/2 个，每家覆盖 strong+mid（+weak），family diversity 充分

### 额外可考虑（但不必要）

代理上还有 `o4-mini` 和 `gpt-5.4-mini`，如果想加 reasoning model 多样性可以替换某个 slot，但当前 9 模型已足够。

Sources:
- [Anthropic Models Overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- [Claude Opus 4.7, Sonnet 4.6, Haiku 4.5 Guide](https://www.knightli.com/en/2026/05/08/anthropic-claude-model-lineup/)
- [OpenAI Model Release Notes](https://help.openai.com/en/articles/9624314-model-release-notes)
- [Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
- [Retiring GPT-4o](https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models)
- [OpenAI o3 and o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/)
- [Gemini API Models](https://ai.google.dev/gemini-api/docs/models)
- [Gemini 2.5 Flash on OpenRouter](https://openrouter.ai/google/gemini-2.5-flash)
- [Gemini 2.5 Pro on OpenRouter](https://openrouter.ai/google/gemini-2.5-pro)
- [GPT-4.1 Mini on OpenRouter](https://openrouter.ai/openai/gpt-4.1-mini)
- [GPT-4.1 Nano on OpenRouter](https://openrouter.ai/openai/gpt-4.1-nano)
- [GPT-5.5 on OpenRouter](https://openrouter.ai/openai/gpt-5.5)
- [OpenRouter Models](https://openrouter.ai/models)

---
