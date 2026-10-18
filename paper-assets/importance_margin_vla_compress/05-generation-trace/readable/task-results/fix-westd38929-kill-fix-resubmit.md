# fix westd38929 kill fix resubmit

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd38929_kill_fix_resubmit_20260525T003914_result.json`
- **Structured JSON:** [`5a6dd713b8da97a0b48a.json`](../../sessions/5a/5a6dd713b8da97a0b48a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

## 执行总结

| Step | 状态 |
|------|------|
| **Kill 4 个旧实验** | 4 个 tmux session + GPU 进程全部 killed，registry 标记 `conclusion=killed` |
| **修改脚本** | `eval_openvla_l2norm_libero.py` 添加 `--model_path` 和 `--unnorm_key` 参数，`--help` 验证通过 |
| **重新提交 4 个实验** | 全部在运行中，模型加载正确 |

**注意**：模型路径与你指定的不同：
- 你指定的 `openvla-7b-finetuned-libero-goal/spatial` 不存在
- 实际使用 `/root/autodl-tmp/openvla-oft-libero-goal` 和 `openvla-oft-libero-spatial`
- unnorm_key 也相应修正为 `libero_goal_no_noops` 和 `libero_spatial_no_noops`（从 `dataset_statistics.json` 确认）

4 个实验已在正确加载模型并运行：
- GPU0: `Loading OpenVLA from: /root/autodl-tmp/openvla-oft-libero-goal` (random k=0.9)
- GPU1: `Loading OpenVLA from: /root/autodl-tmp/openvla-oft-libero-spatial` (random k=0.9)
- GPU2: `Loading OpenVLA from: /root/autodl-tmp/openvla-oft-libero-goal` (attn k=0.85)
- GPU3: `Loading OpenVLA from: /root/autodl-tmp/openvla-oft-libero-spatial` (attn k=0.85)

---
