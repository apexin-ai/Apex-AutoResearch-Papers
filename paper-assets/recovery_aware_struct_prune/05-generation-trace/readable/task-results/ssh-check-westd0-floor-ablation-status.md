# ssh check westd0 floor ablation status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_westd0_floor_ablation_status_20260523T091914_result.json`
- **Structured JSON:** [`b5629d48c3888bd0374d.json`](../../sessions/b5/b5629d48c3888bd0374d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇报

**进程**: PID 114044 已死亡。

**Pipeline 进度**: 走到了第 3 步 GRPO，训练本身已完成（100/100 steps），但在 **保存模型时磁盘空间不足崩溃**。

| 阶段 | 状态 | 产出 |
|------|------|------|
| Prune | ✅ 完成 | `pruned_cka_only_20_floor_0.3/` — 12.3GB model.safetensors |
| SFT | ✅ 完成 | `sft_cka_only_20_floor_0.3/` — 12.3GB model.safetensors |
| GRPO | ❌ 保存失败 | `grpo_cka_only_20_floor_0.3/` — 仅 4.8GB（不完整，缺 tokenizer 等文件） |

**失败原因**: `safetensors_rust.SafetensorError: No space left on device (os error 28)`
- GRPO 训练 100 steps 全部跑完，在 `trainer.save_model()` 写 safetensors 时磁盘满
- 当前数据盘 `/root/autodl-tmp` 用了 532G/650G（82%），剩 119GB — 说明崩溃后有部分临时文件已被清理或其他任务释放了空间

**GPU 0**: 空闲（0% 利用率，0 MiB 显存）。GPU 1/2 被其他任务占用。

**修复建议**: GRPO 训练已完成但模型没存好。可以清理不需要的旧 checkpoint 腾空间后，重新只跑 GRPO save 步骤（或重跑 GRPO，100 steps 约 21 分钟）。grpo 输出目录里已有 4.8GB 的不完整文件需要先删除。

---
