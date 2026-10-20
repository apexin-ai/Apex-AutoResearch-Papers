# code exp 009 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_009_v2_20260514T152658_result.json`
- **Structured JSON:** [`178b4ebb684b8435611d.json`](../../sessions/17/178b4ebb684b8435611d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-009 v2 完成。核心结果：

### NER (n=551, seed42/123 高度一致, max |Δρ|=0.037)

| 信号 | 全局 ρ | 备注 |
|------|--------|------|
| voting_conf | 0.475 | 最强 |
| SJ | 0.431 | |
| FK | 0.325 | |
| EM | 0.292 | |
| logprob | 0.203 | 最弱 |

**独立代理分层结果**：
- **Sentence length**: ρ 在三个 tertile 间相对稳定（SJ: 0.48→0.39→0.40），Fisher z 均不显著。**无 inverted-U**。
- **Entity count**: 只能分两层（合并后 0-2 vs 3+）。FK 在低计数层显著更高 (p=0.011)，logprob 在高计数层显著更高 (p=0.001)。
- **Type diversity**: 变量太离散（T2=0），仅能做二分比较。logprob 在高多样性层显著更高 (p=0.024)。

### RE (n=551)

| 信号 | 全局 ρ | 备注 |
|------|--------|------|
| logprob | 0.400 | RE 中最强（NER 中最弱） |
| FK | 0.226 | |
| voting_conf | 0.220 | |
| SJ | 0.063 | 不显著 |
| EM | -0.132 | 负相关 |

**独立代理分层**：RE 呈**单调递增**而非 inverted-U — 句子越长/关系越多/类型越丰富，信号 ρ 越高。Type diversity Low→High: SJ (p=0.002*), voting_conf (p=0.034*), EM (p=0.005*)。

### 关键结论
1. 用独立代理变量分层后，**inverted-U 模式不成立** — NER 信号 ρ 在各层间稳定，RE 呈单调增。这与 v1 用 greedy F1 分层看到的 inverted-U 不同，**验证了 Dream 审稿人关于 circularity 的担忧**。
2. f1 与 sent_len 几乎不相关 (ρ=0.015)，是最独立的代理变量。ent_count 和 type_diversity 高度相关 (ρ=0.763)。
3. NER 两个 seed 的全局 ρ 高度一致。

输出位于 `output/exp_009_v2/`（results.json, summary.txt, 3 个 PDF 图）。

---
