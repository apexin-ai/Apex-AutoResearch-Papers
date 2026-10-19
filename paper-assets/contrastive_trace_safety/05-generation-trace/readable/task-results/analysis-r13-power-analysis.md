# analysis r13 power analysis

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r13_power_analysis_20260518T143918_result.json`
- **Structured JSON:** [`4954d5d33f8463370c02.json`](../../sessions/49/4954d5d33f8463370c02.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**实际测试集大小**：R1-32B n=30, QwQ-32B n=29（非任务假设的 n=20）

**Power Table（核心结果）**：

| Model | n | 5pp | 10pp | 15pp | 20pp | MDE(80%) |
|-------|---|-----|------|------|------|----------|
| R1-32B | 30 | .368 | **.901** | .998 | 1.00 | 8.6pp |
| QwQ-32B | 29 | .313 | **.837** | .993 | 1.00 | 9.5pp |
| 32B (n=20) | 20 | .239 | **.704** | .963 | 1.00 | 11.2pp |
| R1-8B | 63 | .478 | **.968** | 1.00 | 1.00 | 7.4pp |
| OT-7B | 69 | .558 | **.988** | 1.00 | 1.00 | 6.7pp |

**论文用句**：With n=29-30 paired traces for the 32B models, post-hoc power analysis indicates approximately 84-90% power to detect a 10pp balanced accuracy difference at alpha=0.05, with the minimum detectable effect at 80% power being 8.6-9.5pp. The 7-8B models (n=63-69) are well-powered (>96%) for the same effect size.

结果和脚本已保存到远程 `artifacts/r13_power_analysis/`，report 已注册为 artifact `art_20260518_3e29cc`。

---
