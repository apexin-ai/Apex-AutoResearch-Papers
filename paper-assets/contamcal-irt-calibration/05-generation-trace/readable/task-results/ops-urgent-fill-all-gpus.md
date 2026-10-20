# ops urgent fill all gpus

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_fill_all_gpus_20260516T153312_result.json`
- **Structured JSON:** [`cebb379dc4a528ebebc0.json`](../../sessions/ce/cebb379dc4a528ebebc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出报告

### 1. Kill 确认
- **PID 740063**: ✅ 已 kill（exit=0）
- **PID 808340/808346**（我的重复提交）: ✅ 已 kill，C001 违规修复

### 2. GPU 全面状态 — 另一个 worker 已填满所有 GPU

| GPU | 任务 | PID | VRAM | 状态 |
|-----|------|-----|------|------|
| cuda:0 | Llama d005 SFT + **1.5B-Instruct MMLU signals** | 804570 + 805721 | 21.6/24.5 GB | 跑了 ~3min |
| cuda:1 | **Llama d000 eval** (gsm8k+arc+humaneval) | 807025 | 6.8/24.5 GB | 跑了 ~3.5min |
| cuda:2 | 0.5B eval | 797754 | 1.5/24.5 GB | 运行中 |
| cuda:3 | Llama d025 SFT | 801766 | 17.9/24.5 GB | 运行中 |
| cuda:4 | **1.5B-Instruct ARC signals** | 806079 | 5.6/24.5 GB | 跑了 ~2min |
| cuda:5 | Llama d100 SFT + **1.5B-Instruct GSM8K signals** | 804791 + 806081 | 23.7/24.5 GB | 跑了 ~3min |

### 3. 你要求的 4 个任务全部已被另一个 worker 提交

- **Llama d000 eval**: PID 807025 on cuda:1，gsm8k+arc_challenge+humaneval（MMLU 已有结果 45.4%）
- **1.5B-Instruct signals**: 3 benchmark 已在跑（MMLU/ARC/GSM8K on cuda:0/4/5）
- 模型路径：`/root/autodl-tmp/models/Qwen/Qwen2___5-1___5B-Instruct/`，ref: `/root/autodl-tmp/models/Qwen/Qwen2___5-1___5B/`

### 4. MMLU merge 结果
`/root/autodl-tmp/exp002/signals/Qwen2.5-3B_d000_s123_a32/signals_merged_mmlu.json` **已存在**，包含 s1_embedding + s2_minkpp + s4_selfcritique 三个信号。

### 5. 预计完成时间
- **cuda:4** (1.5B ARC signals): ~1-1.5h → 最先释放
- **cuda:1** (Llama d000 eval): GSM8K ~4h + ARC ~30m + HumanEval ~1h ≈ **~5.5h**
- **cuda:0/5** (Llama SFT): ~2-4h（取决于数据量）
- **cuda:0** (1.5B MMLU signals): ~3-4h（14k items）
- **cuda:5** (1.5B GSM8K signals): ~1-2h

### 6. 风险提示
- cuda:0 和 cuda:5 上 SFT + signals **共享 GPU**。虽然 1.5B signals 内存小（~5GB），但如果 SFT 接近 OOM 可能冲突。
- 807025 的 batch-size=4（比你建议的 8 小），eval 会慢一些但更稳。
- **0 块 GPU 空闲**，无法新提交任务。cuda:4 最先释放（~1h 后）。

---
