# 诊断报告: v4-taxei-recovery-eval

**日期**: 2026-05-14
**结论**: **误报 — 实验正常完成，非失败**

## 失败根因

**无失败。** 实验 47/47 任务全部跑完，结果文件完整写入。cron 监控检测到进程退出（正常退出）后判定为 dead，属于**误报**。

原因：该实验是 eval 任务（非长时间训练），进程正常退出后 PID 消失，cron 5 次检测均为 dead，触发 failed 判定。但进程是正常退出（exit code 0），不是 crash。无 W&B 指标是因为 `injected_eval.py` 未集成 W&B logging，属预期行为。

## 关键日志

日志位置：`/tmp/v4_taxei_recovery_eval.log`（7622 bytes）

```
Found 47 tasks in valid_unseen
Loading base model: /root/autodl-tmp/models/Qwen/Qwen3-8B
Loading LoRA adapter: .../checkpoint-3387
  [1/47] ... OK
  ...
  [47/47] ... FAIL (正常的任务失败，非crash)

Report saved to eval_results/v4_taxei_recovery_eval.json

=== Injected Eval Summary (taxei) ===
Total: 47
Recovery rate (task success): 0.596
Detection rate (think analysis): 0.0
```

注意：日志中有 `bitsandbytes library load error: libnvJitLink.so.13` 警告，未影响运行（非致命错误）。

## 结果数据

输出文件完整：`eval_results/v4_taxei_recovery_eval.json`（482KB, 13427行）

| 指标 | 值 |
|------|-----|
| total_episodes | 47 |
| success/recovery_rate | 0.596 |
| detection_rate | 0.0 |

Per-operator:
- C1_context_truncation: 8/12 (0.667)
- C4_observation_masking: 7/11 (0.636)
- P1_step_order_swap: 7/12 (0.583)
- P2_sub_goal_deletion: 6/12 (0.5)

## 部分结果可回收

**全部结果可用，无需回收。** 结果文件完整，包含 47 个 episode 的详细 step-by-step trajectory。

## 其他实验状态

**v4-vanilla-recovery-eval** 也已正常完成：
- 输出：`eval_results/v4_vanilla_recovery_eval.json`（476KB）
- Recovery rate: 0.617, Detection rate: 0.0
- 所有 GPU 当前空闲（0 MiB / 32607 MiB × 4）
- 无运行中的实验进程

## 重试建议

**无需重试。** 实验已成功完成。建议：
1. cron 监控逻辑改进：对 eval 类任务，检查输出文件是否存在且完整，而非仅依赖进程存活状态
2. eval 脚本未集成 W&B，cron 以"无 W&B 指标"作为 failed 依据不适用于 eval 任务

## GPU 状态

```
GPU 0: 0 MiB / 32607 MiB, 0% util
GPU 1: 0 MiB / 32607 MiB, 0% util
GPU 2: 0 MiB / 32607 MiB, 0% util
GPU 3: 0 MiB / 32607 MiB, 0% util
```

所有 GPU 空闲，无运行中的实验。
