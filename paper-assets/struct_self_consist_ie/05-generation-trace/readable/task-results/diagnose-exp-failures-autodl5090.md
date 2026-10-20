# diagnose exp failures autodl5090

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_failures_autodl5090_20260515T190825_result.json`
- **Structured JSON:** [`afe5b22fc6c15fdca56d.json`](../../sessions/af/afe5b22fc6c15fdca56d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到根因了。scierc_v2 日志显示它实际启动在 **cuda:0** 而非预期的 cuda:3，与 conll finetune 冲突。

---

## 诊断报告

### 服务器健康状态（当前）

| 指标 | 状态 |
|------|------|
| GPU | 4× RTX 5090 32GB，GPU 0/1/3 空闲，GPU 2 被新任务占用（100%，30350MiB） |
| 磁盘 | /root/autodl-tmp 68% (81GB free)，/ 37% (19GB free) — 正常 |
| 内存 | 754GB total，27GB used — 正常 |

### 实验 1: exp_freeform_seed789_v2 — SIGTERM (143)

- **根因：被级联杀死。** 进度 550/551 (99.8%)，在最后一个样本推理时收到 SIGTERM。vLLM EngineCore 在 03:06:16 执行 shutdown，中止了最后 1 个请求。
- **产出：无。** 输出目录 `results/exp_freeform_ablation_seed789/` 为空——vLLM batch inference 在全部完成后才写结果，差 1 个样本所以什么都没保存。
- **触发原因：** 与另外两个实验同时在 03:06 崩溃，属于连锁反应（见下面的根因分析）。

### 实验 2: exp_qwen3_4b_conll_finetune — 进程消失

- **根因：GPU 内存冲突。** 训练正常推进到 step 3920/4390 (89.3%)，loss=0.0086，epoch 4.46。在 ~03:06 突然停止记录。
- **直接原因：** scierc_finetune_v2 在 03:05:37 **错误地启动在 cuda:0**（与 conll finetune 同一张卡），两个训练进程争抢同一块 GPU 显存，导致驱动层面 OOM。
- **可抢救产出：** checkpoint-3800（772MB，完整）。训练已完成 86.5%，可从 checkpoint-3800 恢复，仅损失 120 步（~3%进度）。
- **无 ~/runs/ 日志文件** — 该实验可能不是通过 submit_training_job 启动的。

### 实验 3: exp_qwen3_4b_scierc_finetune_v2 — SIGKILL (137)

- **根因：OOM-Kill。** 日志明确显示 `bash: line 1: 219834 Killed`，EXIT_CODE=137。
- **配置错误：** 日志第一行 `device: cuda:0`，但预期应在 cuda:3。这是 GPU 分配错误，导致它与 conll finetune 争抢 cuda:0。
- **进度：** 仅完成 18/585 步 (3%)，无 checkpoint 保存，无可抢救产出。

### 根因总结

**GPU 设备分配冲突。** scierc_finetune_v2 的 config（`train_config_scierc_4b.yaml`）将设备设为 cuda:0 而非 cuda:3。03:05:37 启动后，cuda:0 上两个 4B 模型 LoRA 训练同时运行（各需 ~15-20GB VRAM），超出 RTX 5090 的 32GB 显存。内核 OOM-kill 了 scierc 进程，级联导致同卡的 conll 进程崩溃，监控脚本随后 SIGTERM 了 cuda:2 上的 freeform 推理。

### exp_qwen3_4b_scierc_finetune_v2 存活检查

**PID 219830 已死亡。** 该实验也是上述级联崩溃的受害者。

### 当前 GPU 2 新进程

PID 220875（父进程 220580）正在运行新的 freeform inference（seed 456），已运行 ~3 分钟。

### 重试建议

| 实验 | 建议 |
|------|------|
| conll finetune | 从 checkpoint-3800 恢复（`--resume_from_checkpoint checkpoint-3800`），仅需 ~16 分钟完成剩余 590 步。确保独占 cuda:0。 |
| freeform seed789 | 需完整重跑。建议等当前 seed456 跑完后再启动，避免 GPU 争抢。 |
| scierc finetune v2 | 重跑前**必须修复 `train_config_scierc_4b.yaml` 中的 GPU 设备分配**，改为 cuda:3（或其他空闲 GPU）。 |

---
