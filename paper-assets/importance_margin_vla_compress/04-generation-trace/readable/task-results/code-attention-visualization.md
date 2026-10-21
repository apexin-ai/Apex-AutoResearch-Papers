# code attention visualization

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_attention_visualization_20260517T100421_result.json`
- **Structured JSON:** [`54f4117cb5fde2fcef84.json`](../../sessions/54/54f4117cb5fde2fcef84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已就绪。总结：

**`analyze_attention.py`** (602 行) 已部署到 `westd-27271:/root/autodl-tmp/importance_margin_vla_compress/`

**工作原理：**
1. 加载 Full FT baseline checkpoint (`checkpoints/libero_full_ft_100k/checkpoint.pt`)
2. Monkey-patch `SmolVLMWithExpertModel.eager_attention_forward` 捕获 softmax attention probs
3. 在 3 个 libero_object tasks (0, 3, 7) 上各跑 1 episode
4. 每次 `predict_actions` 调用时，capture 所有 denoise step 的 attention weights（通过 `q_len == 50` 过滤）
5. 提取 action tokens → vision tokens (0:128) 的 attention，平均 over action tokens

**输出到 `artifacts/`：**
- `attention_heatmap.pdf/png` — X=vision token (0-127), Y=layer call, color=attention weight；标注 cam1/cam2 边界
- `attention_distribution.pdf/png` — 4 panel: per-token bar chart, entropy histogram, camera-wise split, per-head entropy
- `attention_per_task.pdf/png` — 跨 task 对比
- `attention_data.npz` — raw attention data (per-call, per-task)
- `attention_metadata.json` — 模型信息 + entropy/uniformity 统计

**关键架构信息（已验证）：**
- VLM: 15 attention heads, 5 KV heads (GQA groups=3), 16 layers, head_dim=64
- Expert: 720-dim hidden, q_proj maps 720→960 (15 heads)，与 VLM 共用 GQA 结构
- Vision tokens: 64/camera × 2 cameras = 128，位于 prefix 的 positions 0-127
- `attention_mode=cross_attn`，偶数层 self-attn，奇数层 cross-attn

**运行命令（等 GPU 空闲后）：**
```bash
cd /root/autodl-tmp/importance_margin_vla_compress
python analyze_attention.py --gpu 0
```

---
