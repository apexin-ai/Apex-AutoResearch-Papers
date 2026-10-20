# ssh qwen eval prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_qwen-eval-prep_20260521T131554_result.json`
- **Structured JSON:** [`001a3a8c630ec37584b2.json`](../../sessions/00/001a3a8c630ec37584b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇总报告

### 1. Eval 脚本列表

| 脚本 | 路径 | 用途 |
|------|------|------|
| **eval_repo_cwm.py** | `/home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py` (19KB, May 18) | 主 eval 脚本，已支持 `--split`, `--batch_size`, `--max_samples`, `--output_dir`, `--start_idx` |
| eval_cwm_baseline.py | `/root/exec-sim-repair-verifier/eval_cwm_baseline.py` | function-level CWM eval（不适用） |
| cwm8b_final_test_eval.sh | `/root/autodl-tmp/scripts/cwm8b_final_test_eval.sh` | **旧版，有 bug**（传了 `--split`/`--output_dir` 但调用的是旧版 eval_repo_cwm.py）|
| test_qwen_eval_batch2.sh | `/home/sonny/.../test_qwen_eval_batch2.sh` | 旧版 batch test，指向不存在的 checkpoint-4200 |

### 2. GPU 分配

- 所有脚本使用 `CUDA_VISIBLE_DEVICES=$GPU` + `--device cuda:0` 模式（正确）
- 没有硬编码的 GPU 编号问题
- **新建脚本**：s123 eval 默认 GPU 0，s456 eval 默认 GPU 3，均可通过参数覆盖

### 3. batch_size 配置

`/home/sonny/` 版本的 `eval_repo_cwm.py` 已完整支持：
- `--batch_size` (默认=1)
- `--max_samples` (默认=None, 即全量)
- `--max_seq_length` (默认=8192)
- `--max_new_tokens` (默认=512)

### 4. Checkpoint 排序逻辑

使用 `awk -F'checkpoint-' '{print $NF, $0}' | sort -n | tail -1`，**数值排序正确**，不存在 `sort -t'-' -k2` bug。

### 5. 新建脚本

| 脚本 | 路径 | 说明 |
|------|------|------|
| `test_qwen_eval_batch.sh` | `/home/sonny/.../` | 自动检测最新 checkpoint，测试 batch=2/4 各 50 samples，`bash test_qwen_eval_batch.sh [GPU]` |
| `run_qwen_cwm_s123_eval.sh` | `/home/sonny/.../` | s123 全量 test eval，`bash run_qwen_cwm_s123_eval.sh [GPU] [BATCH_SIZE]` |
| `run_qwen_cwm_s456_eval.sh` | `/home/sonny/.../` | s456 全量 test eval，`bash run_qwen_cwm_s456_eval.sh [GPU] [BATCH_SIZE]` |
| `watch_qwen_train_then_eval.sh` | `/home/sonny/.../` | 监控训练 PID，完成后自动启动 eval |

### 6. 训练进度 (**关键更新**)

| Seed | PID | 当前 Step | 总 Step | 进度 | 速度 |
|------|-----|-----------|---------|------|------|
| s123 | 4271 | **5400**/6633 | 6633 | **81%** | ~12.3s/step |
| s456 | 4561 | **5400**/6633 | 6633 | **81%** | ~12.0s/step |

**剩余：1233 steps**
- 纯训练：~4.3h
- 含 12 次 eval（每次 ~19min）：~3.8h
- **预计完成：05:00-05:30 UTC+8 (5月22日)**

⚠️ **这比你预估的 01:00 UTC+8 晚约 4-5 小时。** GPU 全部满载（GPU 0/1/2/3 利用率 99%/80%/100%/98%），batch test 需要等训练完成后才能跑。

### 启动方式

训练完成后手动启动：
```bash
# 先跑 batch test（训练完成后某个 GPU 空闲时）
bash test_qwen_eval_batch.sh 0

# 根据 batch test 结果，启动全量 eval
bash run_qwen_cwm_s123_eval.sh 0 [BATCH_SIZE]
bash run_qwen_cwm_s456_eval.sh 3 [BATCH_SIZE]
```

或者现在启动 watcher 自动触发（默认 batch=1，可改）：
```bash
nohup bash watch_qwen_train_then_eval.sh 1 > watch_qwen_eval.log 2>&1 &
```

---
