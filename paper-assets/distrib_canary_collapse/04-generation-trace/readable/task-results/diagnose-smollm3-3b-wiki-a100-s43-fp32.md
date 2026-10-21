# diagnose smollm3 3b wiki a100 s43 fp32

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_smollm3_3b_wiki_a100_s43_fp32_20260519T232437_result.json`
- **Structured JSON:** [`79169ae0ade4d3a2b15b.json`](../../sessions/79/79169ae0ade4d3a2b15b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**失败原因**：磁盘满（`No space left on device`）。数据盘 250GB 已 100% 占满。

**失败阶段**：gen_2 训练 5000 步已全部完成，但在 `save_pretrained` 写 safetensors 时失败。训练本身没有问题。

**完成情况**：
- gen_0, gen_1：完整
- gen_2：训练完成但 checkpoint 截断（5.36GB vs 期望 12.3GB），不可用
- gen_3~gen_9：未开始（共需 10 generations）

**磁盘占用大户**：`results/generalize/` 共 137GB，其中 `pythia14b_wiki_a100_s43` 占 53GB，`smollm3_3b_wiki_a100_s42_fp32_v3` 占 24GB。

**修复方案**：清理不再需要的实验结果释放空间 → 删除 gen_2 损坏目录 → 从 `start_gen=2` 重跑。剩余 7 个 generation 至少需要 ~84GB 空间。

报告已写入 `artifacts/smollm3_3b_wiki_a100_s43_fp32/diagnose.md`。

---
