# analysis r14 a1 qwq rerun

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r14_a1_qwq_rerun_20260518T174808_result.json`
- **Structured JSON:** [`e4849e200fe4cafa44a6.json`](../../sessions/e4/e4849e200fe4cafa44a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

```
QwQ-32B BA Layer Sweep (max_iter=2000, 60/20/20, PCA=100d):
Layer BA curve:
L0=0.7900, L1=0.7941, L2=0.7795, L3=0.7604, L4=0.7669, L5=0.7689, L6=0.7902, L7=0.7993
L8=0.8031, L9=0.8062, L10=0.7951, L11=0.7733, L12=0.7729, L13=0.7719, L14=0.7760, L15=0.7860
L16=0.7874, L17=0.8063, L18=0.8200, L19=0.8167, L20=0.8009, L21=0.7894, L22=0.8056, L23=0.8262
L24=0.8217, L25=0.8262, L26=0.8270, L27=0.8193, L28=0.8195, L29=0.8199, L30=0.8284, L31=0.8294
L32=0.8330, L33=0.8381, L34=0.8319, L35=0.8305, L36=0.8145, L37=0.8131, L38=0.8318, L39=0.8343
L40=0.8324, L41=0.8441, L42=0.8383, L43=0.8384, L44=0.8352, L45=0.8403, L46=0.8530, L47=0.8709
L48=0.8637, L49=0.8653, L50=0.8698, L51=0.8702, L52=0.8711, L53=0.8671, L54=0.8673, L55=0.8676
L56=0.8768, L57=0.8773, L58=0.8782, L59=0.8747, L60=0.8857, L61=0.8814, L62=0.8833, L63=0.8933

BA-optimal: L63 (ba=0.8933)
BA range: max-min = 13.3pp

HS vs Text on BA-optimal layer L63:
| Metric | HS    | Text  | Delta  | p      | HB? |
|--------|-------|-------|--------|--------|-----|
| Prec   | 0.521 | 0.330 | +0.192 | 0.0057 | Y   |
| BA     | 0.673 | 0.543 | +0.130 | 0.0000 | Y   |
| FPR    | 0.197 | 0.347 | -0.150 | 0.0003 | Y   |
| AUROC  | 0.812 | 0.554 | +0.258 | 0.0000 | -   |
HB pass: 3/3
```

max_iter=2000 + 60/20/20 下 BA-optimal 仍为 **L63**（与 max_iter=500 结果一致）。BA 曲线单调递增，HS 在所有指标上显著优于 text（HB 3/3 pass）。注意 PCA=100d（解释方差 56.7%）用于加速 sweep。结果已写入远程 `artifacts/r14_a1_qwq_rerun/results.json` 并注册。

---
