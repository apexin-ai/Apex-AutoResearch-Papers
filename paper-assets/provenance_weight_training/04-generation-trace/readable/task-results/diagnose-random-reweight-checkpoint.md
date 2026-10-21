# diagnose random reweight checkpoint

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_random_reweight_checkpoint_20260516T130015_result.json`
- **Structured JSON:** [`63fec7b94b6e4c94849c.json`](../../sessions/63/63fec7b94b6e4c94849c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Dry-run verification complete — fix confirmed working.**

## 最终诊断报告

### 根因
`random_reweight_seed42` 训练实际只完成了 ~500 步（8%），而非 99.8%。日志中的 "6092/8477" 是 **eval 进度条**（不是 training 进度条）。进程在第一次 eval（step 500 触发）期间被 SIGKILL 杀死。

HF Trainer 的 `_maybe_log_save_evaluate()` 执行顺序是 eval → save。eval 未完成 → save 从未执行 → 零 checkpoint。

**被杀原因**：`WANDB_MODE=offline` 向 30GB 根分区写入 ~150MB wandb 本地文件，加上其他进程占用，根分区写满后触发 OOM killer。

### 修复内容 (`run_random_reweight_v2_seed42.sh`)
| 改动 | 效果 |
|------|------|
| `WANDB_MODE=disabled` | 不写任何文件到根分区 |
| `output_dir` → `/root/autodl-tmp/output/models/` | checkpoint 写入 250GB 数据盘 |
| `CUDA_VISIBLE_DEVICES=0` → 可按需调整 | 避免 GPU 冲突 |

### Dry-run 验证结果
- 服务器: `westd-47453`, GPU 3
- 配置: `max_steps=5, save_steps=3, eval_steps=3`
- eval 耗时: 21 分 14 秒（8477 步，67823 样本）
- **checkpoint-3**: 已保存，含 `model.safetensors`（1.19GB）+ 完整 tokenizer + trainer_state
- **checkpoint-5**: 已保存，同上
- 训练完整跑完 5 步，无 crash

fix 脚本已就绪，可以直接启动正式训练。

---
