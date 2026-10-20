# ssh check all 6gpu status v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_all_6gpu_status_v2_20260520T142054_result.json`
- **Structured JSON:** [`2bdb80da57c19e5cedaa.json`](../../sessions/2b/2bdb80da57c19e5cedaa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-29022

**nvidia-smi**: cuda:0/1 活跃（99%/92% util），cuda:2/3 空闲（0%）

### cuda:0 - eval_gsm8k_grpo_cka_only_20_seed456_full
- **进程状态**: ALIVE (PID 252604, 运行 49min)
- **进度**: 346/1319 (26%)
- **中间准确率**: **67.00%** @ 300 samples, eos_rate=99.00%, avg_len=198
- **速度**: ~2.5-3s/it
- **预计剩余**: ~50min

### cuda:1 - eval_gsm8k_grpo_cka_only_15_v2
- **进程状态**: ALIVE (PID 252919, 运行 48min)
- **进度**: 476/1319 (36%)
- **中间准确率**: **74.22%** @ 450 samples, eos_rate=99.11%, avg_len=192
- **速度**: ~2-3s/it
- **预计剩余**: ~45min

### cuda:2 - grpo_standard_15_v2
- **进程状态**: DEAD (已完成)
- **训练**: 100/100 steps, 21min49s total (13.09s/it)
- **最终指标 (step 100)**:
  - loss=0.01142, grad_norm=3.547
  - **reward=0.1375**, reward_std=0.2778
  - kl=0.004099, entropy=0.1932
- **reward 趋势**: 0.1875 → 0.1363 → 0.1069 → ... → 0.1375（基本没有明显提升）
- **Checkpoint**: 已保存，model.safetensors 12.1GB

### cuda:3
- 空闲，无进程

---

## westb-23072

**nvidia-smi**: cuda:0/1 都活跃（99% util, ~16.5GB VRAM）

### cuda:0 - eval_gsm8k_sft_qwen_cka_only_20
- **进程状态**: ALIVE (PID 18038, 运行 2h49min)
- **进度**: 144/200 (72%)
- **中间准确率**: **54.00%** @ 100 samples, eos_rate=32.00%, avg_len=1438
- **速度**: 极慢，~60-95s/it（max_new_tokens=2048 导致）
- **预计剩余**: ~1-1.5h

### cuda:1 - eval_gsm8k_sft_qwen_standard_20
- **进程状态**: ALIVE (PID 18114, 运行 2h49min)
- **进度**: 129/200 (65%)
- **中间准确率**: **18.00%** @ 100 samples, eos_rate=35.00%, avg_len=1664
- **速度**: 极慢，~90-97s/it
- **预计剩余**: ~1.5-2h

---

## 关键发现

| 实验 | 状态 | 准确率 | 备注 |
|------|------|--------|------|
| grpo_cka_only_15_v2 | eval 36% done | **74.22%** @ 450 | 目前最高 |
| grpo_cka_only_20_seed456 | eval 26% done | **67.00%** @ 300 | |
| grpo_standard_15_v2 | 训练完成 | 待 eval | reward 始终低（~0.1），训练效果存疑 |
| sft_qwen_cka_only_20 | eval 72% done | **54.00%** @ 100 | eos_rate 仅 32%，生成过长 |
| sft_qwen_standard_20 | eval 65% done | **18.00%** @ 100 | 极差，eos_rate 35% |

- **grpo_cka_only_15_v2 暂时领先**，74.22% 准确率
- westb-23072 的 Qwen SFT eval 非常慢（max_new_tokens=2048 + eos_rate 低 → 几乎每个样本都生成到上限）
- **sft_qwen_standard_20 仅 18% 准确率**，standard 剪枝在 SFT 恢复后效果很差
- westd-29022 cuda:3 空闲，可启动 grpo_standard_15_v2 的 GSM8K eval

---
