# code 8b eval pipeline prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_8b-eval-pipeline-prep_20260514T100453_result.json`
- **Structured JSON:** [`e62e00b0de2e3dd3bdb3.json`](../../sessions/e6/e62e00b0de2e3dd3bdb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据文件、脚本、权限全部就绪。

---

## 产出汇总

### 1. 已有 Checkpoint 列表

| 模型 | 目录 | Checkpoints |
|------|------|-------------|
| **8B CLS seed123** (训练中) | `/root/autodl-tmp/checkpoints_repo_cls_8b_seed123_conda/` | 200, 600, 800, 1000, 1200 (持续增加) |
| **8B CWM** (训练中) | `/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/` | 200, 300, 400, 500, 600 (持续增加) |
| **8B CLS seed42** (已完成) | `/root/autodl-tmp/checkpoints_repo_cls_8b_conda/` | 200, 400, 600 |

### 2. Eval 脚本已就绪
- `run_8b_eval.sh` 已部署到 `/home/sonny/exec-sim-repair-verifier/run_8b_eval.sh`
- 支持三种 model_type: `cls` (seed123), `cwm`, `cls42` (seed42 re-eval)
- 自动跳过已有结果（幂等），结果输出到 `results/8b_{type}/`
- 修正了任务描述中的参数差异：`--checkpoint_dir`（非 `--checkpoint_path`）、CLS 无 `--output_dir`、需指定 `--model_name`

### 3. VRAM 估算（8B bf16 + seq=6144, 5090 32GB）

| batch_size | 估算 VRAM | 是否可行 |
|-----------|----------|---------|
| 1 | ~17.3 GB | OK |
| 2 | ~18.6 GB | OK，建议先试 |
| 4 | ~21.2 GB | 可能可以，CWM 的 max_new_tokens=1024 会额外占用 |

CLS 可以试 batch_size=2（生成 token 少），CWM 保守用 1（生成 1024 tokens 的 KV cache 额外开销）。脚本默认 batch_size=1 保安全。

### 4. 训练完成后执行计划

**Phase 1 — ~06:00 UTC May 15（CLS seed123 训练完成）：**
```bash
# 假设 GPU 0 或 1 空出
nohup bash run_8b_eval.sh 0 cls 6144 > results/8b_cls_seed123_eval.log 2>&1 &

# 同时用另一个 GPU 跑 seed42 re-eval（seq=6144）
nohup bash run_8b_eval.sh 1 cls42 6144 > results/8b_cls42_eval.log 2>&1 &
```

**Phase 2 — ~13:00 UTC May 15（CWM 训练完成）：**
```bash
nohup bash run_8b_eval.sh 2 cwm 6144 > results/8b_cwm_eval.log 2>&1 &
```

**预估时间：** 每个 checkpoint val+test 约 20-30 min（batch_size=1, seq=6144）。CLS seed123 ~7 个 ckpt × 2 splits × 25 min ≈ 6h；CWM 更久（max_new_tokens=1024），~8 个 ckpt × 50 min ≈ 7h。

---
