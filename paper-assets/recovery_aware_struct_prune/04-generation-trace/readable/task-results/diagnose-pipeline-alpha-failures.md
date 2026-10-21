# diagnose pipeline alpha failures

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_pipeline_alpha_failures_20260522T065330_result.json`
- **Structured JSON:** [`e993899293e4db38ee5d.json`](../../sessions/e9/e993899293e4db38ee5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整分析：

**实际时间线（两个实验相同）：**
1. 14:07 — Pruning 开始 → 14:08 完成 ✓
2. 14:11 — SFT 开始（7473 samples, 2 epochs）
3. 14:40 — SFT 完成，模型已保存 ✓（12.3GB model.safetensors）
4. 14:40-14:45 — 中间 GSM8K eval 完成
5. 14:45 — **GRPO v4 训练开始**（5604 steps）
6. ~14:48 — **两个进程同时被 kill 于 step 15/5604**

**关键修正：被 kill 的不是 SFT，是 GRPO 阶段。** SFT 已全部完成。

**证据：**
- alpha0p5 日志末尾：step 15 进度条后无任何输出（SIGHUP 断开）
- alpha2p0 日志末尾：step 15 后紧跟 `Terminated`（SIGTERM）
- 无 tmux session 存活（`tmux ls` 返回空）
- dmesg/journalctl 无 OOM 记录
- 磁盘充足（数据盘 200GB 空闲，根分区 25GB）
- GPU 2/3 当前完全空闲（0 MiB）

**已保存的产出：**
- `pruned_rasp_alpha0p5_20/` ✓
- `pruned_rasp_alpha2p0_20/` ✓
- `sft_rasp_alpha0p5_20/` ✓（完整）
- `sft_rasp_alpha2p0_20/` ✓（完整）
- `grpo_rasp_alpha0p5_20/completions/completions_00010.parquet` — 仅 step 10 的 1 个 parquet

```json
{"root_cause":"tmux session destroyed → SIGHUP(129)/SIGTERM sent to both GRPO processes at step 15/5604 (~14:48). SFT phase already completed at 14:40. Log evidence: alpha0p5 ends abruptly at step 15 progress bar; alpha2p0 shows explicit 'Terminated' after step 15. No OOM in dmesg, disk adequate (200GB free).","error_type":"infrastructure","fix_steps":["从已保存的 SFT 模型直接启动 GRPO（跳过 prune 和 SFT）: sft_rasp_alpha0p5_20 → grpo, sft_rasp_alpha2p0_20 → grpo","用 nohup 或持久 tmux session 启动，防止再次被 session 断开 kill","分别在 cuda:2 和 cuda:3 上启动（当前空闲）","删除已有的不完整 grpo_rasp_alpha{0p5,2p0}_20/ 目录后重启"],"can_auto_fix":true,"affects_both":true,"shared_cause":"两个进程在同一时刻（~14:48）被外部 session 终止（tmux session 被销毁或 reconcile_crons 清理），导致 SIGHUP/SIGTERM。Prune 和 SFT 均已完成，仅 GRPO 需要重跑。"}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "tmux session destroyed → SIGHUP(129)/SIGTERM sent to both GRPO processes at step 15/5604 (~14:48). SFT phase already completed at 14:40. Log evidence: alpha0p5 ends abruptly at step 15 progress bar; alpha2p0 shows explicit 'Terminated' after step 15. No OOM in dmesg, disk adequate (200GB free).",
    "error_type": "infrastructure",
    "fix_steps": [
      "从已保存的 SFT 模型直接启动 GRPO（跳过 prune 和 SFT）: sft_rasp_alpha0p5_20 → grpo, sft_rasp_alpha2p0_20 → grpo",
      "用 nohup 或持久 tmux session 启动，防止再次被 session 断开 kill",
      "分别在 cuda:2 和 cuda:3 上启动（当前空闲）",
      "删除已有的不完整 grpo_rasp_alpha{0p5,2p0}_20/ 目录后重启"
    ],
    "can_auto_fix": true,
    "affects_both": true,
    "shared_cause": "两个进程在同一时刻（~14:48）被外部 session 终止（tmux session 被销毁或 reconcile_crons 清理），导致 SIGHUP/SIGTERM。Prune 和 SFT 均已完成，仅 GRPO 需要重跑。"
  }
}
```

</details>

---
