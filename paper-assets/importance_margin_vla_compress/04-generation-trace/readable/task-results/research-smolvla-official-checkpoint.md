# research smolvla official checkpoint

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_smolvla_official_checkpoint_20260518T115208_result.json`
- **Structured JSON:** [`5261e4ee120177c803f8.json`](../../sessions/52/5261e4ee120177c803f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 官方 LIBERO finetuned checkpoint: **存在**

| 项目 | 值 |
|---|---|
| **Model ID** | `HuggingFaceVLA/smolvla_libero` |
| **Size** | ~1.22 GB |
| **Base model** | `lerobot/smolvla_base` |
| **论文报告训练配置** | batch_size=64, 100K steps, 只训练 action expert，VLM frozen |
| **论文报告 SR** | Spatial 90%, Object 96%, Goal 92%, Long 71%, **平均 87.3%** |
| **旧版 (deprecated)** | `HuggingFaceVLA/smolvla_libero_ckpts` → 已指向上面的新版 |

### 重要警告：复现问题

社区有多个 issue 报告无法复现 87.3%：
- [#1369](https://github.com/huggingface/lerobot/issues/1369) — 从头训练无法复现
- [#2354](https://github.com/huggingface/lerobot/issues/2354) — 无法复现 benchmark 结果
- [#3264](https://github.com/huggingface/lerobot/issues/3264) — **用官方 checkpoint eval 也无法复现**
- [#3287](https://github.com/huggingface/lerobot/issues/3287) — 询问精确训练配置（batch size, LR, commit hash）

这意味着：
1. 官方 checkpoint 存在且可下载，但用它直接 eval 可能因 lerobot 版本/eval 协议差异拿不到 87.3%
2. 论文的 87.3% 可能依赖特定 lerobot commit 和 eval 设置

### 对我们项目的影响

可以直接下载 `HuggingFaceVLA/smolvla_libero` 做 pruning 实验。即使 eval SR 不到 87.3%，只要比我们 batch_size=4 的 44.8% baseline 显著更高，就足以验证 cliff-edge 在强 baseline 上的存在。关键是要用**同一 eval 流程**对比 pruned vs unpruned，保证内部一致性。

Sources:
- [HuggingFaceVLA/smolvla_libero](https://huggingface.co/HuggingFaceVLA/smolvla_libero)
- [SmolVLA paper (arXiv:2506.01844)](https://arxiv.org/abs/2506.01844)
- [Issue #3287 - Training config inquiry](https://github.com/huggingface/lerobot/issues/3287)
- [Issue #3264 - Cannot reproduce with official checkpoints](https://github.com/huggingface/lerobot/issues/3264)
- [HuggingFaceVLA/smolvla_libero_ckpts (deprecated)](https://huggingface.co/HuggingFaceVLA/smolvla_libero_ckpts)
- [SmolVLA docs](https://huggingface.co/docs/lerobot/smolvla)
- [LIBERO Leaderboard](https://huggingface.co/spaces/HuggingFaceVLA/libero-vla-leaderboard)

---
