# ssh cwm repo provenance audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cwm-repo-provenance-audit_20260523T103538_result.json`
- **Structured JSON:** [`2e7cac4c62bf20e50aa2.json`](../../sessions/2e/2e7cac4c62bf20e50aa2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据溯源完成。以下是完整报告。

---

## CWM 8B Repo-level 数据溯源报告

### 汇总：Table 3 的 66.48 ± 1.15 由以下 3 个数据点组成

| Seed | Accuracy | Checkpoint | max_seq_length | max_new_tokens | batch_size | Eval 结果路径 |
|------|----------|-----------|----------------|----------------|------------|-------------|
| s42 | **65.17%** | checkpoint-**400** (step 400/6633, ~6% 训练) | **2048** | **1024** | 8 | `/root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_merged/metrics.json` |
| s123 | **67.33%** | checkpoint-**6633** (final epoch, 100% 训练) | **8192** | **512** | 4 | `/root/autodl-tmp/eval_results/qwen3_8b_cwm_repo_s123_eval/eval_repo_cwm.json` |
| s456 | **66.93%** | checkpoint-**6633** (final epoch, 100% 训练) | **8192** | **512** | 4 | `/root/autodl-tmp/eval_results/qwen3_8b_cwm_repo_s456_eval/eval_repo_cwm.json` |

Mean = (65.17 + 67.33 + 66.93) / 3 = **66.48** ✓
Std = **1.15** ✓

---

### 逐 Seed 详情

**Seed 42:**
- Registry 实验 ID: `cwm8b-ckpt400-test-eval` → 分 shard 执行（shard2/3/4），最终 merge 到 `cwm_8b_ckpt400_test_merged/`
- Checkpoint: `/root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-400`（val-best, eval_loss=0.286）
- 训练配置: `train_repo_cwm.py`, bs=1, ga=32, lr=5e-5, seq2048, epochs=3, lora_r=16
- Eval 脚本: `eval_repo_cwm.py --max_seq_length 2048 --max_new_tokens 1024 --batch_size 8`
- Eval 命令: 原始分 shard 执行（见 registry `cwm8b-ckpt400-test-eval-v3`, `cwm8b-ckpt400-test-eval-shard2` 等）
- Unparseable: 7222/9784 = 73.81%
- 注意: 存在一个**更新的** eval（`qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval`，seq4096，accuracy=64.36%），其 hypothesis 明确说 "Previous Qwen3 CWM evals used seq8192 while DeepSeek CWM used seq4096, creating confound"。**但论文使用的是旧的 65.17% 而非 64.36%。**

**Seed 123:**
- Registry 实验 ID: `qwen3-8b-cwm-repo-s123-eval`
- 训练: `qwen3-8b-cwm-repo-s123-train-v4`（从 checkpoint-3000 恢复）
- Checkpoint: `/root/autodl-tmp/checkpoints_repo_cwm_8b_s123/checkpoint-6633`（final epoch）
- Eval 脚本: `bash run_qwen_cwm_s123_eval.sh` → `eval_repo_cwm.py`
- Eval config: `--max_seq_length 8192 --max_new_tokens 512 --batch_size 4`
- Unparseable: 6257/9784 = 63.95%

**Seed 456:**
- Registry 实验 ID: `qwen3-8b-cwm-repo-s456-eval`
- 训练: `qwen3-8b-cwm-repo-s456-train-v4`（从 checkpoint-6100 恢复）
- Checkpoint: `/root/autodl-tmp/checkpoints_repo_cwm_8b_s456/checkpoint-6633`（final epoch）
- Eval 脚本: `bash eval_qwen_cwm_s456.sh (CVD=3, batch=4, checkpoint-6633)`
- Eval config: `--max_seq_length 8192 --max_new_tokens 512 --batch_size 4`
- Unparseable: 5909/9784 = 60.39%

---

### 确认的配置不一致（3 处）

1. **Checkpoint 不一致**: s42 使用 checkpoint-400（early stopping, 训练 6%），s123/s456 使用 checkpoint-6633（训练 100%，final epoch）。这不是 seed variance，而是 checkpoint selection 差异。

2. **max_seq_length 不一致**: s42 用 2048，s123/s456 用 8192（4 倍差异）。seq_length 直接影响 input truncation 行为和 accuracy 数字。

3. **max_new_tokens 不一致**: s42 用 1024，s123/s456 用 512。这影响 truncation rate 和生成质量。

### 额外发现

- 论文用的 s42 数据（65.17%）来自旧的 sharded eval（seq2048），但**之后专门做了一个 seq4096 的 canonical eval**（`qwen3-8b-cwm-repo-s42-ckpt400-seq4096-eval`，accuracy=64.36%），其目的就是消除 seq_length confound。论文没有使用这个 canonical 版本。
- s42 的 unparseable rate（73.81%）显著高于 s123（63.95%）和 s456（60.39%），这至少部分源于 seq_length 和 max_new_tokens 的差异，而非 seed variance。
- `cwm_8b_ckpt6100_test` 目录下有一个正在进行的新 eval（仅有 incremental results），可能是试图用 checkpoint-6100 重新 eval s42。

---
