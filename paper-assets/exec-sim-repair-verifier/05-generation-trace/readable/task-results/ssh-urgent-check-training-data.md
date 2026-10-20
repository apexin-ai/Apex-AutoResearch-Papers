# ssh urgent check training data

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent-check-training-data_20260520T050302_result.json`
- **Structured JSON:** [`be849116b123978ffeb2.json`](../../sessions/be/be849116b123978ffeb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Here's the summary:

---

## 1. DeepSeek CWM s456

- **脚本**: `train_unified.py --task cwm`
- **数据**: `data/cwm_train.jsonl` — **function-level 短格式** (HumanEval)
- **样本数**: train=15290, val=1896 (dropped 10, 0% truncated)
- **启动时间**: 2026-05-20 13:00:00
- **进度**: 日志到 step ~146/2865 (~5%), ~1.75s/it
- **PID 917644 在 /proc 中不存在** — 进程可能已死或换了 PID

## 2. Qwen CWM s123-v4 (PID 886278)

- **脚本**: `train_repo_cwm.py`
- **命令**: `train_repo_cwm.py --model_name Qwen3-8B --device cuda:0 --seed 123 --epochs 3`
- **数据**: `swebench_full/swebench_train.jsonl` — **repo-level 长格式** (SWE-bench)
- **样本数**: train=70748, val=9335
- **Class weights**: fail=1.7009, pass=0.2991
- **截断率**: train 4.5%, **val 20.2%**
- **进度**: step 100/6633 (~1.5%), ~12s/it
- **Loss**: 24.49 → 18.50

## 3. Qwen CWM s456-v3 (PID 886352)

- **脚本**: `train_repo_cwm.py`
- **命令**: `train_repo_cwm.py --model_name Qwen3-8B --device cuda:0 --seed 456 --epochs 3`
- **数据**: 同上 swebench_full (70748 samples)
- **Class weights**: fail=1.7009, pass=0.2991
- **进度**: step 100/6633 (~1.5%), ~12s/it
- **Loss**: 22.61 → 18.94

两个 Qwen 训练完全对称，只是 seed 不同。

## 4. DeepSeek s42 vs s123 对比

日志文件列表：
```
deepseek-cwm-repo-s123-eval.log
deepseek-cwm-repo-s123-train.log
deepseek-cwm-repo-s123.log
deepseek-cwm-repo-s42-seq4096-eval.log   ← s42 只有 eval 日志，没有 train 日志
deepseek-cwm-repo-s456-train.log
deepseek-cwm-repo.log
```

**DeepSeek s123 训练日志**: 同样使用 `data/cwm_train.jsonl` (function-level, 15290), 已跑到 epoch ~0.99 (step 955/2865), loss 从 2.57 降到 0.039。

## 5. 数据文件

| 文件 | 行数 | 类型 | 内容 |
|------|------|------|------|
| `data/cwm_train.jsonl` | 15,290 | function-level | keys: code, test, target, label, source, problem_id, mutation_type; target="PASS: test completed successfully" |
| `data/swebench_full/swebench_train.jsonl` | 70,748 | repo-level | keys: code(diff), test(test path), label, source, problem_id, mutation_type, error_message, execution_output, metadata |
| `data/cwm_val.jsonl`, `cwm_test.jsonl` | 存在 | function-level | — |
| `swebench_full/cwm_*.jsonl` | **不存在** | — | — |

## 6-7. 训练脚本数据加载逻辑

**`train_unified.py`**:
- `--task cwm` (默认) → `data/cwm_train.jsonl` + `cwm_val.jsonl` (function-level)
- `--task cls` → 优先 `swebench_full/swebench_train.jsonl`，回退 `train.jsonl`
- `--train_file` 可手动覆盖

**`train_repo_cwm.py`**:
- 固定读取 `swebench_full/swebench_train.jsonl` (repo-level)
- 内部有 class weights → **实际做 pass/fail 分类**，虽然名字叫 CWM

---

## 关键发现

**DeepSeek s456 和 s123 用的是完全相同的 function-level 数据 (`cwm_train.jsonl`, 15290 条)**，运行名里虽然有 "repo" 字样，但实际走的是 `train_unified.py --task cwm`，加载的是 HumanEval function-level 短数据，不是 repo-level swebench 数据。

如果 DeepSeek s456 的目的是训 repo-level CWM（和 Qwen 对齐），**那数据加载是错的** — 它应该用 `train_repo_cwm.py` 或者用 `train_unified.py --train_file swebench_full/swebench_train.jsonl`。

---
