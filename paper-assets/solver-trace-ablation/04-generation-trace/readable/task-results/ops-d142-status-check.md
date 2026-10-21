# ops d142 status check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d142-status-check_20260519T070507_result.json`
- **Structured JSON:** [`f9c545c1c66da5b8adf1.json`](../../sessions/f9/f9c545c1c66da5b8adf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D142 Gated ISR 实验状态报告

### 1. GPU 状态
**空闲**。cuda:0 无进程，0MiB 占用。

### 2. Pipeline 状态
**全部完成**，failures: 0。最后一个 seed (s54) 于 `2026-05-19 06:39:20 UTC` 完成。Pipeline 已自动清理 checkpoint 权重，磁盘 41G/250G (17%)。

### 3. 各 seed 详细 metrics

| Metric | s52 | s53 | s54 |
|--------|-----|-----|-----|
| **PR** (Prove Rate) | **100%** (100/100) | **96%** (96/100) | **91%** (91/100) |
| **ISR*** (proved_only_mean) | **1.0000** | **0.6514** | **0.2731** |
| **TS%** (H7 tautology) | 0.0% | 0.0% | 0.0% |
| **CE%** (H1 concl-in-prem) | 0.0% | 3.1% (3/96) | 3.3% (3/91) |
| **PG%** (H8 conj-collapse) | **100.0%** (100/100) | **89.6%** (86/96) | **0.0%** (0/91) |
| **Genuine%** | **0.0%** (0/100) | **7.3%** (7/96) | **96.7%** (88/91) |
| **CI%** (content-indep) | 100.0% (100/100) | 0.0% | 35.2% (32/91) |
| **ISR=1.0 count** | 100 (100%) | 5 (5.2%) | 0 (0%) |
| Single premise | 0 | 0 | 0 |

### 4. 关键发现

**s52 完全崩溃**：100% PG (conjunction collapse)，ISR=1.0 且 genuine=0%。模型学会了一个退化策略——结论 = 所有前提的合取（`∀x(P(x)→Q(x)) ∧ ∃x P(x)`），content-independent predicates 100%。所有样本使用相同模板化公式，完全忽略原始问题内容。

**s53 大部分崩溃**：89.6% PG，仅 7.3% genuine。比 s52 稍好但仍以 hacking 为主。

**s54 表现正常**：0% PG，96.7% genuine，ISR*=0.27。这个 seed 没有学到 conjunction collapse 策略。

**跨 seed 方差极大**：同一 gated ISR (b=0.1) 配置，三个 seed 的 genuine% 分别为 0%、7.3%、96.7%。Gated ISR reward 未能稳定抑制 PG collapse——2/3 seeds 仍崩溃。

注：classify.json 中无 S-NH% 字段，如需该指标需另行计算。

---
