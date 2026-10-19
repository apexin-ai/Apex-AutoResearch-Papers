# code phase1 assembly eval

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase1-assembly-eval_20260515T162251_result.json`
- **Structured JSON:** [`466a7cbda7f951044584.json`](../../sessions/46/466a7cbda7f951044584.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 全部通过。结果摘要：

- **模型加载**: PI0 on cuda:3, 6.5GB 显存
- **路径发现**: PaliGemma layer 6 path = `paligemma_with_expert.paligemma.model.language_model.layers.6`, 72 个 LoRA target modules
- **PAR 路由**: actions shape `(1, 50, 32)`, routing weights `[0.175, 0.224, 0.601]` (sum=1.0)
- **5 种 routing 模式全部验证通过**:
  - `none`: `rw=[0, 0, 0]` — 冻结 baseline，无 LoRA
  - `random`: `rw=[0.027, 0.487, 0.486]` — Dirichlet 随机
  - `universal`: `rw=[1/3, 1/3, 1/3]` — 均等权重
  - `oracle`: `rw=[1, 0, 0]` — ground-truth 单专家
  - `par`: `rw=[0.175, 0.224, 0.601]` — PAR Router 输出

所有模式输出 shape 均为 `(1, 50, 32)`，Scheme C 动态 LoRA 合并 + 两阶段推理管线工作正常。

Step 4 dry-run 验证完成。四步任务（研究 OpenPI 推理逻辑 → 编写 `meta_brain_assembly.py` → 编写 `evaluate_libero_plus.py` + `ablation_ladder.py` → cuda:3 dry-run 验证）全部完成。

---
