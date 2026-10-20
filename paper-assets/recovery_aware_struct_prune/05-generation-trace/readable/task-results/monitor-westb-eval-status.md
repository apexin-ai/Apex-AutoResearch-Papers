# monitor westb eval status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westb_eval_status_20260516T125314_result.json`
- **Structured JSON:** [`67d8d1f85bdaa054eb5e.json`](../../sessions/67/67d8d1f85bdaa054eb5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### eval_sft_standard_25 (PID 598084, cuda:1)
- **进度：1204/1319 (91.3%)** — 即将完成
- 运行时间：5h47m
- 最近 checkpoint (1200): **acc=0.5067**, eos_rate=95.42%, avg_len=327
- **预估剩余：~15-30 分钟**（剩 115 样本，平均 ~2-3s/it，偶有长 generation spike）

### eval_sft_rasp_25 (PID 602990, cuda:0)
- **进度：520/1319 (39.4%)**
- 运行时间：4h30m
- 最近 checkpoint (500): **acc=0.5380**, eos_rate=91.20%, avg_len=490
- **预估剩余：~6-7 小时**（avg_len 更长导致速度约为 standard 的一半）

### GPU 利用率
| GPU | Utilization | VRAM |
|-----|------------|------|
| 0 | 100% | 28.9 / 97.9 GB |
| 1 | 100% | 28.9 / 97.9 GB |

### 初步对比
- RASP 25% SFT 暂时领先：**53.8%** vs Standard 25% SFT **50.7%**（+3.1pp）
- 但 RASP 的 eos_rate 更低 (91.2% vs 95.4%)，avg_len 更长 (490 vs 327)，说明 RASP 模型生成更冗长、部分样本未正常终止
- Standard eval 即将完成，RASP 还需到凌晨~3-4 点

---
