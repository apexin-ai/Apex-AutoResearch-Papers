# code exp008 sft pipeline

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp008_sft_pipeline_20260514T030317_result.json`
- **Structured JSON:** [`908621cb2addec70cafa.json`](../../sessions/90/908621cb2addec70cafa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出报告：exp008 SFT Warmup

### 1. 数据集统计

| 指标 | 值 |
|------|-----|
| 原始数据 | 1200 条（u-10bei/sft_alfworld_trajectory_dataset）|
| 转换成功 | **1200 条（0 过滤）** |
| 任务类型 | pick_and_place / clean_and_place / heat_and_place / cool_and_place / examine / pick_two（各 200） |
| 平均轮数 | 9.6 turns |
| 最大轮数 | 24 turns（< 30 上限） |
| Action 分布 | go: 6696, take: 1400, open: 1388, put: 1200, clean/heat/cool/use: 各 200 |

**格式样例**：
```
[system]: RAGEN system prompt (self-guidance assessment格式)
[user]: You are in the middle of a room...
[assistant]: &lt;think>[Assessment: neutral] [Reasoning: I should look for apple...] [Suggestion: go to microwave 1]&lt;/think>&lt;answer>go to microwave 1&lt;/answer>
[user]: The microwave 1 is open. In it, you see a mug 1.
[assistant]: &lt;think>[Assessment: negative] [Reasoning: apple is not here...] [Suggestion: go to cabinet 1]&lt;/think>&lt;answer>go to cabinet 1&lt;/answer>
```

### 2. 脚本路径
- 转换脚本：`/root/cost-verify-agent-rl/scripts/convert_sft_data.py`
- 训练脚本：`/root/cost-verify-agent-rl/scripts/sft_train.py`
- 转换数据：`/root/autodl-tmp/sft_data/alfworld_sft_ragen.jsonl`

### 3. Dry-run 结果
- **loss**: 3.025（step 1: 3.011, step 2: 3.040）
- **token accuracy**: 68.6%
- **grad_norm**: ~134
- **速度**: 2.06 s/step, 7.8 samples/s
- **状态**: 成功 ✓

### 4. 关键设计决策
- **自定义 ChatML 模板**：Qwen3 默认 template 会在中间轮次剥离 `&lt;think>` 内容，改用简化模板保留所有 `&lt;think>` 标签
- **Action 反推**：从 tool response 用 regex 反推 ALFWorld action（"You pick up X from Y" → "take X from Y" 等），100% 提取成功
- **SDPA attention**：服务器无 flash_attn，使用 SDPA 替代

### 5. 正式训练预估
- 225 steps × 2s/step ≈ **~8 分钟**
- Checkpoint 输出：`/root/autodl-tmp/checkpoints/exp008_sft/`

### 6. 后续需要 Main Agent 做
提交正式训练：
```bash
CUDA_VISIBLE_DEVICES=0 python /root/cost-verify-agent-rl/scripts/sft_train.py
```

---
