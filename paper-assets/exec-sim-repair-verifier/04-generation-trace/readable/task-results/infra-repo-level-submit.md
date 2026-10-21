# infra repo level submit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_repo-level-submit_20260512T110749_result.json`
- **Structured JSON:** [`22bc542f22704dccc18f.json`](../../sessions/22/22bc542f22704dccc18f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功启动并在运行中。

### 汇总

| 实验 | tmux session | PID | GPU | 日志 |
|------|-------------|-----|-----|------|
| repo-level-cls | `repo-level-cls` | 32599 | cuda:2 | `~/runs/exec-sim-repair-verifier/repo-level-cls.log` |
| repo-level-cwm | `repo-level-cwm` | 32678 | cuda:3 | `~/runs/exec-sim-repair-verifier/repo-level-cwm.log` |

### 完整命令

**cls:**
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_verifier.py --max_seq_length 4096 --no_wandb --device cuda:0 && python3 eval_repo_verifier.py --checkpoint_dir checkpoints_repo_cls/best --max_seq_length 4096 --device cuda:0"
```

**cwm:**
```
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 train_repo_cwm.py --max_seq_length 4096 --no_wandb --device cuda:0 && python3 eval_repo_cwm.py --checkpoint_dir checkpoints_repo_cwm/best --max_seq_length 4096 --device cuda:0"
```

日志确认：cls 已加载 70,748 train / 9,335 val，class weights fail=1.7009 / pass=0.2991；cwm 已加载 tokenizer 并开始处理数据。训练完成后会自动接 eval。

---
