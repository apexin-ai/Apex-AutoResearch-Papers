# ops westd triple gpu launch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-triple-gpu-launch_20260520T021228_result.json`
- **Structured JSON:** [`0ec2441827a7bedc8117.json`](../../sessions/0e/0ec2441827a7bedc8117.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 registry 已更新。汇总：

```
磁盘状态: overlay 30G, 1.7G used (6%) — 根分区健康
HF cache 迁移: [已就位] /root/autodl-tmp/.hf_cache/datasets 已存在且被活跃进程使用

cuda:0 Phi-4 GSM8K eval: [已在运行] PID=246700 tmux=gsm8k_phi4_s123
  进度: 59% (97/165 batches), 正在 eval d000_s123, ~13min 后完成 d000 → 自动继续 d100

cuda:1 Qwen-14B d100 retrain: [已在运行] PID=246779 tmux=sft_qwen14b_d100_s123
  进度: 8% (345/4159 steps), ETA ~3h, lora_alpha=32 ✓

cuda:2 OLMo-2 d000_s0: [运行中] PID=238804 tmux=sft_olmo2_s0
  进度: 59% (1841/3125 steps), ~1.8s/it, ETA ~38min, loss=0.953

cuda:3 Gemma-2 d100 retrain: [已在运行] PID=246861 tmux=sft_gemma2_d100_s123
  进度: 9% (358/4159 steps), ETA ~3h, lora_alpha=32 ✓
```

**关键发现：cuda:0/1/3 并非空闲——另一个 worker session 已于 ~18min 前（09:55 UTC）启动了完全相同的 3 个任务。** 按 C001 约束，未重复提交。已将 3 个实验注册到 registry 并标记为 RUNNING。

---
