# research selfguide setup audit

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_selfguide_setup_audit_20260516T031219_result.json`
- **Structured JSON:** [`9411fc41c010b0d90a2a.json`](../../sessions/94/9411fc41c010b0d90a2a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/exp028c_selfguide_recipe/report/selfguide_setup_audit.md`。

核心发现：

**5 个根本差异**（任何一个都可能独立导致 val 不动）：

1. **Step-independent 训练模式** — 最大嫌疑。RAGEN 把 50 步 episode 切成 history_length=2 的独立样本，完全破坏长程信用分配。verl-agent 是 episode-level 训练。gamma=0.95^49 = 7.7%，第 1 步几乎无梯度。

2. **Prompt 格式矛盾** — AlfworldSG 的 system prompt 示例用 `&lt;think>...&lt;/think>go to desk 1`（bare action），但 RAGEN 每个 turn 注入 `Always output: &lt;think>...&lt;/think>&lt;answer>...&lt;/answer>`。两个指令互相矛盾。

3. **Self-guidance reward 完全缺失** — 论文的核心贡献是 ±0.1 step-level reward 带来 8% 提升，我们要求模型输出 assessment 但没有解析/使用它作为 reward。当前是纯 sparse reward。

4. **Val 仅 16 episodes** — 分辨率 6.25%，无法检测小幅改进。Self-Guide 评 ~140 个。

5. **模型规模** — 论文主结果 Qwen3-4B，我们用 1.7B。

超参数层面（LR/KL/clip/temp 等）完全对齐，问题出在框架和方法论层面。

---
