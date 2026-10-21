# 服务器审计报告：bjb2-12179

**日期**：2026-05-23

## GPU 信息

- **型号**：NVIDIA GeForce RTX 5090
- **数量**：8 张（8 个 PCIe 设备）
- **显存**：32GB/卡（RTX 5090 规格）
- **当前使用状态**：nvidia-smi 权限被拒（Permission denied），无法查看实时 GPU 占用和进程

## 磁盘使用

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| /dev/md0 (/root/autodl-tmp) | 250G | 208G | 43G | 83% |

### 大类占用明细

| 类别 | 大小 | 说明 |
|------|------|------|
| **基座模型 (models/)** | **70G** | Qwen3-14B (28G), Qwen3-8B (16G), Meta-Llama-3.1-8B (15G), Qwen3-4B (7.6G), Qwen3-1.7B (3.8G) |
| **SFT checkpoints** | **57G** | 16 个 SFT 输出目录（含 no_evidence、多 seed、多模型） |
| **RejSFT checkpoints** | **65G** | 14 个 RSFT 输出目录（含多模型、多 seed、k1、nli_large、ced） |
| **GRPO checkpoint** | **3.5G** | grpo_bf16_g4/ |
| **Baselines** | **3.0G** | baselines/ |
| **SFT no_evidence** | **2.1G** | sft_no_evidence_output/ |
| **HF cache** | **2.4G** | .hf_cache/ |
| **RSFT 中间产物** | **~1.5G** | scored/filtered/generations/candidates 等 |
| **Eval 结果** | **0.4G** | eval_results/ + eval_outputs/ |
| **数据集** | **0.5G** | data/ |
| **项目代码 (freige/)** | **587M** | 代码 + 配置 + 训练脚本 |
| **杂项** | **~2G** | 日志、分析脚本、figures、artifacts 等 |

**合计约 208G**

## 本项目 (faith-evidence-ie / freige) 相关内容

`/root/autodl-tmp/freige/` 存在，587MB，包含完整项目代码：
- `configs/` — 训练/评估配置
- `training/` — 训练代码
- `eval/` — 评估代码
- `scripts/` — 运行脚本
- `data/` — 数据处理
- `rewards/` — 奖励模型
- `outputs/` — 输出
- `logs/` — 日志

项目相关的 **所有实验产物都在 /root/autodl-tmp/ 下**：
- 5 个基座模型权重（70G）
- 30+ 个训练 checkpoint 目录（SFT + RSFT + GRPO，共约 128G）
- 评估结果（0.4G）
- RSFT 中间数据（scored/filtered/generations，约 1.5G）

## 总结

| 项目 | 状态 |
|------|------|
| GPU | 8× RTX 5090，无法确认是否有活跃进程（nvidia-smi 无权限） |
| 磁盘 | 83% 已用，仅剩 43G 可用 |
| 内容 | **全部为 faith-evidence-ie 项目产物**——基座模型、训练 checkpoint、评估结果 |
| 后续用途 | 取决于实验是否已全部完成。若论文已投稿且不再需要补实验，checkpoint 和基座模型可释放，可回收约 200G |
| 释放建议 | ① 确认所有实验结果已同步到本地/artifacts 后，可清理 checkpoint 目录；② 基座模型可在需要时重新下载，优先清理；③ eval_results 和 rsft_scored 等中间产物体积小，可最后处理 |
