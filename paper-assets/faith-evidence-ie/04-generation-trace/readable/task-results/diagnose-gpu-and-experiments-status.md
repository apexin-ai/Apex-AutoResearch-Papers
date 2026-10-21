# diagnose gpu and experiments status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gpu-and-experiments-status_20260520T143334_result.json`
- **Structured JSON:** [`af60ab585b04b6b2200e.json`](../../sessions/af/af60ab585b04b6b2200e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器诊断结果

### 1. GPU 状态

| GPU | 型号 | 利用率 | 显存占用 | 总显存 | 温度 |
|-----|------|--------|----------|--------|------|
| 0 | RTX PRO 6000 Blackwell | 92% | 32,503 / 97,887 MiB | 33% | 64°C |
| 1 | RTX PRO 6000 Blackwell | 89% | 18,879 / 97,887 MiB | 19% | 54°C |
| **2** | RTX PRO 6000 Blackwell | **0%** | **0 MiB** | **空闲** | 31°C |
| **3** | RTX PRO 6000 Blackwell | **0%** | **0 MiB** | **空闲** | 31°C |

**GPU 上的进程：**
- PID **17649** → GPU 0, 32,494 MiB — `python` (14B rsft generate)
- PID **27327** → GPU 1, 18,870 MiB — `python` (llama eval)

### 2. Registry RUNNING 实验进程

- **d112_rsft_s44_ced_score** (PID 604576): **PID_DEAD** — 进程不存在
- **d112_rsft_s44_generate**: 日志文件 `d112_rsft_s44_ced_score.log` 和 `d112_rsft_s44_generate.log` 均 **LOG_NOT_FOUND**，无相关进程在跑

### 3. 旧 cron 追踪的进程

| 任务 | PID | 状态 | 运行时长 | 说明 |
|------|-----|------|----------|------|
| migration (rsync) | 6660 | **ALIVE** | 6h02m45s | `bash /tmp/rsync_progress_reporter.sh` — rsync 数据迁移仍在跑（PID 5150/5151/5152 也活着） |
| plan017_14b_rsft_generate_r3 | 17644 | **ALIVE** | 2h58m33s | CUDA_VISIBLE_DEVICES=0, 14B RSFT generation, 实际 python PID=17649 |
| eval_llama_sft_s43_no_evidence | 27322 | **ALIVE** | 25m35s | CUDA_VISIBLE_DEVICES=1, Llama-3.1-8B eval, 实际 python PID=27327 |

### 4. 日志尾部

**plan017_14b_rsft_generate_r3.log:**
- 进度: **556/1155 (48%)**, 运行 ~2h58m
- 当前速度: ~20-26s/it
- 最近 monitor: format_ok_rate 99.9%, truncation_rate 6.9%, mean_diversity 7.5/8
- ETA: ~3h53m 剩余

**eval_llama_sft_s43_no_evidence.log:**
- 进度: **52/247 (21%)**, 运行 ~25m
- 当前速度: ~29-32s/it, batch_size=4
- 模型: Llama-3.1-8B + LoRA adapter (s43), `--no_evidence` 已传
- ETA: ~1h35m 剩余

### 5. 磁盘状态

```
/dev/md0  350G  161G  190G  46%  /root/autodl-tmp
```

使用率 46%，剩余 190GB，充裕。

### 6. tmux 会话

`tmux ls` 被 read-only 模式阻止，无法查询。从 `ps aux` 看没有 tmux server 进程，应该没有活跃 tmux 会话。

---

**总结：** GPU 0/1 各跑一个任务（14B generate + 8B eval），GPU 2/3 完全空闲。d112 系列实验（registry 中标记 RUNNING）的进程和日志均不存在，registry 状态与实际不符。数据迁移 rsync 仍在后台运行中。

---
