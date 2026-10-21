# ssh fix eval checkpoint bug

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-eval-checkpoint-bug_20260521T131432_result.json`
- **Structured JSON:** [`0ff0f25ae41ef23ce0a7.json`](../../sessions/0f/0ff0f25ae41ef23ce0a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成，验证通过。汇总报告：

---

## 1. Diff（7 个脚本，同一 bug 模式）

**6 个 tail-1 脚本**（eval_deepseek_cwm_s123_v2.sh, eval_deepseek_cwm_s456_v2.sh, eval_qwen_cwm_s123.sh, eval_qwen_cwm_s456.sh, eval_14b_cwm_pilot.sh, cwm8b_final_test_eval.sh）：

```diff
- FINAL_CKPT=$(ls -d ${CKPT_DIR}/checkpoint-* 2>/dev/null | sort -t'-' -k2 -n | tail -1)
+ FINAL_CKPT=$(ls -d ${CKPT_DIR}/checkpoint-* 2>/dev/null | awk -F'checkpoint-' '{print $NF, $0}' | sort -n | tail -1 | cut -d' ' -f2-)
```

**1 个 sweep 脚本**（cwm8b_val_sweep.sh）：

```diff
- mapfile -t CKPTS < <(ls -d ${CKPT_BASE}/checkpoint-* 2>/dev/null | sort -t'-' -k2 -n)
+ mapfile -t CKPTS < <(ls -d ${CKPT_BASE}/checkpoint-* 2>/dev/null | awk -F'checkpoint-' '{print $NF, $0}' | sort -n | cut -d' ' -f2-)
```

**验证**：s456 目录 BUG 版→`checkpoint-8418`，FIXED 版→`checkpoint-12627` ✓

## 2. s456 epoch 2 eval 进度

| 项目 | 值 |
|------|----|
| PID | 56657（仍在跑） |
| Checkpoint | checkpoint-8418（epoch 2） |
| 进度 | **360 / 9784 样本（3.7%）** |
| 速率 | ~12.9 samples/min |
| 预计剩余 | ~12 小时 |
| 输出路径 | `/root/autodl-tmp/eval_results/deepseek_cwm_repo_s456_v2_eval/results_incremental.jsonl` |

完成后需标注为 epoch2 结果。

## 3. s123 训练进度

| 项目 | 值 |
|------|----|
| PID | 28200（仍在跑） |
| 进度 | **8120 / 12627 steps（64.3%），epoch 1.9** |
| 速率 | ~8s/step |
| 已跑时间 | 8h50m（从 checkpoint-4209 resume） |
| 预计剩余 | **~10 小时**（⚠️ 远晚于 22:30 UTC 的预估） |

## 4. Qwen eval 脚本

`eval_qwen_cwm_s123.sh` 和 `eval_qwen_cwm_s456.sh` **均有相同 bug，已修复** ✓

## 5. 自动触发机制

- **无 crontab**
- **无 inotifywait / watch / auto-eval 脚本**
- eval 需手动触发。s123 训练完成后需要手动运行 `eval_deepseek_cwm_s123_v2.sh`。

---
