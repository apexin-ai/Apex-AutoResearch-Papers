# code baseline training prep

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline_training_prep_20260519T175659_result.json`
- **Structured JSON:** [`89cd6b039e79c8d3ba0f.json`](../../sessions/89/89cd6b039e79c8d3ba0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务完成。总结：

**已部署到服务器 (`/root/colliforce-vla/scripts/`)**：
- `train_baseline.py` — LoRA fine-tune 脚本，支持单/多 GPU、dry-run、WandB
- `eval_safelibero.py` — SafeLIBERO 评估脚本，输出 CAR/TSR/轨迹平滑度

**已验证**：
- openpi config 导入 ✅（5 个 LIBERO config 可用）
- SafeLIBERO benchmark 导入 ✅（4 suite 全部有 Level I/II init_states）
- 环境兼容性修复：datetime.UTC patch、缺失依赖补装、.safelibero 路径配置

**无法 dry-run**：训练数据（Worker 2）和 pi0_base 权重（Worker 1）均未就绪。报告在 `artifacts/report_baseline_prep.md`。

---
