# infra home gpu audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_home-gpu-audit_20260514T193727_result.json`
- **Structured JSON:** [`ac160e6d9271bb38706f.json`](../../sessions/ac/ac160e6d9271bb38706f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告 — home-1x5090

### GPU
| 项目 | 值 |
|------|-----|
| GPU | RTX 5090 (32GB) |
| 显存占用 | 31727 / 32607 MiB (97%) |
| GPU 利用率 | 100% |
| **状态** | **忙碌** |

### 当前进程
| PID | 用户 | 显存 | 启动时间 | CPU 时间 | 命令 |
|-----|------|------|----------|----------|------|
| 3159474 | sonny | 31718 MiB | 11:51 | 47min+ | `python eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_seed123_home/checkpoint-400 --model_name Qwen/Qwen3-4B --split val --max_seq_length 5120 --output_dir results/repo_cls_seed123_ckpt400_val5120 --device cuda:0` |

正在对 **Qwen3-4B + checkpoint-400 (seed123)** 在 val 集上做 eval，seq_len=5120。

### Checkpoint 目录 (20 个)
关键目录：
- `checkpoints_repo_cls_seed123_home/` — checkpoint-200 到 checkpoint-1000 (5个)
- `checkpoints_repo_cls_v5/`, `checkpoints_repo_cls_8b_westd/`, `checkpoints_repo_cls_8b_conda_westd/`
- `checkpoints_cwm*/`, `checkpoints_traj*/`, `checkpoints_seed*/` 等

### Eval 结果 (`results/` 目录)
| 目录 | 时间 |
|------|------|
| `repo_cls_seed123_ckpt400_val5120` | 正在写入 (11:51) |
| `repo_cls_8b_ckpt3000_val5120` | May 14 11:51 |
| `repo_cls_8b_conda_ckpt400_val5120` | May 14 09:46 |
| `repo_cls_v5_ckpt4600` | May 13 22:59 |
| `repo_cls_v5_ckpt4{400,200,000}` | May 13 21-22h |
| `repo_cls_v5_ckpt600` | May 13 21:10 |
| `repo_cls_seed123_ckpt{1000,800,600,400}` | May 13 19-20h |
| `repo_cls_v4_eval` | May 12 |

还有一个 `val_sweep.log` (May 14 11:52) 在记录 sweep 进度。

**结论**: GPU 满载运行中，正在做 repo_cls seed123 ckpt400 的 val eval。无 `eval_results_*` 目录（eval 结果存在 `results/` 下）。

---
