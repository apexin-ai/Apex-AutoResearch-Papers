# code arxiv multi source

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_arxiv_multi_source_20260524T084745_result.json`
- **Structured JSON:** [`e2defffc51cca0d28bf6.json`](../../sessions/e2/e2defffc51cca0d28bf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 全部通过。汇总：

---

## 现状

| Generator | arXiv 数据 | Cross-scored? | 已有 K* |
|-----------|-----------|--------------|---------|
| Qwen2.5-1.5B | ✅ 2200×6 depths | ✅ 自评=cross-score | K*=3 (exp-024) |
| Pythia-1.4B | ✅ 2200×6 depths | ✅ 有缓存 | K*=3 (exp-025) |
| OLMo-1B | ✅ 2200×6 depths | ❌ 仅自评(K*=1) | **需 cross-score** |

## 脚本

**路径**: `/root/autodl-tmp/gen-depth-contamination/scripts/run_arxiv_multi_source_1b5.py`

功能：
1. 加载 Qwen2.5-1.5B scorer
2. 复用 Pythia cached cross-scored features（无需重新计算）
3. Cross-score OLMo 2200×6=13,200 texts
4. 每个模型单独跑 pairwise AUC + 10K bootstrap CI
5. 三模型 pooled multi-source detection（with/without gen label）
6. 输出到 `results/exp_arxiv_multi_source/`

## GPU 需求

- 4x RTX PRO 6000 (97GB each)，全空闲
- Scorer (Qwen2.5-1.5B base) 需 ~3GB VRAM，1 卡即可
- 无需多卡

## 预估时间

| 阶段 | 时间 |
|------|------|
| OLMo cross-scoring (13.2K texts) | ~10-15 min |
| Per-model pairwise + bootstrap ×3 | ~15 min |
| Pooled multi-source ×2 conditions | ~5 min |
| **总计** | **~30-40 min** |

## Seed data 确认

三个 generator 共享同一批 arXiv seed data（depth_0 = exp-024 的 2200 篇 abstracts）。

---

需要启动运行吗？

---
