# diag exp1 random b03 s43 fail

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp1-random-b03-s43-fail_20260514T233717_result.json`
- **Structured JSON:** [`d77df29ecf877e33b315.json`](../../sessions/d7/d77df29ecf877e33b315.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### exp1-random-b03-s43: 实际上训练成功完成

日志显示 **500/500 steps 全部跑完**，最终模型已保存：
```
2026-05-15 07:34:30 INFO Saving final model
2026-05-15 07:34:55 INFO Final reward stats: {'parse_rate': 1.0, 'prove_rate': 0.5505, 'mean_isr': 0.13576825459814446}
EXIT_CODE=129
```

EXIT_CODE=129 (SIGHUP) 发生在训练完成之后——tmux session 在脚本结束后收到挂断信号。**训练本身没有失败**，output 目录（31G）包含完整的 final model。

### 磁盘状态

```
/dev/md0  250G  181G  70G  73%
```

当前 **70GB 可用**（不是 96% 占用），足够提交下一个实验（预估 ~31G）。

主要占用：
| 目录 | 大小 | 状态 |
|------|------|------|
| exp1_random_b03_s43 | 31G | 刚完成（有效模型） |
| exp1_isr_b03_s43 | 31G | 已完成 |
| exp1_isr_b03_s44_r2 | 23G | **正在跑（GPU 0）** |
| plan006 × 4 | 64G | 旧实验 |
| plan018_random_b01_s44 | 16G | 旧实验 |
| plan009_sft_baseline | 7.6G | 旧实验 |

### GPU 状态

- **GPU 0**: 81419 MiB 占用（exp1_isr_b03_s44_r2 在跑）
- **GPU 1**: 0 MiB，完全空闲，干净可用

### 结论

- **失败原因**：不是失败。训练正常完成 500 steps，SIGHUP 发生在脚本退出后
- **剩余空间**：70GB，够用
- **cuda:1**：干净可用
- **可以安全提交 exp1-random-b03-s44**

如果后续需要更多空间，plan006 系列（64G）和 exp1_isr_b03_s43（31G）是最大的可清理候选。需要我清理吗？

---
