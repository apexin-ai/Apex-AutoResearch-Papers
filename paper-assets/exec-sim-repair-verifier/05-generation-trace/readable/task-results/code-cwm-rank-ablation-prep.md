# code cwm rank ablation prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_cwm-rank-ablation-prep_20260515T122747_result.json`
- **Structured JSON:** [`6233890fe39e7abb7309.json`](../../sessions/62/6233890fe39e7abb7309.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动，进度正常。

**汇报：**

| 项目 | 值 |
|------|------|
| 原始 LoRA rank | **16**（alpha=32, dropout=0.05） |
| rank=32 实验 | **已成功提交**，tmux session `cwm-rank32-ablation`，PID 368813 |
| 训练数据 | train=15,290, val=1,896 |
| 总 steps | 1,434（15290 / (batch=2 × accum=16) × 3 epochs） |
| trainable params | 23,592,960（0.58%，rank=32 比 baseline 的 rank=16 翻倍） |
| 预估完成时间 | ~2h，约 **2026-05-15 22:30 UTC+8** |
| eval | train 完成后自动串联执行 `eval_cwm_baseline.py`，输出 `eval_cwm_rank32_results.json` |
| registry | `cwm-rank32-ablation` 状态 RUNNING |

**rank=64**：需等 rank=32 完成后再提交到同一张 cuda:0。届时命令为：
```
--lora_rank 64 --output_dir checkpoints_cwm_rank64/ --output eval_cwm_rank64_results.json
```

---
