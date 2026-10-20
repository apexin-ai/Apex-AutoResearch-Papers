# code check westb full status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_westb_full_status_20260517T100540_result.json`
- **Structured JSON:** [`61bd59d9443a25db048f.json`](../../sessions/61/61bd59d9443a25db048f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### gradient SFT (cuda:0) — 已完成 ✓
- tmux `scoring_ablation_v2` 显示 gradient SFT **18:02:59 完成**
- 完整模型已保存: `/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20/model.safetensors` (12.3GB)
- 训练参数: 2 epochs, final loss=0.644, token_accuracy=0.825
- cuda:0 当前 **空闲** (0 MiB)

### random scoring (cuda:1) — eval 进行中
- tmux `scoring_ablation_random`: 正在做 **random post-prune eval**
- 进度: 118/200 (59%), acc=0.37 @ 100/200
- PID 696141, 12889 MiB on GPU 1

### scoring_ablation_batch_v2 — 两个失败
1. **gradient SFT (旧)**: 在 step 935/1870 因磁盘满崩溃 (`No space left on device`)，但后来通过 `scoring_ablation_v2` 重新跑完了
2. **magnitude eval**: 跑到 60/200 被 Terminated, acc=0.0000 @ 50/200

### 已有结果
| 方法 | post-prune acc | post-SFT acc |
|------|---------------|--------------|
| gradient | 0.255 | **待跑** |
| magnitude | 0.000 (50 samples, 被kill) | 待跑 |
| random | ~0.37 (进行中) | 待跑 |

### tmux sessions
- `scoring_ablation_v2` — gradient SFT 已完成，idle
- `scoring_ablation_random` — random eval 进行中

**注意**: `gradient_sft_v3` tmux 不存在。磁盘 `/root/autodl-tmp` 93% (20GB free)。

### 下一步需要
1. **cuda:0 空闲 → 立即可跑 gradient post-SFT eval** (模型已在 `sft_gradient_20`)
2. random eval 完成后 → random SFT → random post-SFT eval
3. magnitude 需要重跑（之前 acc=0 且被 terminated，可能有问题）

是否要我在 cuda:0 上启动 gradient post-SFT eval？

---
