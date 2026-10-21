# code gen cross inst heatmap

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gen_cross_inst_heatmap_20260517T043900_result.json`
- **Structured JSON:** [`fd7cd22d6bedbcf439d4.json`](../../sessions/fd/fd7cd22d6bedbcf439d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PDF 已成功传输到本地。图表数据和布局正确：

- **Trained last_preaction**: L0=10, L1-L31 全部 100（训练后 action token 完美编码指令信息）
- **Untrained last_preaction**: L0=10, L1=100, L4=100, 从 L8 开始逐渐下降 98→92→86→82（未训练模型高层逐渐丢失指令区分度）
- **Trained image_mean / DINOv2**: 全部 10（chance level，视觉 token 不编码指令信息）

文件位置：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/fig2_cross_instruction_heatmap.pdf`（22,895 bytes）

服务器端副本：`/root/autodl-tmp/vla-ssd/results/cross_instruction/fig2_cross_instruction_heatmap.pdf` + `.png`

---
