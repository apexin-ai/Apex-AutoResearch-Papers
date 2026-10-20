# code ablation p3 per dof

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ablation_p3_per_dof_20260516T085732_result.json`
- **Structured JSON:** [`737dcad792f4c29a731e.json`](../../sessions/73/737dcad792f4c29a731e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果完整且一致。

**结果摘要:**

| Condition | xyz peak | rpy peak | gripper peak | full peak |
|-----------|----------|----------|-------------|-----------|
| trained_image_mean | L13, 0.193 | L12, 0.175 | L13, 0.106 | L13, 0.176 |
| trained_last_preaction | L12, 0.294 | L13, 0.296 | L12, 0.180 | L12, 0.280 |
| untrained_image_mean | L0, 0.184 | L0, 0.159 | L0, 0.093 | L0, 0.163 |
| untrained_last_preaction | L1, 0.190 | L2, 0.187 | L2, 0.103 | L1, 0.171 |

**Dominance**: xyz 在所有条件下贡献最大（略高于 rpy），gripper 贡献最低。trained_last_preaction 中 xyz ≈ rpy（0.294 vs 0.294），差距极小。

**关键发现:**
- xyz 和 rpy 贡献接近，translation 略占优
- gripper（离散 0/1）RSA 显著低于连续维度（预期行为）
- Trained 模型 RSA 峰值在 L12-13（中间层），untrained 在 L0-2（早期层即衰减）

脚本: `/root/vla-ssd/scripts/ablations/rsa_per_dof.py`
结果: `/root/autodl-tmp/vla-ssd/results/ablations/rsa_per_dof.json` (612s, 18KB)

---
