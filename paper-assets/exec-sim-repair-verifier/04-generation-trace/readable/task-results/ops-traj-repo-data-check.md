# ops traj repo data check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_traj-repo-data-check_20260516T143829_result.json`
- **Structured JSON:** [`e07338f04ab8ba75d112.json`](../../sessions/e0/e07338f04ab8ba75d112.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. Repo-level TRAJ 数据是否存在？

**不存在。** `data/swebench_full/` 下无任何 traj 文件。现有 traj 文件全是 func-level（在 `data/` 下）：

| 文件 | 行数 | 级别 |
|------|------|------|
| `data/traj_train.jsonl` | 8,052 | func-level (HumanEval/MBPP) |
| `data/traj_val.jsonl` | — | func-level |
| `data/traj_train_cls.jsonl` | — | func-level 变种 |

### 2. 能否快速生成？

**可以，<5分钟。** `build_traj_data.py` 已就绪，它将 per-test CLS 数据按 `(problem_id, mutation_type, code)` 分组，聚合为 trajectory-level：
- all tests pass → `label=1` (resolved)
- any test fail → `label=0` (unresolved)

输出格式含 `code`, `test_summary`, `label`——正是 `train_traj_verifier.py` 期望的格式。

**需要先建 symlink**，因为 `build_traj_data.py` 期望输入文件名为 `train.jsonl` 而非 `swebench_train.jsonl`：

```bash
cd /home/sonny/exec-sim-repair-verifier/data/swebench_full/
ln -s swebench_train.jsonl train.jsonl
ln -s swebench_val.jsonl val.jsonl
ln -s swebench_test.jsonl test.jsonl

cd /home/sonny/exec-sim-repair-verifier/
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
python build_traj_data.py --input_dir data/swebench_full --output_dir data/swebench_full --prefix traj
```

输入 70,748 per-test → 预估产出 ~20,000-35,000 trajectories（参考 func-level 压缩比 15,290 → 8,052 ≈ 1.9x）。

### 3. `train_traj_verifier.py` 数据格式要求

每行 JSONL 需要：
- `code` (str): 代码 patch / diff
- `test_summary` (str): 测试摘要，格式 `"N tests:\n- test1\n- test2..."`
- `label` (int): 1=resolved, 0=unresolved

加载路径：`{data_dir}/{data_prefix}_train.jsonl` 和 `{data_dir}/{data_prefix}_val.jsonl`

### 4. 建议的训练命令

与 repo-level CLS/CWM 保持一致的超参（DeepSeek-6.7B, seq=8192, LoRA r=16/α=32, 3 epochs）：

```bash
cd /home/sonny/exec-sim-repair-verifier/
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

CUDA_VISIBLE_DEVICES=2,3 python train_traj_verifier.py \
  --data_dir data/swebench_full \
  --data_prefix traj \
  --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct \
  --output_dir checkpoints_traj_repo/ \
  --run_name deepseek-traj-repo-s42 \
  --max_seq_length 8192 \
  --batch_size 2 \
  --grad_accumulation 16 \
  --lr 2e-4 \
  --epochs 3 \
  --seed 42
```

### 注意事项

- `train_traj_verifier.py` 没有 `StderrLogCallback`（不像 `train_repo_verifier.py`），监控需要看 wandb 或 stdout log
- `train_traj_verifier.py` 没有 class weighting——如果 traj 数据不均衡（resolved 远多于 unresolved），可能需要加
- `train_unified.py` 只支持 `cls`/`cwm` task，不支持 `traj`，必须用 `train_traj_verifier.py`

---
