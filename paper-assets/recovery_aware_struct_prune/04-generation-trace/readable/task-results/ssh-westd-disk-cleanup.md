# ssh westd disk cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd_disk_cleanup_20260522T160111_result.json`
- **Structured JSON:** [`30b71bb367465bcc0ec7.json`](../../sessions/30/30b71bb367465bcc0ec7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No pycache or temp files. Cleanup complete.

---

## 磁盘清理结果
- 清理前: 91% (588 GB used / 650 GB total)
- 清理后: 89% (574 GB used / 650 GB total)
- 释放空间: ~14 GB

## 删除明细
- `grpo_random_20_seed123_v2/checkpoint-100/optimizer.pt`: 15 GB（训练已完成 100/100 steps，无需 resume）

---

## MATH-500 α=2.0 SFT eval 状态
- 进程状态: **running** (PID 57202, elapsed 1h14m)
- 进度: 109/500 (22%)
- 预估剩余: ~5h（平均 ~45s/it，波动大）
- 日志路径: `/root/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20.log`

**补充说明**: 如果需要进一步释放空间，还可删除 5 个 23G GRPO 目录和 1 个 23G SFT 目录中 checkpoint 子目录里重复的 `model.safetensors`（与根目录的最终模型相同），每个约 12G，合计可再释放 ~60G。需要的话告知。

---
