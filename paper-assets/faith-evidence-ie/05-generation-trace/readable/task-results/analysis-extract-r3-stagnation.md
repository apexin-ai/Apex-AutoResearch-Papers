# analysis extract r3 stagnation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_extract_r3_stagnation_20260514T152014_result.json`
- **Structured JSON:** [`0d7e22a4f2762a7d4033.json`](../../sessions/0d/0d7e22a4f2762a7d4033.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

- **停滞类型：不可恢复**
- **停滞起始 step：~70 / 总 756 steps**（仅用了 9% 的训练即崩塌）
- **grad_norm=0 前最佳 checkpoint：不存在**（所有 checkpoint 520-600 均在崩塌区，最早 checkpoint 也晚了 ~450 步）
- **建议：kill，所有 checkpoint 均无保留价值**

## 关键指标趋势

| 阶段 | Steps | grad_norm | entropy | completion_len | frac_zero_std | f1_reward |
|------|-------|-----------|---------|---------------|---------------|-----------|
| 健康期 | 5-65 | 0.2-3.1 | 0.07→0.04 | 707→84 | 0.25-0.75 | 0.02→0.51 |
| 崩塌拐点 | ~70 | →0.0 | →0.03 | →44 | →0.95 | →0.04 |
| 死区 | 70-490 | 偶发非零 | 0.02→0.01 | 44±2 | 0.85-1.0 | 0.02-0.53 |
| 完全死亡 | 490-608 | 全零 | 0.003-0.008 | 43±1 | 0.90-1.0 | 0.20-0.53 |

## 崩塌机制

经典 GRPO entropy collapse 链条：

1. **kl_coef=0.0** → 无参考策略锚定，模型可自由偏移
2. 模型在 ~65 步内学会输出极短模板（44 tokens），完成长度从 707 骤降
3. **num_generations=4 太少** → 4 个相同短输出 = 同一个 reward = reward_std=0
4. **frac_reward_zero_std 在 step 70 跳至 0.95** → 95% 的 batch 内 reward 无方差
5. GRPO advantage = (reward - mean) / std → 分母为零 → advantage=0 → grad_norm=0
6. 策略锁死，不可逆

## r4 修复建议

- `num_generations`: 4 → **8 或 16**（增加 batch 内多样性）
- `kl_coef`: 0.0 → **0.01-0.05**（防止策略过度偏移）
- 生成温度提高（如 1.2）或加 entropy bonus
- 前 100 步每 20 步存一个 checkpoint（健康期太短，当前 save_steps 太大错过了所有有用的状态）

---
