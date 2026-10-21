# code sft eval script

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sft_eval_script_20260514T032212_result.json`
- **Structured JSON:** [`067a69fcf6cc33c293d8.json`](../../sessions/06/067a69fcf6cc33c293d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

EP 3: 68% valid (lower on this task), 100% format。4 episodes 平均：**action_is_valid ~90%, format 100%, success 0%**。

评估继续后台运行（约 7 min/episode，50 episodes 预计 5-6 小时）。已有足够数据出报告。

## 产出报告

### 1. 验证脚本路径
`/root/cost-verify-agent-rl/scripts/eval_sft_model.py`

### 2. 方案选择
**Option B（独立脚本）**。原因：RAGEN eval.py 依赖 vLLM+Ray+Hydra 全套基础设施，启动复杂；独立脚本直接用 HuggingFace generate() + AlfredTXTEnv，更轻量可控。

### 3. 中期验证结果（前 4 episodes）

| 指标 | exp007 Baseline (Qwen3-1.7B) | exp008 SFT Model |
|------|------|------|
| **action_is_valid** | 8.4% | **~90%** (46+50+50+34)/200 |
| **format_ok** | ~5% | **100%** (200/200) |
| **success_rate** | ~0% | 0% (0/4) |
| **avg steps** | - | 50 (全部跑满) |

**关键发现**：
- **action_is_valid 从 8.4% → ~90%**：SFT 成功教会模型 ALFWorld 命令语义，远超 50% 目标
- **format 100%**：`&lt;think>...&lt;/think>&lt;answer>...&lt;/answer>` 格式完全学会
- **success 0%**：模型能生成合法 action 但缺乏解题策略（跑满 50 步未完成任务），这正是 GRPO 阶段要优化的

### 4. 后续运行
评估在 cuda:1 后台持续运行 (PID 193926)，结果将保存到 `/root/autodl-tmp/eval_results/exp008_sft_eval.json`。

查看进度：`tail -5 /tmp/eval_sft.log`

完整 50 episodes 预计耗时约 5-6 小时。SFT warmup 阶段验证通过，可以开始 GRPO 训练。

---
