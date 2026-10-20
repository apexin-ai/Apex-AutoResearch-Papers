# code instruction retention test

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_instruction_retention_test_20260521T025340_result.json`
- **Structured JSON:** [`719fa4ad39b35d91c11a.json`](../../sessions/71/719fa4ad39b35d91c11a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报：

## 1. Prompt 数据（18 个）

| check_fn | 指令类型 | 检测方式 |
|---|---|---|
| `bullet_points` | 每行以 `-` 开头 | ≥80% 行首匹配 |
| `start_sure` | 以 "Sure!" 开头 | startswith |
| `end_hope` | 以 "Hope that helps!" 结尾 | endswith |
| `one_emoji` | 恰好 1 个 emoji | Unicode range 计数 |
| `three_sentences` | 恰好 3 个句子 | 终止标点 + 空格/结尾 计数 |
| `mention_ai_assistant` | 包含 "AI assistant" | 子串匹配 (case-insensitive) |
| `no_the` | 不含 "the" | word boundary regex |
| `numbered_list` | 使用编号列表 | `^\d+\.` 行首匹配 ≥2 |
| `include_certainly` | 包含 "certainly" | 子串匹配 |
| `end_question` | 以 `?` 结尾 | endswith("?") |
| `all_caps` | 全大写 | ≥95% alpha 为大写 |
| `start_let_me_think` | 以 "Let me think..." 开头 | startswith |
| `no_commas` | 不含逗号 | `"," not in` |
| `include_remember` | 包含 "remember that" | 子串匹配 |
| `no_exclamation` | 不含感叹号 | `"!" not in` |
| `start_well` | 以 "Well," 开头 | startswith |
| `include_interesting` | 包含 "interesting" | 子串匹配 |
| `max_two_sentences` | ≤2 句 | 句子计数 ≤2 |

## 2. 脚本结构

- **模型加载**: 复用 `eval_attention_steering.load_model_eager()`（eager attention + LoRA + gate hooks）
- **对话生成**: 复用 `eval_attention_steering.generate_conversation()`（steering + gate + 逐 turn 生成）
- **GAR 测量**: 复用 `eval_attention_steering.measure_gar_and_ppl()`（teacher-forcing + steering + per-turn GAR）
- **Goal positions**: 复用 `eval_attention_steering.get_initial_goal_positions()`
- **新增**: 18 个 check function + `evaluate_prompt()` + `compute_summary()` + summary 打印

## 3. 运行命令

```bash
cd /root/turn_residual_gating
python src/eval_instruction_retention.py \
    --checkpoint runs/phase2_tg_s42_v7 \
    --prompts data/instruction_retention_prompts.json \
    --betas 0 3 \
    --output results/instruction_retention.json
```

**Summary 输出**：per-turn following rate、late-turn (turn 3-5) β=0 vs β=3 McNemar test、GAR × compliance point-biserial correlation。

---
