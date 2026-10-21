# code per test majority voting

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_per-test-majority-voting_20260512T081800_result.json`
- **Structured JSON:** [`faa6ab408e3893416e26.json`](../../sessions/fa/faa6ab408e3893416e26.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

### 1. Checkpoint 和 Base Model 路径

| 项目 | 路径 | 状态 |
|------|------|------|
| Qwen3-4B base model | `/root/.cache/huggingface/hub/Qwen/Qwen3-4B/` | seetacloud 上存在 |
| 4B LoRA checkpoint | `/home/sonny/exec-sim-repair-verifier/checkpoints/best/` | **仅在 home-1x5090 上存在** (61MB) |
| test.jsonl | `/home/sonny/exec-sim-repair-verifier/data/test.jsonl` | seetacloud 上存在 (1890 条) |

### 2. 脚本 Dry-run
- `python3 -c py_compile`: **SYNTAX_OK**
- `python3 eval_majority_voting.py --help`: **正常输出**
- 脚本已上传到 seetacloud `/home/sonny/exec-sim-repair-verifier/eval_majority_voting.py`

### 3. **BLOCKER: 4B checkpoint 无法传输**

scp 从 seetacloud → home-1x5090 失败：`Could not resolve hostname home-1x5090: Name or service not known`。两台服务器之间没有 SSH 互通配置。

seetacloud 上只有 8B 的 `checkpoints_cls8b` 和 `checkpoints_cwm8b`（都是 Qwen3-8B LoRA），不能用于此实验。

### 4. 无法提交

因为 checkpoint 不在 seetacloud 上，实验无法提交。预备的提交命令：

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && cd /home/sonny/exec-sim-repair-verifier && python3 eval_majority_voting.py --base_model_path /root/.cache/huggingface/hub/Qwen/Qwen3-4B --checkpoint_path checkpoints/best --data_dir data/ --output eval_majority_voting.json --K 3 --temperature 0.7 --gpu 2"
```

**需要解决**: 手动将 `home-1x5090:/home/sonny/exec-sim-repair-verifier/checkpoints/best/` 复制到 seetacloud 同路径，之后即可直接用 `submit_training_job` 提交。

---
