# analysis r14 a1 r1 32b rerun

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r14_a1_r1_32b_rerun_20260518T172841_result.json`
- **Structured JSON:** [`95ce8e26e4fac3e38bd7.json`](../../sessions/95/95ce8e26e4fac3e38bd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

```
R1-32B BA Layer Sweep (max_iter=2000, 60/20/20):
Layer BA curve:
  L00=0.8737  L01=0.8717  L02=0.8747  L03=0.8852  L04=0.8830  L05=0.8932  L06=0.9045  L07=0.9149
  L08=0.9187  L09=0.9132  L10=0.9076  L11=0.9009  L12=0.8865  L13=0.8772  L14=0.8655  L15=0.8593
  L16=0.8533  L17=0.8564  L18=0.8660  L19=0.8684  L20=0.8565  L21=0.8580  L22=0.8758  L23=0.8864
  L24=0.8864  L25=0.8858  L26=0.8855  L27=0.8885  L28=0.8960  L29=0.9009  L30=0.9015  L31=0.9053
  L32=0.8983  L33=0.9020  L34=0.9016  L35=0.9062  L36=0.9029  L37=0.8963  L38=0.8989  L39=0.9136
  L40=0.9187  L41=0.9228  L42=0.9143  L43=0.9222  L44=0.9216  L45=0.9311  L46=0.9331  L47=0.9350
  L48=0.9350  L49=0.9355  L50=0.9319  L51=0.9327  L52=0.9309  L53=0.9260  L54=0.9270  L55=0.9256
  L56=0.9236  L57=0.9250  L58=0.9259  L59=0.9271  L60=0.9313  L61=0.9263  L62=0.9321  L63=0.9315
BA-optimal: L49 (ba=0.9355)

HS vs Text on BA-optimal layer L49:
| Metric | HS     | Text   | Delta   | p      | HB? |
|--------|--------|--------|---------|--------|-----|
| Prec   | 0.5542 | 0.4726 | +0.0816 | 0.0057 | Y   |
| BA     | 0.7184 | 0.6286 | +0.0898 | 0.0004 | Y   |
| FPR    | 0.3092 | 0.3482 | -0.0390 | 0.2447 | -   |
| AUROC  | 0.7786 | 0.6664 | +0.1122 | 0.0000 | Y   |
HB pass: 3/3
```

BA 曲线呈双峰结构：L8 处第一个峰 (0.9187)，L16 处谷底 (0.8533)，之后持续上升至 L49 处全局最优 (0.9355)。BA-optimal 从之前的 L63 移至 L49（约 77% depth），L45-L63 区间整体>0.92 高原。HS 在所有 3 个 HB 指标上显著优于 text baseline。

---
