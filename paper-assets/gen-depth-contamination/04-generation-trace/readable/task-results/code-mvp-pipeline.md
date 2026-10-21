# code mvp pipeline

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp_pipeline_20260512T111111_result.json`
- **Structured JSON:** [`658b004eb3acbe14f4bf.json`](../../sessions/65/658b004eb3acbe14f4bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

SSH 仍不可用。代码已在本地就绪，等 SSH 恢复后部署。

---

**产出报告：**

1. **代码文件**：`scripts/run_pipeline.py`，619 行
2. **Dry-run 验证**：AST 语法检查通过，argparse 配置验证通过。完整 import 验证需在服务器上执行（本地 Python 3.14 的 scipy/mock torch 冲突，非代码问题）
3. **预估运行时间（4090D 24GB）**：
   - Step 2（C4 采样）：~5 min（网络下载为主）
   - Step 3（5轮 × 5000条生成，batch=16）：~3-4 小时（每轮约 40-50 min，Qwen2.5-1.5B fp16 在 4090D 上约 50-80 tokens/s batch）
   - Step 4（surprisal 提取 30000条，batch=8）：~1.5-2 小时；vocab diversity + self-BLEU：~30 min
   - Step 5（LightGBM 分析）：< 5 min
   - **总计：约 5-7 小时**
4. **注意事项**：
   - 生成阶段 batch_size=16 在 24GB 4090D 上应该可行（1.5B fp16 ≈ 3GB，KV cache + batch ≈ 10-15GB）。如果 OOM，降到 `--batch_size 8`
   - 特征提取的 surprisal batch 保留了完整 logits（vocab_size=151k），`--feat_batch_size 8` 是保守值。如果 OOM 降到 4
   - Self-BLEU 仅对 200 条采样计算，其余为 NaN（分析时用列均值填充）
   - 每步都有断点续传，pipeline 中断后可直接重跑
   - **SSH 当前不可用**，AutoDL 实例可能已重启——需确认新端口后更新 `~/.ssh/config`

---
