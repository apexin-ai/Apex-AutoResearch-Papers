# research 3B signal coverage audit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_3B_signal_coverage_audit_20260516T101702_result.json`
- **Structured JSON:** [`9eee97d73b89ea8e261c.json`](../../sessions/9e/9eee97d73b89ea8e261c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整审计报告。

---

## 1. 3B s42 覆盖矩阵

### Eval (exp-001): ✅ 16/16 COMPLETE

| Dosage | aligned | para_aligned |
|--------|---------|--------------|
| d000 s42 | ✅ | ✅ |
| d005 s42 | ✅ | ✅ |
| d025 s42 | ✅ | ✅ |
| d100 s42 | ✅ | ✅ |
| d000 s123 | ✅ | ✅ |
| d005 s123 | ✅ | ✅ |
| d025 s123 | ✅ | ✅ |
| d100 s123 | ✅ | ✅ |

+1 RUNNING: 3B-Instruct baseline eval (cuda:3)

### Signals (exp-002): 6/8 complete

| Dosage | s42 | s123 |
|--------|-----|------|
| **d000** | ✅ 9/9 files (7.8MB s1 mmlu confirmed) | ❌ **MISSING** — no directory on disk |
| **d005** | ✅ complete + merged | ✅ complete + merged |
| **d025** | ✅ 9/9 (v3 alpha=32) | ✅ 9/9 (individual files + merged gsm8k/arc) |
| **d100** | 🔄 **RUNNING** cuda:1 (2/9: s1+s2 mmlu only) | ✅ complete + merged |

---

## 2. GPU 实时状态

| GPU | 显存 | 状态 |
|-----|------|------|
| cuda:0 | 4.1/24.6 GB | busy |
| cuda:1 | 6.6/24.6 GB | busy — d100_s42 signals |
| cuda:2 | 4.2/24.6 GB | busy |
| cuda:3 | 9.1/24.6 GB | busy — Instruct eval |
| cuda:4 | **0/24.6 GB** | **FREE** |
| cuda:5 | 1.9/24.6 GB | busy |

---

## 3. RRF 聚合 (exp-003) 前置条件

**RRF 输入要求** (`rrf_aggregation.py --generate-exposure`):
- 扫描 `/root/autodl-tmp/exp002/signals/` 下所有 `Qwen2.5-*` 目录
- 每个目录需要 `signal_{s1/s2/s4}_{mmlu/gsm8k/arc_challenge}.json`（9 files）或 merged
- 自动跳过 ALPHA16_BLOCKLIST
- 可以处理部分信号（graceful degradation）

**0.5B + 1.5B RRF: ✅ 已完成**
- 产出: `/root/autodl-tmp/exp003/rrf_05B_15B/exposure_scores.json`
- 覆盖: 0.5B × 4 dosages × 2 seeds + 1.5B × 4 dosages × 2 seeds = 16 respondents

**3B RRF: 阻塞中**
| 阻塞项 | 状态 | 预估剩余时间 |
|---------|------|------------|
| d100_s42 signals | RUNNING cuda:1, 2/9 done | ~3-5h |
| d000_s123 signals | **未开始** | ~2-3h (可立即在 cuda:4 启动) |

**最小可行 RRF**: 可先用 6/8 跑 partial RRF（缺 d100_s42 和 d000_s123），但会损失 2 个 respondents（N=35→33 含 0.5B/1.5B，或 N=21→19 仅 1.5B+3B）。

---

## 4. GPU 释放后任务优先级队列

按 C007 约束 + paper critical path:

| 优先级 | 任务 | GPU 需求 | 预估耗时 | 阻塞什么 |
|--------|------|----------|----------|----------|
| **P0** ⚡ | 3B d000_s123 signals (全部 s1/s2/s4 × 3 benchmarks) | 1 GPU (~6GB) | 2-3h | 3B RRF 完整性 |
| P1 | 等 d100_s42 完成 (cuda:1) | 已占用 | 3-5h | 3B RRF 完整性 |
| P2 | 3B RRF 聚合 | CPU only | 5-10min | IRT fitting |
| P3 | pooled IRT fitting (per-benchmark γ_k, Stan NUTS) | CPU only | 1-2h | paper results |

**cuda:4 现在空闲 → 应立即提交 3B d000_s123 signals**

---

## 5. Paper Timeline 影响评估

```
May 16 (今天, T-9):
  - 立即提交 d000_s123 signals → cuda:4 [2-3h]
  - d100_s42 继续在 cuda:1 [3-5h]
  
May 16 晚 / May 17 (T-8):
  - 两个 signals 任务完成 → 3B 矩阵 8/8 ✅
  - RRF 聚合 (CPU, 10min) → exposure_scores for 3B
  
May 17 (T-8):
  - pooled IRT fitting: N=35 (0.5B+1.5B+3B, 全 dosage × 双 seed)
  - 7 baselines 对比 + ablation
  
May 18-19 (T-7~T-6):
  - Results table 定稿, paper writing
  
May 20-24 (T-5~T-1):
  - Review 迭代 + 提交
```

**结论: 3B pipeline 可在 T-8 (May 17) 前全部完成，不阻塞 EMNLP deadline。**

唯一风险：d100_s42 如果 cuda:1 有 OOM 或进程中断需要重启，可能滑到 May 17 下午。建议几小时后检查 cuda:1 进度。

---

## 6. 立即行动项

**cuda:4 空闲 → 提交 3B d000_s123 signals**

需要确认：
1. d000_s123 的 SFT checkpoint 路径（应为 `Qwen2.5-3B_d000_s123` 或类似）
2. `cat adapter_config.json | grep lora_alpha` 验证 alpha=32（C006）
3. CUDA_VISIBLE_DEVICES=4 显式设置（C004）

是否要我现在查找 checkpoint 路径并准备提交命令？

---
