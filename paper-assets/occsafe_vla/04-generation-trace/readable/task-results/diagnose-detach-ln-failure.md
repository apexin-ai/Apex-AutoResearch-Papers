# diagnose detach ln failure

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_detach_ln_failure_20260523T170710_result.json`
- **Structured JSON:** [`e93419343e56e27e2ed1.json`](../../sessions/e9/e93419343e56e27e2ed1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

---

## 诊断报告

### 1. 失败错误

三个实验都崩在同一个地方：`finetune.py:725` 的 `save_training_checkpoint()` 函数。

```
OSError: Incorrect path_or_model_id: 
  '/root/autodl-tmp/checkpoints/detach_ln_s{0,1,2}/openvla-7b+...--image_aug--{resume_step}_chkpt'
  Please provide either the path to a local folder or the repo_id of a model on the Hub.
```

完整调用链：
```
finetune.py:1256  finetune() → save_training_checkpoint(...)
finetune.py:725   save_training_checkpoint() → AutoModelForVision2Seq.from_pretrained(cfg.vla_path)
```

### 2. 训练进度

| 实验 | resume_step | 实际训完的 step | 崩溃时间 |
|------|-------------|-----------------|----------|
| s0 | 20000 | 30000 (训了 10000 步) | 05-24 01:03:15 |
| s1 | 20000 | 30000 (训了 10000 步) | 05-24 01:03:07 |
| s2 | 10000 | 20000 (训了 10000 步) | 05-24 01:04:34 |

三个实验都在第一次触发 checkpoint save 时崩溃。训练本身没有问题（无 NaN / OOM / CUDA error）。

### 3. Root Cause

`merge_lora_during_training` 默认为 `True`（`finetune.py:131`）。save checkpoint 时，代码在 line 725 尝试从 `cfg.vla_path` 重新加载 base model 以合并 LoRA 权重。

问题：当使用 `--resume True` 时，`cfg.vla_path` 被设为 resume checkpoint 路径（如 `...--20000_chkpt`）。但这个路径：
- **不存在**（`ls` 确认 `--20000_chkpt` 和 `--10000_chkpt` 目录均不在磁盘上）
- 即使存在也只包含 LoRA adapter + 组件权重，不含完整 base model（无 `config.json`）

`from_pretrained()` 找不到 `config.json` → 抛出 `OSError`。

**LoRA adapter 和 occ_head 等组件权重已经成功保存**（`--30000_chkpt` 目录存在且包含 `action_head`, `occ_head`, `lora_adapter` 等文件），只是最后的 merge 步骤失败。

### 4. 修复建议

**快速修复（推荐）**：启动时加 `--merge_lora_during_training False`。LoRA adapter 会单独保存，跳过 merge 步骤，不会触发 `from_pretrained`。merge 可以离线做。

**代码修复**：在 `finetune.py` 中分离 `cfg.vla_path`（用于 resume 加载组件）和 base model 路径（用于 merge）。例如在 resume 逻辑中保存原始 base model 路径到 `cfg.base_model_path`，line 725 改用 `cfg.base_model_path`。

**恢复训练**：`--30000_chkpt`（s0/s1）已有 adapter 和组件权重，可以从 step 30000 resume（s2 从 20000 resume），加上 `--merge_lora_during_training False`。

---
