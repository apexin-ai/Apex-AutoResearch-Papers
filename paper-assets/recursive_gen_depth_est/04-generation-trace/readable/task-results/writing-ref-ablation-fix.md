# writing ref ablation fix

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_ref_ablation_fix_20260516T080519_result.json`
- **Structured JSON:** [`6b039ae1f20ecbdbe7e5.json`](../../sessions/6b/6b039ae1f20ecbdbe7e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三处修改均已生效：

1. **method.tex L43**: `78.6%` → `78.5%`（四舍五入修正）
2. **method.tex L43**: claim 弱化为 "suggesting ... not critically dependent on the specific reference model"，加入 robustness threshold 量化
3. **conclusion.tex L37-38**: 删除 "future work should validate with a truly independent reference model" 旧句，替换为与 ablation 结果一致的表述，明确指出 scale/architecture 共性及 encoder-only/larger-scale 验证仍 open

---
