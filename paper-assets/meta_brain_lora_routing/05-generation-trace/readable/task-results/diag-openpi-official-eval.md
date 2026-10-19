# diag openpi official eval

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_openpi_official_eval_20260516T092654_result.json`
- **Structured JSON:** [`f39e1bad13f28ef29f9e.json`](../../sessions/f3/f39e1bad13f28ef29f9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，所有关键信息已收集齐。

---

## 最终诊断结果

### 1. Fine-tuned Checkpoint 存在性

| 项目 | 状态 |
|------|------|
| 服务器上 pi0_libero / pi05_libero | **不存在** |
| 服务器上仅有 | `pi0_base` at `/root/autodl-tmp/checkpoints/pi0_base/` |
| 官方 fine-tuned checkpoint | `gs://openpi-assets/checkpoints/pi05_libero/` (GCS) |
| pi0_base README 明确说明 | "Base model to fine tune on your specific use case" |

openpi README 中的官方结果表：
| Model | Spatial | Object | Goal | 10 | Avg |
|-------|---------|--------|------|-----|-----|
| π0.5 fine-tuned @ 30k | 98.8 | 98.2 | 98.0 | 92.4 | **96.85** |

### 2. 官方 Eval 对比

- 官方 eval (`examples/libero/main.py`) 使用 **pi05_libero** fine-tuned checkpoint（config `pi05_libero`，从 pi05_base 微调 30k steps）
- MetaBrain 当前使用 `pi0_base`（从未在 LIBERO 上训练）
- **无法用 pi0_base 运行官方 eval 来获得 baseline**——它同样会得到 ~0%

### 3. norm_stats / 预处理差异

| 处理步骤 | MetaBrain | 官方 openpi |
|----------|-----------|-------------|
| State 维度 | 8-dim → pad to 32 | 8-dim → pad to 32 (via Normalize with 32-dim identity stats) |
| Action 输出 | 32-dim → slice [:, :7] | 32-dim → slice [:, :7] (LiberoOutputs) |
| norm_stats | identity (mean=0, std=1) | identity (mean=0, std=1) |
| Image 处理 | uint8 HWC → BCHW torch | uint8 HWC → BCHW torch |
| Image mask | base=True, left_wrist=True, right=**False** | 与 PI0 模型相同(False) |
| Prompt | tokenize string | tokenize string |
| Replan | 每 5 步 | 每 5 步 |

**结论：MetaBrain 的预处理流程与官方 LIBERO pipeline 一致，无显著差异。**

### 4. 结论

**根因：pi0_base 从未在 LIBERO 上训练过，不能 zero-shot 完成 LIBERO 任务。0% 成功率是预期行为。**

MetaBrain 集成无问题。需要：

**方案 A（推荐）：下载 fine-tuned checkpoint**
```bash
# 从 GCS 下载 pi05_libero（需 gcloud 或 gsutil）
gsutil -m cp -r gs://openpi-assets/checkpoints/pi05_libero/ /root/autodl-tmp/checkpoints/pi05_libero/
```
或从 openpi 代码自动下载（serve_policy.py `--env LIBERO` 会自动拉取）。

**方案 B：用 openpi 训练框架自行微调**
- Config: `pi0_libero`（从 pi0_base 开始，在 LIBERO 数据上训练 30k steps）
- 需要先准备 LeRobot 格式的 LIBERO 训练数据（`physical-intelligence/libero` dataset）

**对 MetaBrain 研究的影响**：MetaBrain 的 LoRA routing 应该建立在一个已经能完成 LIBERO 任务的 base policy 之上（pi0_libero 或 pi05_libero），然后用 LoRA 修正扰动场景。在一个完全不能做任务的 base 上加 LoRA 是无效的。

---
