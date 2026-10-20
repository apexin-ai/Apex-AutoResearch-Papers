# research 8b eval pipeline prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_8b-eval-pipeline-prep_20260514T140119_result.json`
- **Structured JSON:** [`b388a4ddeda5619ea0e9.json`](../../sessions/b3/b388a4ddeda5619ea0e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕，汇总如下。

---

## Eval 脚本就绪状态

### CLS (`eval_repo_cls.py`) — ✅ 就绪，无需修改
- `--model_name` 默认 `Qwen/Qwen3-4B`，CLI 传 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/` 即可覆盖
- 支持 `--split val/test`、`--max_seq_length 4096`、`--checkpoint_dir` 任意路径
- 之前 8B eval 已成功使用 `batch_size=8`，4096 seq_len 时建议降到 4

### CWM (`eval_repo_cwm.py`) — ✅ 就绪，无需修改
- 同上，`--model_name` CLI 覆盖即可
- 支持 `--split val/test`、`--max_seq_length 4096`、`--max_new_tokens 1024`
- 默认 `batch_size=8`，8B 建议用 4；seq_len 4096 + 8B 建议用 2
- 额外支持 `--output_dir`、`--max_samples`，以及增量恢复（自动跳过已完成样本）

两个脚本的 `load_model()` 从 CLI `--model_name` 加载 base model，adapter_config.json 中 `base_model_name_or_path` 均已正确指向 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/`。

---

## 8B 训练进度

| 模型 | GPU | Step | 速度 | Epoch | 最新 Loss | 预计完成 |
|------|-----|------|------|-------|-----------|---------|
| CWM 8B s42 | cuda:2 | 1266/6633 (19%) | 12.2s/it | 0.54 | 0.69 | **May 15 ~17:30** |
| CLS 8B s123 | cuda:3 | 2400/6633 (36%) | 8.3s/it | 1.09 | 0.25 | **May 15 ~12:00** |

CWM 比 CLS 慢（每步 12.2s vs 8.3s）因为 CWM 用了更长的 label（执行输出而非 pass/fail）。

当前已保存的 checkpoints：
- CWM 8B: ckpt-400, 900, 1000, 1100, 1200（save_total_limit=5）
- CLS 8B s123: ckpt-200, 1600, 1800, 2000, 2200（save_total_limit=5）

---

## 已有 8B 结果（CLS 8B s42, test, seq2048）

| Checkpoint | Accuracy | F1_macro | 备注 |
|-----------|----------|----------|------|
| ckpt-200 | 70.22% | 68.21% | 低于 majority baseline (72.96%) |
| **ckpt-400** | **84.52%** | **80.89%** | **best** |
| ckpt-600 | 78.51% | 74.56% | 过拟合下降 |

---

## Eval 矩阵

| # | 模型 | Split | SeqLen | Checkpoint | batch_size | 状态 | 备注 |
|---|------|-------|--------|------------|------------|------|------|
| 1 | CLS 8B s42 | test | 2048 | ckpt-200,400,600 | 8 | ✅ done | best=ckpt-400 (84.52%) |
| 2 | CLS 8B s42 | val | 4096 | ckpt-400 | 4 | ⏳ **可立即执行** | D063, cuda:0/1 空闲 |
| 3 | CLS 8B s123 | test | 2048 | 训练后所有 ckpts | 8 | ⏳ 等训练完 (~May 15 12:00) | checkpoint sweep |
| 4 | CLS 8B s123 | val | 4096 | sweep 后 best ckpt | 4 | ⏳ 等 #3 完 | D063 |
| 5 | CWM 8B s42 | test | 2048 | 训练后所有 ckpts | 4 | ⏳ 等训练完 (~May 15 17:30) | checkpoint sweep |
| 6 | CWM 8B s42 | val | 4096 | sweep 后 best ckpt | 2 | ⏳ 等 #5 完 | D063 |

**可立即执行的 eval**：#2（CLS 8B s42, val, 4096, ckpt-400），需要一张空闲 GPU（cuda:0 或 cuda:1）。示例命令：

```bash
cd /home/sonny/exec-sim-repair-verifier && python eval_repo_cls.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls_8b_conda/checkpoint-400 \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ \
  --split val --max_seq_length 4096 --batch_size 4 --device cuda:0 \
  --output results/repo_cls_8b_conda_val4096/eval_repo_cls.json \
  --pred_output results/repo_cls_8b_conda_val4096/eval_repo_cls_predictions.jsonl
```

是否现在启动 #2？

---
