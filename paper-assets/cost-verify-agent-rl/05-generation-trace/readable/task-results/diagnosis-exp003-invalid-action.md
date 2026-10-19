# diagnosis exp003 invalid action

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_exp003_invalid_action_20260513T235331_result.json`
- **Structured JSON:** [`b8e1e9dadc918bc215d3.json`](../../sessions/b8/b8e1e9dadc918bc215d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因：Qwen3-1.7B base 模型不生成 `&lt;answer>` 标签。**

因果链：
1. Qwen3 的原生 thinking 格式是 `&lt;think>reasoning&lt;/think> + 直接文本`，没有 `&lt;answer>` 标签
2. 模型输出 `&lt;/think>` 后继续生成自然语言（重复格式指令或自由文本），不产生 `&lt;answer>`
3. RAGEN 的正则 `&lt;think>(.*?)&lt;/think>\s*&lt;answer>(.*?)&lt;/answer>` 匹配失败 → `actions=[]`
4. `manager_invalid_action=95.3%`，`pg_loss≈0`

实验验证：32/32 样本全部确认此模式。Tokenizer 和 `skip_special_tokens` 不是问题。

修复建议优先级：SFT warmup > 修改解析器适配 Qwen3 格式 > 用 Instruct 模型（exp004 已在测试）。

报告已注册：`artifacts/exp003/report/exp003_invalid_action_diagnosis.md`

---
