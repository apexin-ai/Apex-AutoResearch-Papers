# gen figure2 and lpm

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gen_figure2-and-lpm_20260522T123736_result.json`
- **Structured JSON:** [`575ac9ee25ba9565c87a.json`](../../sessions/57/575ac9ee25ba9565c87a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务执行完毕。

---

## 任务 A: Figure 2

生成成功：
| 文件 | 大小 |
|------|------|
| `/root/autodl-tmp/figures/paper/figure2_v2.pdf` | 20,869 B |
| `/root/autodl-tmp/figures/paper/figure2_v2.png` | 111,739 B |

---

## 任务 B: LPM Regression

执行完成，但与论文预期值有偏差。关键结果：

### DeepSeek cross-complexity (N=57,512, 139 clusters)
- **CWM coef = -0.225, z = -64.44, p < 0.001**
- TRAJ coef = -0.428, z = -31.21
- complexity coef = -0.114, z = -3.71
- 注意：触发了 singular matrix fallback，交互项被丢弃，退化为加法模型

### Repo cross-model (N=97,840, 25 clusters)
- **CWM deficit z = -69.35, p < 0.001**
- Qwen3-8B effect = +0.079, z = +23.49, p < 0.001
- 同样退化为加法模型

### Verification MISMATCH 原因
1. **N 不匹配** (57,512 vs 56,480)：TRAJ func 只有 1 seed (1,032 samples)，且 CWM func s123 可能加载了 repo 级别的预测文件 (`eval_repo_cwm_predictions.jsonl`)
2. **CWM main coef 不匹配** (-0.225 vs -0.002)：交互项被丢弃后，CWM 系数吸收了交互效应
3. **cls8b_* 目录解析为 model=UNKNOWN**：目录名缺少 "qwen" 前缀，需要修复 `infer_metadata` 或重命名目录

输出保存在 `/root/autodl-tmp/artifacts/w5_full_regression/results.json` 和 `paper_numbers.txt`。

---
