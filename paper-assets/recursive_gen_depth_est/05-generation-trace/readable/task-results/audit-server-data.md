# audit server data

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_server-data_20260525T194518_result.json`
- **Structured JSON:** [`d1d096603d554fa8ac48.json`](../../sessions/d1/d1d096603d554fa8ac48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计报告已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/audit_server_data.md`。

提取覆盖：
- 9-cell 主结果 (4-class acc + d1-d3 balanced acc + 95% CI + per-class recall)
- Pairwise AUC decay 全部 9 cells (含 std)
- EDD@T=0.70 分布
- Cross-model rank correlation (Spearman ρ)
- Cross-model transfer (LOO balanced acc)
- 14B scale (cross-ref + self-ref, Qwen-7B/14B)
- Detection baselines (Binoculars + Fast-DetectGPT + Combined)
- PPL threshold vs RF 对比
- Feature importance (universal ranking + conditional PI)
- Accumulation mix25/50 (含 verified 500-tree 版本)
- Wild data calibration FPR (C4/FineWeb/RedPajama) + threshold sweep
- FPR-coverage tradeoff
- LoRA 完整训练配置 (r=16, alpha=32, lr=2e-4, bs=8, epoch=3, 939 steps)

---
