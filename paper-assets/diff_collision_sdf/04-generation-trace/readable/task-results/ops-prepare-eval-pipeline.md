# ops prepare eval pipeline

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare_eval_pipeline_20260523T015023_result.json`
- **Structured JSON:** [`ad2b25d015e54f926e6c.json`](../../sessions/ad/ad2b25d015e54f926e6c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个文件：

1. **`artifacts/eval_commands_d012.md`** — 6 个模型的完整 eval 命令模板
   - westd-45947: s0_l005 (GPU0:8000), s0_l01 (GPU1:8001)
   - westd-35807: s1_l005~s2_l01 (GPU0-3:8000-8003)
   - 每个包含：环境激活 → serve_policy 启动 → eval 执行 → 清理
   - `&lt;STEP>` 占位符待训练完成后替换（`best` 或具体 step）

2. **`artifacts/analyze_d012_results.py`** — 独立分析脚本
   - 读取 6 个 JSON，输出 per-task/overall metrics
   - D012 pass/fail 判定（CAR≥33%, TSR≥50%, frozen_rate≤baseline）
   - vs Pi0.5 baseline 的 Welch t-test + Cohen's d
   - 按 λ=0.005/0.01 分组聚合 + 组间对比
   - 生成 Markdown 对比表
   - 用法：`python analyze_d012_results.py --scan_dir /root/autodl-tmp/eval_results/d012`

---
