# code plan002 label only loss

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan002-label-only-loss_20260515T021458_result.json`
- **Structured JSON:** [`a8b8ffbe7037091e46df.json`](../../sessions/a8/a8b8ffbe7037091e46df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有验证完成。以下是总结：

---

## 实现方案
- **选择**: 修改 `train_sft.py`，添加 `--label_only_loss` 参数
- **修改的文件**: `/root/trace-verdict-study/train/train_sft.py`
- **关键代码改动**:
  - 新增 `to_prompt_completion()` 函数：用 `apply_chat_template(add_generation_prompt=True)` 生成 prompt（含完整 trace），completion 仅为 "pass"/"fail"
  - 使用 TRL 1.1.0 的 `completion_only_loss=True`（仅对 prompt-completion 格式生效）
  - 添加 `--max_steps` 参数方便 dry-run

## 数据/配置
- 训练数据: `/root/autodl-tmp/trace-verdict-study-data/full_trace_train.jsonl` (4720 样本)
- 测试数据: `/root/autodl-tmp/trace-verdict-study-data/full_trace_test.jsonl` (1190 样本)
- **不需要生成新数据文件**——使用与 v5 相同的 full_trace 数据
- Loss 计算: **仅在 2 个 token 上**——label token ("pass"=6385 或 "fail"=18403) + EOS token (`<|im_end|>`=151645)
- 对比：原始 full SFT 在全部 ~2048 tokens 上计算 loss

## 验证
- **Masking 验证**: PASS — 2/2047 tokens 有 loss（label + EOS），其余全部 mask 为 -100
- **Dry-run 5 steps**: 成功，每步 ~40s，GPU 1 使用 ~41 GiB 显存
- **End-to-end token check**: 数据使用 v5 修复版，0 样本超 2048 tokens

## 训练命令
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/trace-verdict-study && python train/train_sft.py --condition full_trace --label_only_loss --gpu 1 --seed 42 --wandb_run_name full_trace_label_only_seed42"
```

**注意**: GPU 0 当前被占满（90 GiB），GPU 1 有其他训练进程占 41 GiB，剩余 ~56 GiB 足够运行。如两个 GPU 都被占满，需等待现有训练完成。

---
