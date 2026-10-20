# code prepare seed analysis

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-seed-analysis_20260516T040932_result.json`
- **Structured JSON:** [`a8105643152f246fb509.json`](../../sessions/a8/a8105643152f246fb509.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度报告

| Seed | 进度 | 速度 | 预估剩余 |
|------|------|------|----------|
| seed123 | 92/444 (21%) | ~18.7s/step | ~1h52m |
| seed456 | 92/444 (21%) | ~18.9s/step | ~1h52m |

两个训练进度一致，均在 epoch 1 中段（444 steps = 3 epochs × 148 steps/epoch）。预计约 2 小时后完成。

## Eval 脚本参数确认

`eval/evaluate.py` 的 `--max_length` 默认值已经是 **2048**，无需显式传参。训练完成后的 eval 命令：

```bash
# seed123 (可用 cuda:0)
python eval/evaluate.py --condition ae_only \
  --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed123/final \
  --gpu 0 --save_predictions \
  --output /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed123/final/eval_results.json

# seed456 (可用 cuda:1)
python eval/evaluate.py --condition ae_only \
  --checkpoint_dir /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed456/final \
  --gpu 1 --save_predictions \
  --output /root/autodl-tmp/trace-verdict-study-checkpoints/ae_only_seed456/final/eval_results.json
```

## seed_robustness_summary.py

已写入 `/root/trace-verdict-study/analysis/seed_robustness_summary.py`。功能：

- 读取 3 个 seed 的 `eval_results.json` + `predictions.jsonl`
- 计算 mean ± std accuracy
- 两两 McNemar test（含连续性校正）
- Paired bootstrap CI（10000 次，α=0.05）
- 输出 LaTeX table
- 保存 `seed_robustness_ae_only.json`

当前只有 seed42 的结果可用，已验证脚本能正确运行（检测到缺失的 seed 会 warn 并等待）。两个训练完成并 eval 后，直接运行 `python analysis/seed_robustness_summary.py` 即可。

---
