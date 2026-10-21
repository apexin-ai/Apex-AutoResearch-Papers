# code exp 019 supervised verifier

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_019_supervised_verifier_20260515T100946_result.json`
- **Structured JSON:** [`090c7b1391eb93dab5eb.json`](../../sessions/09/090c7b1391eb93dab5eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实际上训练脚本不需要改——运行时在命令行设 `HF_HUB_OFFLINE=1` 即可。现在所有验证已通过：

**总结:**

1. **`train_supervised_verifier.py`** 已部署到 `autodl-5090:/root/autodl-tmp/struct_self_consist_ie/`
   - 5-fold GroupKFold CV（无 instance 泄露，每 fold ~110/440 val/train instances）
   - DeBERTa-v3-large 回归模型（435M params, ~1.7GB GPU）
   - 输入: `[CLS] sentence [SEP] Entities: ... Relations: ... [SEP]`
   - 标签: per-sample strict-match F1
   - 训练完成后输出 OOF predictions JSON + 快速 selection F1 摘要

2. **`evaluate_verifier.py`** 已部署
   - 计算 6 种方法的 selection F1 + Spearman ρ + AUROC
   - Supervised Verifier / LP / SJ / FK(LOO) / EM / VC
   - Greedy / Oracle / Random baselines

3. **验证通过:**
   - `--help` 正常
   - 数据加载: 551 instances × 8 = 4408 samples, NER F1 mean=0.5835
   - Fold 划分: 5 fold 无泄露, ~110 val instances each
   - Forward pass: token shape [4, 107], loss=0.5254, GPU 1.7GB

4. **DeBERTa-v3-large 已缓存**在 `/root/autodl-tmp/.hf_cache/`

**运行命令（待审批后执行）:**
```bash
cd /root/autodl-tmp/struct_self_consist_ie
export HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1
# NER
python train_supervised_verifier.py --data_path output/exp_012_rerun_1024/samples.jsonl --subtask ner --output_dir output/exp_019_supervised_verifier
# RE
python train_supervised_verifier.py --data_path output/exp_012_rerun_1024/samples.jsonl --subtask re --output_dir output/exp_019_supervised_verifier
```

---
