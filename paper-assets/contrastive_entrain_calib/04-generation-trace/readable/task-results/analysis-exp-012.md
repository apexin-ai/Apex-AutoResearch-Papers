# analysis exp 012

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-012_20260520T072338_result.json`
- **Structured JSON:** [`5565e13d9a405eadfaa4.json`](../../sessions/55/5565e13d9a405eadfaa4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是分析报告：

---

## 结论
**success** — Llama-3-8B CV AUROC = 0.779 > 0.75 阈值，跨模型泛化确认。

## 核心指标
- **CV AUROC**: 0.7793 ± 0.0189 (5-fold, all folds best at layer 16)
- **Full AUROC**: 0.7779
- **Best layer**: 16 (Llama 32层模型的第16层，即中间层)
- **Style-controlled AUROC**: 0.9227
- **Bootstrap CI 95%**: 未单独输出，但 5-fold std=0.019 表明稳定性好

## 与 Qwen3-8B 对比

| 指标 | Qwen3-8B (exp-001) | Llama-3-8B (exp-012) |
|------|-----|-----|
| CV AUROC | 0.827 | 0.779 |
| Best layer | 19 (of 40) | 16 (of 32) |
| Best layer 相对位置 | ~48% depth | ~50% depth |
| Style-controlled AUROC | — | 0.923 |
| Strong evidence | — | 0.911 |
| Weak evidence | — | 0.711 |

两个模型的最佳层都在网络中间（~50% depth），模式一致。Llama 绝对 AUROC 低约 0.05，但仍然显著高于 chance (0.5)。

## 对论文的意义

d_syc 线性方向在两个架构族（Qwen/Llama）上均可提取且 AUROC 显著高于 chance，支持 "discriminability is a general property of instruction-tuned LLMs" 的 claim。这强化了 "discriminability ≠ reward utility" 的核心论点——模型内部能区分 sycophantic vs. faithful responses，但这种信号并未被 reward model 利用。

## 意外发现

1. **Layer 16 独占最佳**：所有 5 个 fold 最佳层都是 16，与 Qwen 的 layer 19 一样集中在网络中层，但 Llama 的其余层 AUROC 衰减更快（次优层 31 仅 0.747 vs best 0.779），说明 Llama 的 d_syc 信号更集中于单一层。
2. **Evidence strength 分层清晰**：strong (0.911) > medium (0.864) > weak (0.711)，说明 d_syc 方向对"更明显的 sycophancy"区分度更高，符合直觉。
3. **`std_auroc_per_layer` 字段有 bug**：报告中所有层的 std 值均为 0.743（实际是 fold 4 的 AUROC），应为各层各 fold AUROC 的标准差。不影响最终结果（`best_std_auroc` 字段正确计算为 0.0189），但代码需修复。

---
