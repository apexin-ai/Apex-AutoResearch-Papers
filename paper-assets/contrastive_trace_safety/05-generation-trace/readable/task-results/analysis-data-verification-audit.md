# analysis data verification audit

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_data_verification_audit_20260523T102119_result.json`
- **Structured JSON:** [`b907ea88a71f0140cc84.json`](../../sessions/b9/b907ea88a71f0140cc84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核查完成。报告已写入 `artifacts/data_verification_report.md`。

**核心结论：**

- **42个数值/声明验证通过** — 包括 Table 2/3 的关键精度差值（R1-8B +20.1pp, QwQ +19.2pp）、AdvBench bootstrap 全部6个数值、nested CV 全部fold结果、R1-8B full layer sweep 全表、随机CP控制全表、AdvBench cosine compression 的 L2=0.307/L14=0.472/ratio=1.54× 均精确匹配。

- **1处确认的数值错误 (§4.3, experiments.tex L100):**
  论文写 "margin +4.5pp"，但 0.832−0.796 = 3.6pp。Table 4 正确报告 −3.6pp。+4.5pp 来自 `exp_r7` 的 precision margin，被错误引用为 BA margin。

- **18组数值无法追溯到独立源文件** — 主要是 OT-7B/R1-32B 的 holdout 结果、全部 1024d 比较值、Table 4 R1-32B 值、Table 5 ensemble holdout 值。这些实验可能在项目早期运行，输出文件未保留。通过 nested CV 和 multi-seed 间接证据支持其合理性，但无法做到逐值精确验证。

---
