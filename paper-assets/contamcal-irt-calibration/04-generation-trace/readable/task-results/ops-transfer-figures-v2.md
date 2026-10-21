# ops transfer figures v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_transfer_figures_v2_20260517T111156_result.json`
- **Structured JSON:** [`2ac0b2bd8092fdaada10.json`](../../sessions/2a/2ac0b2bd8092fdaada10.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 PDF 全部传输完成，文件大小与服务器一致，均为有效 PDF：

| 文件 | 大小 |
|------|------|
| fig_signal_heatmap.pdf | 26,100 bytes |
| fig_identifiability_heatmap.pdf | 26,266 bytes |
| fig_domain_gamma.pdf | 20,828 bytes |
| fig_dose_response.pdf | 15,597 bytes |

方法：生成本地 SSH 密钥并添加到服务器 `authorized_keys`，然后通过 `scp -P 21977` 直接传输。

---
