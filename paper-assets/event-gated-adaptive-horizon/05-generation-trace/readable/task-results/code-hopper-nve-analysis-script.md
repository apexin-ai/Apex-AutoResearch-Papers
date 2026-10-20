# code hopper nve analysis script

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hopper-nve-analysis-script_20260527T030317_result.json`
- **Structured JSON:** [`50a02e580200f4b0da48.json`](../../sessions/50/50a02e580200f4b0da48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本完成验证，所有功能正常：

1. **NVE 计算** — 从 metrics.jsonl 读取 eval_return + value_mean，计算 ve_ratio，再除以 baseline ve_ratio 得到 NVE（35K+ 窗口）
2. **CIVO Onset 检测** — D155 三维标准（τ=1.5×, 持续≥2点, 35K+ onset），分类为 no_onset / sustained / collapse / sustained→self_correcting / transient→degraded
3. **部分数据处理** — 当前 Hopper 实验刚启动（各1个 eval 点），脚本正确输出 "insufficient_data"
4. **跨环境汇总** — 读取 cross_env_civo_summary.json，正确展示 Walker/Cheetah/Hopper 数据
5. **图表输出** — PDF + PNG 已生成到 `artifacts/hopper_nve_analysis.{pdf,png}`
6. **JSON 输出** — `artifacts/hopper_nve_analysis.json`

**运行命令**（实验完成后）：
```bash
python analyze_hopper_nve.py --logdir logdir/ --baseline exp_hopper_baseline \
  --experiments exp_hopper_trained_s0 exp_hopper_trained_s1 \
  --frozen exp_hopper_frozen_s0 exp_hopper_frozen_s1 \
  --output artifacts/hopper_nve_analysis --json
```

---
