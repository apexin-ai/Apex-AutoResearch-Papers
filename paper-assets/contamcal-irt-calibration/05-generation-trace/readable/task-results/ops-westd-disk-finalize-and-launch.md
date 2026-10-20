# ops westd disk finalize and launch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-disk-finalize-and-launch_20260520T015246_result.json`
- **Structured JSON:** [`45e47527d221d6eb5730.json`](../../sessions/45/45e47527d221d6eb5730.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。

```
磁盘最终状态: 6% (/root) — symlink → /root/autodl-tmp/.cache_migrated（释放 20G）
cuda:0: Phi-4 GSM8K eval — PID=246700, 33G ✅
cuda:1: Qwen-14B d100 重训 — PID=246779, 29G ✅
cuda:2: OLMo-2 s0 — PID=238804, 67G 继续运行 ✅
cuda:3: Gemma-2 d100 重训 — PID=246861, 61G ✅
```

4 个 tmux session 活跃：`gsm8k_phi4_s123`, `sft_qwen14b_d100_s123`, `sft_olmo2_s0`, `sft_gemma2_d100_s123`。Registry 3 个新实验均已标记 RUNNING。

---
