# ops fix 19828 env resubmit

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_19828_env_resubmit_20260520T231427_result.json`
- **Structured JSON:** [`6d4827234275996d4120.json`](../../sessions/6d/6d4827234275996d4120.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在正常运行。

**结果：**

| 实验 | 状态 | GPU | PID | 说明 |
|------|------|-----|-----|------|
| `scale_14b_a050_s42_bf16` | 无需修复，正常运行 | cuda:0 | 619323 | Gen 0 训练中，网络警告非致命 |
| `generalize_pythia1b_c4_a100_s43_v2` | 已修复并重新提交 | cuda:1 | 620796 | 模型加载成功，进入 Gen 0 |

**修复内容：** pythia-1b 的 HF hub 缓存 snapshots 目录为空（下载不完整），改用本地模型路径 `/root/autodl-tmp/.hf_cache/pythia-1b-local` 替代 `EleutherAI/pythia-1b`，同时保留 `TRANSFORMERS_OFFLINE=1` 和 `HF_HUB_OFFLINE=1` 防止网络请求。

---
