# eval exp1 isr b03 s43 prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp1-isr-b03-s43-prep_20260514T231704_result.json`
- **Structured JSON:** [`89e79f506261745a5ef3.json`](../../sessions/89/89e79f506261745a5ef3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证结果：

**Checkpoint 完整性：确认完整**
- 路径：`/root/autodl-tmp/outputs/exp1_isr_b03_s43/`
- 4 个 safetensors 分片齐全，总大小 ~15.0GB：
  - model-00001-of-00004.safetensors: 4.65GB
  - model-00002-of-00004.safetensors: 4.60GB
  - model-00003-of-00004.safetensors: 4.65GB
  - model-00004-of-00004.safetensors: 1.08GB
- `checkpoint-500/` 目录也存在，内含完整的模型文件和 trainer_state.json
- 输出目录和 checkpoint-500 目录均含完整 tokenizer 文件

**训练步数：500/500 确认完成**
- 日志显示 `100%|██████████| 500/500` 进度条完成
- `Saving final model` 于 2026-05-15 07:01:21
- Final stats: `parse_rate=1.0, prove_rate=0.56125, mean_isr=0.1515`
- `train_runtime=4142.3s (~69min), epoch=2.0`
- `EXIT_CODE=129` 是 tmux 清理的 SIGHUP，模型已保存完毕

**GPU 当前状态：两卡满载**
- GPU 0: 85059/97887 MiB (87%), utilization 91%
- GPU 1: 83123/97887 MiB (85%), utilization 90%

两张卡都在跑训练，不宜现在启动 eval。

---
