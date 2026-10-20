# figure fig r2 collapse v2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_fig_r2_collapse_v2_20260522T125718_result.json`
- **Structured JSON:** [`9c3142998e5aa85f5b99.json`](../../sessions/9c/9c3142998e5aa85f5b99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表已完成。总结：

**fig_r2_collapse 已更新**，包含 1×3 subplots：

| Subplot | 模型 | Trained Peak | Exit R² | Δ | NLP Baseline |
|---------|------|-------------|---------|------|-------------|
| OpenVLA (Llama-2-7B) | 32层 | 0.8693 (L10) | 0.8532 | 0.0161 | ✅ R²=0.155 灰色虚线 |
| TracVLA (Phi-3-mini) | 32层 | 0.8024 (L18) | 0.5741 | 0.2283 | — |
| NORA (Qwen2.5-VL-3B) | 36层 | 0.6875 (L9) | -0.0039 | 0.6914 | — |

每个 subplot 含蓝色实线(trained)、红色虚线(untrained)，OpenVLA subplot 加了 Llama-2-chat NLP control baseline (R²=0.155) 灰色点线。

文件位置（服务器 westd-19183）：
- PDF: `/root/autodl-tmp/vla-ssd/figures/fig_r2_collapse.pdf` (36KB)
- PNG: `/root/autodl-tmp/vla-ssd/figures/fig_r2_collapse.png` (285KB)
- 同步到: `/root/autodl-tmp/vla-ssd/docs/paper/figures/`
- 脚本: `/root/vla-ssd/scripts/gen_fig_r2_collapse_v2.py`

---
