# ops gsm8k ds check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gsm8k_ds_check_20260515T161651_result.json`
- **Structured JSON:** [`6d1b3735c5256bede2cb.json`](../../sessions/6d/6d1b3735c5256bede2cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### DS (DeepSeek) — gsm8k_profiling_ds

| 条件 | GPU | 进度 | 状态 |
|------|-----|------|------|
| ds_importance | cuda:0 (76%, 21GB) | **50/50** | **完成** — Verdict: PASS |
| ds_random | cuda:1 (90%, 45GB) | **41/50** | 运行中 |

**ds_importance 输出文件：**
- `profiling_results.json` — 2.1MB, JSON 格式完整
- `generations.json` — 179KB, 50 条生成结果

**ds_importance 关键指标：**
- high_sparsity: 19344 tokens, 352 segments
- mid_sparsity: 21307 tokens, 267 segments  
- low_sparsity: 25973 tokens, 359 segments
- CI overlap test: low vs mid non-overlapping at threshold 0.3 → **PASS**

**ds_random** 还在跑，约剩 ~18 分钟（~2 min/problem × 9 remaining）。

---

### QW (Qwen) — gsm8k_profiling_qw

| 条件 | GPU | 进度 | 状态 |
|------|-----|------|------|
| qw_importance | cuda:2 (97%, 66GB) | **30/50** | 运行中 |
| qw_random | cuda:3 (94%, 52GB) | **30/50** | 运行中 |

QW 两个条件每问题约 3 分钟，预估还需 **~60 分钟**。

---

### 结论

两个实验都**未完成**，不更新 registry、不删除 cron。所有 4 张 GPU 仍在活跃工作，无 error/OOM。

建议 **30-40 分钟后再次检查**：届时 DS random 应已完成（可更新 DS registry），QW 可能也接近完成。

---
