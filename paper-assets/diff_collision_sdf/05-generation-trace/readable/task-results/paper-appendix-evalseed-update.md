# paper appendix evalseed update

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix-evalseed-update_20260528T033807_result.json`
- **Structured JSON:** [`54442cde853bff67d9ad.json`](../../sessions/54/54442cde853bff67d9ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。汇总：

**5 路 multi-eval-seed 结果汇总：**

| 进程 | Avg TSR | Avg CAR | 状态 |
|------|---------|---------|------|
| lora_s0_eseed7 | 51.5% | 56.5% | 基准 |
| lora_s0_eseed42 | 46.0% | 56.5% | 完成 |
| lora_s0_eseed123 | 50.5% | 53.0% | 完成 |
| sdf_l01_s0_eseed7 | 52.5% | 57.0% | 基准 |
| sdf_l01_s0_eseed42 | 52.5% | 59.0% | 完成 |
| sdf_l01_s0_eseed123 | 53.5% | 58.5% | 完成 |
| sdf_l01_s0_eseed256 | 48.0% | 57.0% | 完成 |

**关键发现：**
- LoRA s0 CAR 跨 eval seed 稳定：55.3% ± 2.0%
- SDF λ=0.1 s0 CAR 更稳定：57.9% ± 1.0%
- 在 3 个匹配 seed 上 SDF 均高于 LoRA（ΔCAR = +0.5, +2.5, +5.5 pp）
- Per-task ordering (CP highest, BBQ lowest) 在所有 seed 下保持不变

**完成项：**
- Appendix 新增 `\section{Evaluation Seed Robustness}` 含 CAR 和 TSR 两张表
- PDF 编译成功（17 页）
- paper_switch.py --verify 全部 OK（Scenario B: 10/10, Scenario C: 11/11）

---
