# audit deploy cqa1 32758 fill gaps

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit-deploy_cqa1-32758-fill-gaps_20260523T112852_result.json`
- **Structured JSON:** [`073c21bc13c45f142e92.json`](../../sessions/07/073c21bc13c45f142e92.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:0 已在加载模型 (1263 MiB)，cuda:5 正在初始化。

## 审计总结

**cqa1-32758 GPU 状态 (6/6 占用)**：

| GPU | 实验 | 状态 |
|-----|------|------|
| cuda:0 | eval-supp-obj-reconvla-s44 (PID 180864) | **新部署** |
| cuda:1 | eval-supp-k2mean-spatial-s44 (PID 174449) | 运行中 |
| cuda:2 | eval-supp-k2mean-object-s43 (PID 16441) | 运行中 |
| cuda:3 | eval-supp-k2mean-object-s44 (PID 177864) | 运行中 |
| cuda:4 | eval-supp-long-k2mean-s42 (PID 172251) | 运行中 |
| cuda:5 | eval-supp-spatial-vla-only-s43 (PID 181168) | **新部署** |

**已完成实验结果提取**：
- **goal-reconvla-s43**: 81.0% (s42=81.0%, 两 seed 一致)
- **k2mean-spatial-s43**: 78.0% (已在 registry 中)

---
