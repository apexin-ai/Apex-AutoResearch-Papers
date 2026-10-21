# ops verify p0 startup

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-p0-startup_20260514T194102_result.json`
- **Structured JSON:** [`48c1710c40582bc05cb8.json`](../../sessions/48/48c1710c40582bc05cb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**P0 启动成功。**

| 检查项 | 状态 |
|--------|------|
| 进程 PID 90080 | 存活，运行 1 分 18 秒 |
| 模型加载 | Qwen3-4B (4-bit QLoRA) + SFT adapter 合并完成 |
| NLI reward 模型 | `cross-encoder/nli-deberta-v3-base` 加载成功，entailment_index=1 |
| 数据集 | 3053 docs → 38180 relation samples → 3027 GRPO prompts |
| 训练状态 | Stage 3 GRPO 已启动，CED reward，tau 0.30→0.50，0/200 steps |
| GPU 0 | 7527 MiB 占用，63% 利用率 |

关键参数确认：`lr=5e-6`, `max_steps=200`, `num_generations=8`, `ced_reward_weight=1.0`, `f1_reward_weight=3.0`, `format_reward_weight=0.3`, `kl_coef=0.01`。

有两个非阻塞 warning：vLLM 版本 0.18.1 超出 TRL 支持范围（0.11-0.17.1），4-bit LoRA merge 精度警告。均不影响训练。

---
