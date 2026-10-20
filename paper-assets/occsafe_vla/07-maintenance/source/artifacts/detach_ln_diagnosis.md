# detach_ln 实验失败诊断报告

## 总结

三个实验全部在 checkpoint 保存时崩溃，根因相同：`save_training_checkpoint` 函数的 LoRA merge 步骤调用 `AutoModelForVision2Seq.from_pretrained(cfg.vla_path)`，但 `cfg.vla_path` 指向的 checkpoint 目录在训练过程中被删除。

---

## 逐实验分析

### detach_ln_s0
- **vla_path**: `/root/autodl-tmp/checkpoints/detach_ln_s0/openvla-7b+...--image_aug--20000_chkpt`
- **训练进度**: ~30000/50005 步（13%），运行约 3 小时
- **崩溃时间**: 2026-05-24 01:03:15
- **错误原文**:
  ```
  OSError: Incorrect path_or_model_id: '/root/autodl-tmp/checkpoints/detach_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--20000_chkpt'
  ```
  发生在 `finetune.py:725 save_training_checkpoint → AutoModelForVision2Seq.from_pretrained(cfg.vla_path)`
- **Checkpoint 状态**: `--30000_chkpt` 目录存在（部分保存），包含 LoRA adapter、action_head、occ_head、proprio_projector。**无 merged base model**。`--20000_chkpt` 目录已不存在。

### detach_ln_s1
- **vla_path**: 同 s0 模式，指向 `--20000_chkpt`
- **训练进度**: ~30000/50005 步
- **崩溃时间**: 2026-05-24 01:03:07
- **错误**: 与 s0 完全相同
- **Checkpoint 状态**: 同 s0。`--30000_chkpt` 部分保存，`--20000_chkpt` 已不存在。

### detach_ln_s2
- **vla_path**: 指向 `--10000_chkpt`
- **训练进度**: ~20000/50005 步
- **崩溃时间**: 2026-05-24 01:04:34
- **错误**: 同上，但路径为 `--10000_chkpt`
- **额外问题**: 日志头部显示曾有一次启动失败（`/root/occsafe_vla/vla-scripts/finetune.py: No such file or directory`，用了错误的 Python 和脚本路径），后续重试成功启动但仍在 checkpoint 保存时崩溃
- **Checkpoint 状态**: `--20000_chkpt` 部分保存（有 LoRA adapter 等），`--10000_chkpt` 已不存在。

---

## 根因分析

`finetune.py` 第 725 行的 `save_training_checkpoint` 函数在保存 checkpoint 后会执行 LoRA merge：

```python
if cfg.use_lora and cfg.merge_lora_during_training:
    base_vla = AutoModelForVision2Seq.from_pretrained(
        cfg.vla_path, torch_dtype=torch.bfloat16, low_cpu_mem_usage=True, trust_remote_code=True
    )
```

`cfg.vla_path` 指向用于 resume 的旧 checkpoint 目录（`--20000_chkpt` 或 `--10000_chkpt`）。训练启动时该目录存在并成功加载了模型，但在训练过程中（~3 小时后）该目录被删除，导致 `from_pretrained` 找不到路径而报错。

**不是 OOM，不是梯度爆炸，纯粹是文件系统路径问题。**

---

## 已有 Checkpoint 可恢复性

| 实验 | 可用 Checkpoint | 包含内容 | 缺失 |
|------|----------------|---------|------|
| s0 | `--30000_chkpt` | LoRA adapter, action_head, occ_head, proprio_projector, processor | merged base model (config.json, model weights) |
| s1 | `--30000_chkpt` | 同上 | 同上 |
| s2 | `--20000_chkpt` | 同上 | 同上 |

这些 checkpoint **可以恢复**：只需从 `openvla/openvla-7b` 加载 base model，再加载 LoRA adapter 和各组件即可继续训练。

---

## 修复建议

1. **根本修复**：`save_training_checkpoint` 中的 `cfg.vla_path` 应指向一个不会被删除的 base model 路径（如 HF Hub 的 `openvla/openvla-7b`，或一个持久化的本地副本），而非用于 resume 的 checkpoint 目录
2. **快速 workaround**：设 `merge_lora_during_training=False`，训练结束后离线 merge
3. **防止旧 checkpoint 被删**：调查为什么 `--20000_chkpt` / `--10000_chkpt` 在训练期间消失（可能是磁盘清理、其他进程、或手动删除）
4. **重跑时从现有 checkpoint resume**：s0/s1 可从 `--30000_chkpt` resume（需修复 vla_path），s2 可从 `--20000_chkpt` resume
