# research ood eval discrepancy

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ood_eval_discrepancy_20260519T132420_result.json`
- **Structured JSON:** [`55efd000f9c842ec6b6a.json`](../../sessions/55/55efd000f9c842ec6b6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。以下是完整对比分析。

---

## 参数对比表

| 参数 | RAGEN 内置 eval (reeval config) | 独立 eval 脚本 |
|------|------|------|
| temperature | **0.4** | **0.0 (greedy)** |
| do_sample | **True** | **False** (vLLM temp=0 隐式关闭) |
| top_p | 1.0 | 1.0 (vLLM 默认) |
| top_k | -1 | -1 (vLLM 默认) |
| max_tokens | 1024 (rollout.response_length) | 1024 |
| n_rollouts / group_size | 1 | 1 |
| max_turn | 50 | 50 |
| system_prompt | `"You're a helpful assistant. " + env_instruction` (SG prompt) | 基本相同的 SG prompt |
| stop tokens | 模型自行生成 EOS | `["&lt;/answer>"]` + include_stop_str |
| **observation 格式** | **带 turn 编号 + 剩余步数 + 格式提醒**: `"Turn X:\nState:\n{obs}\nYou have N actions left. Always output: &lt;think>...&lt;/think>&lt;answer>...&lt;/answer>..."` | **裸观测**: `"{obs}\n\nAdmissible actions: [...]"` |
| generation prefix | 强制追加 `&lt;think>` token (若 enable_think=True) | 无强制前缀 |

## 关键差异分析

### 1. Temperature (主因)
RAGEN 用 `temperature=0.4 + do_sample=True`（随机采样），独立脚本用 `temperature=0.0`（贪心解码）。ALFWorld 中模型需要探索不同位置找对象，温度 0.4 引入的随机性让一些贪心路径失败的 task 有概率"碰巧"成功。这是 **10 个 task 差异的最大来源**。

### 2. Observation 格式 (次因)
RAGEN 的 ctx_manager 在每个 turn 的 observation 中注入了：
- `Turn X:` 编号（让模型感知进度）
- `You have N actions left`（剩余预算）
- 格式提醒（`Always output: &lt;think>...&lt;/think>&lt;answer>...&lt;/answer>`）

独立脚本只传了裸 observation + admissible actions，没有这些 scaffolding。这些额外提示可能帮助模型在长 episode 中保持格式一致和策略连贯。

### 3. Stop token 处理 (轻微影响)
独立脚本显式用 `stop=["&lt;/answer>"]`，截断 `&lt;/answer>` 后的所有内容。RAGEN 让模型自行决定何时停止。这可能在极少数 case 下影响 action 解析。

## 结论

**差异根因**：温度 0.4 vs 0.0，辅以 observation 格式差异。

**论文应引用哪个数字**：取决于你的 eval protocol 设计：

- 若论文所有实验统一用 **greedy (temp=0.0)**：引用 **16.4%**，这是确定性、可复现的数字
- 若论文所有实验统一用 **temp=0.4**（与训练 eval 一致）：引用 **23.88%**
- **关键要求**：所有 cell（A/B/C/D）和 baseline 必须用 **同一套 eval 参数**，否则不可比

建议：用独立 eval 脚本（temp=0.0）统一重跑所有 checkpoint，确保 apple-to-apple 比较。如果论文已经在其他 cell 报了 RAGEN 内置 eval 的数字（temp=0.4），那 exp029 也应该用 RAGEN 内置 eval 的数字以保持一致。

---
