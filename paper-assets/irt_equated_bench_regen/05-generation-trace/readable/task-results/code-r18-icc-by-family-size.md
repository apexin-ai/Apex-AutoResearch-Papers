# code r18 icc by family size

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r18_icc_by_family_size_20260522T163330_result.json`
- **Structured JSON:** [`ed16a7ab91c8e1a4a802.json`](../../sessions/ed/ed16a7ab91c8e1a4a802.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。产出文件：

- **脚本**: `artifacts/r18_icc_by_family_size/icc_family_analysis.py`
- **报告**: `artifacts/r18_icc_by_family_size/icc_family_report.md`
- **图表**: `artifacts/r18_icc_by_family_size/icc_vs_family_size.png/pdf`
- **数据**: `artifacts/r18_icc_by_family_size/icc_family_results.csv`

**结果与预期不同**：ICC 与 family size **无显著相关**（ρ = −0.009, p = 0.96）。大家族的 ICC 既不高也不低，稳定在 0.4–0.5 区间。但这恰好支持 simple-mean DEFF：

- 既然 ICC ≈ 0.46 在所有 size 上基本恒定，那加权 m̄ = 254（被 Mistral/Llama 拉高）就是不合理的——它假设大家族贡献更多 clustering，但实际上大家族并不比小家族更 homogeneous
- Simple m̄ = 63 → DEFF ≈ 29，weighted m̄ = 254 → DEFF ≈ 117，差 4 倍
- 小家族 (m<10) 方差极大（SD=0.34），包含 near-clone 家族（wizardlm-2: r̄=0.99）和异质家族（olmo: r̄=0.11），这些在 simple mean 中被平均掉

---
