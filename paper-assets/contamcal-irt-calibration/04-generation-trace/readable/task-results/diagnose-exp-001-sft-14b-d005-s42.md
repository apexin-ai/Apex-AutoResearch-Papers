# diagnose exp 001 sft 14b d005 s42

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_001_sft_14b_d005_s42_20260518T190656_result.json`
- **Structured JSON:** [`c6d0854ae08b5d9b64cb.json`](../../sessions/c6/c6d0854ae08b5d9b64cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论：训练已正常完成，非真实失败

**证据：**

| 指标 | 值 |
|------|-----|
| `global_step` | 3177 / 3177 (100%) |
| `epoch` | 1.0 |
| `should_training_stop` | true |
| 最终 loss | ~0.85-0.95（从 1.44 正常收敛） |
| final adapter | 275MB, 2026-05-19 02:47 |
| lora_alpha | 32 ✓ |
| checkpoint-3177 | 完整（optimizer + scheduler + rng_state） |

**误判原因：**

1. **无 W&B 数据** — 脚本默认 `report_to="none"`，启动命令未覆盖
2. **无 sentinel 文件** — `train_sft.py` 不创建任何 sentinel（DONE/SUCCESS 标记）
3. **无 tmux 日志** — `/root/runs/` 下没有此实验的日志文件，说明可能未通过标准 tmux 日志管道启动
4. **PID 38915 不存在** — 进程正常退出（训练完成后退出），被监控系统误判为"死亡"

"连续死亡 5 次"很可能是监控重复检测到进程不存在后多次标记。

```json
{"root_cause":"训练已正常完成(epoch=1.0, step=3177/3177)，但因 report_to='none' 且脚本无 sentinel 文件机制，监控系统误判为进程死亡","error_type":"infrastructure","fix_steps":["将实验状态从 failed 改为 completed","注册产出 /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d005_s42/lora_adapter/","后续 14B 实验启动时添加 --report-to wandb 参数，或在脚本末尾添加 sentinel 文件写入"],"can_auto_fix":true}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "root_cause": "训练已正常完成(epoch=1.0, step=3177/3177)，但因 report_to='none' 且脚本无 sentinel 文件机制，监控系统误判为进程死亡",
    "error_type": "infrastructure",
    "fix_steps": [
      "将实验状态从 failed 改为 completed",
      "注册产出 /root/autodl-tmp/exp001/checkpoints/Qwen2.5-14B_d005_s42/lora_adapter/",
      "后续 14B 实验启动时添加 --report-to wandb 参数，或在脚本末尾添加 sentinel 文件写入"
    ],
    "can_auto_fix": true
  }
}
```

</details>

---
