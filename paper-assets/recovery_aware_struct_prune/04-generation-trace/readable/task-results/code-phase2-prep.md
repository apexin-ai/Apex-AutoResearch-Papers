# code phase2 prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase2-prep_20260514T194829_result.json`
- **Structured JSON:** [`2ed8c30c292b9f0a28ff.json`](../../sessions/2e/2ed8c30c292b9f0a28ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。创建了 3 个文件并部署到 westb-23072，全部验证通过（语法检查、import、--help）：

**任务 1 — 多 seed GRPO**
- `src/run_grpo_multiseed.sh`：接受 `&lt;method> &lt;sparsity> &lt;gpu_id> &lt;seed>` 四个参数
- Fast config：`max_completion_length=1024, epochs=1, max_samples=2000`
- 输出到 `/root/autodl-tmp/recovered_{method}_{sparsity}_seed{seed}/`
- W&B run name: `grpo_{method}_{sparsity}_seed{seed}`
- `train_grpo.py` 已有 `--seed` 参数，无需改动

**任务 2 — GraSP baseline**
- `src/grasp_scoring.py`：独立模块，用 Hessian-gradient product（`Hg = ∂/∂θ[g^T · stop_grad(g)]`）计算 `-θ⊙Hg` 分数
- 按 GQA group / MLP group 粒度聚合（sum），与 `importance_score.py` 输出格式完全兼容
- 使用方式：`grasp_scoring.py` 生成 scores → `prune.py --mode standard --importance_path` 执行剪枝
- `src/run_grasp_prune.sh`：一键跑完 scoring + pruning

已在服务器 git commit（`e6ce5f7`）。

---
