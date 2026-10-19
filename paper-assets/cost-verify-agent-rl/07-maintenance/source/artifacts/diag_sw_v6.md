# 诊断报告：scienceworld_grpo_cell_c_v6

## 失败根因

**模型路径不存在。** config 中指定的 `model_path` 指向一个不存在的目录：

```
model_path: /root/autodl-tmp/checkpoints/qwen3_scienceworld_sft/huggingface
```

该路径在服务器上不存在（`ls` 返回 No such file or directory）。整个 `qwen3_scienceworld_sft` 目录都不存在。

## 错误类型

**代码/配置 bug**，不是 OOM 或环境问题。

huggingface_hub 的 `validate_repo_id()` 将本地路径当作 repo ID 进行验证（因为本地路径不存在，库回退到 Hub 查找），触发格式校验失败。

## 完整 Traceback

```
ray.exceptions.RayTaskError(HFValidationError):
  ray::TaskRunner.run() (pid=426830)
  File ".../huggingface_hub/utils/_validators.py", line 106, in _inner_fn
    validate_repo_id(arg_value)
  File ".../huggingface_hub/utils/_validators.py", line 154, in validate_repo_id
    raise HFValidationError(
huggingface_hub.errors.HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name':
  '/root/autodl-tmp/checkpoints/qwen3_scienceworld_sft/huggingface'. Use `repo_type` argument if needed.
```

## 修复建议

1. **确认 SFT 模型的实际位置。** 服务器上 `/root/autodl-tmp/checkpoints/` 下现有的相关目录：
   - `exp021_ragen_sft_v4/` (含 checkpoint-160, checkpoint-320, final)
   - 多个 exp029 变体的 HF 格式 checkpoint

2. **将 config 的 `model_path` 修改为正确路径。** 如果 SFT 模型尚未训练/转换，需要先完成该步骤。

3. 如果意图是用 v5 同款 SFT 模型，检查 v5 config 中的 `model_path` 并复用。

## v5 日志对比

v5 的失败模式完全不同——v5 成功启动并训练了 ~2.25 小时，最终在 **checkpoint 保存阶段因磁盘写入错误崩溃**：

```
RuntimeError: [enforce fail at inline_container.cc:668] . unexpected pos 3761481024 vs 3761480912
```

这是 `torch.save()` 写入 optimizer state 时的典型磁盘空间不足/IO 错误。v5 崩溃位置在 `fsdp_checkpoint_manager.py:244`。

**结论：v6 和 v5 是完全不同的失败原因。** v6 是启动阶段的配置错误（模型路径不存在），v5 是运行中期的磁盘 IO 错误。

## 当前磁盘状态

```
/dev/md0  250G  197G  54G  79% /root/autodl-tmp
```

54GB 可用，对于 v6 重跑应该够用（但需要关注 checkpoint 累积）。
