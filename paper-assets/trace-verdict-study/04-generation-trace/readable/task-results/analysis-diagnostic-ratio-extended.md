# analysis diagnostic ratio extended

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_diagnostic_ratio_extended_20260522T043449_result.json`
- **Structured JSON:** [`7300232ed4bbfaaf59b3.json`](../../sessions/73/7300232ed4bbfaaf59b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Complete. Results:

**Full_trace fix**: Diagnostic ratio corrected from 0.0000 to 0.0014. The 70 `[No trace available]` samples (all fail cases) were missed by the original code which hardcoded `return []` for full_trace.

**Extended results (15 conditions)**:

| Condition | Total Tok | Diag Tok | DiagRatio | Accuracy |
|-----------|-----------|----------|-----------|----------|
| no_trace | 153 | 0.0 | 0.0000 | 0.7513 |
| full_trace | 1912 | 0.3 | 0.0014 | 0.8144 |
| loop_only | 1152 | 25.5 | 0.0202 | 0.8513 |
| ae_only | 1287 | 174.8 | 0.1789 | 0.9992 |
| exception_only | 398 | 242.8 | 0.2308 | 0.9983 |
| vota | 1879 | 212.4 | 0.1083 | 0.9941 |
| vota_no_ae | 819 | 106.1 | 0.1373 | 0.9941 |
| tail_256 | 242 | 0.1 | 0.0008 | 0.7748 |
| tail_384 | 524 | 0.3 | 0.0014 | 0.7983 |
| tail_512 | 644 | 0.3 | 0.0014 | 0.9361 |
| tail_1024 | 949 | 0.3 | 0.0014 | 0.9647 |
| tail_2048 | 1913 | 0.3 | 0.0014 | 0.9731 |
| head_2048 | 1912 | 0.3 | 0.0014 | 0.8101 |
| nomarker | 391 | 0.0 | 0.0000 | 0.9782 |
| padded2048 | 2047 | 242.8 | 0.1186 | 0.9983 |

**Correlation**: Pearson r = 0.6295 (p=0.012), Spearman r = 0.7656 (p=0.001)

**Key findings**:
- Tail conditions break the linear diagnostic ratio → accuracy relationship: tail_512–tail_2048 achieve 93–97% accuracy with near-zero diagnostic ratio (~0.001), demonstrating that raw variable dumps near the end of execution carry strong **implicit** diagnostic signal
- **nomarker** achieves 97.8% accuracy with literally zero diagnostic content — the model uses code+test features alone
- Original 5 conditions still show strong correlation (r=0.95), but the extended set reveals the metric captures only explicit signals, not implicit ones

Output files:
- `/root/trace-verdict-study/artifacts/diagnostic_token_ratio/diagnostic_token_ratio_extended.json`
- `/root/trace-verdict-study/artifacts/diagnostic_token_ratio/diagnostic_token_ratio_extended.pdf`
- `/root/trace-verdict-study/artifacts/diagnostic_token_ratio/diagnostic_token_ratio_extended.png`

---
