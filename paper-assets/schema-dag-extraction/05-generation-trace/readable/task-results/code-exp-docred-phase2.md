# code exp docred phase2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_docred_phase2_20260516T043709_result.json`
- **Structured JSON:** [`13bc771c508289169da3.json`](../../sessions/13/13bc771c508289169da3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 2 DocRED Confusability Study 完成。

**结果总结：**

**Phase 2a — Count Curve** (accuracy vs. schema size):
- count=1: 88.0% → count=4: 77.0% → count=8: 77.4% → count=16: 52.4% → count=32: 52.1% → count=64: 42.4% → count=96: 38.7%
- 单调递减，验证 Claim 1（schema size 增大导致性能退化）

**Phase 2b — BCS-Controlled** (confusability effect, holding count fixed):
- count=16: low-BCS 67.9% vs high-BCS 44.7% → **23.3pp gap**
- count=32: low-BCS 57.8% vs high-BCS 40.3% → **17.6pp gap**
- 验证 Claim 2（高 confusability 独立于 count 导致性能下降）

**Phase 2c — Bootstrap CI** (statistical significance):
- count=16: slope=-0.713 CI[-0.909, -0.529], Spearman r=-0.661 (p=1.5e-5)
- count=32: slope=-0.690 CI[-0.854, -0.519], Spearman r=-0.509 (p=0.002)
- 两个 count level 的 BCS-accuracy 负相关均显著，quartile gap CI 不含 0

所有 artifacts 已注册，registry 已更新为 DONE。

---
