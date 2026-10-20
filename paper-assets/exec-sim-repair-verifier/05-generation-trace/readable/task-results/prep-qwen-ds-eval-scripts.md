# prep qwen ds eval scripts

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_qwen-ds-eval-scripts_20260521T135420_result.json`
- **Structured JSON:** [`4c06fcbce4bb57fb4edc.json`](../../sessions/4c/4c06fcbce4bb57fb4edc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕，汇报如下。

---

## 汇总

### 1. Eval 脚本状态

3 个脚本**全部已存在**，无需创建：

| 脚本 | CKPT_DIR | GPU | seq_len | batch | 
|------|----------|-----|---------|-------|
| `eval_qwen_cwm_s123.sh` | `checkpoints_repo_cwm_8b_s123` | **1** | 8192 | **1** |
| `eval_qwen_cwm_s456.sh` | `checkpoints_repo_cwm_8b_s456` | **2** | 8192 | **1** |
| `eval_deepseek_cwm_s123_v2.sh` | `checkpoints_deepseek_cwm_repo_s123_v2` | 2 | 4096 | 4 |

### 2. Checkpoint 快照

| Training | 当前步 | 总步数 | 进度 | 训练 GPU |
|----------|--------|--------|------|----------|
| Qwen s123 | 5400 | 6633 | **81%** | GPU 0 |
| Qwen s456 | 5400 | 6633 | **81%** | GPU 3 |
| DS s123_v2 | 4209 | 12627 | **33%** | GPU 2 |

Qwen 两个约还剩 1233 步，预计几小时内完成。**DS s123 只完成 1/3，远未即将结束。**

### 3. 潜在问题

**A) GPU 分配冲突**：

当前 GPU 占用：GPU 0=Qwen s123训练, GPU 1=DS s456 eval, GPU 2=DS s123训练, GPU 3=Qwen s456训练

- `eval_qwen_cwm_s123.sh` 指定 GPU 1 → 但 DS s456 eval 可能还在跑
- `eval_qwen_cwm_s456.sh` 指定 GPU 2 → DS s123 训练在 GPU 2（且还要跑很久）

**建议修改**：训练完成后 eval 用各自释放的 GPU：
- Qwen s123 eval → GPU **0**
- Qwen s456 eval → GPU **3**

**B) Qwen batch_size=1 问题确认**：两个 Qwen 脚本都是 batch=1 + seq8192，9784 samples 确实会 30-50h。

### 4. Batch Test 命令模板

`eval_repo_cwm.py` 支持 `--max_samples`，可直接用：

```bash
# Qwen s123 batch=2 测试 (训练完后在 GPU 0)
cd /home/sonny/exec-sim-repair-verifier
CKPT=$(ls -d /root/autodl-tmp/checkpoints_repo_cwm_8b_s123/checkpoint-* | awk -F'checkpoint-' '{print $NF, $0}' | sort -n | tail -1 | cut -d' ' -f2-)
CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python eval_repo_cwm.py \
    --checkpoint_dir "$CKPT" \
    --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
    --split test --device cuda:0 --max_seq_length 8192 --max_new_tokens 512 \
    --batch_size 2 --max_samples 50 \
    --output_dir /root/autodl-tmp/eval_results/qwen_batch_test_bs2

# batch=4 测试
CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python eval_repo_cwm.py \
    --checkpoint_dir "$CKPT" \
    --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
    --split test --device cuda:0 --max_seq_length 8192 --max_new_tokens 512 \
    --batch_size 4 --max_samples 50 \
    --output_dir /root/autodl-tmp/eval_results/qwen_batch_test_bs4
```

### 5. 下一步建议

需要确认是否现在修改两个 Qwen eval 脚本的 GPU 分配（`1→0`, `2→3`）？batch_size 等 batch test 出结果后再改。

---
