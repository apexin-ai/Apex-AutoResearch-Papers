# analysis exp 004 re diagnostic

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_004_re_diagnostic_20260514T114103_result.json`
- **Structured JSON:** [`fc3a6f869f9ac88c2432.json`](../../sessions/fc/fc3a6f869f9ac88c2432.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-004 RE 诊断分析完成。关键发现：

**Per-relation-type breakdown**
| 类型 | n | mean F1 | ρ_sj | ρ_fk | ρ_voting |
|---|---|---|---|---|---|
| HYPONYM-OF | 36 | 0.513 | +0.545 | +0.646 | +0.628 |
| CONJUNCTION | 86 | 0.480 | +0.383 | +0.350 | +0.484 |
| USED-FOR | 299 | 0.422 | +0.236 | +0.255 | +0.286 |
| FEATURE-OF | 50 | 0.254 | +0.004 | +0.052 | +0.014 |

FEATURE-OF 是拖后腿的主力——所有信号 ρ 接近 0。HYPONYM-OF 最强但样本少。USED-FOR 占总量 55% 但 ρ 只有 ~0.24，是整体 RE rho 低的主因。

**Error propagation**: 553 个 FN 中，entity span 错误占 55.5%（head 17.7% + tail 21.9% + head_tail 15.9%），type 错误仅 8.3%。说明 RE 的低 ρ 主要源于 entity 定位不稳定而非关系类型判断。

**Threshold sensitivity**: thr=0 (conditional) 时 ρ_voting=0.384 最佳；一旦切到 thr=0.05 急剧下降到 0.236，说明 all-zero 实例是关键过滤对象。

**Bootstrap CI**: RE SJ ρ 95%CI=[0.142, 0.339]，NER SJ ρ 95%CI=[0.295, 0.459]，两者不重叠。

**Fisher z-test**: NER ρ_sj 显著高于 RE ρ_sj (z=2.31, p=0.021)。FK 和 voting_conf 差异不显著。

产出文件在服务器 `/root/autodl-tmp/struct_self_consist_ie/output/exp004_re_diagnostic/`，已注册到 registry。

---
