# code val5120 sweep prep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_val5120-sweep-prep_20260514T172722_result.json`
- **Structured JSON:** [`61766cc6159a95d74076.json`](../../sessions/61/61766cc6159a95d74076.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入服务器。调研结果：

**脚本参数确认：** 两个脚本都已支持 `--split val` 和 `--max_seq_length 5120`，无需修改。

**Checkpoints 确认：**

| 模型 | 目录 | 可用 ckpts | eval 脚本 |
|------|------|-----------|-----------|
| CLS v5-conda (seed42) | `/root/autodl-tmp/checkpoints_repo_cls_v5_conda/` | 200, 400, 600 | `eval_repo_cls.py` |
| CWM v12 (seed42) | `/root/autodl-tmp/checkpoints_repo_cwm_conda_v12/` | 300, 400, 500, 600, 700 | `eval_repo_cwm.py` |
| CWM seed123 | `/root/autodl-tmp/checkpoints_repo_cwm_seed123_conda/` | 200, 300, 400, 500, 600 | `eval_repo_cwm.py` |

**注意事项：**
- CWM 脚本 D077 逻辑：val split 默认 max_seq_length=8192，但我们显式传 5120 覆盖
- CLS 脚本不自动创建输出目录，命令清单里包含了 `mkdir -p`
- CWM 脚本有 `--output_dir` + 自动 makedirs
- CLS batch_size=8（轻量，max_new_tokens=8），CWM batch_size 自动=2（max_new_tokens=1024）
- 总计 13 runs，6 phases 双 GPU 并行，预计 6-12hr

命令清单已写到 `/home/sonny/exec-sim-repair-verifier/val5120_sweep_commands.txt`。

---
