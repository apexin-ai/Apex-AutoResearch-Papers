# code cwm 8b eval prep dryrun

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cwm-8b-eval-prep-dryrun_20260515T115025_result.json`
- **Structured JSON:** [`43f6e09f409be0e0e4f5.json`](../../sessions/43/43f6e09f409be0e0e4f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇报

### CWM eval 脚本
- **脚本**: `eval_repo_cwm.py`
- **vs CLS**: 生成执行 trace（max_new_tokens=1024 vs CLS 的 8），通过关键词匹配提取 pass/fail，system prompt 为 "code execution simulator"
- **支持**: `--max_samples`、`--dry_run`、`--output_dir`、增量 resume（results_incremental.jsonl）

### Dry-run 结果: 成功
- checkpoint-4300（中间 checkpoint）+ GPU 0 + 5 samples
- 模型加载 → 推理 → 输出 → 指标计算 → 文件保存，全链路通过
- 4/5 样本 unparseable（中间 checkpoint 预期内，模型还在训练）
- 每样本耗时 15-33 秒（平均 ~20s）

### 训练状态
- 总步数 6633，save_steps=100，当前 step 4300（epoch 1.94/3.0）
- Checkpoint 目录: `/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/`（checkpoint-400, 4000, 4100, 4200, 4300）
- 最终 checkpoint 预计为 `checkpoint-6600` 或 `checkpoint-6633`
- **注意**: eval_loss 从 step 400 的 0.286 持续上升到 step 4300 的 0.482，存在过拟合趋势

### 时间估算
- 全量 test set: 9784 样本
- batch_size=1: **~54 小时**（太慢）
- batch_size=2: **~27 小时**（32GB 5090 应该能跑 bs=2）

### CWM 8B eval 完整命令（训练完成后替换 checkpoint 路径）

```bash
nohup bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=2 python3 eval_repo_cwm.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-6600 \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ \
  --split test \
  --device cuda:0 \
  --batch_size 1 \
  --max_new_tokens 1024 \
  --output_dir /root/autodl-tmp/eval_results/cwm_8b_final/" > ~/runs/exec-sim-repair-verifier/cwm-8b-eval-final.log 2>&1 &
```

### 注意事项
1. 训练完成后确认最终 checkpoint 编号（ls checkpoint 目录找最后一个）
2. eval_loss 从 step 400 后持续上升，可能需要同时 eval best checkpoint（checkpoint-400）和 final checkpoint 做对比
3. 全量 eval 耗时长（~27-54h），可考虑先 eval val split（9335 samples）或减少 max_new_tokens
4. GPU 1 上有另一个进程（27GB），勿用 GPU 1

---
