# ssh eval params check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval-params-check_20260520T212614_result.json`
- **Structured JSON:** [`7f0c9bc893361eb10d86.json`](../../sessions/7f/7f0c9bc893361eb10d86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## 1. 所有 eval 脚本参数

| 脚本 | GPU | model | batch_size | max_seq_length | max_new_tokens |
|------|-----|-------|-----------|----------------|----------------|
| eval_qwen_cwm_s123.sh | `CUDA_VISIBLE_DEVICES=1` | Qwen3-8B | **1** | **8192** | 512 |
| eval_qwen_cwm_s456.sh | `CUDA_VISIBLE_DEVICES=2` | Qwen3-8B | **1** | **8192** | 512 |
| eval_deepseek_cwm_s123_v2.sh | `CUDA_VISIBLE_DEVICES=2` | DeepSeek-6.7B | **4** | **4096** | 512 |
| eval_deepseek_cwm_s456_v2.sh | `CUDA_VISIBLE_DEVICES=1` | DeepSeek-6.7B | **4** | **4096** | 512 |

**max_new_tokens**: 全部是 **512**，没有设 1024 的。

---

## 2. 当前 s123-v2 eval 进度

- **进程**: PID 978461，已运行 **5h41m**
- **实际参数**: `deepseek-coder-6.7b-instruct`, checkpoint-4209, `--batch_size 4 --max_seq_length 4096 --device cuda:0`（脚本写 `CUDA_VISIBLE_DEVICES=2` 但进程 cmdline 显示 `cuda:0`，说明映射到物理 GPU2）
- **进度**: **4412 / 9784** 样本 = **45.1%**，运行 5h41m
- **速度**: ~4412 / 341min ≈ **12.9 样本/min**
- **预估剩余**: ~(9784 - 4412) / 12.9 ≈ **416 min ≈ 7h** 剩余

---

## 3. eval_repo_cwm.py 支持的参数

支持 `--max_samples`（不叫 `--limit`）和 `--start_idx`，可用于截取子集测试。

---

## 4. Qwen s42 CWM checkpoint 路径

| seed 组 | 路径 | 内容 |
|---------|------|------|
| s123 | `/root/autodl-tmp/checkpoints_repo_cwm_8b_s123/` | checkpoint-2700~3000 |
| s456 | `/root/autodl-tmp/checkpoints_repo_cwm_8b_s456/` | checkpoint-2700~3000 |

---

## 5. GPU VRAM 状态

| GPU | Used | Total | Util |
|-----|------|-------|------|
| 0 | 21257 MiB | 32607 MiB (5090) | 97% |
| 1 | 20253 MiB | 32607 MiB | 99% |
| 2 | 30651 MiB | 32607 MiB | 100% |
| 3 | 31263 MiB | 32607 MiB | 96% |

---

## 6. batch_size=2 可行性判断

**Qwen3-8B (seq8192, batch=1)**：
- 当前 GPU0/1 占用 ~20-21 GB，说明 Qwen3-8B 在 batch=1 + seq8192 下占用约 **20-21 GB / 32 GB**
- 剩余 ~11 GB headroom

**batch=2 的估算**：
- KV cache 是主要增量，seq8192 的 KV cache 对 8B 模型约 2-4 GB/sample（取决于 GQA）
- batch=2 大约需要额外 3-5 GB → 总计 ~24-26 GB，**理论可行**（32 GB 卡有余量）
- 但需注意 max_new_tokens=512 的生成阶段也需要 KV cache 空间

**建议**：用 `--max_samples 50` 做快速测试验证 batch=2 是否 OOM，命令：
```bash
CUDA_VISIBLE_DEVICES=3 python eval_repo_cwm.py \
    --checkpoint_dir /root/autodl-tmp/checkpoints_repo_cwm_8b_s123/checkpoint-3000 \
    --model_name /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
    --split test --device cuda:0 --max_seq_length 8192 \
    --max_new_tokens 512 --batch_size 2 --max_samples 50 \
    --output_dir /tmp/batch2_test
```

当前 GPU2/3 被占满（30-31 GB），需等现有任务完成后才能跑这个测试。

---
