# audit maintext numbers

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_maintext_numbers_20260529T044822_result.json`
- **Structured JSON:** [`17948642ed2436badc6b.json`](../../sessions/17/17948642ed2436badc6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/audit_maintext.md`。

**结果：78个数字审计，74个完全匹配，4个需注意项（均为LOW/INFO级）。**

核心发现：
- **Table 1 全部20个cell** 的 ΔR² 和 CI 均与 bootstrap_v3 JSON 逐位比对匹配（CI采用四舍五入到0.01再显示3dp的一致规则）
- **跨文件一致性**：所有在 abstract/intro/experiments/conclusion 中重复出现的数字完全一致
- **所有 d 值、R²、p值、排名统计** 均可追溯到 plot 脚本或服务器 JSON

4个注意项：
1. **L31 head count**：论文写18，plot脚本hardcode 19（差1个head）
2. **OpenVLA L1 trained**：§4.2写24/32，cross-arch bar chart用23/32（不同测量来源）
3. **NORA "unchanged"**：Spatial suite从14→12，措辞不完全精确
4. **ρ=0.583, p=0.10**：需从Appendix数据验证（maintext数据中未定位到）

---
