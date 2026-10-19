# diagnose sft baseline ood eval v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_sft_baseline_ood_eval_v2_20260521T134646_result.json`
- **Structured JSON:** [`48365b07f07cfd830a43.json`](../../sessions/48/48365b07f07cfd830a43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断信息已充分。以下是结论。

---

## 诊断结论

### 根因：eval 完成后 wandb 服务崩溃导致进程退出

**不是 OOM、不是 Ray 问题、不是配置错误。** 实验本身运行正常并完成了全部 134 个 OOD 任务的评估（耗时 1549.6 秒 ≈ 25.8 分钟），但在评估完成后的 **metrics 上报阶段** 崩溃。

### 故障链

1. 评估完成时，134 个任务 × ~50 turns 产生了 **6000+ 行 `Skipping non-numeric metric 'anchor_obs'` 警告**，瞬间涌入 stdout
2. wandb 试图一次性将 6319 行 console output 上传，触发 flowcontrol backpressure（offloaded 4313 records to disk）
3. wandb 内部服务进程的 UnixTransport 被关闭（可能是内存压力或被信号杀死）
4. 主进程的 wandb client 写入关闭的 socket 时抛出 `RuntimeError: unable to perform operation on &lt;UnixTransport closed=True>`
5. 进程崩溃退出，未能执行 `wandb.finish()` 和 metrics summary 写入

### 证据

| 项目 | 状态 |
|------|------|
| Hydra 输出 | `outputs/2026-05-21/21-08-33/` 已创建，train.log 为空 |
| wandb run | `r9llx4v7`，PID 289370，21:09 启动，21:35 崩溃 |
| 评估生成 | 完成（output.log 6328 行，末行 "validation generation time: 1549.6s"） |
| table.json | 存在（877KB），含 20 个 sample 的 input/output/score |
| wandb-summary.json | **不存在**（metrics 未上报） |
| checkpoint 目录 | **不存在** |
| GPU 3 当前 | 空闲（0 MiB），进程已完全释放 |
| 磁盘 | `/root/autodl-tmp` 49% used (130GB free)，无问题 |
| exp029_seed7 | 不受影响，GPU 0,1 正常运行 |

### 可以重试，需改两处

1. **抑制 `anchor_obs` 警告洪泛**：这是直接触发 wandb 崩溃的原因。在 eval 代码或 logging 配置中过滤掉 `anchor_obs` 类型的 non-numeric metric 日志，或者将 log level 提升到 ERROR，避免数千行 WARNING 同时涌入 wandb
2. **设置 `WANDB_CONSOLE=off`**（临时方案）：如果不想改代码，可在启动命令中加 `WANDB_CONSOLE=off`，让 wandb 不截获 stdout/stderr，避免 console output 引发 transport 崩溃。metrics 仍正常上报

重试命令建议（在原命令基础上加 `WANDB_CONSOLE=off`）：
```bash
RAY_ADDRESS=local CUDA_VISIBLE_DEVICES=3 WANDB_PROJECT=cost-verify-agent-rl WANDB_CONSOLE=off python train.py --config-name _alfworld_sft_baseline_ood_eval_v2
```

### 备选：直接从本地数据恢复

评估结果已保存在 `wandb/run-20260521_210930-r9llx4v7/files/media/table/val/generations_0_*.table.json`（877KB），包含 20 个 sample 的得分。如果只需 aggregate score 而不需完整 W&B dashboard，可以用 `wandb sync` 补传这个 run，或者直接从 table.json 提取。不过 table 只有 20 个 sample，完整 134 个任务的聚合指标需要重跑。

---
