# ops cleanup deploy vllm alpacaeval

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_deploy_vllm_alpacaeval_20260521T072358_result.json`
- **Structured JSON:** [`5d7c5dc99b42c290c21c.json`](../../sessions/5d/5d7c5dc99b42c290c21c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项任务全部完成。汇报：

**1. 清理残余进程**
- 杀掉了 GPU 2 上的 vLLM 进程（PID 114905, 114900, 115174），原为 Qwen3-32B tp=1 on port 8002
- jupyter-lab (1233) 和 tensorboard (1235) 保留未动
- 清理后 4 张 GPU 全部空闲（0 MiB）

**2. exp-006 CF gen 完成确认**
- 文件路径：`/root/causal_style_decomp_judge/data/counterfactuals_scaled_formality.jsonl`
- 行数：**400/400** ✓
- 注：文件名是 `counterfactuals_scaled_formality.jsonl`，不是 `counterfactuals_formality_*.jsonl`

**3. vLLM Qwen3-32B 部署**
- PID：121776（API server pid 121781）
- GPU：cuda:0,1，tp=2
- 端口：8000
- 状态：**已就绪**（"Application startup complete"）
- 模型 ID：`/root/autodl-tmp/models/Qwen3-32B/`
- max_model_len：8192

---
