# LLM IAA API Key Fallback Evaluation

**Date**: 2026-05-18 | **DDL**: 2026-05-25 (7 days remaining)

## 服务器可用模型

**GPU**: 2x NVIDIA RTX PRO 6000 Blackwell (96GB VRAM each, 192GB total)

| 模型 | 路径 | 大小 | 是否被研究 |
|------|------|------|-----------|
| QwQ-32B | `.hf_cache/Qwen/QwQ-32B/` (14 shards) | ~65GB FP16 | **YES** |
| DeepSeek-R1-Distill-Qwen-32B | `.hf_cache/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B/` (8 shards) | ~65GB FP16 | **YES** |
| DeepSeek-R1-Distill-Llama-8B | `.hf_cache/deepseek-ai/DeepSeek-R1-Distill-Llama-8B/` (2 shards) | ~16GB FP16 | **YES** |
| DeepSeek-R1-Distill-Qwen-7B | HF hub cache | ~14GB FP16 | YES (same family as R1-8B) |
| OpenThinker-7B | HF hub cache | ~14GB FP16 | **YES** |
| BGE-large-en-v1.5 | `models/` | embedding only | N/A |
| e5-mistral-7b-instruct | HF hub cache | embedding only | N/A |

**关键发现**: 服务器上所有 instruction-tuned LLM 都是本研究的被研究模型 (QwQ-32B, R1-32B, R1-8B, OT-7B)。

## Trace 数据规模

| 模型 | Traces | Steps | Tokens | Avg tokens/trace |
|------|--------|-------|--------|-----------------|
| QwQ-32B | 95 | 4,852 | 78,641 | ~828 |
| R1-32B | 100 | 3,506 | 64,727 | ~647 |

CP 标注任务 token 估算 (per trace):
- Input: prompt template (~500) + full trace text (~1,500-3,000) = ~2,000-3,500 tokens
- Output: CP label + reasoning = ~50-150 tokens
- **100 traces total**: ~250K-400K input tokens, ~10K-15K output tokens

## 方案对比

| 方案 | 可行性 | 质量 | Circular 风险 | 时间 | 成本 |
|------|--------|------|--------------|------|------|
| 1. 本地模型 (vLLM) | 高 (192GB VRAM) | 高 (32B) | **高**: 全部是被研究模型 | ~30min | 免费 (GPU 时间) |
| 2a. Groq (Qwen3-32B) | 高 (免费) | 高 (32B reasoning) | **无**: 非被研究模型 | ~60-90min (rate limit) | 免费 |
| 2b. Google AI Studio (Gemini 2.5 Flash) | 高 (1500 req/day) | 中高 | **无**: 完全不同 model family | ~30min | 免费 |
| 3. Cross-model (R1 标注 QwQ, QwQ 标注 R1) | 高 | 高 | **中**: 同 Qwen 架构, reviewer 会质疑 | ~30min | 免费 |
| 4. 等 Claude API key | 不确定 | 最高 | **无** | <30min (once key available) | ~$1.50 |

### 方案详细分析

**方案 2a: Groq Free Tier (Qwen3-32B)** — 推荐
- Groq 免费 tier: 30 RPM, 6,000 TPM (部分资料称 30K TPM), 14,400 req/day
- Qwen3-32B 有 60 RPM 的更高限额
- 保守估算 6K TPM: ~3.5K tokens/req → ~1.7 req/min → 100 traces ~60min
- 乐观估算 30K TPM: ~8.5 req/min → 100 traces ~12min
- **关键优势**: Qwen3-32B 不是本研究的四个被研究模型之一, 完全消除 circular concern
- 注册即用, 无需信用卡

**方案 2b: Google AI Studio (Gemini 2.5 Flash)** — 备选
- 1,500 req/day, 1M context window
- 免费, 无需信用卡
- Gemini 是完全不同的 model family, 零 circular risk
- 但 CP 标注需要理解 reasoning trace 的内部结构, Gemini Flash 可能不如 reasoning-specialized 模型

**方案 1/3 的 Circular Concern 分析**:
- 本研究的 4 个被研究模型: QwQ-32B, R1-32B (DeepSeek-R1-Distill-Qwen-32B), R1-8B (DeepSeek-R1-Distill-Llama-8B), OT-7B (OpenThinker-7B)
- Cross-model (方案 3): 用 R1-32B 标注 QwQ traces 或反之。虽然不是 "同一个模型", 但两者都基于 Qwen-32B 架构, 且都是被研究对象。Reviewer 会合理质疑: "标注者本身就是被分析对象, 它对自己 reasoning 过程的理解可能有系统性偏差"
- 如果使用外部 7B 模型 (非被研究的): 质量不足, CP 标注需要对长 reasoning trace 的深入理解

## 推荐

**首选: 方案 2a (Groq Qwen3-32B)**

理由:
1. **零 circular concern**: Qwen3-32B 不在被研究模型列表中, 是独立第三方模型
2. **质量足够**: 32B reasoning model, 理解 trace 结构的能力有保障
3. **立即可用**: 免费注册, 无需等待审批
4. **时间可控**: 即使 rate limit 保守, 60-90 分钟可完成全部 100 条标注
5. **论文可辩护**: "We used Qwen3-32B (via Groq API) as an independent annotator" 比 "We used the studied models themselves" 干净得多

**操作步骤**:
1. 注册 Groq 账号 (groq.com)
2. 获取 API key
3. 写标注脚本, 用 OpenAI-compatible API format 调用 Qwen3-32B
4. 对 100 条 trace 执行 CP 标注
5. 与人工标注计算 Cohen's kappa

**Fallback**: 如果 Groq 不可用, 用 Google AI Studio (Gemini 2.5 Flash) 作为备选。

**方案 4 (等 Claude API key) 可以并行推进**: 先用 Groq 完成标注, 如果 Claude key 后续到位, 可以追加一轮 Claude 标注作为额外验证。
