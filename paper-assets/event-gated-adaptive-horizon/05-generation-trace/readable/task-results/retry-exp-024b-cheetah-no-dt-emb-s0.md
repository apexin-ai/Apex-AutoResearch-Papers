# retry exp 024b cheetah no dt emb s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_retry_exp_024b_cheetah_no_dt_emb_s0_20260517T224923_result.json`
- **Structured JSON:** [`66e145234c1bf9cf615f.json`](../../sessions/66/66e145234c1bf9cf615f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常启动，已通过 prefill 阶段进入 step 5000 的 evaluation。

总结：
- 确认参数名为 `--gate_dt_embed_dim`（configs.yaml 中定义）
- 旧 exp_024 标记为 DONE(failed)，释放 cuda:0
- 新 exp_024b_cheetah_no_dt_emb_s0 已提交并成功启动（PID 705737, cuda:0, bjb1-45299）
- 训练已完成 prefill，正在运行 step 5000 evaluation

---
