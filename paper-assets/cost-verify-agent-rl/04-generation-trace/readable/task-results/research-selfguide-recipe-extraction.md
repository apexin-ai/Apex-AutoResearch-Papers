# research selfguide recipe extraction

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_selfguide_recipe_extraction_20260515T212518_result.json`
- **Structured JSON:** [`f298c9adc96efe909379.json`](../../sessions/f2/f298c9adc96efe909379.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/exp028c_selfguide_recipe/report/selfguide_grpo_recipe.md`。

核心发现：

**Self-Guide 论文只披露了 5 个参数**（总步数 100、max_prompt 4096、max_response 1024、episode 50 步、温度 1.0/0.4），其余参数未公开。但论文明确使用 verl-agent 框架，因此其他参数可从 GiGPO 论文附录 E.1 + verl-agent `run_alfworld.sh` 高置信度推断。

**exp027 与目标 recipe 的 11 项关键差异**（按影响排序）：

| # | 差异 | exp027 → exp028c |
|---|------|-------------------|
| 1 | SFT 起点 | SFT checkpoint → **Instruct cold-start** |
| 2 | Invalid action penalty | 0 (binary) → **-0.1** |
| 3 | Mini-batch size | 32 → **256** (8×) |
| 4 | 总训练步数 | 50 → **100** (2×) |
| 5 | LR | 5e-7 → **1e-6** (2×) |
| 6 | KL coef | 0.005 → **0.01** (2×) |
| 7 | Env groups | 8 → **16** (2×) |
| 8 | Group size | 16 → **8** (0.5×) |
| 9 | Entropy coef | 0.01 → **0.001** (10×降) |
| 10 | History length | 5 → **2** |
| 11 | Loss agg | seq-mean-token-mean → **token-mean** |

**硬件风险**：2×RTX PRO 6000 (48GB) vs 参考 2×H100 (80GB)，VRAM 少 40%。Qwen3-1.7B 较小应够用，但 4096 prompt + 16 env_groups 可能 OOM → 准备 fallback 到 2048/512。

---
