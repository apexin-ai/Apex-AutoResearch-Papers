# ssh exp001 llama arena hard

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp001_llama_arena_hard_20260522T015143_result.json`
- **Structured JSON:** [`6dd64aa77e8d330eb677.json`](../../sessions/6d/6dd64aa77e8d330eb677.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

收集正在稳定运行。状态总结：

**已完成 3 条 judgments：**
| 时间 | model_a vs model_b | position | score | 备注 |
|------|-------------------|----------|-------|------|
| 10:05:40 | gpt-3.5 vs gpt-4-0314 | AB | 0.0 (B wins) | 正确 |
| 10:06:44 | gpt-3.5 vs gpt-4-0314 | BA | 0.0 (B wins) | position swap 一致 |
| 10:07:28 | gpt-4-0314 vs gpt-4-0314 | AB | 0.5 (tie) | 自比较 = tie ✓ |

**运行参数：**
- 命令：`python -u collect.py --config config_llama_arena.yaml --benchmark arena_hard`
- tmux session: `exp001-llama`
- 输出：`/root/gated_mfrm_judge_bias/exp001/results/arena_hard_judgments.jsonl`

**速度与 ETA：**
- 每条 judgment 约 50 秒（70B AWQ 模型单序列推理）
- 总量：3000 条（500 prompts × 3 models × 2 positions AB/BA）
- 预估完成时间：~42 小时

**注意事项：**
1. `reference_model` 用的是 `gpt-4-0314`（Arena-Hard 标准 baseline），因为 gpt-4o 的 response 文件不存在
2. config 中修正了 `base_url: http://localhost:8001` 和 `model_name: llama-3.3-70b-instruct` 以匹配实际 vLLM 部署
3. 脚本支持断点续跑（读取已完成的 keys 跳过）

如果想加速，可以考虑将 `max_tokens` 从 1024 降到 512（实际 judge 输出通常 < 300 tokens），或启用 vLLM 并发请求。

---
