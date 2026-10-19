# infra de bootstrap v2 check

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_de-bootstrap-v2-check_20260523T070348_result.json`
- **Structured JSON:** [`c74e7491c86f0f0fbca0.json`](../../sessions/c7/c74e7491c86f0f0fbca0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程已退出，运行成功。** 结果文件已生成（1.3MB，15:01 写入）。

## 结果汇总

| 方向 | Mean Accuracy | 95% CI | 
|------|-------------|--------|
| EN→EN (within) | 0.7709 | [0.7463, 0.7978] |
| DE→DE (within) | 0.7626 | [0.7390, 0.7868] |
| EN→DE (cross) | 0.6923 | [0.6324, 0.7390] |
| DE→EN (cross) | 0.7047 | [0.6654, 0.7426] |

**Asymmetry (DE→EN − EN→DE):** Δ = +1.24pp, 95% CI = [−4.78, +8.09], **p = 0.4045**

## 解读

- Within-language probing 两个方向都很强（~77%/76%），且 CI 重叠，说明 DE 和 EN 的 factual representation 质量相当。
- Cross-language 显著低于 within（~69-70% vs ~77%），drop 约 7-8pp，说明跨语言 transfer 存在明显损失。
- **Asymmetry 不显著**（p=0.40），DE→EN 和 EN→DE 的 cross-lingual transfer 没有统计上的方向性差异。CI 跨零，无法拒绝对称假设。

---
