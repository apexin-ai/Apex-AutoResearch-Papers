# analysis phase diagram t15 a050 s42 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase_diagram_t15_a050_s42_fp32_20260521T175410_result.json`
- **Structured JSON:** [`b821c5405134dab70a0d.json`](../../sessions/b8/b821c5405134dab70a0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，registry 已更新为 DONE(success)。

**结果摘要：**

| 指标 | 值 |
|------|-----|
| PermG FDR forward | **6/8** |
| PermG FDR reverse | 0/8 |
| diff_xcorr FDR fwd | 6/8 |
| K≥3 consensus | 4/8 |
| threshold_onset | 2/8 |
| TY Granger | 2/8 |

**跨 T 对比（α=0.50）：**
- T=5: PermG=1/8（近 α_c≈0.526）
- T=10: PermG=6/8
- T=15: PermG=**6/8**（本实验）
- T=20: PermG=6/8

α=0.50 在 T≥10 后 PermG 稳定在 6/8，缺失的 2 对始终是 mauve 配对。α=0.50 >> α_c(15)≈0.304，理论预测验证通过。

值得注意：T=15 α=0.45 (D178) 给出 PermG=8/8，优于 α=0.50 的 6/8，说明最优检测 α 可能略低于 0.50。

---
