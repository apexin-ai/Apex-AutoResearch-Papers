# ops check cuda2 ckpt40 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cuda2-ckpt40-eval_20260514T212431_result.json`
- **Structured JSON:** [`15ee1db5bafc6d5a8850.json`](../../sessions/15/15ee1db5bafc6d5a8850.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### cuda:2 — ckpt-40 eval: **ALIVE**
- PID 100549/100555 均存活，运行 12 分钟
- GPU 2 占用 9710 MiB
- 推理进度：**7/62 batches (11%)**，速率 ~93s/batch，预计还需 ~85 分钟完成
- 985 个 eval 文档，12275 gold triples

### cuda:0 — P0 GRPO 训练: **ALIVE**
- PID 90080/90085 均存活，运行 1h45m
- 训练进度：**step 55/200 (28%)**，速率 ~115s/step
- 已保存 checkpoint-20 和 checkpoint-40
- ⚠️ **KL 爆炸**：step 30 时 KL=70285858019737.61（阈值 100），但后续 step 已恢复正常（step 33: KL=0.157，step 34: KL=0.006）
- reward 趋势向好：step 34 的 mean reward=0.318，format_reward=0.201，f1_reward=0.038，ced_reward=0.079
- 预计剩余 ~4.7h 完成全部 200 步

---
