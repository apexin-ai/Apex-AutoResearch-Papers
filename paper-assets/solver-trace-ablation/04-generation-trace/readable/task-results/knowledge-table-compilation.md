# knowledge table compilation

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_table-compilation_20260514T172319_result.json`
- **Structured JSON:** [`541e2f760e7a1a55ec69.json`](../../sessions/54/541e2f760e7a1a55ec69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译完成。artifact 已注册 (`art_20260514_94a4d3`)。

文件包含 6 个 panel：
- **Panel A**: FOL 主结果（SFT / exec-only / exec+ISR / exec+random，含 β=0.1 和 β=0.3）
- **Panel B**: FOL β=0.3 ISR vs Random 对照
- **Panel C**: Hacking 模式分类（H7/H1/H3/Genuine，s42 D044 strict）
- **Panel D**: 跨逻辑对比（Prolog vs FOL exec-only 3-seed）
- **Panel E**: ISR 崩塌轨迹（0→100→500→1000 步）
- **Panel F**: Premise-count-matched 分析（D051 定论，1.06×）

主要数据缺口：
1. plan006-prolog-sta s43/s44 仍在 RUNNING — Claim 3 待闭环
2. plan001-exec-only-s43 使用 sampling eval（非 eval_sta.py），H7/H1 缺失
3. plan002-b03 和 plan017（β=0.3 条件）无 H7/H1 分类
4. plan016（1000 步）无 H7/H1 分类

---
