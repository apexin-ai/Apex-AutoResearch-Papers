# research pi05 official eval

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_pi05-official-eval_20260522T092201_result.json`
- **Structured JSON:** [`b442dd8ba153f610b806.json`](../../sessions/b4/b442dd8ba153f610b806.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。以下是完整结果。

---

## π0.5 LIBERO 评估调研报告

### 1. π0.5 官方 repo / 发布渠道

| 渠道 | 链接 |
|------|------|
| OpenPI (Physical Intelligence 官方) | [github.com/Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) |
| lerobot HuggingFace 模型 (base) | [lerobot/pi05_libero_base](https://huggingface.co/lerobot/pi05_libero_base) |
| lerobot HuggingFace 模型 (finetuned) | [lerobot/pi05_libero_finetuned](https://huggingface.co/lerobot/pi05_libero_finetuned) |
| lerobot LIBERO fork | [huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero) |
| π0.5 论文 | [arXiv 2504.16054](https://arxiv.org/abs/2504.16054) |

### 2. LIBERO eval 脚本：**Yes，两套**

**方案 A — OpenPI 官方（server-client 架构）**

位于 [`examples/libero/`](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/README.md)：

```bash
# Terminal 1: 启动 policy server
uv run scripts/serve_policy.py --env LIBERO

# Terminal 2: 运行 LIBERO eval
MUJOCO_GL=glx python examples/libero/main.py
```

预训练 checkpoint: `gs://openpi-assets/checkpoints/pi05_libero/`

**方案 B — lerobot 统一 eval（推荐，更简洁）**

```bash
lerobot-eval \
  --policy.path=lerobot/pi05_libero_finetuned \
  --policy.n_action_steps=10 \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1 \
  --output_dir=./eval_logs/
```

标准 benchmark protocol: 每 task 10 episodes，4 个 suite 共 400 episodes。

### 3. 官方与社区报告的 LIBERO SR 数字

| 来源 | Spatial | Object | Goal | Long (10) | 备注 |
|------|---------|--------|------|-----------|------|
| **OpenPI 官方 finetuned** | 97.4% | 98.4% | 97.6% | 93.0% | [issue #734](https://github.com/Physical-Intelligence/openpi/issues/734) |
| **lerobot 官方 finetuned** | 98.8% | 98.2% | 98.0% | 92.4% | [lerobot docs](https://huggingface.co/docs/lerobot/pi05) |
| 社区复现 (issue #2114) | 77% | 66% | 89% | 55% | finetuned model, 远低于官方 |
| 社区复现 (issue #2533) | 0% | — | — | — | base model, 完全失败 |
| **我们的数字 (VLA-only)** | **84.2%** | **81.5%** | — | — | 与社区复现数量级一致 |

### 4. 关键发现与分析

**官方数字 vs 社区复现存在巨大差距（20-30%）**，这是已知问题：

- [lerobot issue #2114](https://github.com/huggingface/lerobot/issues/2114): "Fine-tuned π0 and π0.5 models fail to replicate reported success rates"
- [lerobot issue #2533](https://github.com/huggingface/lerobot/issues/2533): base model 零成功率
- [lerobot issue #2375](https://github.com/huggingface/lerobot/issues/2375): "Reproducing pi0.5 results on libero"

差距可能来源于：
- lerobot 的 finetuned checkpoint 是在 8×H100 上额外训练 6k steps 得到的特定版本
- 评估时的 action chunking 配置 (`n_action_steps=10`) 对结果敏感
- 环境版本和渲染后端差异
- LIBERO-PRO 论文 ([arXiv 2510.03827](https://arxiv.org/abs/2510.03827)) 直接指出官方数字反映的是 "rote recall rather than genuine task understanding"

### 5. 对我们论文的影响

**我们的数字（81.5% Object, 84.2% Spatial）是合理的**，与社区独立复现的数量级一致。论文中建议：

1. **引用 lerobot issue #2114** 作为复现困难的证据
2. **报告我们自己的 baseline** 而非抄官方数字，注明使用 `evaluate.py` 独立评估
3. **核心论点不变**：无论 VLA-only baseline 是 80% 还是 98%，conformal refinement 的增量改进都是有效的（因为是同 pipeline 对比）
4. 可以补充一句："Our VLA-only baselines are consistent with community reproduction results (lerobot issue #2114), which are 20-30% lower than the originally reported numbers."

### 6. lerobot 对 LIBERO 的支持情况

- **完整支持**：lerobot 原生集成 LIBERO，提供 `lerobot-eval` 统一评估命令
- **HuggingFace fork**：[huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero) 是 LIBERO 的官方 fork，简化了安装
- **支持的 suite**：libero_spatial, libero_object, libero_goal, libero_10 (即 LIBERO-Long)
- **支持的模型**：pi0, pi0.5, pi0-FAST, SmolVLA 等均可通过 `--policy.path` 指定

Sources:
- [OpenPI GitHub](https://github.com/Physical-Intelligence/openpi)
- [OpenPI LIBERO README](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/README.md)
- [lerobot LIBERO docs](https://huggingface.co/docs/lerobot/libero)
- [lerobot π0.5 docs](https://huggingface.co/docs/lerobot/pi05)
- [lerobot/pi05_libero_finetuned](https://huggingface.co/lerobot/pi05_libero_finetuned)
- [Issue #2114 - fail to replicate](https://github.com/huggingface/lerobot/issues/2114)
- [Issue #2533 - zero success rate](https://github.com/huggingface/lerobot/issues/2533)
- [Issue #734 - LIBERO-90 18%](https://github.com/Physical-Intelligence/openpi/issues/734)
- [LIBERO-PRO paper](https://arxiv.org/abs/2510.03827)
- [π0.5 paper](https://arxiv.org/abs/2504.16054)
- [huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero)

---
