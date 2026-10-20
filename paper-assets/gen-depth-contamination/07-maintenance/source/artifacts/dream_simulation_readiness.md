# Dream Simulation Readiness Report

> Generated: 2026-05-19

## Part 1: Registry RUNNING Experiments Status

### 5 RUNNING Experiments

| exp_id | server | gpu | pid | command | data_path | model_name | seed | 完整性 |
|--------|--------|-----|-----|---------|-----------|------------|------|--------|
| exp_pythia_retrain_depth7 | cqa1-22115 | ❌ missing | ❌ missing | ✅ | ✅ | ✅ pythia-1.4b | ✅ 42 | **缺 gpu, pid** |
| exp_code_qwen7b | cqa1-22115 | ✅ cuda:1 | ✅ 114228 | ✅ | ✅ | ✅ Qwen2.5-7B | ✅ 42 | 完整 |
| exp_code_mistral7b | cqa1-22115 | ✅ cuda:3 | ✅ 107037 | ✅ | ✅ | ✅ Mistral-7B-v0.3 | ✅ 42 | 完整 |
| exp_code_llama8b | cqa1-22115 | ✅ cuda:2 | ✅ 96335 | ✅ | ✅ | ✅ LLaMA-3.1-8B | ✅ 42 | 完整 |
| exp_32b_c4 | westd-42896 | ✅ cuda:1 | ✅ 44715 | ✅ | ❌ missing | ❌ missing | ❌ missing | **缺 data_path, model_name, seed** |

### 缺失字段汇总

1. **exp_pythia_retrain_depth7**: 缺 `gpu`, `pid`（实验已 RUNNING 但 spec 未记录 GPU 分配和进程 ID）
2. **exp_32b_c4**: 缺 `data_path`, `model_name`, `seed`（从 hypothesis 可知 model=Qwen2.5-32B, 但 spec 未记录）

### exp_pythia_retrain_depth7 状态确认
- 当前状态: **RUNNING** ✅（符合预期，无需更新）

---

## Part 2: Dream Simulation 前置检查

### 2.1 paper_framing.md 检查

- **4 域 K* 值**: arXiv=3, C4=2, Code=2, Wiki=1 ✅ 已更新
- **Dream simulation 相关 claim**: 无。paper_framing.md 中无直接提及 dream simulation 的 claim 或 section
- domain ceiling 阶梯已明确写入 C1' claim

### 2.2 experiment_plan.yaml 检查

- **无独立 dream simulation 计划条目**
- 仅在 exp-006 和 exp-007 的 description 中出现 `[Dream 行动项]` 标注（指已完成实验的后续分析）
- ROADMAP.md 中列为待做任务: "Dream simulation (Code cross-model 结果后)"
- **需要创建**: experiment_plan.yaml 中需要新增 dream simulation 的正式条目

### 2.3 数据可用性（Qwen2.5-1.5B features.csv）

| Domain | 源实验 | data_path | features.csv 确认 |
|--------|--------|-----------|-------------------|
| **C4** | exp_016_base_vs_instruct | `/root/autodl-tmp/gen-depth-contamination/data_exp016_qwen_base/features.csv` | ✅ 在 registry 中被 exp_028 引用 |
| **arXiv** | exp_024_arxiv_domain | `data/exp_024_arxiv/` | ⚠️ 未在 registry 中显式确认，需文件系统验证 |
| **Code** | exp_code_qwen1b5 | `data/exp_code_qwen1b5/` | ⚠️ 未在 registry 中显式确认，需文件系统验证 |
| **Wikipedia** | exp_023_domain_ablation | `data/exp_023_wiki/` | ⚠️ 未在 registry 中显式确认，需文件系统验证 |

### 2.4 结论: Dream Simulation 能否现在发起？

**不能立即发起。** 缺少以下条件:

1. **数据验证未完成**: 4 域中仅 C4 的 features.csv 路径在 registry 中被确认引用。arXiv/Code/Wiki 三域需要 SSH 到服务器确认文件存在
2. **无正式实验计划**: experiment_plan.yaml 中无 dream simulation 条目，需要定义:
   - 模拟的具体内容（不同 domain K* 组合下的检测效果）
   - 输入数据路径
   - 输出指标定义
   - 与论文 claim 的映射关系
3. **Code cross-model 结果未出**: ROADMAP 明确标注 "Code cross-model 结果后" 才做 dream simulation。当前 3 个 Code 实验 (LLaMA/Mistral/Qwen-7B) 仍在 RUNNING

### 下一步行动

1. SSH 验证 arXiv/Code/Wiki 三域的 features.csv 文件是否存在
2. 等待 Code cross-model 实验完成（预计 May 19 12:00-18:00 UTC）
3. 在 experiment_plan.yaml 中创建 dream simulation 条目
4. 补全 exp_pythia_retrain_depth7 和 exp_32b_c4 的缺失 spec 字段
