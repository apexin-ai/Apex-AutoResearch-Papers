# d064 DocRED Full Beam Search — 状态报告
**时间**: 2026-05-19 20:50 CST | **服务器**: westd-21461 | **DDL**: 5/25

## 结论：实验正在运行，未失败

Registry 显示 DONE（可能是早期设置），但实际两条 GPU 流水线正在正常推理中。

---

## GPU & 进程状态

| GPU | 显存 | 利用率 | PID | 当前任务 |
|-----|------|--------|-----|---------|
| 0 (RTX PRO 6000 96GB) | 18.3GB / 97.9GB | 89% | 102892 | Llama greedy unconstrained |
| 1 (RTX PRO 6000 96GB) | 18.9GB / 97.9GB | 88% | 98185 | Qwen beam-4 unconstrained |

磁盘: 根分区 69% (9.6GB free), /root/autodl-tmp 71% (75GB free) — 无风险。

---

## 各步骤完成状态

### GPU 0 流水线 (Llama)

| # | 步骤 | 状态 | 进度 | 输出文件 |
|---|------|------|------|---------|
| 1 | LoRA Training (3 epochs) | ✅ DONE | 100% | checkpoints/llama_lora_docred_merged/ |
| 2 | Merge LoRA → Full Model | ✅ DONE | 100% | checkpoints/llama_lora_docred_merged/ |
| 3 | Greedy Unconstrained | 🔄 RUNNING | 554/998 (55%) | d064_llama_docred_greedy_unconstrained.jsonl |
| 4 | Greedy Constrained (S1) | ⏳ QUEUED | 0/998 | — |
| 5 | Beam-4 Unconstrained | ⏳ QUEUED | 0/998 | — |
| 6 | Beam-4 Constrained (S1) | ⏳ QUEUED | 0/998 | — |

训练指标: train_loss=0.057, eval_loss=0.062, eval_accuracy=98.07%, 3 epochs, ~90 min

### GPU 1 流水线 (Qwen)

| # | 步骤 | 状态 | 进度 | 输出文件 |
|---|------|------|------|---------|
| 1 | Beam-4 Unconstrained | 🔄 RUNNING | 620/998 (62%) | d064_qwen_docred_beam4_unconstrained.jsonl |
| 2 | Beam-4 Constrained (S1) | ⏳ WAITING | 0/998 | — (cascade 等 PID 98185 完成) |

---

## 预估完成时间

| 步骤 | 速率 | 剩余 | 预估耗时 | ETA |
|------|------|------|---------|-----|
| Llama greedy unc | ~14s/doc | 444 docs | ~1.7h | ~22:35 |
| Llama greedy con | ~14-20s/doc | 998 docs | ~3.9-5.5h | ~02:30-04:00 |
| Llama beam-4 unc | ~25-35s/doc | 998 docs | ~6.9-9.7h | ~09:30-14:00 |
| Llama beam-4 con | ~25-35s/doc | 998 docs | ~6.9-9.7h | ~16:30-23:00 (5/20) |
| **GPU 0 全部完成** | | | **~19-27h** | **5/20 16:00-23:00** |
| Qwen beam-4 unc | ~21.5s/doc | 378 docs | ~2.3h | ~23:10 |
| Qwen beam-4 con | ~21.5-30s/doc | 998 docs | ~6-8.3h | ~05:10-07:30 (5/20) |
| **GPU 1 全部完成** | | | **~8-10.3h** | **5/20 05:00-07:30** |

**瓶颈**: GPU 0 的 Llama 流水线（4个步骤串行）。最晚 5/20 23:00 完成，距 DDL 5/25 有 4+ 天余量。

---

## 部分评估指标（进行中数据，非最终结果）

| 配置 | N | Parse Fail% | ET% | RV% | DR% | CF% | E-F1 | R-F1 |
|------|---|-------------|-----|-----|-----|-----|------|------|
| Qwen beam-4 unc (620 docs) | 620 | 3.7% | 0.00 | 0.14 | 0.70 | 0.04 | 83.28 | 44.78 |
| Llama greedy unc (554 docs) | 554 | 4.5% | 0.00 | 0.29 | 0.27 | 0.13 | 83.43 | 44.97 |

**初步观察**:
- 两个模型 Entity F1 接近（~83%），Relation F1 也接近（~45%）
- 违约率极低：ET=0%, RV<0.3%, DR<0.7%, CF<0.15%
- Llama greedy 稍高的 parse fail（4.5% vs 3.7%）主要来自 max_new_tokens 截断（FAIL 样本耗时均 ~31s）
- 20个 Llama FAIL docs 和 16个 Qwen FAIL docs 集中在实体/关系较少的短文档

---

## Cascade 脚本

- GPU 0: `scripts/d064_gpu0_llama_all_with_greedy.sh` — 等训练PID完成 → greedy unc → greedy con → beam unc → beam con
- GPU 1: `scripts/d064_gpu1_qwen_con_fixed.sh` — 等 Qwen unc PID 完成 → beam con

---

## 无需重跑

所有步骤要么已完成要么正在运行/排队中。Cascade 脚本自动串联，无需人工干预。建议：
1. 不要触碰服务器，让流水线自然跑完
2. 5/20 上午检查 Qwen beam-4 con 是否完成
3. 5/20 晚检查 Llama 全部 4 步是否完成
4. 全部完成后用 `python scripts/eval_d064.py` 对 6 个 JSONL 运行最终评估
