# code repo level data prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_repo-level-data-prep_20260512T093859_result.json`
- **Structured JSON:** [`098fd236ef17af110ef5.json`](../../sessions/09/098fd236ef17af110ef5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

42.7 MB (46.4%). The transfer is progressing steadily at ~1 MB/min. Estimated 50 min remaining.

Let me give you a status report rather than continuing to poll:

---

**当前进度**

| 步骤 | 状态 |
|------|------|
| **Step 1: 数据传输** | 进行中 — `swebench_pilot_data.jsonl.gz` (92 MB) 传输到 seetacloud，当前 42.7/92.1 MB (46%)，约 50 分钟完成 |
| **Step 2: 数据切分** | 已自动化 — `post_transfer.sh` 会在传输完成后自动解压 + 运行 `split_swebench_data.py` |
| **Step 3: 训练/评估脚本** | 已完成 ✅ — 4 个脚本已写入 seetacloud 并通过 `--help` 验证 |

**已部署的脚本 (seetacloud: `/home/sonny/exec-sim-repair-verifier/`)**

| 脚本 | GPU | 用途 |
|------|-----|------|
| `split_swebench_data.py` | - | 80/10/10 按 instance_id 分层切分，计算 class weights |
| `train_repo_verifier.py` | cuda:2 | Repo-level 分类训练 (pass/fail)，带 WeightedCausalLMTrainer |
| `train_repo_cwm.py` | cuda:3 | Repo-level CWM 训练 (生成 execution output)，带 WeightedCausalLMTrainer |
| `eval_repo_verifier.py` | cuda:2 | 分类评估 (P/R/F1, confusion matrix, MVP-B criteria) |
| `eval_repo_cwm.py` | cuda:3 | CWM 评估 (exact match, per-error-type breakdown) |

**自动化 pipeline (PID 27744)**

传输完成后会自动执行：
1. `gunzip swebench_pilot_data.jsonl.gz`
2. `python split_swebench_data.py` → 生成 `swebench_train.jsonl`, `swebench_val.jsonl`, `swebench_test.jsonl`
3. 结果写入 `/tmp/post_transfer.log`

**检查命令**（随时可用）：
```bash
# 查传输/pipeline 状态
cat /tmp/post_transfer.log
# 查文件大小
stat --format="%s" /home/sonny/exec-sim-repair-verifier/data/swebench_full/swebench_pilot_data.jsonl.gz
```

**推荐训练命令**（pipeline 完成后）：
```bash
# 分类模型 (cuda:2)
python train_repo_verifier.py --device cuda:2

# CWM 模型 (cuda:3)  
python train_repo_cwm.py --device cuda:3
```

需要我继续等待传输完成并报告切分结果，还是你稍后手动检查 `/tmp/post_transfer.log`？

---
