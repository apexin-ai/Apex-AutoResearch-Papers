# paper writing analysis

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_analysis_20260519T224949_result.json`
- **Structured JSON:** [`8089c5b57704cf937309.json`](../../sessions/80/8089c5b57704cf937309.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`analysis.tex` 已写入，~1000 words，4 个子节结构完整。

要点核查：
- **§6.1**: 描述性观察，明确标注非因果 claim，含 Table 1 (3-row gradient conflict 数据)
- **§6.2**: 27/28 层 gate 行为与设计意图相反，Wilcoxon p=3.73e-8，inference-time attenuation 仅 2-7%，引用 Figure 3(a)
- **§6.3**: PCGrad 消除方向冲突 (cos_sim 转正 +0.086) 但 L_GAR 仍坍塌，modus tollens 编号列表，claim scope 限定为 direction conflict，GradNorm/Nash-MTL 留作 future work，引用 Figure 2(b)
- **§6.4**: Same-dist GAR 0.49 vs cross-dist 0.016 (30x gap)，GAR-Dongre 无 gap 作为 control，连接 exposure bias 文献 (bengio2015scheduled, he2019exposure)，处理 He et al. tension (primary objective robust, auxiliary objective fragile)，引用 Figure 3(b)
- 风格：零 em-dash，零 -ing 结尾，零 AI buzzwords

---
