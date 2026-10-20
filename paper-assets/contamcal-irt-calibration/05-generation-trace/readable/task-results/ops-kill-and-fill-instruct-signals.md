# ops kill and fill instruct signals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_and_fill_instruct_signals_20260516T152803_result.json`
- **Structured JSON:** [`30c192ad91afc00af530.json`](../../sessions/30/30c192ad91afc00af530.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前 GPU 布局：

| GPU | PIDs | Memory | 进程 |
|-----|------|--------|------|
| cuda:0 | 804570 (16.2G) + 805721 (576M) | 16.8/24 GB | Llama d005 SFT + **MMLU signals** |
| cuda:1 | — | FREE | |
| cuda:2 | 797754 (1.5G) | 1.5/24 GB | 未知 |
| cuda:3 | 801766 (17.8G) | 17.8/24 GB | 未知 |
| cuda:4 | 806079 (576M) | 0.6/24 GB | **ARC signals** |
| cuda:5 | 804791 (20.6G) + 806081 (576M) | 21.1/24 GB | Llama d100 SFT + **GSM8K signals** ⚠️ |

**关键风险**：cuda:5 已用 21.1GB。当 GSM8K signals 进入 S2 (Min-K%++) 阶段需要加载 1.5B 模型时（~3-4GB），将 OOM。

---

## 产出报告

### 1. Kill 确认
- PID 800570 (cuda:1 重复 Llama eval): ✅ 已 kill
- PID 700982 (挂起 ModelScope 下载): ✅ 已 kill
- PID 804438 (我启动的 HF 下载，不需要了): ✅ 已 kill

### 2. 1.5B-Instruct signals 状态
**另一个 session 已先于我提交了全部 3 个任务**（C001 规则：不重复提交）：

| Benchmark | GPU | PID | 提交命令 |
|-----------|-----|-----|---------|
| MMLU | cuda:0 | 805721 | `CUDA_VISIBLE_DEVICES=0 python compute_signals.py --model-path /root/autodl-tmp/models/Qwen/Qwen2___5-1___5B-Instruct/ --benchmark mmlu --signal all --ref-model-path /root/autodl-tmp/models/Qwen/Qwen2___5-1___5B/ --output-dir /root/autodl-tmp/exp002/signals/Qwen2.5-1.5B-Instruct/ --batch-size 8` |
| ARC | cuda:4 | 806079 | 同上，`--benchmark arc_challenge`, `CUDA_VISIBLE_DEVICES=4` |
| GSM8K | cuda:5 | 806081 | 同上，`--benchmark gsm8k`, `CUDA_VISIBLE_DEVICES=5` |

### 3. mmlu merge 结果
`signals_merged_mmlu.json` **已存在**（14042 items）。无需操作。

### 4. 风险与预计时间

**⚠️ cuda:5 OOM 风险**：Llama d100 训练占 20.6GB + GSM8K signals S2 需 ~3-4GB = 超出 24GB。GSM8K signals 大概率在 S1 完成后（~3 min）进入 S2 时 OOM crash。

**建议**：
- 如果 Llama d100 是高优先级，应 kill GSM8K signals (PID 806081) 并在 cuda:1（空闲）上重跑
- 如果 signals 是 P0，等 d100 训练完再跑 GSM8K

**预计完成时间**（如无 OOM）：
- S1 embedding: ~2-5 min（当前进行中）
- S2 Min-K%++: ~15-20 min per benchmark
- S4 self-critique: ~10-15 min per benchmark  
- **总计**: ~45-60 min（假设无 OOM）

---
