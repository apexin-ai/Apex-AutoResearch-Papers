# paper fix review issues

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_fix-review-issues_20260515T220149_result.json`
- **Structured JSON:** [`61814fee4bf484138bf6.json`](../../sessions/61/61814fee4bf484138bf6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Here's the summary:

---

### 修复完成

| Issue | 严重度 | 文件 | 改动 |
|-------|--------|------|------|
| **R2-M2** | Critical | `experiments.tex:116` | `(D088 protocol)` → 删除 |
| **R2-M2** | Critical | `experiments.tex:146` | 删除 `% exp_ids: model-size-scaling-cls8b ...` 注释 |
| **R2-M2** | Critical | `experiments.tex:179` | 删除 `% exp_ids: cwm-baseline, cwm-rank32-ablation-v2 ...` 注释 |
| **R2-W4** | Warning | `main.tex:29` | 标题 `Scales` → `Succeeds` |
| **R2-W6** | Warning | `references.bib` | 添加 `ni2023lever` (LEVER, ICML 2023) 和 `chen2023codet` (CodeT, ICLR 2023) |
| **R2-W6** | Warning | `related_work.tex` | 已有 "Learned Code Verifiers" 段落引用 LEVER/CodeT（无需改动） |
| **R1-M4** | Info | `method.tex:24` | §2.2 末尾补充 unparseable predictions 处理策略：默认到 majority-class label (Pass) |

### R1-N1 状态（无法完全修复）

函数级 scaling table (tab:scaling) 已以 8B-8B 对比为主（Gap 2.43pp 加粗）。**Repo-level table 无法切换为 8B-8B primary**——CWM 8B 数据尚未到位（R1-N2 显示训练 57%，ETA May 16 05:30）。CWM 8B eval 完成后需要：
1. 填入 `tab:repo_level` 中 CWM 8B 行
2. 更新 caption 将 8B-8B 设为 primary comparison
3. 更新 abstract/intro 中 repo-level 数字（当前引用 4B-4B 25.59pp）

### Info #6（其他内部引用扫描）

全部 tex 文件已扫描，仅发现上述 3 处内部引用（均已清除），无其他残留。

---
