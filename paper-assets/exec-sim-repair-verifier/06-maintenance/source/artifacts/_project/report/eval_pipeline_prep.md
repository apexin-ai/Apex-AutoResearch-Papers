# Repo-Level Eval Pipeline 准备报告

**日期**: 2026-05-12

---

## 1. 可用 Eval 脚本

### seetacloud-westd-4x5090 (root)

| 脚本 | 用途 | 关键参数 |
|------|------|----------|
| `eval_repo_verifier.py` | CLS (pass/fail 分类) 评估 | `--checkpoint_dir` (必填), `--data_dir`, `--model_name`, `--output`, `--batch_size`, `--max_seq_length`, `--save_predictions`, `--device` |
| `eval_repo_cwm.py` | CWM (执行结果生成) 评估 | `--checkpoint_dir` (必填), `--data_dir`, `--model_name`, `--output`, `--batch_size`, `--max_seq_length`, `--max_new_tokens`, `--device` |

- 默认 model_name: `/root/.cache/huggingface/hub/Qwen/Qwen3-4B`
- 默认 data_dir: `/home/sonny/exec-sim-repair-verifier/data/swebench_full`
- CLS 默认 device: `cuda:2`，CWM 默认 device: `cuda:3`
- eval_repo_verifier.py 额外支持截断分析（truncation-aware evaluation）

### home-1x5090 (sonny)

| 脚本 | 用途 | 关键参数 |
|------|------|----------|
| `eval_repo_level.py` | 统一 CLS/CWM 评估 | `--mode cls/cwm` (必填), `--checkpoint_dir` (必填), `--data_dir`, `--model_name`, `--output`, `--batch_size`, `--max_seq_length`, `--max_new_tokens`, `--save_predictions`, `--device` |

- 默认 model_name: `Qwen/Qwen3-4B`（需从 HF 缓存或下载）
- 默认 device: `cuda:0`

---

## 2. Eval 数据路径与样本数

两台服务器路径相同：`data/swebench_full/`

| 文件 | 样本数 | 大小 |
|------|--------|------|
| `swebench_train.jsonl` | 70,748 | ~394MB |
| `swebench_val.jsonl` | 9,335 | ~64MB |
| `swebench_test.jsonl` | 9,784 | ~58MB |

另有 pilot 预测文件: `predictions_gold.jsonl`, `predictions_mutation_*.jsonl`

---

## 3. Checkpoint 状态

### 当前 repo-level checkpoint（全部为空）

| 路径 | 服务器 | 状态 |
|------|--------|------|
| `/root/autodl-tmp/checkpoints_repo_cwm/` | seetacloud | **空** |
| `/root/autodl-tmp/checkpoints_repo_cwm_v4/` | seetacloud | **空** |
| `/root/autodl-tmp/checkpoints_repo_cwm_v6/` | seetacloud | **空** |
| `/root/autodl-tmp/checkpoints_repo_cls/` | seetacloud | **空** |
| `/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_home/` | home | **空** |

训练脚本完成后会将 best adapter 保存到 `{output_dir}/best/`。

### 已有的旧（非 repo-level）checkpoint

**seetacloud:**
- `checkpoints_cls8b/best`, `checkpoints_cls8b_seed123/best`, `checkpoints_cls_seed0/best`
- `checkpoints_cwm8b/best`, `checkpoints_cwm8b_seed123/best`, `checkpoints_cwm8b_seed456/best`
- `checkpoints_cwm_seed123/best`, `checkpoints_cwm_seed789/best`

**home:**
- `checkpoints/best`, `checkpoints_seed42/best`, `checkpoints_seed123/best`, `checkpoints_seed456/best`, `checkpoints_seed789/best`
- `checkpoints_cwm/best`, `checkpoints_cwm_seed0/best`, `checkpoints_cwm_seed456/best`
- `checkpoints_cls8b_seed456/best`
- `checkpoints_traj*/best`, `checkpoints_trace/best`

---

## 4. Eval 命令模板

### CLS — seetacloud (训练完成后)

```bash
cd /home/sonny/exec-sim-repair-verifier

python eval_repo_verifier.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cls/best \
  --model_name /root/.cache/huggingface/hub/Qwen/Qwen3-4B \
  --output eval_results/repo_cls_results.json \
  --save_predictions \
  --device cuda:2
```

### CLS — home (训练完成后)

```bash
cd /home/sonny/exec-sim-repair-verifier

python eval_repo_level.py \
  --mode cls \
  --checkpoint_dir checkpoints_repo_cls_home/best \
  --output eval_results/repo_cls_home_results.json \
  --save_predictions \
  --device cuda:0
```

### CWM v6 — seetacloud (训练完成后)

```bash
cd /home/sonny/exec-sim-repair-verifier

python eval_repo_cwm.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cwm_v6/best \
  --model_name /root/.cache/huggingface/hub/Qwen/Qwen3-4B \
  --output eval_results/repo_cwm_v6_results.json \
  --max_new_tokens 64 \
  --device cuda:3
```

注意：如果 CWM v6 训练使用了不同的 output_dir，需调整 `--checkpoint_dir` 路径。

---

## 5. 缺失项清单

| 项目 | 状态 | 说明 |
|------|------|------|
| repo-level checkpoint (CLS) | **等待训练完成** | seetacloud → `/root/autodl-tmp/checkpoints_repo_cls/best`; home → `checkpoints_repo_cls_home/best` |
| repo-level checkpoint (CWM v6) | **等待训练完成** | seetacloud → `/root/autodl-tmp/checkpoints_repo_cwm_v6/best` 或 `/root/autodl-tmp/checkpoints_repo_cwm/best` |
| eval_results/ 目录 | **seetacloud 已存在**; home 需创建 | `mkdir -p eval_results` |
| home 上的 eval_repo_cwm 脚本 | **不需要** | `eval_repo_level.py --mode cwm` 覆盖 |
| save_predictions 支持 | CLS 两台都有; **CWM (seetacloud) 缺少** | `eval_repo_cwm.py` 没有 `--save_predictions` 参数，如需保存 per-sample 预测需手动加 |

### 无需写新脚本

两台服务器的 eval 脚本已就绪，参数体系完整。训练完成后只需确认 checkpoint 路径，直接执行上述命令即可。
