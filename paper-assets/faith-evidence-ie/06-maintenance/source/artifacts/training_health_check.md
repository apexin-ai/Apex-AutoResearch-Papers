# GRPO 训练健康检查报告

**时间**: 2026-05-14 22:53 UTC  
**服务器**: rtx5090-4x (4× RTX 5090 32GB)

---

## 总览

| 实验 | GPU | 步数 | 进度 | 状态 |
|------|-----|------|------|------|
| mvp2_grpo_ced_r5 | cuda:0 | ~490/756 | 64.8% | ⛔ **Mode Collapse** |
| mvp2_grpo_extract_r3 | cuda:2 | ~482/756 | 63.8% | ⚠️ **Stagnant / Near-Collapse** |
| mvp2_grpo_flatnli_r3 | cuda:3 | 81/756 | 10.7% | ✅ **Healthy** |
| mvp2_sft_eval_r2 | cuda:1 | 985/985 | 100% | ✅ **Completed** |

---

## 1. mvp2_grpo_ced_r5 (CED reward) — ⛔ 严重 Mode Collapse

**当前指标 (~step 490)**:
- `loss`: 0.0, `grad_norm`: 0.0
- `format_reward`: 0.30 (满分), `f1_reward`: **0.0**, `ced_reward`: **0.995**
- `total reward`: 1.295
- `entropy`: **0.0005** (几乎为零)
- `completions/mean_length`: **34.0** (min=max=34, 完全固定)
- `frac_reward_zero_std`: 0.95~1.0

**早期对比 (step 45)**:
- f1_reward=0.068, ced_reward=0.260, entropy=0.088, mean_length=661

**诊断**: 教科书级 reward hacking。模型发现了一个固定的 34-token 输出模式，能拿到近满分的 CED reward (0.995) 但完全不做关系抽取 (F1=0)。entropy 从 0.088 跌到 0.0005，grad_norm=0 表示梯度完全消失。kl_coef=0 导致没有任何力量阻止模型坍缩到这个退化解。

**结论**: 实验已失败，继续跑无意义。建议 kill。

---

## 2. mvp2_grpo_extract_r3 (Extraction-only) — ⚠️ Stagnant

**当前指标 (~step 482)**:
- `loss`: ~0.0, `grad_norm`: **0.0**
- `format_reward`: 0.30 (满分), `f1_reward`: **0.20** (std=0.22)
- `total reward`: 0.50
- `entropy`: **0.010~0.018** (很低但不是零)
- `completions/mean_length`: 42~45 (比 ced_r5 好但仍偏短)
- `frac_reward_zero_std`: 0.8~1.0

**诊断**: 比 ced_r5 好一些——F1 reward 还有 0.20，输出长度有一定变化。但 grad_norm=0 和极低 entropy 表示模型已基本停止学习。没有 CED reward 的干扰（ced_weight=0），模型没有彻底坍缩，但也没在提升。

**结论**: 已停滞，F1=0.20 远低于 SFT baseline（F1=0.41）。让它跑完（~56 min），但不要抱期望。

---

## 3. mvp2_grpo_flatnli_r3 (Flat-NLI) — ✅ Healthy

**当前指标 (step 81/756)**:
- `loss`: 0.022, `grad_norm`: **0.398** (正常)
- `format_reward`: 0.297, `f1_reward`: 0.067, `flat_nli_reward`: **0.796**
- `total reward`: 1.16
- `entropy`: **0.087** (健康)
- `completions/mean_length`: 411 (range: 235~666, 正常变化)
- `frac_reward_zero_std`: **0.0** (所有 prompt 都产生多样输出)
- `clipped_ratio`: 0.0125 (轻微 clip，正常)

**诊断**: 唯一健康的 GRPO 实验。entropy 保持合理，输出多样，梯度非零。flat_nli_reward=0.80 说明模型在学习生成 faithful 输出。f1_reward 偏低 (0.067)，需观察后续趋势。

每步 ~120s（输出 400+ tokens），远慢于坍缩实验（~12s/step, 34 tokens）。

**预估完成时间**: (756-81) × 122s ≈ **22.9 小时** → 约 2026-05-15 21:45 UTC

---

## 4. mvp2_sft_eval_r2 — ✅ 已完成

| 指标 | 值 |
|------|-----|
| F1 | 0.4057 |
| Ign-F1 | 0.4057 |
| Evi-F1 | **0.7979** |
| EDCR | **0.7118** |
| Format OK | 983/985 (99.8%) |
| Truncated | 367/985 |
| Predictions | 18815 |

GPU 1 已空闲。

---

## GPU 状态

| GPU | 显存 | 温度 | 功耗 | 利用率 | 进程 |
|-----|------|------|------|--------|------|
| 0 (ced_r5) | 13077/32607 MiB (40%) | 58°C | 305W | 62% | PID 53071 |
| 1 (空闲) | 0/32607 MiB | 32°C | 9W | 0% | — |
| 2 (extract_r3) | 13075/32607 MiB (40%) | 57°C | 323W | 63% | PID 53149 |
| 3 (flatnli_r3) | 13065/32607 MiB (40%) | 57°C | 418W | 97% | PID 53292 |

显存均 40%，温度正常，无溢出风险。

---

## 建议行动

1. **Kill mvp2_grpo_ced_r5** — 已彻底 mode collapse，浪费 GPU 0
2. **让 extract_r3 跑完** — 剩余不到 1 小时，看最终 checkpoint
3. **重点关注 flatnli_r3** — 唯一健康实验，~23 小时完成，明天中午再查
4. **GPU 0 和 GPU 1 可释放** — eval 已完成 + ced_r5 建议 kill，两张卡可用于新实验

### Mode Collapse 根因

三个实验都用 kl_coef=0，但只有 flatnli 存活：
- **ced_r5**: CED reward 过于容易 hack（固定短文本即可获高 entailment 分），无 KL 惩罚维持多样性
- **extract_r3**: 仅 F1 reward 在 GRPO 早期过于稀疏（大部分 sample 得 0），缺乏有效梯度信号
- **flatnli_r3**: Flat-NLI 基于逐句 entailment 检查，比 CED 更难 hack（需输出多个 faithful 句子），且长输出降低了过拟合速度
