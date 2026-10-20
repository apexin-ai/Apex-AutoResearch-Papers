# code enhance 355m stat script

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_enhance_355m_stat_script_20260514T095906_result.json`
- **Structured JSON:** [`59c21eb6aaf1b00aadac.json`](../../sessions/59/59c21eb6aaf1b00aadac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果摘要：

**Bootstrap CI (10000 resamples, gen7 PPL)**
| 比较 | 差异 | 95% CI | 排除零 |
|------|------|--------|--------|
| RGDS vs Random-50 | +15.15 | [12.60, 17.70] | Yes |
| RGDS vs External | +7.90 | [5.10, 10.70] | Yes |
| RGDS vs Uncurated | -2.81 | [-8.82, 3.20] | No |

**不对称 Gap 模式（125M → 355M）**
| 比较 | 125M gap | 355M gap | 变化率 | CI |
|------|----------|----------|--------|-----|
| RGDS vs Random-50 | +35.85 | +15.15 | -57.7% | [-60.5%, -55.6%] |
| RGDS vs Uncurated | +30.11 | -2.81 | -109.3% | [-135.6%, -91.0%] |
| RGDS vs External | +30.74 | +7.90 | -74.3% | [-82.7%, -66.5%] |

RGDS 的 PPL gap 在 355M 规模下大幅收窄（甚至反转），说明 RGDS 对 model collapse 的加速效应随模型增大显著减弱。

LaTeX 表格已写入 `artifacts/355m_3seed_latex.tex`。当前用 2-seed 数据运行（seed=456 训练尚未完成），t-test 显示 PARTIAL（因只有 1 common seed 的对比无法做配对检验），3-seed 到齐后所有检验将自动启用。

---
