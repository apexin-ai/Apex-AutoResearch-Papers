# ssh verify seed100 eval config and prep seed200v4

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_seed100_eval_config_and_prep_seed200v4_20260522T204403_result.json`
- **Structured JSON:** [`26ab2fcfeac9791b5a4b.json`](../../sessions/26/26ab2fcfeac9791b5a4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。

---

## 汇报

### Part 1: westd seed100 OOD eval runtime config

从 log config dump 确认的关键参数：

| 参数 | 实际值 | 状态 |
|------|--------|------|
| `enable_think` | `True` | ✅ |
| `enable_response_mask` | `False` | ✅ |
| `val_only` | `True` | ✅ |
| `temperature` (val_kwargs) | `0.4` | ✅ |
| `context_window_mode` | `full` | ✅ |

**Eval 进度**: 1861 行 log，尚无 `step:` 输出。GPU 0 占用 100%/90GB，进程活跃，仍在模型加载/生成阶段（wandb run 启动于 2026-05-23 04:22:43）。eval 配置为 134 个 OOD env_groups。

### Part 2: bjb1 seed200 v4 训练准备

| 检查项 | 结果 |
|--------|------|
| 磁盘空间 | 113GB free (56% used) ✅ |
| SFT checkpoint | 存在，3.2GB model.safetensors ✅ |
| seed200 config | 已创建 `_alfworld_exp029_seed200_episode.yaml` ✅ |
| config 参数 | seed=200, steps=5, save_freq=5, 输出到 `/root/autodl-tmp/checkpoints/exp029-seed200/` |

**seed300 eval v3**: 已完成。结果 — success=0.0, pass@1=0.0, num_actions=50（全部 max out），134 个 OOD episodes 全部失败。

**bjb1 GPU**: GPU 0 占用 94%/56GB, GPU 1 占用 0%/56GB（VRAM 被占但利用率为 0，可能是残留进程）。

---
