# code phase2 qwen ioi acdc k3

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase2-qwen-ioi-acdc-k3_20260513T081516_result.json`
- **Structured JSON:** [`ed82d3c35a41e09fd46f.json`](../../sessions/ed/ed82d3c35a41e09fd46f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果文件确认存在。Registry 已更新。

## 实验总结

**phase2_qwen05b_ioi_acdc_k3** — 完成，D025 未通过。

| 指标 | 值 |
|------|-----|
| 运行时间 | 46.5s (EAP-IG 3s, EP 28s, ACDC 11s) |
| Total edges | 179,388 |
| Top-0.3% per method | 538 edges |
| CSS 3/3 (core) | **0** |
| CSS ≥2/3 | 66 |
| Max Jaccard | 0.0426 |
| D025 条件①② | PASS |
| D025 条件③④ | **FAIL** |

**根因分析：**

EP 和 ACDC 都用组件级评分 + 源端展开到边——同一源组件的所有边得分相同。Top-0.3% 只选 538/179388 条边，实际效果是各方法只选了各自 top 2-3 个组件的全部出边，形成互不相交的"块状"电路：

- ACDC top 组件：m0 (12.52), input (6.45), a8.h7 (3.16)
- EP top 组件：不同于 ACDC 的组件集合
- EAP-IG：边级评分，选的边更分散

结果：Jaccard 全 < 0.05，3/3 重叠为零。

**可能的修复方向：**
1. 改用 **per-method binarization**（如 YAML 配置中的 topn-200 / threshold-0.5 / top-0.3%）
2. **增大 top_percent** 到 1-2%，给方法间更多重叠空间
3. 实现 **边级 ACDC 评分**（不仅依赖源组件，而是 src×dst 或真正的逐边 activation patching）

---
