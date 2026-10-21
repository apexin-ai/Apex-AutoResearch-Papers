# gpu sft 05B d100 s123

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_sft_05B_d100_s123_20260514T192552_result.json`
- **Structured JSON:** [`b4b1bb11a7d034ad98b5.json`](../../sessions/b4/b4b1bb11a7d034ad98b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 1 被占用，无法提交。**

当前进程（PID 426479）：
- 实验: `exp_001_eval_15B_d025_para_aligned`
- 命令: `evaluate.py --model-path Qwen2.5-1.5B --adapter-path Qwen2.5-1.5B_d025_s42 --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir ...`
- 显存: 5880MiB，利用率 52%

这是 1.5B d025 的 paraphrase aligned eval，正在跑中。需要等它完成后才能在 GPU 1 上提交 SFT 训练。

其余前置条件均满足：
- 数据文件 `sft_dosage_100.jsonl` 存在（~96MB）
- 模型 `Qwen2.5-0.5B` 已缓存
- 输出目录 `Qwen2.5-0.5B_d100_s123/` 不存在（无冲突）

等 GPU 1 空闲后可以立即提交。需要我轮询等待还是稍后手动触发？

---
