# ops check and fill westd41074 westd27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-and-fill-westd41074-westd27271_20260521T071705_result.json`
- **Structured JSON:** [`6be130639b54d2973dd7.json`](../../sessions/6b/6be130639b54d2973dd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both random k=0.5 and k=0.3 都落到了 GPU 0（CUDA_VISIBLE_DEVICES=1 在 nohup 链中未生效）。GPU 0 有 98GB 显存充足（当前仅用 ~21GB），两实验可以并行跑完，只是稍慢。GPU 1 仍空闲。

---

## 汇总报告

### westd-41074 (4× RTX PRO 6000 Blackwell 98GB)

| GPU | 进程 | 状态 |
|-----|-------|------|
| 0 | π0.5 random k=0.5 (PID 912506) + random k=0.3 (PID 914719) | RUNNING (共享 GPU 0, ~21GB/98GB) |
| 1 | — | **空闲** |
| 2 | PID 68539 (训练, 29GB) | 运行中 |
| 3 | PID 738642 (训练, 28GB) | 运行中 |

**π0.5 L2norm k=0.5 结果 (DONE, negative):**
- **Overall SR = 33.4%** (167/500, 95.6min)
- Baseline = 76% → **下降 42.6pp**
- Per-task: 0% (salad dressing, bbq sauce) ~ 64% (milk)
- **结论: π0.5 对 L2norm pruning 不免疫。** 尽管 CV=0.055（近均匀 importance），L2norm 仍然造成严重性能下降。这意味着 "低 CV → 免疫" 假设**只对 random pruning 成立，L2norm 另有机制**。

**π0.5 random k=0.5:** 原 PID 899206 因网络不可达（tokenizer 下载失败）崩溃，已用 `HF_HUB_OFFLINE=1` 重启为 PID 912506。

**π0.5 random k=0.3:** 新启动 PID 914719，已通过 tokenizer 加载，正在 eval。

**注意:** `CUDA_VISIBLE_DEVICES=1` 在 `bash -c "... && VAR=val nohup python ..."` 链中不生效，需要改用 `export CUDA_VISIBLE_DEVICES=1` 形式。两进程共享 GPU 0 但显存充足。

### westd-27271 (2× RTX PRO 6000 Blackwell 98GB)

| GPU | 进程 | 状态 |
|-----|-------|------|
| 0 | M128 eval v2 (PID 188254) | RUNNING |
| 1 | PID 921279 (42GB) | 运行中 |

**M128 eval v2:** 运行 ~57min，第一个 task 完成 7/50 episodes，**全部 FAIL**（每个 episode 都跑满 280 步超时）。每 episode ~8 min 非常慢。按此速率完成 10 tasks × 50 eps 需要 ~66 小时。前 7 eps 全 FAIL 强烈暗示模型输出有问题（actions 不驱动任何有效行为）。

### Registry 更新
- `eval_pi05_l2norm_k05_object_seed42`: **DONE (negative)**, SR=33.4%
- `eval_pi05_random_k05_object_seed42`: RUNNING (restarted, noted)
- `eval_pi05_random_k03_object_seed42`: **新建 RUNNING**

---
