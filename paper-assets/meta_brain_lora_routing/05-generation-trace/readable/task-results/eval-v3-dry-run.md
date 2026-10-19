# eval v3 dry run

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_v3_dry_run_20260516T204351_result.json`
- **Structured JSON:** [`285503f70429c553434f.json`](../../sessions/28/285503f70429c553434f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果：PASS

v3 base checkpoint eval pipeline **端到端成功跑通**，无报错。

### 运行结果
- **Success rate: 1/2 = 50.0%**
- Ep0: PASS (79 steps) — "pick up the black bowl between the plate and the ramekin and place it on the plate"
- Ep1: FAIL (220 steps, timeout) — "pick up the black bowl in the top drawer of the wooden cabinet and place it on the plate"

### 诊断数据
- Action 范围合理: [-1.03, 1.05]
- Action chunk shape: (50, 7)，每 5 步 replan
- 模型加载耗时 ~40s，Policy 构建正常
- jaxtyping disable 生效，无类型检查报错
- MUJOCO_GL=egl headless 渲染正常

### 完整运行命令
```bash
cd /root/meta_brain_lora_routing/phase1 && \
CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl python3 eval_base_no_lora.py
```

### 与之前 60%/10eps 结果一致
50% (1/2) 与之前 60% (6/10) 量级一致——失败 episode 均为 timeout（220 steps 未完成），非 crash。抽屉类 task 本身比桌面 pick-and-place 难。

### 注意
最近批量 eval 输出（`phase1/outputs/eval_none_*`）全是 0%——可能是其他脚本 (`evaluate_libero_plus.py`) 的 perturbation 运行或参数配置问题，与 `eval_base_no_lora.py` 不同。base pipeline 本身是通的。

---
