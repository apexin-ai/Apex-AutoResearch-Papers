# analysis a3 complementarity

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a3_complementarity_20260522T081553_result.json`
- **Structured JSON:** [`f2d315c68ff6776b452a.json`](../../sessions/f2/f2d315c68ff6776b452a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

A3 完成。所有输出在 `westb-48145:/root/entrainment_gated_ft/results/a3_complementarity/`。

## 核心发现

### 四类分解 (所有 benchmark 通用模式)

| 类别 | 含义 | 典型占比 |
|------|------|---------|
| **UC** (3/3 correct) | 共识正确 | 35-66% |
| **MC** (2/3 correct) | MV 可利用 | 7-16% |
| **mC** (1/3 correct) | 浪费的互补性 | 5-15% |
| **UW** (0/3 correct) | 共识错误 | 18-35% |

### 关键指标

- **Complementarity Index (CI)**: 0.38–0.48，随 attention ratio 增加略有上升（LAMBADA 从 0.40→0.48），说明 attention 增加并未消除架构互补性，反而稍微增强
- **MV Efficiency: 几乎全部为负值**（-0.20 到 +0.13），说明 MV 准确率通常低于最佳单一架构。这是最重要的发现——3 个架构的多数投票反而比"挑最好的一个"还差
- **Wasted Complementarity**: LAMBADA 最高（~14%），PIQA 最低（~6%）。attention ratio 对这个指标影响较小

### 趋势

- UC/UW 在不同 attention ratio 下**基本稳定**，共识区域不随 attention 显著变化
- MV Efficiency 负值意味着：当一个架构一致性更强时（如 ARC-Easy 上 HGRN2 持续领先），两个较弱架构会"投票淹没"最好的那个
- Oracle-MV gap（即 mC 样本）= 14-15% on LAMBADA，代表"存在正确信息但 MV 无法提取"的上界

---
