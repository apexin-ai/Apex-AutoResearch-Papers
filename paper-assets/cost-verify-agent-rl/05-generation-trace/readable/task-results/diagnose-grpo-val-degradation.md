# diagnose grpo val degradation

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_grpo-val-degradation_20260515T042229_result.json`
- **Structured JSON:** [`8ce0b47830a9cbe74220.json`](../../sessions/8c/8ce0b47830a9cbe74220.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告写入 `/root/cost-verify-agent-rl/RAGEN/artifacts/grpo_val_degradation_diagnosis.md`。

## 核心结论

**根因是 prompt 格式分布偏移**：SFT 训练（`sft_train_v2.py`）使用简化 ChatML 格式（原始 observation + `&lt;answer>` 标签指令），但 GRPO val 使用 RAGEN ctx_manager 构建的完全不同格式（"Turn N: State:" wrapper + 矛盾的系统提示 + 轮间 Reward 消息）。

三个差异叠加导致退化：

1. **格式偏移**：模型从未在训练中见过 GRPO 的 prompt 格式
2. **系统提示自相矛盾**：env_instruction 说"不要用标签"，per-turn FORMAT_PROMPT 说"用 `&lt;answer>` 标签"
3. **低温放大**：temp=0.4 确定性地选择了模型在陌生格式下的错误偏好（GRPO train 用 temp=1.0 反而得 70.3%，被随机性部分掩盖）

采样参数（temperature/top_p/top_k）已验证正确应用，不是原因。

**推荐修复**：对齐 GRPO env_instruction 和 turn formatting 到 SFT 训练数据的格式，消除分布偏移。

---
