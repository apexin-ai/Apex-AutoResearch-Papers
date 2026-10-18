# infra gpu status check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-status-check_20260515T020802_result.json`
- **Structured JSON:** [`80f77c9bf3a14294b2a6.json`](../../sessions/80/80f77c9bf3a14294b2a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

- **cuda:0** — 占用 15,629 / 97,887 MiB (16%)，GPU 利用率 46%。占用进程 PID 233355：`generate_next_depth.py`（gpt2xl_topk50 pipeline 的 depth-3 生成阶段）
- **cuda:1** — 占用 58,733 / 97,887 MiB (60%)，GPU 利用率 99%。占用进程 PID 241774：`dcol_trainer.py`（dcol_v3 DeBERTa 训练）
- **PID 240552 (dcol_deberta_003)** — 已死。当前 dcol 训练是新进程 PID 241774，在 cuda:1 上跑
- **PID 211326 (gpt2xl_topk50_001)** — 存活。pipeline 已完成 depth-2 的 LoRA 训练（3 epoch，loss 1.755），正在执行 Step 5：用 depth-2 adapter 生成 depth-3 数据（top-k k=50），模型加载已完成，生成进行中
- **僵尸 GPU 进程** — 无。两张卡各跑一个有效任务

---
