# paper writing introduction

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_introduction_20260514T215352_result.json`
- **Structured JSON:** [`7a8bb35b835211abf5de.json`](../../sessions/7a/7a8bb35b835211abf5de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Introduction 已写入 `artifacts/_project/paper/introduction.tex` 并注册。

结构概览：
1. **Hook** — SlopCodeBench 记录的 silent stagnation 问题，77% 结构退化，75.5% 冗余增长
2. **Gap** — 三类现有方法的局限：repetition detectors（漏语义停滞）、PRM（step-level 丢时序）、self-reflection（循环依赖 stuck model）
3. **Setup** — 弱监督框架，SWE-Agent 54K + OpenHands 150K windows，三个 LF + majority vote
4. **Core finding** — 30 结构特征 0.9951 in-domain / 0.967 cross-agent，+33.3pp vs LLM judge，encoder-agnostic（3 encoders >0.90），<5ms/window
5. **Temporal dynamics** — cmd_rep leading -1.87 步（SWE-Agent）→ lagging +3.32 步（OH），去掉后 FT F1 +17.6pp
6. **TLM negative** — TWV/HMM/lag-HMM 均未超 MV，TWV 下游 -2.57pp
7. **Contributions** — C1 structural signal, C2 LF temporal dynamics + circular evaluation, C3 TLM negative finding

待处理：1 个红色引用标记（ICLR 2025 Workshop monitoring paper），需确认后替换为 `\citep{}`；新增引用（orlanski2026slopcodebench, xi2025agentprm, shinn2023reflexion, yao2023tot, zhou2024lats）需加入 bib 文件。

---
