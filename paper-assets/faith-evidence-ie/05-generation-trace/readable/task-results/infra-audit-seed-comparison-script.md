# infra audit seed comparison script

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_audit_seed_comparison_script_20260516T032044_result.json`
- **Structured JSON:** [`b867a92a4ec962019947.json`](../../sessions/b8/b867a92a4ec962019947.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

**原脚本：不兼容。** 使用硬编码目录名映射，缺少 reeval 目录，只读 metrics.json。

### 修改内容

1. **METHODS 目录映射**——添加 reeval 优先级链（`_reeval_r2` > `_reeval` > 原始）：
   - CED s42: `["rsft_ced_s42_reeval", "rsft_r2b_maxtok1536"]`
   - CED s44: `["rsft_ced_s44_reeval", "rsft_s44"]`
   - flat-NLI s42: `["rsft_flat_nli_s42_reeval", "rsft_flat_nli"]`
   - flat-NLI s43: `["rsft_flat_nli_s43_reeval_r2", "rsft_flat_nli_s43_reeval", "rsft_flat_nli_s43"]`

2. **load_metrics** 优先读 `metrics_v2.json`，fallback 到 `metrics.json`

3. **新增 `--dry-run`** 和 **sources 追踪**（report 显示每个 seed 的实际数据来源）

### Dry-run 输出

```
=== CED_RSFT ===
  s42: LOADED from rsft_r2b_maxtok1536/metrics_v2.json  (f1=0.4504)  ← 旧协议(bs=8,tok=1536), 等 rsft_ced_s42_reeval
  s43: LOADED from rsft_s43/metrics_v2.json              (f1=0.4683)  ← 旧协议(bs=8,seed=42), 等 rsft_ced_s43 完成
  s44: LOADED from rsft_s44/metrics_v2.json              (f1=0.4655)  ← 旧协议(bs=8,seed=42), 等 rsft_ced_s44_reeval
  s45: NOT FOUND                                                      ← rsft_ced_s45 RUNNING 中

=== flatNLI_RSFT ===
  s42: LOADED from rsft_flat_nli/metrics_v2.json         (f1=0.4539)  ← 待确认协议, 等 rsft_flat_nli_s42_reeval
  s43: LOADED from rsft_flat_nli_s43_reeval/metrics_v2.json (f1=0.4523) ← bs=16 非D076, 等 _r2 完成自动切换
  s44: LOADED from rsft_flat_nli_s44/metrics.json        (f1=0.4615)  ← ✅ D076 协议
  s45: LOADED from rsft_flat_nli_s45/metrics.json        (f1=0.4551)  ← ✅ D076 协议
```

当各 reeval 目录产生 metrics 后，脚本会自动切换到更高优先级的目录，无需再改代码。

---
