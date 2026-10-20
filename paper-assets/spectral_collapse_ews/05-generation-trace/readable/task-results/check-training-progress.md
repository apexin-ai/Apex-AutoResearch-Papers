# check training progress

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training_progress_20260516T153916_result.json`
- **Structured JSON:** [`4c82cc71cf2a479a6d36.json`](../../sessions/4c/4c82cc71cf2a479a6d36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

report.md 不支持手动写入（auto-generated）。以下是状态汇总：

---

## 实验状态 — 2026-05-16 23:45 CST

| exp_id | 模型 | 状态 | 进度 | PID |
|--------|------|------|------|-----|
| exp_001 | Pythia 410M (cuda:0) | **RUNNING** (7h31m) | Gen 3/10 | 7396 |
| exp_002 | Pythia 1B (cuda:1) | **CRASHED** — disk full | Gen 0 完成后崩溃 | 25232 (zombie) |

### Spectral Metrics 趋势 (exp_001)

| Gen | eff_rank | log_det | σ₁ (top SV) | ppl | distinct4 | train_loss | hellaswag_acc_norm |
|-----|----------|---------|-------------|-----|-----------|------------|--------------------|
| 0 | 417.55 | 2366.68 | 1942.8 | 9.55 | 0.7414 | — | 0.4130 |
| 1 | 491.77 | 2464.76 | 804.0 | 11.38 | 0.6256 | 1.623 | 0.3897 |
| 2 | 496.44 | 2469.93 | 712.0 | 13.58 | 0.5153 | 1.268 | 0.3764 |

### 关键发现

- **eff_rank 非单调下降，反而上升** (417→492→496)。原假设需修正。
- 原因：σ₁ 急剧下降 (1943→804→712)，谱变平 → rank 反而升高。
- **model collapse 确认**：ppl ↑ (9.55→13.58)，distinct-4 ↓ (0.74→0.52)，hellaswag ↓ (0.413→0.376)。
- log_det 从 Gen 0→1 跳升 (+98)，Gen 1→2 几乎持平 (+5)，趋于饱和。

### exp_002 崩溃详情

- Gen 0 评估完成：eff_rank=516.14, ppl=8.07, distinct4=0.7510
- 保存 checkpoint 时报 `SafetensorError: No space left on device`
- 1B checkpoint ~4GB，根分区 30GB 已满

### 磁盘空间

| 分区 | 容量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| / (root) | 30G | 25G | 5.1G | 84% ⚠️ |
| /root/autodl-tmp/ | 250G | 95G | 156G | 38% |

### 预估完成时间

- **exp_001**: 平均每代 ~2.5h，剩余 8 代 → **预计 2026-05-17 ~19:00 CST**
- **exp_002**: 需修复后重启。1B 每代 ~4-5h，10 代需 ~45-50h

### 下一步

1. **紧急**：修复 exp_002 — checkpoint 路径改到 `/root/autodl-tmp/spectral_collapse_ews/checkpoints/`，清理根分区，重启
2. exp_001 的 checkpoints 也建议迁到数据盘，防止根分区爆满
3. 原假设（eff_rank 单调下降）不成立 → EWS 指标需重新定义，σ₁ 衰减率或奇异值方差可能是更好的信号

---
