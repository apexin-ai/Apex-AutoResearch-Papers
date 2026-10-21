# research inference diff diagnosis

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_inference-diff-diagnosis_20260515T042541_result.json`
- **Structured JSON:** [`2abe979b565465f29e93.json`](../../sessions/2a/2abe979b565465f29e93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/inference_diff_diagnosis.md`。

**核心发现**（导致 action_is_valid 从 87.5% → 68.75% 的主因）：

1. **System prompt 自相矛盾** — RAGEN 的 AlfworldSG env_instruction 说"Do NOT wrap the action in any tags"，但 ctx_manager 在每轮 user content 中又说"Always output: `&lt;think>...&lt;answer>...&lt;/answer>`"。SFT eval 一致要求 `&lt;answer>` tags。模型收到矛盾指令，输出格式混乱。

2. **User content 格式 OOD** — SFT 模型训练时见的是裸 observation，RAGEN 在每轮加了 `Turn N:`、`You have X actions left`、FORMAT_PROMPT、LENGTH_PROMPT 等模板文本，加上 turn 间的 `Reward:` 反馈。输入分布偏移直接降低输出质量。

3. **top_p=1.0 vs 0.95** — RAGEN val 未设 top_p，默认 1.0（无 nucleus sampling），增加采到无效 action 的概率。

**修复优先级**：
1. 下个实验加 `val_kwargs.top_p: 0.95`
2. 统一 AlfworldSG env_instruction 的 `&lt;answer>` tag 指令与 SFT 训练一致
3. 评估 ctx_manager user content 格式是否需要与 SFT 训练对齐

---
