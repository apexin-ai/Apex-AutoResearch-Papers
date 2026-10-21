# ops investigate ckpt40 eval crash

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate-ckpt40-eval-crash_20260514T213326_result.json`
- **Structured JSON:** [`4a300e13fea93a878cd5.json`](../../sessions/4a/4a300e13fea93a878cd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调查结论

### 进程状态
**PID 101842 仍在运行**，占用 cuda:2（9710MiB / 32607MiB, 62% util）。

### 时间线
1. **05:12** — `eval_lr5e6_ckpt40.sh` 通过 `batch_eval` 启动 inference 子进程
2. **05:12→05:29** — inference 运行到 16%（10/62 batches），速度 ~93s/batch
3. **~05:29** — inference 子进程被 **SIGTERM** (exit -15) 杀掉。batch_eval 记录 "Failed: 1"
4. **05:25** — PID 101842 被重新启动为**直接 `freige.eval.inference` 调用**（非 batch_eval），输出目录改为 `/root/autodl-tmp/eval_results/lr5e6_r1_ckpt40/checkpoint-40`

### 关键发现
- **不是崩溃/OOM**。SIGTERM（信号15）是人为或程序发送的终止信号，不是内核 OOM killer（那个发 SIGKILL/信号9）
- **已被重启**。当前 PID 101842 的 cmdline 指向不同的 output_dir（`lr5e6_r1_ckpt40` vs 日志中的 `grpo_ced_lr5e6`），说明有人（或 cron）在原始失败后手动重启了 eval
- **当前仍在推理中**。output dir 为空（无 metrics.json），进程创建于 05:25，按 ~93s/batch 推算 62 batches 约需 96 分钟，预计 **~06:55-07:00** 完成
- **原始 batch_eval 无结果**。`grpo_ced_lr5e6/checkpoint-40/` 和 `summary.json`（`{}`）均为空

### 判断
原始 batch_eval 的 inference 子进程被 SIGTERM 杀掉（原因不明，可能是 batch_eval 自身的超时机制，或外部干预）。随后 eval 被以直接 inference 方式重启，**当前正在正常运行**，无需干预。等待 ~80 分钟后检查结果即可。

---
