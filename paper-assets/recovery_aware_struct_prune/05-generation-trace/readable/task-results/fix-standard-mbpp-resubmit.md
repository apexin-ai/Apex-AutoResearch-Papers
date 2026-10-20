# fix standard mbpp resubmit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_standard_mbpp_resubmit_20260519T222254_result.json`
- **Structured JSON:** [`13c74e80410f0bf320a0.json`](../../sessions/13/13c74e80410f0bf320a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 v4 eval 都**正在运行中**，无需重新提交。

## 当前状态

| Session | GPU | 进度 | Pass@1 | 状态 |
|---------|-----|------|--------|------|
| `eval_mbpp_sft_standard_20_v4` | cuda:0 (98% util, 17277 MiB) | 85/374 (23%) | 0.1750 | **运行中** |
| `eval_mbpp_grpo_standard_20_v4` | cuda:2 (97% util, 17019 MiB) | 108/374 (29%) | 0.1100 | **运行中** |

## 关键细节

- **MBPP 数据集缓存**: `/root/autodl-tmp/.hf_cache/datasets/mbpp/full/0.0.0/4bb6404fdc6cacfda99d4ac4205087b89d32030c`
- GRPO v4 最初在线下载了数据集（网络当时可用），现在 SFT v4 使用了离线缓存
- 两个 eval 都已正确设置 `HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1`
- 第三个 session `cka_stability` 也在运行（GPU 1 和 3 空闲，该 session 可能使用其他资源）

**不需要重新提交。两个 v4 eval 都在正常跑，预计还需 2-4 小时完成。**

---
