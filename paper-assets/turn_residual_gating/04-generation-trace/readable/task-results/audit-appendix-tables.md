# audit appendix tables

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_appendix_tables_20260525T201208_result.json`
- **Structured JSON:** [`47d5e4bba5337f8b79a7.json`](../../sessions/47/47d5e4bba5337f8b79a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。550+ 个数字已逐一验证，发现 10 个问题：

**4 个中等问题需修正：**
1. **Table 1 IID 列** — IID PPL（2.78）疑似从 Heldout 列复制，registry 实测为 2.62-2.63；TG/LoRA IID GAR-O 也偏高
2. **MMLU 最大 per-category 降幅** — 正文写 1.2pp，实际 STEM 列为 1.49pp
3. **SS max ratio 矛盾** — appendix-hyper 写 0.5，appendix-ss 写 0.3，实际数据来自 0.3 协议
4. **Llama VRAM** — 表写 46GB，registry 显示 63.4GB

**6 个低优先级问题：** gap ratio 四舍五入不一致（7.8× vs 7.9×，~1.3× vs 1.2×）、"≤1pp" 声明实际为 2pp、PPL std ±0.001 应为 ±0.002、MMLU 表标签 "Base (LoRA-only)" 误导、训练时间四舍五入偏差。

报告已写入 `artifacts/audit_appendix_tables.md`。

---
