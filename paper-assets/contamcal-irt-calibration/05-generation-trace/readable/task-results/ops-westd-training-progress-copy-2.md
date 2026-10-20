# ops westd training progress

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-training-progress_20260519T223906_result.json`
- **Structured JSON:** [`0348f0b4860245394548.json`](../../sessions/03/0348f0b4860245394548.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All s42 checkpoints (d000 + d100) exist on westd for Phi-4, Gemma-2, OLMo-2, and Qwen-14B. All GSM8K s123 scripts are hardcoded to `CUDA_VISIBLE_DEVICES=0` — they'll need modification for parallel execution on multiple GPUs.

Now let me compile the full report.

---

## 训练进度报告（CST 时间，~07:00 查询）

| GPU | 当前模型 | 当前 dosage | 进度 | 速度 | 剩余 dosage | 预计完成 |
|-----|---------|-------------|------|------|------------|---------|
| **cuda:0** | Phi-4 | d100 (5/5) | 78/4159 (2%) | ~2.2s/it | 无 | **~09:00** |
| **cuda:1** | Qwen-14B | d050 (4/5) | 635/3642 (17%) | ~3.0s/it | d100 | **~12:00** |
| **cuda:2** | OLMo-2 (Qwen-7B 已完成) | d100 (5/5) | 3763/4159 (90%) | ~1.7s/it | 无 | **~07:15** |
| **cuda:3** | Gemma-2 | d050 (4/5) | 1198/3642 (33%) | ~2.8s/it | d100 | **~11:30** |

### 各 GPU 的 per-dosage 训练用时参考
- **Phi-4**: ~2h10-2h20m/dosage
- **Qwen-14B**: ~2h45-2h55m/dosage
- **OLMo-2/Qwen-7B**: ~1h45-1h55m/dosage
- **Gemma-2**: ~2h36-2h46m/dosage

---

## GSM8K 脚本就绪状态

**s123 GSM8K 脚本**: 5 个全部就绪（`scripts/gsm8k_s123/`），覆盖 phi4/gemma2/qwen14b/qwen7b/olmo2。每个脚本 eval d000+d100，含 C009 md5 校验。

**s42 GSM8K 脚本**: **不存在**，需要创建。

**s42 checkpoints on westd**: Phi-4/Gemma-2/OLMo-2/Qwen-14B 的 d000+d100 全部就绪。Qwen-7B 的 s42 可在 cqa1 跑。

**注意**: 所有 s123 GSM8K 脚本都硬编码了 `CUDA_VISIBLE_DEVICES=0`，并行执行需要修改。GSM8K 结果目录（`results/gsm8k/`）尚不存在。

---

## 建议任务链

### cuda:2（最先空闲，~07:15）
1. **07:15** → GSM8K s42 eval: OLMo-2 d000+d100（~30min，需创建脚本，CUDA=2）
2. **07:45** → GSM8K s123 eval: OLMo-2 d000+d100（~30min，修改现有脚本 CUDA=2）
3. **08:15** → GSM8K s42 eval: Qwen-7B d000+d100（如果 cqa1 不跑的话）
4. **08:45** → 开始 s0 训练（Qwen-7B + OLMo-2 sweep，同 s123 的组合模式）

### cuda:0（~09:00 空闲）
1. **09:00** → GSM8K s42 eval: Phi-4 d000+d100（~30min，CUDA=0）
2. **09:30** → GSM8K s123 eval: Phi-4 d000+d100（~30min）
3. **10:00** → 开始 Phi-4 s0 训练

### cuda:3（~11:30 空闲）
1. **11:30** → GSM8K s42 eval: Gemma-2 d000+d100（~30min，CUDA=3）
2. **12:00** → GSM8K s123 eval: Gemma-2 d000+d100（~30min）
3. **12:30** → 开始 Gemma-2 s0 训练

### cuda:1（~12:00 空闲）
1. **12:00** → GSM8K s42 eval: Qwen-14B d000+d100（~45min，14B 模型较慢，CUDA=1）
2. **12:45** → GSM8K s123 eval: Qwen-14B d000+d100（~45min）
3. **13:30** → 开始 Qwen-14B s0 训练

### 待办
1. 创建 s42 GSM8K eval 脚本（5 个 family，参照 s123 脚本结构，改 checkpoint 路径和 CUDA 分配）
2. 修改 s123 GSM8K 脚本的 CUDA_VISIBLE_DEVICES，使其可在对应 GPU 上运行
3. cuda:2 即将空闲（~15min），是否现在就准备 OLMo-2 的 s42 GSM8K 脚本？

---
