# code exp021 ragen sft v4

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp021-ragen-sft-v4_20260515T020209_result.json`
- **Structured JSON:** [`17c0fb7b1a276541b3a9.json`](../../sessions/17/17c0fb7b1a276541b3a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练稳定运行，~9.3s/step，预计总时长 ~50 分钟。

## 产出总结

### 1. RAGEN 精确格式文档

| 组件 | RAGEN 运行时格式 |
|------|-----------------|
| **System** | `"You're a helpful assistant. "` + AlfworldSG env_instruction (含 "Do NOT wrap" + 示例) |
| **User Turn 1** | `\nTurn 1:\nState:\n{obs}\nYou have 50 actions left. Always output: &lt;think>...&lt;/think> &lt;answer>...&lt;/answer> with no extra text. Strictly follow this format. Max response length: 512 words (tokens).\n` |
| **User Turn 2+** | `Reward:\n0.0\n` + Turn N state content (同上) |
| **Assistant** | `&lt;think>[Assessment]...[Suggestion]&lt;/think>&lt;answer>action&lt;/answer>` |
| **Action 解析** | `_parse_response`: 先匹配 `&lt;answer>` 标签，fallback 匹配 `&lt;/think>` 后裸文本 |

源码位置：`ctx_manager.py:_build_system_content` (L577), `_build_turn_state_content` (L656), `_parse_response` (L201)

### 2. 转换脚本
`/root/autodl-tmp/expert_sft_v4/convert_sft_to_ragen_format.py`

### 3. v4 数据
- Train: 2546 samples (3-40 turns), val: 133 samples
- 路径: `/root/autodl-tmp/expert_sft_v4/expert_sft_{train,val}.jsonl`

### 4. exp021 训练
- PID: 406279, tmux session: `exp021_ragen_sft_v4`
- Base: exp008_sft/final → LR=5e-6, 2 epochs, 320 steps
- 输出: `/root/autodl-tmp/checkpoints/exp021_ragen_sft_v4/`
- 预计 ~50 分钟完成
- 日志: `/root/runs/cost-verify-agent-rl/exp021_ragen_sft_v4.log`

训练完成后需要用 RAGEN `val_before_train` 验证（非 eval_sft_fast）。Pass 条件：success >= 10%, action_is_valid >= 85%。

---
