# code exp15c roberta large mlm

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp15c-roberta-large-mlm_20260519T112517_result.json`
- **Structured JSON:** [`6696aabf095e9bca67d5.json`](../../sessions/66/6696aabf095e9bca67d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- 脚本 `scripts/exp15c_roberta_large_mlm.py` 已写入服务器
- 训练已通过 `submit_training_job` 提交到 westd-33183 cuda:0
- Registry 已更新（hypothesis, spec, status=RUNNING）

流程：MLM DAPT (4 epochs, lr=2e-5, batch=8) → 冻结 encoder → 3 seeds GRU 训练 → DD OOD + ActorAttack 评估 (K=1,3,Full) → 结果存 `results/exp15c_roberta_large_mlm.json`。

---
