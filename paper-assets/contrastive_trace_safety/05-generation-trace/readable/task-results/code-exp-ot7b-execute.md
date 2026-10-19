# code exp ot7b execute

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_ot7b_execute_20260517T065302_result.json`
- **Structured JSON:** [`9b3422f3a89bc91b7cf7.json`](../../sessions/9b/9b3422f3a89bc91b7cf7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Pipeline 完成。** 全部 6 个阶段执行成功，结果已录入 registry 和 artifacts。

## 关键结果

| 指标 | HS Probe (W=3, L=0) | Text Probe (W=25) | Delta | p-value | Bonferroni |
|------|---------------------|-------------------|-------|---------|------------|
| bal_acc | 0.6721 → 0.7373* | 0.6141 → 0.6558* | +8.15pp | 0.001 | **Yes** |
| precision | 0.3571 → 0.4249* | 0.3291 → 0.3459* | +7.9pp | 0.056 | No |
| pre_cp_fpr | 0.1877 | 0.2709 | -8.3pp | 0.007 | **Yes** |

*bootstrap 重训估计

- **Best layer = 0**（embedding 层，depth=0%），crossing_rate=53.2%，所有层 bal_acc 在 0.63-0.68 范围内相对平坦
- **Selectivity = 18.5 pp**（real=0.672 vs random=0.487），远超随机水平
- **结论**: HS > Text 在 bal_acc 和 FPR 上通过 Bonferroni 显著性检验。OpenThinker-7B（非 R1 蒸馏、STILL 训练）确认 HS 优势泛化到非 R1 模型家族。

### 修复记录
- Phase 4 首次运行因 `KeyError: 'sentences'` 崩溃——.pt 文件未保存 sentences 字段。已修复：在 `main()` 中合并原始 traces 的 sentences。用 continuation script 跳过已完成的 Phase 2-3，节省 50+ 分钟重跑时间。

---
