# code prep cwm repo eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-cwm-repo-eval_20260516T183630_result.json`
- **Structured JSON:** [`6b6f32aeb3d6b1f5d84f.json`](../../sessions/6b/6b6f32aeb3d6b1f5d84f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在情况清楚了。以下是完整分析：

---

## 状况纠正：训练远未完成

**训练实际进度：epoch 1/3 完成（33%），当前正在跑 epoch 1 的 val eval（4373/4668 batches, ~1.5分钟后 eval 结束）。**

关键数据：
- 总训练步数：13,266（4,422 步/epoch × 3 epochs）
- 已完成：epoch 1（4,422步），耗时 ~10 小时
- 剩余：epoch 2 + epoch 3 ≈ **20+ 小时**
- 当前进度条 `4373/4668` 是 val eval（9335 val samples / batch_size=2 = 4668 batches），不是训练

用户说的"7分钟内完成"可能看到了 eval 进度条的 94% 误判为整体训练进度。

---

## 1. Eval 脚本

**路径**: `/home/sonny/exec-sim-repair-verifier/eval_repo_cwm.py`

**参数**:
| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--checkpoint_dir` | 无 | LoRA checkpoint 目录 |
| `--model_name` | `Qwen/Qwen3-4B` | 基座模型路径 |
| `--split` | `test` | val 或 test |
| `--batch_size` | 1 | 推理 batch |
| `--max_new_tokens` | 512 | 生成长度 |
| `--max_seq_length` | 8192 | 输入截断 |
| `--device` | `cuda:0` | GPU |
| `--output_dir` | None | 输出目录 |
| `--data_dir` | `data/swebench_full` | 数据目录 |
| `--start_idx` | None | 分片起点 |
| `--max_samples` | None | 最大样本数 |

---

## 2. Checkpoint 状态

- `/root/autodl-tmp/checkpoints_deepseek_cwm_repo/` — **当前为空**（epoch 1 eval 完成后会保存第一个 checkpoint）
- 预期结构（参考其他实验）：`best/` 子目录（PEFT adapter 格式）

---

## 3. 准备好的 Eval 命令

### Val split（快速验证，~9335 samples）
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 python3 eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/best/ --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --split val --device cuda:0 --batch_size 8 --max_new_tokens 512 --output_dir /root/autodl-tmp/eval_results/deepseek_cwm_repo_val/"
```

### Test split（正式评测，~9784 samples）
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /home/sonny/exec-sim-repair-verifier && CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 python3 eval_repo_cwm.py --checkpoint_dir /root/autodl-tmp/checkpoints_deepseek_cwm_repo/best/ --model_name /root/autodl-tmp/models/deepseek-ai/deepseek-coder-6.7b-instruct --split test --device cuda:0 --batch_size 8 --max_new_tokens 512 --output_dir /root/autodl-tmp/eval_results/deepseek_cwm_repo_test/"
```

---

## 4. 参考：Qwen CWM repo eval 的做法

从 registry 中成功的 `cwm8b-ckpt400-test-eval-shard2`：
```
CUDA_VISIBLE_DEVICES=1 python3 eval_repo_cwm.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_conda/checkpoint-400 \
  --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B/ \
  --split test --device cuda:0 --batch_size 8 --max_new_tokens 1024 \
  --output_dir /root/autodl-tmp/eval_results/cwm_8b_ckpt400_test_shard2/
```

差异：Qwen 用了 `max_new_tokens=1024`，DeepSeek 用默认 512 应该够（DeepSeek 生成通常更简洁）。

---

## 5. 注意事项

1. **训练还需 ~20 小时**，eval 命令暂时无法执行（`best/` 目录不存在）
2. **~1.5 分钟后** epoch 1 eval 完成 → 会保存 epoch 1 checkpoint。如果想提前跑中间 checkpoint 的 eval，需等目录出现后用 `checkpoint-XXX` 代替 `best/`
3. `CUDA_VISIBLE_DEVICES=1` 是训练占用的 GPU，eval 时需换到空闲 GPU（cuda:0 或等训练结束后用 cuda:1）
4. 同时在跑的还有 `deepseek-cwm-repo-s123`（cuda:3）和 `deepseek-cls-repo-s123`（cuda:2），eval 时建议用 **cuda:0**

---
