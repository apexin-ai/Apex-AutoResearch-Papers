# code check 340m eval results

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_340m_eval_results_20260519T043025_result.json`
- **Structured JSON:** [`c78e1884606e82e7fee2.json`](../../sessions/c7/c78e1884606e82e7fee2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

10 个模型（RetNet×5 + HGRN2×5）全部完成，无失败。目录中还有一些 GatedDeltaNet 的残留文件（非本次评测范围）。

## 340M 批量评测结果

| Model | Lambada Acc | Lambada PPL | HellaSwag Acc_norm | ARC-E Acc_norm | ARC-C Acc_norm | WinoGrande Acc | MMLU Acc |
|---|---|---|---|---|---|---|---|
| **RetNet-pure** | 0.3644 | 26.12 | 0.4120 | 0.5332 | 0.2730 | 0.5114 | 0.2384 |
| **RetNet-hybrid-3-1** | 0.3454 | 31.65 | 0.4089 | 0.5257 | 0.2841 | 0.5280 | 0.2376 |
| **RetNet-hybrid-6-1** | 0.3468 | 30.03 | 0.4171 | 0.5391 | 0.2816 | 0.5280 | 0.2514 |
| **RetNet-hybrid-12-1** | 0.3606 | 28.30 | 0.4189 | 0.5358 | 0.2747 | 0.5296 | 0.2444 |
| **RetNet-hybrid-24-1** | 0.3635 | 27.31 | 0.4121 | 0.5194 | 0.2901 | 0.5185 | 0.2340 |
| **HGRN2-pure-baseline** | 0.3186 | 33.51 | 0.4317 | 0.5581 | 0.3046 | 0.5185 | 0.2303 |
| **HGRN2-hybrid-3-1** | 0.3637 | 26.65 | 0.4373 | 0.5354 | 0.2918 | 0.5383 | 0.2322 |
| **HGRN2-hybrid-6-1** | 0.3716 | 25.11 | 0.4372 | 0.5387 | 0.3063 | 0.5391 | 0.2317 |
| **HGRN2-hybrid-12-1** | 0.3633 | 25.51 | 0.4392 | 0.5610 | 0.3003 | 0.5375 | 0.2312 |
| **HGRN2-hybrid-24-1** | 0.3367 | 29.62 | 0.4316 | 0.5421 | 0.3055 | 0.5114 | 0.2424 |

**状态**: 10/10 模型全部成功完成，ALL DONE 于 2026-05-19 12:26:15 CST。

**初步观察**:
- **HGRN2 整体优于 RetNet**：HellaSwag、ARC-C 上 HGRN2 各配置普遍领先
- **HGRN2-hybrid-6-1** 在 Lambada Acc (0.3716)、Lambada PPL (25.11) 上表现最佳
- **HGRN2-hybrid-12-1** 在 HellaSwag (0.4392)、ARC-E (0.5610) 上最佳
- Hybrid 配置对 HGRN2 的 Lambada PPL 改善显著（pure 33.51 → hybrid-6-1 25.11）
- RetNet 的 hybrid 配置未见一致性提升，部分指标反而低于 pure baseline
- MMLU 全部接近随机水平（~0.23-0.25），符合 340M 规模预期

---
