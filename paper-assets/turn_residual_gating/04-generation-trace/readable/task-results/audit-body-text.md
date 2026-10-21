# audit body text

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_body_text_20260525T201154_result.json`
- **Structured JSON:** [`f2356843016da172f2fc.json`](../../sessions/f2/f2356843016da172f2fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/audit_body_text.md`。

**168 个数字中 161 个验证通过（95.8%），发现 9 个问题：**

**2 个重大问题：**
1. **SS TF GAR 0.498±0.004** — per-seed 表显示 0.517±0.032，值和标准差都不匹配。疑似仅用 2 个种子或来自旧版实验（eval_v8b_ss）
2. **Figure 1(c) Llama TG gap** — 图中柱状图显示 12.5×（mean-based），但 caption 和正文均写 ~27×（median-based），图文矛盾

**4 个中等问题：**
3. "held-out GAR differs by ≤1 pp" — UG 实际差 ~1.3 pp
4. AUC=0.98（residual stream probes）— registry 无对应实验记录
5. AR eval 标注 N=50 但有效 N=39
6. Llama SS β=3=0.173 无 registry 可追溯记录

**3 个轻微问题：** PPL std 四舍五入、图标题范围、multiseed 脚本末位数字偏差。

---
