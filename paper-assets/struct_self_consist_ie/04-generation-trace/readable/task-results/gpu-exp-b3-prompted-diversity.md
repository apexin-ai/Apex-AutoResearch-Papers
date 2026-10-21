# gpu exp b3 prompted diversity

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_exp_b3_prompted_diversity_20260520T172625_result.json`
- **Structured JSON:** [`f8005b679e86f20a629c.json`](../../sessions/f8/f8005b679e86f20a629c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态已为 PENDING，spec 已更新。准备完成，汇总如下：

---

**exp_b3_prompted_diversity 准备就绪**

| 项目 | 状态 |
|------|------|
| 代码 | `/root/autodl-tmp/struct_self_consist_ie/code/exp_b3_prompted_diversity.py` (581行，与本地一致) |
| 数据 | `/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json` (37648行，取前3000条有实体的) |
| 模型 | `checkpoints/qwen3-8b-fewnerd-exp021-merged` ✓ |
| 依赖 | vLLM + xgrammar 已安装 (conda base, Python 3.12) |
| GPU | cuda:3 空闲 (0 MiB / 32607 MiB) |
| Registry | PENDING, spec 已写入 |

**运行命令：**
```bash
CUDA_VISIBLE_DEVICES=3 python /root/autodl-tmp/struct_self_consist_ie/code/exp_b3_prompted_diversity.py --phase both --num_instances 3000 --seed 42
```

**注意事项：**
- seed 改为 42（代码默认 123），与 spec 一致
- `CUDA_VISIBLE_DEVICES=3` 让脚本内 cuda:0 映射到物理 GPU 3
- 预计时长 2-4h（vLLM batch inference: greedy 1轮 + single 8 samples + multi 4×2 = 共 17 轮推理，3000 instances）
- 输出目录：`/root/autodl-tmp/struct_self_consist_ie/output/exp_b3_prompted_diversity/`
- Prior run conclusion: negative (cross_template_jaccard=0.67, multi strictly worse)

---
