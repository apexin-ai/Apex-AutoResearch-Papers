# ssh kill s456 find eval retrain s123

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-s456-find-eval-retrain-s123_20260520T054155_result.json`
- **Structured JSON:** [`79bf4440e09811b66e6a.json`](../../sessions/79/79bf4440e09811b66e6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模型加载缓冲中（可能需要数分钟加载 6.7B 量化模型到 GPU）。数据行数已确认正确：**train=70748**（符合预期 ~70748）。

先报告当前状态，total steps 等训练开始后日志自动打印。根据 70748 / (batch_size 2 × grad_accum 8) × epochs 3 = 70748 / 16 × 3 = 13265.25 → **预期 total steps = 13266**，数据匹配，无需 kill。

---

## 产出报告

### 第 1 步：Kill PID 917649
```
kill -9 917649 → return_code=0
确认: DEAD
nvidia-smi 计算进程:
  PID 886278, GPU-fc6e3..., 21246 MiB
  PID 886352, GPU-02eb6..., 31252 MiB
→ GPU 2 已释放（无进程占用）
```

### 第 2 步：CWM eval 结果位置
**没有名为 `results.jsonl` 的文件。** CWM eval 结果以其他文件名存在，主要位置：

| 路径 | head -3 格式 |
|------|-------------|
| `/root/autodl-tmp/eval_results/deepseek_cwm_repo_s123_test/results_incremental.jsonl` | `{index, problem_id, label, pred, correct, truncated, gen_text, unparseable}` — 逐条推理结果 |
| `/root/autodl-tmp/eval_results/deepseek_cwm_repo_s123_test/eval_deepseek_cwm_repo_s123_predictions.jsonl` | 同结构，但 gen_text 更短（仅 PASS/FAIL 行） |
| `/root/autodl-tmp/eval_results/deepseek_cwm_repo_s123_seq4096/results_incremental.jsonl` | 同结构 |
| `/root/autodl-tmp/eval_results/deepseek_cwm_repo_s123_seq4096/eval_repo_cwm_predictions.jsonl` | 同结构 |
| `/root/autodl-tmp/eval_results/deepseek_cwm_repo_s42_test/forced_parse_results.jsonl` | 含额外字段 `forced_pred, forced_strategy, forced_correct, orig_unparseable` |
| `/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_merged/results_merged.jsonl` | 含额外字段 `mutation_type` |

其他 CWM eval 目录：`deepseek_cwm_func_test`, `deepseek_cwm_func_s123_test`, `deepseek_cwm_repo_s42_epoch2`, `deepseek_cwm_repo_s42_epoch3_seq2048`, `deepseek_cwm_repo_s42_e3_seq4096`, `qwen3_8b_cwm_repo_s42_ckpt400_seq4096`, `cwm_8b_ckpt400_test_shard{2,3,4}`, 以及 `/root/autodl-tmp/results/repo_cwm_{v10,seed123,v12}_*_eval/`。

### 第 3 步：训练提交 + 日志验证
```
submit_training_job → 成功
  PID: 925633
  tmux session: deepseek-cwm-repo-s123-train-v2
  log: ~/runs/exec-sim-repair-verifier/deepseek-cwm-repo-s123-train-v2.log
  GPU: cuda:2

日志验证:
  train=70748 ✓ (预期 ~70748)
  val=1896
  预期 total steps = 70748 / (2×8) × 3 = 13266 ✓
  模型加载中，尚未打印 trainer 信息（6.7B 量化模型加载到 GPU 需 2-3 分钟）
  进程 ALIVE，无 DATA_MISMATCH
```

---
