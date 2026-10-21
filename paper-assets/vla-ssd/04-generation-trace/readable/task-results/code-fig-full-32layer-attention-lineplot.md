# code fig full 32layer attention lineplot

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fig_full_32layer_attention_lineplot_20260517T073909_result.json`
- **Structured JSON:** [`0d4a25a8e2a3915d4b18.json`](../../sessions/0d/0d4a25a8e2a3915d4b18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PDF + PNG 已生成至 `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/attention/fig_full_32layer_attention.{pdf,png}`。

关键 pattern 总结：
- **VLA Trained**: L0-L1 峰值 (21, 24 heads) 标注 "entry routing"，L31 回升 (18 heads) 标注 "exit routing"，中间层低谷
- **Llama-2 Base**: L10-L16 区域高峰 (最高 22 heads) 标注 "mid-layer processing"，两端低
- **Untrained VLA**: 全零，mean attention 恒定 0.0778

脚本也已保存至服务器 `/root/vla-ssd/scripts/plot_full_32layer_attention.py`。

---
