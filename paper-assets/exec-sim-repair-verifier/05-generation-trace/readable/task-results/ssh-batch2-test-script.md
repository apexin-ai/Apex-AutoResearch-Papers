# ssh batch2 test script

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_batch2-test-script_20260521T061628_result.json`
- **Structured JSON:** [`df4594fc758525471cfd.json`](../../sessions/df/df4594fc758525471cfd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### Part A: GPU 2 状态

**GPU 2 正在跑 DeepSeek s123-v2 resume 训练**，占用 20.5 GB VRAM。

- PID 28200: `train_unified.py --task cwm --resume_from_checkpoint checkpoint-4209 --seed 123 --epochs 3 --run_name deepseek-cwm-repo-s123-v2-resume`
- Watcher 日志 (`watch_s123_resume.log`) 确认：eval PID 978461 于 **04:24 UTC** 退出，watcher 随即启动 resume 训练
- 一切按预期运行

### Part B: 测试脚本

`/home/sonny/exec-sim-repair-verifier/test_qwen_eval_batch2.sh` 已创建，chmod +x 完成。

**路径修正**：你指定的 `/root/autodl-tmp/checkpoints_repo_cwm_8b_s42/best/` 不存在。Qwen CWM 8B 没有 s42 checkpoint，也没有 `best/` 子目录。脚本改用了 **`checkpoints_repo_cwm_8b_s123/checkpoint-4200/`**（s123 最新 step）。可用的 Qwen CWM 8B checkpoints：

| 目录 | 可用 steps |
|------|-----------|
| `checkpoints_repo_cwm_8b_s123` | 300, 3900-4200 |
| `checkpoints_repo_cwm_8b_s456` | 300, 4000-4300 |

`eval_repo_cwm.py` 已确认支持 `--max_samples`、`--batch_size`、`--output_dir` 参数，脚本无需额外适配。

---
