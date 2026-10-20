# code exp 001 sft 3B d000 s123 verify eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_001_sft_3B_d000_s123_verify_eval_20260515T024615_result.json`
- **Structured JSON:** [`e43e9990de14854d82c6.json`](../../sessions/e4/e43e9990de14854d82c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Checkpoint 验证 ✓
- **路径**: `/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter`
- **adapter_model.safetensors**: 114 MB（合理范围）
- **超参确认**: lr=5e-5, r=16, lora_alpha=16, seed=123 ✓
- **训练指标**: train_loss=1.1361, mean_token_accuracy=0.748, steps=3125
- **Registry 已更新**: ANALYZING → **DONE**

### GPU 4 状态 ✗ — 不空闲
GPU 4 被 PID 488065 占用（3718 MiB），正在运行 **0.5B d005 s123 的 para_aligned eval**：
```
evaluate.py --model-path Qwen2.5-0.5B --adapter-path Qwen2.5-0.5B_d005_s123 --mc-format aligned
```

全部 6 块 GPU 均被占用：
| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | 8985 MiB | 69% | 忙 |
| 1 | 3695 MiB | 35% | 忙 |
| 2 | 5857 MiB | 51% | 忙 |
| 3 | 17651 MiB | 42% | 忙 |
| 4 | 3727 MiB | 0% | 被 0.5B eval 占用 |
| 5 | 17981 MiB | 36% | 忙 |

### Aligned eval 命令（GPU 空闲后提交）
```bash
bash -c "source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache"
```

GPU 4 上的 0.5B eval 完成后即可提交。需要等待还是要我检查其他 GPU 的释放时间？

---
