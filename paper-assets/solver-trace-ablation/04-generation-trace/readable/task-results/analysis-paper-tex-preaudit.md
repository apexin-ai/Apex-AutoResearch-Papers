# analysis paper tex preaudit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper-tex-preaudit_20260515T145531_result.json`
- **Structured JSON:** [`1b0de3606d46a4947297.json`](../../sessions/1b/1b0de3606d46a4947297.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。58 项定量 claim 检查结果：

## 3 项 RED LINE 违规

| ID | 问题 | 论文值 | 应为 |
|---|---|---|---|
| **RL-01** | Taxonomy 说 7 种 hacking mode | 7 modes | **8 modes**（缺 H8 conjunction collapse，registry 显示 6.45%-43.2%） |
| **RL-02** | H7 比例未应用 D085 修正 | 64.5% (149/231) | **69.7%** (161/231)，s44 的 12 个 H7b obfuscated tautology 未计入 |
| **RL-03** | N-H 率未应用 D084+D085 | ISR β=0.1 pooled N-H=17% | **6.9%** (16/231)，未扣 H8、未重分类 H7b |

## 6 项其他问题

- **ISS-01 (HIGH)**: Random β=0.1 三 seed 聚合用了 DEPRECATED 数据（s43/s44 正在重训）
- **ISS-02 (HIGH)**: D085 H7b 三层 gaming 分析（最强 meta-Goodhart 证据）未写入论文
- **ISS-03 (MEDIUM)**: Bootstrap CI 统计检验缺失
- **ISS-04 (MEDIUM)**: s42 "31% non-hacking" 既不等于 32.1%（pre-D084）也不等于 17.3%（post-D084）
- **ISS-05 (MEDIUM)**: Exec-only N-H=13% 包含 H8 样本，应为 7.5%
- **ISS-06 (LOW)**: SFT baseline 仅报单 seed，3-seed 数据已有

## 27 项验证通过

ISR 崩塌轨迹、PR 轨迹、214× 崩塌、premise-count-matched 1.06×、β=0.3 全部 seed 数据、Prolog 全部数据、无 2.4x、无 43.2%、无 "significantly" — 均正确。

已注册 artifact `art_20260515_515c5d`。

---
