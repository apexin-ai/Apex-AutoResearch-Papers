# data irt extract v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_irt_extract_v2_20260516T202827_result.json`
- **Structured JSON:** [`75aa7660c9a7ea256464.json`](../../sessions/75/75aa7660c9a7ea256464.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。文件已保存到：
`/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/irt_calibration_data.json`

内容概览（8.2KB, 213行）：
- **主要结果**: 2PL+γ pooled IRT (N=16 MMLU/ARC, N=24 GSM8K) — gamma, CI, PPP, MAE
- **历史对照**: N=13/21 早期结果
- **MMLU 分域 gamma**: 7个 domain（Simpson's Paradox：STEM 正向，人文/社科/医学负向）
- **Scale-stratified**: 0.5B/1.5B/3B 分层结果
- **模型对比**: 2PL vs 4PL ablation
- **Exposure scores**: RRF 元数据

**限制**: 由于 SSH 不可直接访问，per-model theta 和 item_params 原始数组未提取（需要直接读服务器 raw JSON）。如需这些细粒度数据，需要通过有 SSH 权限的 worker 再次提取。

---
