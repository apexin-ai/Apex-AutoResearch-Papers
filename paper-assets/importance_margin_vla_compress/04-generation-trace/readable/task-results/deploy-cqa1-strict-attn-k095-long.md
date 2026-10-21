# deploy cqa1 strict attn k095 long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_strict_attn_k095_long_20260527T031120_result.json`
- **Structured JSON:** [`cb242986a1765727ed40.json`](../../sessions/cb/cb242986a1765727ed40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已成功启动并正在运行：

- **服务器**: cqa1-33015, GPU 2 (~9.5GB VRAM)
- **tmux session**: `eval_pi05_attn_k095_long_strict`
- **日志**: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/eval_pi05_attn_k095_long_strict.log`
- **注册状态**: RUNNING

**修复过程总结**:
1. lerobot 0.5.2 + transformers 4.40.1 不兼容 → 升级 transformers 到 5.5.3 并降级 lerobot 到 0.5.1（匹配 westd）
2. huggingface_hub 1.16.4 的 `@strict` decorator 导致 groot dataclass 失败 → 降级到 1.15.0
3. lerobot `__init__.py` 和 `factory.py` 中非必要 policy（eo1, groot 等）的 eager import 仍报错 → 用 try/except 包裹

评估第一条 pruning 诊断已输出：`attention: n_keep=243/256, score_range=[0.000002, 0.003847]`，确认 attention pruning k=0.95 + strict `if done:` 条件生效。10 tasks × 50 episodes × max 520 steps，预计运行数小时。

---
