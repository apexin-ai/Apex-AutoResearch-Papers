# code e1d cleanup and grpo

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e1d_cleanup_and_grpo_20260518T124101_result.json`
- **Structured JSON:** [`d6cae07002c65d777d17.json`](../../sessions/d6/d6cae07002c65d777d17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

1. **磁盘清理**: 删除冗余 `model.safetensors` (~11.5GB)，数据盘从 5.8GB → 18GB 可用
2. **cuda:0 释放**: eval 批处理 (standard + cka_only 两个 1.5B 模型 quick eval) 自然完成后释放
3. **GRPO 启动**: PID 806188, W&B run `grpo_cka_only_20_1p5b` (8zkpr0hh), GPU 占用 ~63GB 生成中
4. **初始 log**: 模型加载正常 (非均匀 MLP [3738, 8960])，7473 训练样本，进度条 0/100 首步生成中
5. **预计完成时间**: 1.5B 模型 100 steps，每步约 3-5 分钟（含生成），预计 5-8 小时

---
