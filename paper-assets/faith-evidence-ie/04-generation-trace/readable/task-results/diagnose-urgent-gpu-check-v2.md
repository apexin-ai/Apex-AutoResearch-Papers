# diagnose urgent gpu check v2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_urgent-gpu-check-v2_20260523T032800_result.json`
- **Structured JSON:** [`41dd00fd725624522c94.json`](../../sessions/41/41dd00fd725624522c94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

原始数据如下：

```
=== NVIDIA-SMI ===
0, 96 %, 26857 MiB, 97887 MiB
1, 92 %, 32479 MiB, 97887 MiB
2, 0 %, 0 MiB, 97887 MiB
3, 45 %, 6071 MiB, 97887 MiB

=== GPU PROCESSES ===
220069, 26848 MiB    (GPU 0)
194682, 32470 MiB    (GPU 1)
214028, 6062 MiB     (GPU 3)

=== DPO PID 218955 ===
DEAD

=== DPO OUTPUT DIR ===
README.md
adapter_config.json
adapter_model.safetensors
chat_template.jinja
checkpoint-100
checkpoint-187
ref
tokenizer.json
tokenizer_config.json
training_args.bin

=== DPO LOG TAIL ===
(空 — 日志文件不存在或为空)

=== 8B NO-EVI PID 220069 ===
PID 220069, ELAPSED 34:29, CPU 112%

=== 8B NO-EVI RESULTS ===
(无结果文件，仍在运行)

=== 1.7B PID 214028 ===
PID 214028, ELAPSED 02:20:05, CPU 101%

=== 1.7B PROGRESS ===
(无日志输出)

=== 14B PID 194682 ===
PID 194682, ELAPSED 09:11:40, CPU 100%

=== 14B GEN PROGRESS ===
12744 /root/autodl-tmp/rsft_generations_14b_s43/generations.jsonl

=== TMUX ===
plan017_14b_rsft_s43_generate: 1 windows (created Sat May 23 02:17:02 2026)
```

**摘要：**
- **GPU 2 空闲**，其余三卡被占用
- **DPO (218955)**: 已结束，输出目录有 adapter 和 2 个 checkpoint (100, 187)
- **8B no-evi eval (220069)**: GPU 0, 运行 34 分钟，尚无结果文件
- **1.7B eval (214028)**: GPU 3, 运行 2h20m，无日志输出
- **14B gen (194682)**: GPU 1, 运行 9h11m，已生成 12744 行 generations.jsonl

---
