# code exp51 oasst2 download

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp51_oasst2_download_20260522T092313_result.json`
- **Structured JSON:** [`e71a8a94c6dc8353cae7.json`](../../sessions/e7/e71a8a94c6dc8353cae7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

格式和数量都正确。

另外注意到 `lmsys_benign_200.json` 里 source 是 "ultrachat"（合成数据），需要提醒。

---

## 数据质量报告

| 项目 | 值 |
|------|-----|
| **数据集** | OpenAssistant/oasst2 |
| **数据性质** | 真实众包人类对话（非 LLM 生成） |
| **总消息数** | 128,575 |
| **对话树数** | 13,162 |
| **筛选后池** | 454 条（英文 + ≥3 用户轮 + benign） |
| **平均用户轮数** | 3.0 |
| **轮数分布** | 全部为 3 轮（oasst2 树结构偏浅，满足 ≥3 轮条件的路径大多恰好 3 轮） |
| **评估集** | 200 条 → `oasst2_benign_eval_200.json` |
| **适配集** | 50 条 → `oasst2_benign_adapt_50.json` |

**前 3 条样本（首轮用户消息）：**
1. "What is miming and where did it first appear?"
2. "What are some advantages of film cameras compared to digital ones?"
3. "Can you give me a list of tips and tricks as a new Valheim player? I want it to have as few spoilers as possible."

**与 WildChat 的区别：**
- oasst2 是 Open Assistant 项目的众包标注数据，志愿者按提示写对话并互评排名，对话质量经过人工筛选
- WildChat 是 GPT-3.5/4 用户的自然使用日志，反映真实用户行为分布，话题更广更随机
- oasst2 树结构偏浅（多数路径 3 轮），WildChat 多轮对话更长

**注意：** 已有的 `lmsys_benign_200.json` 实际 source 为 "ultrachat"（合成数据），如需用于 exp51 评估应替换为本次生成的 oasst2 数据。

---
