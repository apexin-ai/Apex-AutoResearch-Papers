# code check resume support

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check-resume-support_20260518T095823_result.json`
- **Structured JSON:** [`cdf9e18fcf3c0c5b3ff6.json`](../../sessions/cd/cdf9e18fcf3c0c5b3ff6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### run_phase1.py 是否已支持 resume？
`src/pipeline.py` 的 `run_recursive_training()` **已有** `resume_from_gen` 参数（完整逻辑：加载 `gen_{N-1}` checkpoint + 加载已有 results JSON + 从 gen N 开始循环）。但 `run_phase1.py` 之前没有暴露该参数。

### 代码改动（2 处）
- **Line 100-101**: 添加 `--start_gen` 参数定义
- **Line 192**: 在 `run_recursive_training()` 调用中传入 `resume_from_gen=args.start_gen`

### exp_007 (r=0.2) 状态
- **Checkpoints**: 仅 `gen_0` 存在（pretrained baseline），无 gen_1 ~ gen_5
- **Results JSON**: **不存在** (`phase1_fixed_mix_r02_seed42_results.json` 文件缺失)
- 结论：exp_007 只完成了 Gen 0 评估和 checkpoint 保存，之后中断。**无法从 Gen 5 续跑**，需要从 Gen 0 重新开始

### Launch script
已创建 `/root/spectral_collapse_ews/scripts/launch_fixed_mix_r02_resume.sh`，接受两个参数：`GPU_ID`（默认 0）和 `START_GEN`（默认 0）。用法：
```bash
# 从头跑（当前状态只能这样）
bash scripts/launch_fixed_mix_r02_resume.sh 0 0
# 未来如果有 gen_4 checkpoint + results JSON，可以续跑
bash scripts/launch_fixed_mix_r02_resume.sh 0 5
```

---
