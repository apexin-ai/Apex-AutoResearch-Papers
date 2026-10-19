# ssh start connector only eval

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_start_connector_only_eval_20260518T010047_result.json`
- **Structured JSON:** [`d1b76ef2648a2cbf755c.json`](../../sessions/d1/d1b76ef2648a2cbf755c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。模型加载成功，环境初始化正常，开始 rollout，无报错。

## 产出汇总

| 项目 | 结果 |
|---|---|
| **LoRA 训练** | step 13600/20000, loss≈0.20, 1.8 steps/s, GPU 0 |
| **GPU 1** | 空闲（0 MiB, 0%） |
| **eval 脚本** | 新创建 `/root/acib/run_connector_only_eval.sh` |
| **connector_only 支持** | checkpoint config 已含 `freeze_mode: connector_only`，eval_acib.py line 129 自动读取 |
| **dry-run** | 成功（checkpoint 加载、环境初始化、rollout 启动均正常） |

### Full eval 启动命令

通过 `submit_training_job` 提交，关键参数：
- **script**: `/root/acib/run_connector_only_eval.sh`
- **gpu**: `1`（物理 cuda:1，脚本内 `--gpu 0` 会被 CUDA_VISIBLE_DEVICES 映射）
- **log**: `~/runs/action_cond_info_bottleneck/connector_only_eval_alpha0.0.log`

---
