# analysis paper n5 cleanup

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper_n5_cleanup_20260521T195631_result.json`
- **Structured JSON:** [`3a6a4b2669203eb08aef.json`](../../sessions/3a/3a6a4b2669203eb08aef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完毕。

---

## 报告

### A. N=5 steering 残留

**有残留，已修复。** 摘要/引言/结论/讨论4个文件引用了 N=5 特定数值（β=0 GAR 0.029, β=5 GAR 0.697），已全部替换为 N=50 数据（0.064, 0.727）：

| 文件 | 修改内容 |
|---|---|
| `abstract.tex:2` | 0.029→0.064, 0.697→0.727 |
| `introduction.tex:16` | 0.029→0.064, 0.697→0.727 |
| `introduction.tex:18` | 0.029→0.064, 0.697→0.727 |
| `conclusion.tex:3` | 0.697→0.727 |
| `discussion.tex:3` | 0.029→0.064, 0.697→0.727 |

**保留未动的 N=5 引用**：`experiments.tex:49-51`（steering 实验小节）中 N=5 pilot 的详细描述和 N=50 段落中对 N=5 baseline 的回溯说明。这些是实验叙事的一部分（对应 Figure 5 panel a），不属于"残留引用"。

### B. Gap ratio 一致性

**有不一致，已修复。** 所有 scheduled sampling 上下文中的 "30×" 统一为 registry 精确值 "32×"；跨模型范围 "12.5--30×" 修正为 "12.5--33×"（与论文其他处 "20--33×" 一致）：

| 文件 | 修改 |
|---|---|
| `introduction.tex:16,18` | 30×→32×（2处，replace_all） |
| `discussion.tex:5` | 30×→32× |
| `conclusion.tex:3` | 30×→32× |
| `analysis.tex:49` | 12.5--30×→12.5--33× |

### C. plan_018 清理

**已完成。** 删除了第二条 plan_018（claim C3/MF4, deps plan_002, 无 registry_id），保留第一条（registry_id: phase2_tg_s42_v9_pcgrad）并将 status 从 `planned` 更新为 `done`。

---
