# code exp gemma2b depth

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_gemma2b_depth_20260520T062049_result.json`
- **Structured JSON:** [`6af98814e9ab46eaa0a1.json`](../../sessions/6a/6af98814e9ab46eaa0a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务运行正常。状态汇总：

| 项目 | 状态 |
|------|------|
| **模型就绪** | Gemma-2-2B 已通过 ModelScope 下载到 `/root/autodl-tmp/.hf_cache/gemma-2-2b-ms/google/gemma-2-2b/`，GPU 0 已加载（6.5GB 显存） |
| **脚本创建** | `run_gemma2b_depth.py` 已部署到 `/root/autodl-tmp/gen-depth-contamination/scripts/` |
| **训练提交** | tmux session `exp_gemma2b_depth` 运行中，PID 288886，GPU 利用率 75% |
| **当前阶段** | Step 3: Depth Chain — depth 1 生成中（刚开始 ~1 min，313 batches，~5.5s/batch） |

**预估时间线**（当前 14:52）：
- Depth chain 生成（5 depths × ~29 min）：~2.4h → 约 17:15 完成
- Feature extraction（Qwen2.5-1.5B scorer，30K docs）：~30-60 min
- Analysis + Bootstrap CI（10K resamples + 10K permutations）：~15 min
- **总计预估完成时间：约 18:00-18:30（服务器时间）**

---
