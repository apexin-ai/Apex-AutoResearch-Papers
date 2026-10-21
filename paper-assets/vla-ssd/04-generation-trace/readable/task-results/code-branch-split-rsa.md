# code branch split rsa

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_branch_split_rsa_20260516T033714_result.json`
- **Structured JSON:** [`d7d2a5c17426c8a3f6c8.json`](../../sessions/d7/d7d2a5c17426c8a3f6c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

### Branch-Split RSA (Method B)

| 表征层 | 维度 | RSA | 95% CI |
|--------|------|-----|--------|
| DINOv2 branch | 1024d | **0.619** | [0.522, 0.705] |
| SigLIP branch | 1152d | **0.621** | [0.520, 0.701] |
| Fused pre-projector | 2176d | **0.634** | [0.537, 0.722] |
| Projector output | 4096d | **0.615** | [0.526, 0.695] |

参考 baselines：standalone DINO patch_mean=0.631, standalone CLIP cls=0.557, VLA trained=0.501

### 关键发现

1. **DINOv2 和 SigLIP 贡献几乎相等**（0.619 vs 0.621），CI 高度重叠，无显著差异
2. **Fused > 两个单独分支**（0.634 > 0.619/0.621），拼接带来约 +0.015 的互补增益
3. **Projector 略降 RSA**（0.634→0.615），MLP 投影轻微损失 action-relevant structure
4. **修正**：实际维度是 DINOv2=1024d + SigLIP=1152d（非任务描述中的 1088+1088），已由提取脚本 h5 metadata `DINOv2(0:1024)|SigLIP(1024:2176)` 确认

结果已保存至 `westd-19183:/root/vla-ssd/branch_split_rsa_results.json`。

---
