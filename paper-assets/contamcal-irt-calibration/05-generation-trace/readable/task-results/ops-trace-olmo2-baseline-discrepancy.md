# ops trace olmo2 baseline discrepancy

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_trace-olmo2-baseline-discrepancy_20260521T140736_result.json`
- **Structured JSON:** [`524aefe0fd6b8aacd8bf.json`](../../sessions/52/524aefe0fd6b8aacd8bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整分析。

---

## 所有 OLMo-2 d000 MMLU 数值汇总

| 来源 | 准确率 | 正确/总数 | Seed | 日期 | 服务器 |
|------|--------|-----------|------|------|--------|
| `eval_results_v2/olmo2_d000/` | **53.79%** | 7553/14042 | s42 | 05-19 20:18 | westd |
| `eval_results_cross_family/olmo2_d000_s42_westd/` | **58.60%** | 8229/14042 | s42 | 05-19 18:04 | westd |
| `results/mmlu_eval/olmo2/d000_s0/` | **55.34%** | — | s0 | 05-20 18:39 | westd |
| `results/mmlu_eval/olmo2/d000_s123/` | **55.66%** | — | s123 | 05-20 19:35 | westd |

cqa1 上无 OLMo-2 eval 数据。

## 53.79% 的来源

**`eval_results_v2/olmo2_d000/eval_results.json`**（westd），由 `phase2_summary.csv` 引用，被论文 results.tex 和所有分析脚本使用。

## 关键发现：v2 和 cross_family 的 dosage 对比

| Dosage | cross_family (s42) | v2 (s42) | Δ (pp) |
|--------|-------------------|----------|--------|
| d000 | 58.60% | 53.79% | **4.81** |
| d005 | 58.10% | 56.14% | 1.96 |
| d025 | 56.17% | 56.17% | **0.00** |
| d050 | 59.18% | 57.25% | 1.93 |
| d100 | 59.49% | 57.00% | 2.49 |

**d025 的 MMLU 和 ARC 在两个目录下精确到所有小数位完全一致**——说明 v2 的 d025 数据直接复制自 cross_family，而非独立 re-eval。

## 分析：为什么 d000 差 4.81pp

1. **cross_family 日志可追溯**：`olmo2_d000_s42_westd.log` 明确记录 `Loading base model + adapter: .../OLMo-2-7B_d000_s42/lora_adapter`（alpha=32 confirmed）
2. **v2 d000 没有 eval log**：monitor 日志显示 GPU0 三次启动 "OLMo d000+d005"（check 5/17/29），但无法找到对应的 eval log，无法确认是否加载了 adapter
3. **53.79% 低于所有 d000 SFT 结果**：s42 cross_family=58.60%, s0=55.34%, s123=55.66%，v2 s42 是唯一低于 55% 的
4. **d000 的差异 (4.81pp) 是其他 dosage 差异的 ~2 倍**，不符合单纯脚本版本差异的预期（脚本差异应对所有 dosage 影响相似）

**最可能的原因**：v2 d000 eval **未加载 SFT adapter**（即评估了 raw base model），或加载了错误的 adapter。53.79% 更可能是 OLMo-2-7B 原始 base model 的 MMLU 表现，不是 d000 SFT 模型的表现。

## 对论文的影响

如果 53.79% 是 base model 而非 d000 SFT：
- 论文的 OLMo-2 Benefit = +3.21pp **包含了 SFT 本身的效果**（而非纯 contamination 效果）
- 真实 d000 SFT baseline 应为 ~58.60%，contamination effect 从 d000→d100 仅约 +0.9pp
- OLMo-2 可能应从 "Benefit" 重分类为 "Immune"
- Threshold 假说（53.79% 低于 ~64.7% 阈值→Benefit）也需重新评估

## 建议

1. **用 cross_family d000 s42 westd (58.60%) 替代**——有完整日志、确认加载了正确 adapter
2. 但 cross_family 其他 dosage 和 v2 也不完全一致（d005 差 1.96pp），**混用两个数据源违反 C010**
3. **最安全方案：用当前标准化 evaluate.py 重跑 OLMo-2 全部 5 个 dosage 的 s42 eval**，获得一套完全一致的数据

---
