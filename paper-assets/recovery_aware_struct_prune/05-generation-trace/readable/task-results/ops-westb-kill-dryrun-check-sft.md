# ops westb kill dryrun check sft

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb-kill-dryrun-check-sft_20260516T052529_result.json`
- **Structured JSON:** [`6f9a2db11ab8aaca4ae5.json`](../../sessions/6f/6f9a2db11ab8aaca4ae5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中。

**汇报：**

1. **Dry run 进程**: 原始 PID 587393、587614 已不存在（自行退出）。额外清理了 PID 589182（dry run on cuda:0, 16GB）和 PID 590608（dry run on cuda:1, 45GB）。

2. **sft_standard_25**: 已成功重启并正在训练。
   - 7473 samples, 2 epochs, 1870 steps total
   - 当前进度: ~31/1870 steps, ~1.1s/step
   - 预计训练时间: ~34 分钟
   - loss logging 每 10 steps 一次

3. **当前 GPU 使用**:
   - cuda:0: 29653 MiB / 97887 MiB — PID 585623 eval_grpo_rasp_v9_step10（运行 ~35min）
   - cuda:1: 47705 MiB / 97887 MiB — PID 591607 sft_standard_25（正常训练中）

注意：之前启动失败的原因有两个：(1) `--per_device_train_batch_size` 应为 `--batch_size`；(2) `HF_HUB_OFFLINE=1` 阻止了 datasets 加载 GSM8K。已通过 `source /etc/network_turbo` + SSL 证书配置解决。

---
