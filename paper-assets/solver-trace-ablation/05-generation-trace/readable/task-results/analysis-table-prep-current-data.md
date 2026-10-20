# analysis table prep current data

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table-prep-current-data_20260514T141632_result.json`
- **Structured JSON:** [`4102ad5dea6488c9ad1d.json`](../../sessions/41/4102ad5dea6488c9ad1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 artifact 已注册（`art_20260514_f21549`, `art_20260514_e8d24a`）。

## 产出摘要

**Table 1** (`table1_draft.md`) 包含 7 个子表：
- **1a**: 主条件汇总（8 行，含 3-seed mean±std）
- **1b–1d**: FOL exec-only / ISR β=0.1 / Random β=0.1 逐 seed 明细
- **1e**: Prolog 条件
- **1f**: ISR 崩塌轨迹（0→100→500→1000 步）
- **1g**: β 剂量-效应对照

**Table 2** (`table2_draft.md`) 包含 5 个子表：
- **2a**: ISR vs Random s42 strict 分类对比（D044 可复现）
- **2b**: ISR β=0.1 三 seed H7 分布（66.4% 3-seed mean）
- **2c**: plan012 聚合分类
- **2d**: 跨 logic H7 对比（FOL vs Prolog）
- **2e**: 6 种 hacking 模式全分类

## 关键标注

- ISR β=0.1 三 seed mean ISR (0.68±0.23) **不可直接报告**——2/3 seeds 被 H7 conclusion duplication 膨胀
- 5 个 pending cells：plan018 s43/s44、plan006 exec s43/s44、plan006-sta s43/s44
- plan001-s43 ISR 需用 eval_sta.py 重新评估（当前值来自 training log，不符合 C004）
- s44 exec-only ISR=0.582 是机械性 fake-high（94% 两组件 tautological proof）

---
