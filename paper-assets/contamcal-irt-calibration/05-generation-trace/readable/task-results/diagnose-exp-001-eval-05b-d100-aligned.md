# diagnose exp 001 eval 05B d100 aligned

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_eval_05B_d100_aligned_20260514T151255_result.json`
- **Structured JSON:** [`505f2441b9c8427a8539.json`](../../sessions/50/505f2441b9c8427a8539.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**进程状态**: PID 389866 **活着且正常运行**（state=R, 167213 CPU ticks, GPU 2 占用 3686MiB, 37% utilization）。启动于 22:47，已运行约 28 分钟。

**根因**: Cron 误报。进程正常运行，但 cron 监控检测不到它，原因如下：
1. **stdout/stderr 输出到 `/dev/pts/5`（终端）**，不是日志文件——没有 sentinel 文件供 cron 检查
2. **没有 W&B 集成**
3. **输出目录为空**——evaluate.py 在全部 benchmark 完成后才写 `eval_results.json`/`correctness_matrix.json`/`item_responses.json`
4. **tmux session 已死但 python 进程存活**（与之前 notes 一致）

**前一个 batch 运行** (`exp_001_eval_05B_aligned_batch.log`) 在做 d005 GSM8K 到 37%（492/1319）时超时退出（EXIT_CODE=124）。当前 PID 389866 是专门针对 d100_s42 aligned 的独立重试。

**预估进度**: 对 0.5B 模型，MMLU(~5min) 应已完成，GSM8K(~116min total) 约在 22%。预计还需 ~2 小时完成全部 4 个 benchmark。

```json
{
  "root_cause": "Cron 误报——进程存活但 stdout 输出到终端(/dev/pts/5)而非日志文件，无 sentinel 文件且无 W&B run，cron 5次检测均未发现活跃标记，误判为死亡",
  "error_type": "infrastructure",
  "process_alive": true,
  "partial_results": {
    "mmlu": "in_progress (likely done, not yet written to disk)",
    "gsm8k": "in_progress (~22% estimated)",
    "arc": "pending",
    "humaneval": "pending"
  },
  "output_dir": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned",
  "fix_steps": [
    "无需干预——进程正常运行，等待约2小时自然完成",
    "可选：重新 attach 一个 tmux session 监控进度（cat /proc/389866/stat 观察 utime 增长）",
    "后续：batch 启动脚本应将 stdout 重定向到日志文件，并在开始时写 sentinel，避免 cron 误报"
  ],
  "can_auto_fix": false
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "Cron 误报——进程存活但 stdout 输出到终端(/dev/pts/5)而非日志文件，无 sentinel 文件且无 W&B run，cron 5次检测均未发现活跃标记，误判为死亡",
    "error_type": "infrastructure",
    "process_alive": true,
    "partial_results": {
      "mmlu": "in_progress (likely done, not yet written to disk)",
      "gsm8k": "in_progress (~22% estimated)",
      "arc": "pending",
      "humaneval": "pending"
    },
    "output_dir": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s42_aligned",
    "fix_steps": [
      "无需干预——进程正常运行，等待约2小时自然完成",
      "可选：重新 attach 一个 tmux session 监控进度（cat /proc/389866/stat 观察 utime 增长）",
      "后续：batch 启动脚本应将 stdout 重定向到日志文件，并在开始时写 sentinel，避免 cron 误报"
    ],
    "can_auto_fix": false
  }
}
```

</details>

---
