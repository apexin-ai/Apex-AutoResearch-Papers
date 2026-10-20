# code dino rsa provenance

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_dino_rsa_provenance_20260516T035131_result.json`
- **Structured JSON:** [`f2a4cd12fc7e44293725.json`](../../sessions/f2/f2a4cd12fc7e44293725.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

| Feature | Mean RSA | 95% CI | 之前 hardcode |
|---------|----------|--------|--------------|
| **cls_token** | **0.6915** | [0.6409, 0.7401] | 0.692 |
| **patch_mean** | **0.6307** | [0.5331, 0.7040] | 0.631 |

两个值与之前 hardcode 引用高度一致（cls_token 0.6915 ≈ 0.692，patch_mean 0.6307 ≈ 0.631），四舍五入到小数点后两位完全匹配。

产出：
- 脚本：`/root/vla-ssd/scripts/rsa_dino_standalone.py`
- 结果：`/root/autodl-tmp/vla-ssd/results/rsa/rsa_dino_standalone.json`
- 全部 10 个 task × 50 demos，无 hardcode，7 秒完成

---
