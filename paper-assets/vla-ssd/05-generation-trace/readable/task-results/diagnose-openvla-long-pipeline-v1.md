# diagnose openvla long pipeline v1

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_openvla_long_pipeline_v1_20260521T160330_result.json`
- **Structured JSON:** [`cdeb97b1174a64486ca1.json`](../../sessions/cd/cdeb97b1174a64486ca1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 修复总结

### 修复内容

**文件**：`/root/autodl-tmp/vla-ssd/scripts/libero_long_full_pipeline.py`（备份在 `.bak`）

**改动 1 — UNNORM key 修复（根因）**：
- `UNNORM = "libero_10"` → 拆为两个常量：
  - `UNNORM_TRAINED = "libero_10_no_noops"` — trained 模型（OFT微调）的 `dataset_statistics.json` 中的实际 key
  - `UNNORM_UNTRAINED = "bridge_orig"` — base 模型 `config.json` 中的 OXE key
- `main()` 循环中按 condition 切换 `global UNNORM`

**改动 2 — OFT 模型 norm_stats 合并**：
- 加载模型后检测并合并 `dataset_statistics.json` 到 `model.norm_stats`，因为 OFT 微调模型的 `config.json` 未更新 norm_stats（仍是 base 模型的 OXE keys）

**改动 3 — `--only-counterfactual` 增量重跑**：
- 新增 CLI flag，跳过 Phase 1-5 直接执行 Phase 6

### 根因分析

Long pipeline 用的是 **OFT (Orthogonal Fine-Tuning)** 微调的模型 (`openvla-7b-oft-finetuned-libero-10`)。与标准微调不同，OFT 方式不更新 `config.json` 中的 `norm_stats`（仍保留 base 模型的 OXE dataset keys），而是将微调数据集的统计信息单独存在 `dataset_statistics.json` 中（key 为 `libero_10_no_noops`）。Object pipeline 用的是标准微调模型，其 `config.json` 直接包含 `libero_object` key，所以不受此影响。

### 增量重跑结论

**可以增量重跑**。Phase 1-5 trained 的 4 个输出文件完整存在。Phase 6 独立于 Phase 1-5（直接调用 `generate_action`，不依赖提取的特征）。使用 `--only-counterfactual --conditions trained` 只跑 trained Phase 6；untrained 需全量跑（Phase 1-6 全部未执行）。

---
