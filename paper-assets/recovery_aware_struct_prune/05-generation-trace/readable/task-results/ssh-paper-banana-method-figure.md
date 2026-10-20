# ssh paper banana method figure

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_paper_banana_method_figure_20260523T154754_result.json`
- **Structured JSON:** [`07f619466f94cf02e988.json`](../../sessions/07/07f619466f94cf02e988.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报结果：

### 结果

1. **连通性测试**: `http://47.94.22.126/v1` 返回 200，可用。但该代理**仅支持 OpenAI 文本模型**（gpt-4o 等），不支持 `/images/generations` 端点和 image modality。

2. **paperbanana 自定义 base_url**: 原生不支持。修改了两个 provider 源码（`openrouter.py` 和 `openrouter_imagen.py`）支持 `OPENROUTER_BASE_URL` 环境变量。同时修改了 `visualizer.py`，让 methodology 模式改用 VLM 生成 matplotlib 代码（而非调图片生成 API）。

3. **生成结果**:
   - PNG: `/root/recovery_aware_struct_prune/docs/paper/figures/paper/fig1_method_framework.png` (276KB, 4295×1745px, 300DPI, ~14.3×5.8 inches)
   - PDF: `/root/recovery_aware_struct_prune/docs/paper/figures/paper/fig1_method_framework.pdf` (57KB)
   - 生成脚本: `/root/recovery_aware_struct_prune/scripts/gen_fig1_framework.py`

4. **说明**: 第一轮 paperbanana 自动生成的 matplotlib 代码质量差（文字重叠、布局粗糙），且 critic 因无法读取图片而误判 "publication-ready"。最终由手写 matplotlib 脚本生成，包含三阶段流程、公式、28 层剪枝可视化、SFT/GRPO 收敛、Recovery Capacity Spectrum 梯度条。

---
