# ssh check all running progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_all_running_progress_20260514T000901_result.json`
- **Structured JSON:** [`402eb1ce810c29dc1f2c.json`](../../sessions/40/402eb1ce810c29dc1f2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

| GPU | exp_id | PID | 进度 | ETA | 状态/备注 |
|-----|--------|-----|------|-----|-----------|
| 0 | exp_001_sft_d100_05B | 235243 ✅ | **1719/4159 (41%)** epoch 0.38 | ~40 min | ~1 it/s, checkpoint 空 |
| 1 | exp_001_eval_05B_d000_s42 | 229370 ✅ | GSM8K **764/1319 (58%)**, benchmark 2/4 | ~2.5h+ | MMLU ✓, GSM8K 进行中, 还剩 ARC+HumanEval |
| 2 | exp_001_eval_05B_d000_s123 | 229516 ✅ | GSM8K **733/1319 (56%)**, benchmark 2/4 | ~2.5h+ | MMLU ✓, GSM8K 进行中, 还剩 ARC+HumanEval |
| 3 | exp_001_sft_0pct_3B_s123 | 216935 ✅ | **3054/3125 (98%)** epoch 0.89 | **~6 min** | 即将完成! |
| 4 | exp_001_eval_15B_d000_s42 | 221376 ✅ | benchmark **2/4 完成**, 正在加载 ARC | ~1.5h+ | MMLU ✓, GSM8K ✓, 正 HF 超时→用缓存加载 ARC |
| 5 | exp_001_sft_d005_05B_v3 | 239729 ✅ | **642/3177 (20%)** epoch 0.20 | ~45 min | ~1 it/s, checkpoint 空 |

### 关键发现

1. **3B s123 baseline SFT (GPU 3) 约 6 分钟内完成** — 完成后 GPU 3 立即可用，可启动 3B eval 或 Phase 3 3B 训练。

2. **1.5B s42 eval (GPU 4) 进度最快** — 已完成 MMLU + GSM8K，正在加载 ARC-Challenge（HF 超时但已 fallback 到缓存）。GPU 利用率暂 0% 因为在加载数据集。

3. **0.5B 两个 eval (GPU 1, 2) 还需较长时间** — GSM8K 才做到 ~57%，之后还有 ARC + HumanEval。预计 2.5h+。

4. **d100_05B 和 d005_05B_v3 两个 Phase 3 SFT** — 分别在 41% 和 20%，约 40-45 分钟完成。Checkpoint 目录均为空（应该是训练结束才保存）。

5. **所有 eval_results 子目录均为空** — 尚无任何 benchmark 结果 JSON 写出。

6. **HuggingFace 连接问题** — 所有 eval 都遇到 HF Hub 超时（未开 `network_turbo`），但均成功 fallback 到本地缓存。

### 建议优先级

- **GPU 3** 约 6 min 释放 → 优先安排 3B baseline eval 或 Phase 3 3B contaminated SFT
- **GPU 0, 5** 约 40-45 min 释放 → d100/d005 SFT 完成后可接 eval
- **GPU 1, 2, 4** 的 eval 还需较长时间，暂无法释放

---
