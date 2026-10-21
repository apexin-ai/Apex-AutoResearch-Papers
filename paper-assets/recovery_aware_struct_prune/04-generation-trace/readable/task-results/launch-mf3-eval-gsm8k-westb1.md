# launch mf3 eval gsm8k westb1

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_mf3_eval_gsm8k_westb1_20260522T093356_result.json`
- **Structured JSON:** [`34b84e46a75572221c89.json`](../../sessions/34/34b84e46a75572221c89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正常运行。GPU 1 99% 利用率，14603 MiB 显存。日志显示 0% 是 tqdm 的 `\r` 覆写导致，实际在跑。

```
GRPO 状态: 完成 (100/100, 1h38m31s, wandb: eushw8ks)
Eval 启动: 成功 PID=179898, 输出 → results/eval_gsm8k_grpo_qwen_math_cka_only_20.json
GPU 1 显存: 14603 MiB, 99% 利用率
Chat template: 已处理 (eval_gsm8k.py L154/L244 有 apply_chat_template)
```

**补充发现**:
- GPU 0 上有 alpha3.0 GRPO 训练在跑（PID 170676, 55min elapsed）
- 杀掉了一个重复的 eval 进程（PID 164705），它与我们的 eval 评估同一模型但输出路径不对，共享 GPU 1 会互相拖慢
- GSM8K eval 1319 样本 + max_new_tokens=2048，预计需要 1-2 小时完成

---
