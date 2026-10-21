# check gpu and ss chain

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_and_ss_chain_20260523T070442_result.json`
- **Structured JSON:** [`4eedd925ecc657cf1d7c.json`](../../sessions/4e/4eedd925ecc657cf1d7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

### GPU 状态
- **RTX PRO 6000 (96GB)**，占用 11.5GB / 96GB，利用率 19%
- 当前进程：`eval_split_softmax.py` 正在跑 base model TF 模式（PID 81629）

### SS 实验链进度

| 环节 | 状态 |
|------|------|
| AR N=50 existing s42 eval | **已完成** — 结果在 `results/d048_ar_n50_existing/`（6个条件全部完成） |
| SS s123 train | **已完成** — 5月22日由 queue_runner 执行，eval 结果在 `runs/eval_v8b_ss_s123/` |
| SS s456 train | **失败 (OOM)** — Epoch 1 Step 3400 崩溃，只保存了 epoch_0。原因：PaperBanana 进程（PID 75061）同时占用 ~39GB GPU 显存导致 OOM |
| Split-softmax eval | **正在执行** — 刚启动（15:01），当前跑 base_tf_n50，`results/split_softmax/` 目录还是空的 |

### 关键问题
**SS s456 因 PaperBanana 抢显存而 OOM 崩溃。** d048_remaining_queue.sh 跳过了 s456 eval 直接进入 split-softmax eval。PaperBanana 进程（PID 75061）目前仍在运行。

### 下一步建议
- Split-softmax eval 正在跑，等它完成
- SS s456 需要重跑 — 等 PaperBanana 结束后单独启动，或先 kill PaperBanana 再跑
- GPU 当前不空闲，不能立即排新任务

---
