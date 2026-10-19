# doc phase0 experiment spec

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_doc_phase0-experiment-spec_20260515T110032_result.json`
- **Structured JSON:** [`b106a58c58f2b4a117a4.json`](../../sessions/b1/b106a58c58f2b4a117a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 不在当前可用工具列表中，无法自动注册。文档已写入：

**`/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/meta_brain_lora_routing/artifacts/phase0_experiment_spec.md`**

覆盖内容：
1. **实验目标** — early-kill gate 定位，GO/NO-GO 逻辑
2. **扰动 Taxonomy** — 7→3 映射表 + 排除 Language 的理由 + Visual 类内方差风险分析
3. **模型架构** — π₀ 双 Transformer 参数 + 修正后的 12 层提取方案 + 2-layer MLP 分类器
4. **数据收集** — 580 episodes 分布 + 4 种 pooling 全存储 (~5.4 GB)
5. **评估 Protocol** — 3-class (主) / 6-class (对照) / binary (sanity check) + per-layer breakdown / activation source 对比 / pooling 对比 / t-SNE 可视化
6. **Hyperparameter Sweep** — 27 configs × 3 modes × 5-fold = 405 runs
7. **GO/NO-GO 判据** — 5 档判定 (GO/AUGMENT/RETHINK/PIVOT/信息) + chance-level 参考
8. **资源预算** — ~20 H100-hrs, 2-4 天墙钟
9. **风险与缓解** — 8 项风险 + 缓解方案
10. **附录** — SAFE 对比 / 已有代码基础 / π₀ baseline 参考值

`register_artifact` 需要你手动执行或等该工具可用后补注册。

---
