# ops diagnose s1 l005 exit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_s1_l005_exit_20260523T055314_result.json`
- **Structured JSON:** [`1d50bc3dd8e1a7e98c5f.json`](../../sessions/1d/1d50bc3dd8e1a7e98c5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。诊断结论：

## 诊断结果

**根因：数据盘 `/root/autodl-tmp` 100% 满（350G/350G，仅剩 8K）**

**所有 4 个实验同时在 step 8000 checkpoint 保存时崩溃**，训练本身正常运行到 step 7999（27%/30000）。

| 实验 | GPU | 最后 step | 错误 | 已保存 checkpoint |
|------|-----|-----------|------|-------------------|
| s1_l005 | cuda:0 | 7999 | safetensors serialize ENOSPC | 4000, 6000, best |
| s1_l01 | cuda:1 | 7999 | safetensors serialize ENOSPC | 4000, 6000, best |
| s2_l005 | cuda:2 | 7999 | mkdir tmp_8000 ENOSPC | 4000, 6000, best |
| s2_l01 | cuda:3 | 7999 | mkdir tmp_8000 ENOSPC | 4000, 6000, best |

**磁盘占用分布**（checkpoints ~313G / 350G）:
- baseline_object_pudding: 76G
- baseline_spatial_bowl: 76G
- a1_sdf_pi05_object_pudding (本次 4 实验 + lora baseline): 112G
- 其他: ~49G

**已完成操作**:
- 4 个 cron 已删除
- 4 个实验 registry 已更新为 DONE/failed

**恢复建议**：
1. 清理不再需要的旧 checkpoint（baseline 两组占 152G）释放空间
2. 删除 seed1 的 `tmp_8000` 残留目录
3. 从 step 6000 checkpoint resume 训练（需先确保磁盘有足够空间，30000 steps 每 2000 步存一次约需额外 ~80G）

---
