# code plan022 training dynamics

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan022_training_dynamics_20260519T032219_result.json`
- **Structured JSON:** [`575b8689829d99d2bd76.json`](../../sessions/57/575b8689829d99d2bd76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都正常启动：

- **exception_only** (cuda:0): ~8-10s/step, 444 steps ≈ 预计 ~1h 训练
- **full_trace** (cuda:1): ~18s/step (full_trace 序列更长), 444 steps ≈ 预计 ~2h 训练

训练完成后会自动运行 batch eval（对 8 个中间 checkpoint + final 逐个评估，每个需要跑 1190 条推理），然后清理中间 checkpoint，保留 `dynamics_log.jsonl` 和 `final/`。

完成后的画图命令：
```bash
/root/miniconda3/bin/python eval/plot_dynamics.py \
  --exception_only /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_exception_only_dynamics_seed42/dynamics_log.jsonl \
  --full_trace /root/autodl-tmp/trace-verdict-study-checkpoints/qwen7b_full_trace_dynamics_seed42/dynamics_log.jsonl
```

**总结**：
1. `train_sft.py` 已添加 `--save_steps` 参数（save_strategy/eval_strategy 切换为 steps）
2. `eval/batch_eval_dynamics.py` 创建完成（基模型加载一次，逐 checkpoint swap adapter 评估）
3. `eval/plot_dynamics.py` 创建完成（3 panel: accuracy, per-class F1, train loss）
4. 两个实验已提交至 cuda:0 / cuda:1，pipeline 为 train → batch eval → cleanup

exception_only 预计 ~2-3h 完成全流程（训练 + 9 个 checkpoint 评估），full_trace 预计 ~3-4h。

---
