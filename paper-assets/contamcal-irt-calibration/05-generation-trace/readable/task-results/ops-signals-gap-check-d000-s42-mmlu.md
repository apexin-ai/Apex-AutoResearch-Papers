# ops signals gap check d000 s42 mmlu

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_signals-gap-check-d000-s42-mmlu_20260515T182644_result.json`
- **Structured JSON:** [`a12b2ebe7bf6f88a5bd8.json`](../../sessions/a1/a12b2ebe7bf6f88a5bd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。汇总所有发现：

## 诊断结果

### 缺失范围

**不仅是 3B d000_s42 的 mmlu**——所有 3B 模型的 mmlu selfcritique 都缺失：

| Model | Dosage | mmlu s4 | mmlu merged | gsm8k s4 | arc s4 |
|-------|--------|---------|-------------|----------|--------|
| 0.5B  | all    | ✅ (旧命名) | ✅ | ✅ | ✅ |
| 1.5B  | all    | ✅ (旧命名) | ✅ | ✅ | ✅ |
| 3B    | d000   | ❌ | ❌ | ✅ | ✅ |
| 3B    | d005   | ❌ | ❌ | ❌ | ✅ |
| 3B    | d025   | ❌ (仅有 s1) | ❌ | ❌ | ❌ |

### 根因

**3B mmlu selfcritique 在运行中崩溃（大概率 OOM），不是设计跳过。**

证据：
1. **代码无特殊处理**：`s4_selfcritique.py` 对所有 benchmark 逻辑完全一致，没有 mmlu 跳过逻辑
2. **compute_signals.py 无 try/except**：s4 崩溃会直接杀死整个进程
3. **规模差异巨大**：mmlu 有 **14,042** 项，gsm8k 仅 1,319，arc 仅 1,172。selfcritique 需要对每项做 `model.generate()` 生成答案再做 critique forward pass，3B 模型处理 14K 项的显存和时间开销约 10 倍于 gsm8k/arc
4. **时间线佐证**：d000 的 mmlu s2 完成于 00:28，gsm8k s1 直到 01:07 才开始（39 分钟空白），这段时间 s4 被尝试但未产出文件
5. **渐进退化**：d000 完成了 gsm8k/arc 全部信号，d005 只完成 arc，d025 仅有 mmlu s1——pipeline 被逐步中断

### 需要补算

**是，需要补算。** 3B 的 mmlu selfcritique 缺失会导致：
- `signals_merged_mmlu.json` 无法生成（merge 需要 ≥2 信号在同一次运行中完成）
- 下游 RRF 聚合跳过 mmlu
- 3B 模型的污染检测在 mmlu 上缺少 selfcritique 维度

**补算建议**：
- 单独运行 `--benchmark mmlu --signal s4`（不需要重算 s1/s2）
- 降低 batch_size（当前 32 太大，建议 2-4）
- 运行后再单独做 merge（需要加载已有 s1/s2 结果合并）
- 3 个 dosage（d000/d005/d025）都需要补

---
