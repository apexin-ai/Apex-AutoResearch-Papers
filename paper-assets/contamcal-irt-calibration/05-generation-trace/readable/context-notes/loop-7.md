# director / loop_7.md

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_7.md`
- **Structured JSON:** [`4e2f199657f852c4a90e.json`](../../sessions/4e/4e2f199657f852c4a90e.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: max_messages
updated: '2026-05-15T10:43:42+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 只能用 cuda:0-5（cqa1-21977 项目分配），不得越界
- `train_sft.py` 已移除 `--gpu` 参数，提交 SFT 必须用 `CUDA_VISIBLE_DEVICES=N`，绝不用 `--gpu N`
- `--model-name` 必须用本地路径 `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-{size}`，不用 HF hub 格式（AutoDL 无外网）
- Registry API `update_registry` 有回写 bug——不会写入 YAML 文件。必须**直接编辑 registry.yaml 文件**才能持久化状态变更
- 0.5B MMLU/ARC 数据已排除出 IRT pooling（D045，position bias confound），只保留 GSM8K/HumanEval
- 3B d000 GSM8K 已排除出 IRT（D018，LoRA 超参损伤导致 11-26%）
- `get_project_resource_usage` 工具 GPU 状态误报严重（C002），判断 GPU 占用必须用 `nvidia-smi`

### 2. 🖥️ 基础设施快照
- 服务器：cqa1-21977 (connect.cqa1.seetacloud.com)，6× RTX 4090D
- 工作目录：`/root/contamcal-irt-calibration`
- Python：`/root/miniconda3/bin/python`（conda base env，不用 venv）
- HF cache：`/root/autodl-tmp/.hf_cache/`
- Checkpoints：`/root/autodl-tmp/exp001/checkpoints/`
- Eval 输出：`/root/autodl-tmp/exp001/eval_results/`
- Stan 模型：`/root/contamcal-irt-calibration/stan_models/`
- TMPDIR for Stan：`/root/autodl-tmp/tmp_sim`（根分区 30GB 会满，Stan 必须用数据盘）
- 活跃进程（handoff 时刻）：
  - cuda:0: 1.5B d025 s123 SFT v3 (PID 533174)，~ETA UTC 18:45
  - cuda:3: 1.5B d005 s123 SFT v4 (PID 534536)，~ETA UTC 18:50
  - cuda:1: 空闲，Agent 在找合适任务
  - cuda:2: 0.5B base pretrained eval (PID 530893)
  - cuda:4: 1.5B base pretrained eval (PID 530975)
  - cuda:5: 1.5B d000 s123 eval — 刚完成，待 registry 更新
  - CPU: extreme gamma sweep (PID 528993)，80 runs，~2/80 done，ETA ~UTC 23:00+
  - CPU: 2PL full pipeline 重跑刚派出（matched 4000 draws，coverage 对比）

### 3. 📊 当前状态
**刚做完**：
- 2PL joint_fit.py bug 修复（4处）+ Reviewer PASS
- 2PL vs 4PL 消融对比：gamma 点估计一致(~0.14)，2PL 严格优于 4PL（CI 窄 45%，MAE 低 77%），但两者 CI 均含零（N=8 功效不足）
- 3B eval 全部完成（d000/d025/d100，两个 seed）
- 0.5B d000 s123 eval 完成，0.5B d005 s123 eval 数据已存在
- 极端 gamma sweep 启动（2/80），首批结果支持假说 A（model misspecification 而非极端 gamma 问题）
- D039-D045 系列决策已记录

**RUNNING/PREPARING**：
- 1.5B d025 s123 SFT v3 (cuda:0) — seed=123 N 扩展
- 1.5B d005 s123 SFT v4 (cuda:3) — seed=123 N 扩展
- 0.5B base pretrained eval (cuda:2) — SFT tax 量化 + exp008
- 1.5B base pretrained eval (cuda:4) — SFT tax 量化 + exp008
- extreme gamma sweep (CPU) — 隔离 model misspec vs extreme gamma
- 2PL full pipeline (CPU) — coverage 对比，刚派出

**等待**：
- Agent 队列深度 ~3，在处理 2PL pipeline 指令 + GPU 1 调度 + d100 s123 eval 提交
- 1.5B d000 s123 eval 完成待 registry 更新
- SFT 完成后 → 对应 eval → pooled IRT N 扩展

### 4. 📋 待办（条件触发式）
- 1.5B d025/d005 SFT 完成 → 立即提交对应 aligned eval → 完成后 pooled IRT N ≥ 16
- base pretrained eval (0.5B/1.5B) 完成 → 汇报 raw vs d000 SFT tax 分解，更新 D043/D044 分析
- extreme gamma sweep 完成 → gamma ∈ {0.5, 2.0, 4.0} coverage 对比，确认 model misspecification 结论
- 2PL full pipeline 完成 → 2PL vs 4PL coverage 对比，如果 2PL coverage 显著优于 4PL → model selection 的强证据
- N ≥ 16 pooled IRT 完成 → 检查 coverage 是否改善 → 决定 model misspecification 修复路径
- exp008 base pretrained 数据到手 → 完成 base→SFT→Instruct 三阶段信号比较
- GPU 空出 → 按优先级填：seed=123 eval 缺口 > 3B signal (exp-002) > exp-014 multi-family

### 5. 🎯 战略上下文
**投稿目标**：EMNLP 2026 ARR May 25（还剩 10 天）

**核心结论链**（D035-D045）：
- D038/D039: Paper framing pivot 到 characterization-first。Core claims 重排：(1) characterization (2) signal failure (3) identifiability (4) conditional calibration (demoted)
- D036/D042: Coverage collapse 20-33% 是 model misspecification（非小 N）。极端 gamma sweep 初步支持
- D040: exp008 S2 Min-K++ RL-robust (d=0.01) 是 Claim 2 headline finding
- D043: gamma 语义包含 SFT tax（d000 counterfactual 膨胀 ~2.8x）
- D044: Format confound — 生成任务 gamma 还包含 data composition effect
- D045: 0.5B MC eval 不可靠（position bias A=46→98%），已排除

**最易判断错的事**：
- Registry YAML 必须直接编辑文件，API 不回写（本 session 踩了 4 次）
- Worker 连续 status=done 但无持久效果是常态，关键更新必须让 Agent 自己做不派 Worker
- 0.5B 数据看起来"contamination 反而降低准确率"——这是 position bias + SFT capacity 问题，不是方法失败
- GSM8K/HumanEval 的 gamma 包含 format forgetting 成分（d000 不含格式数据），论文必须明确讨论
- 3B d000 GSM8K 跨种子方差大（s42=12% vs s123=27%），是 v1/v2 超参版本混淆，非纯种子方差


---
