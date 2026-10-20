# paper figure update dual benchmark

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure-update-dual-benchmark_20260520T193001_result.json`
- **Structured JSON:** [`e9c483ec4287aaf6a3f8.json`](../../sessions/e9/e9c483ec4287aaf6a3f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

生成完毕。输出文件：

| 文件 | 路径 | 大小 |
|------|------|------|
| Fig 1 PDF | `westd-29999:/root/contamcal-irt-calibration/figures/fig1_dose_response.pdf` | 22K |
| Fig 1 PNG | `westd-29999:/root/contamcal-irt-calibration/figures/fig1_dose_response.png` | 278K |
| Fig 2 PDF | `westd-29999:/root/contamcal-irt-calibration/figures/fig2_cross_benchmark_scatter.pdf` | 36K |
| Fig 2 PNG | `westd-29999:/root/contamcal-irt-calibration/figures/fig2_cross_benchmark_scatter.png` | 164K |

**Fig 1 数据确认**（s123 seed，accuracy %）：

| Family | d000 | d005 | d025 | d050 | d100 | Pattern |
|--------|------|------|------|------|------|---------|
| **MMLU** |
| Phi-4 | 76.31 | 75.92 | 77.02 | 77.30 | 78.14 | Benefit (+1.83) |
| Qwen-14B | 68.67 | 70.84 | 63.68 | 60.99 | 55.93 | Collapse (-12.74) |
| Qwen-7B | 66.59 | 63.37 | 64.82 | 65.00 | 66.59 | Immune (-0.01) |
| Gemma-2 | 65.84 | 65.81 | 63.02 | 66.74 | 67.33 | V-recovery (+1.49) |
| OLMo-2 | 55.66 | 56.14 | 54.97 | 55.92 | 55.11 | Immune (-0.55) |
| **ARC** |
| Phi-4 | 91.89 | 91.89 | 92.24 | 92.58 | 92.75 | Benefit (+0.85) |
| Qwen-14B | 90.44 | 91.47 | 89.76 | 88.74 | 87.29 | Collapse (-3.16) |
| Qwen-7B | 87.12 | 82.42 | 85.15 | 85.07 | 84.73 | V-recovery (-2.39) |
| Gemma-2 | 85.84 | 83.36 | 85.67 | 85.24 | 88.57 | V-recovery→Benefit (+2.73) |
| OLMo-2 | 76.88 | 77.22 | 76.62 | 79.18 | 79.78 | Benefit (+2.90) |

**Fig 2 scatter 数据**（多种子均值 Δ(d100) pp）：
- Phi-4: MMLU +0.73, ARC +0.65 (n=3, 实心)
- Qwen-14B: MMLU -11.05, ARC -2.86 (n=2, 空心)
- Qwen-7B: MMLU -0.89, ARC -2.65 (n=2, 空心)
- Gemma-2: MMLU +2.62, ARC +2.73 (n=1, 空心)
- OLMo-2: MMLU +1.35, ARC +3.44 (n=3, 实心)

---
