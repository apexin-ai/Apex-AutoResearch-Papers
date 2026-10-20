---
loop: 26
reason: max_wall_time
updated: '2026-05-25T07:04:03+00:00'
---

### 1. 🔴 硬约束 / 红线
- 服务器 `seetacloud-westd-4x5090` 只有 4 张 5090（cuda:0/1/2/3），全部在白名单内，无越界风险
- CWM reeval 的 ckpt-300 @ seq2048 数据 **不可** 与 Table 2 对比（三重 confound：seq2048 vs seq8192, max_new_tokens 1024 vs 512, ckpt-300 vs ckpt-400/6633）。之前 Director 决策 "seq2048 不入论文"
- 论文已提交 ARR，Table 2 CWM 8B 值固定为 66.48 ± 1.15（3 seeds @ seq8192）。后续 eval 数据仅作 author response 储备
- Abstract ≤ 200 words（当前 ~173 words），Limitations 只在正文有一个 section

### 2. 🖥️ 基础设施快照
- 服务器：`seetacloud-westd-4x5090`，工作目录 `/home/sonny/exec-sim-repair-verifier`
- Python：`/root/miniconda3/bin/python`（conda base 环境）
- 模型路径：`/root/autodl-tmp/models/Qwen/Qwen3-8B`，14B 在 `/dev/shm/Qwen3-14B`（tmpfs）或 `/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B`
- Checkpoint 路径模式：`/root/autodl-tmp/checkpoints_repo_cwm_8b_s{seed}/` 或 `checkpoints_repo_cwm_8b_conda/`（s42 原始训练）
- Eval 结果：`/root/autodl-tmp/eval_results/`
- 本地 workspace：`/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/`
- 论文源码：`docs/paper/`（main.tex, abstract.tex, experiments.tex, appendix.tex 等）
- 无活跃 W&B（实验用 `WANDB_MODE=offline`）
- 活跃进程（截至 May 25 00:05 UTC）：
  - PID 328069: ckpt-6100 @ seq8192 eval（GPU 3, CUDA_VISIBLE_DEVICES=3），97.8% 完成，running acc 70.2%
  - PID 309505/309866/312223: 3× ckpt-300 reeval **已完成**（结果已写入各自 output_dir）

### 3. 📊 当前状态
我刚完成 3 个 ckpt-300 @ seq2048 reeval 的结果收集（s42: 68.20%, s456: 66.09%, s123: 63.91%），已报告 Director。

**唯一仍在运行的 eval**：ckpt-6100 @ seq8192（PID 328069），9564/9784 (97.8%)，running acc 70.2%。预计 May 25 ~00:20 UTC 完成。

Registry 中无 RUNNING/PREPARING 实验（这些 reeval 未被注册到 registry——是 Agent 直接 nohup 启动的探索性 eval）。

论文状态：R18 fixes 已验证，R19 Action Matrix 已确认（全 no_action），anonymized repo 已推送，论文已提交。

### 4. 📋 待办（条件触发式）
- ckpt-6100 @ seq8192 完成 → 读 `/root/autodl-tmp/eval_results/qwen3_8b_cwm_repo_s42_ckpt6100_seq8192_eval/eval_repo_cwm.json`，核实 final accuracy 和 unparseable rate → 对比 Table 2 s42 (65.18%) → 报告 Director 作为 author response 储备
- 如 ckpt-6100 accuracy > 68%（超 Table 2 mean 66.48 + 1.5pp）→ 建议 Director 记录为 "checkpoint selection sensitivity" 证据，可在 author response 中说明 CWM 性能上限高于 Table 2 报告值
- 如 ckpt-6100 accuracy 仍 < majority baseline 72.96% → 确认 format collapse 核心结论不变
- Director 若请求新一轮写作审查 → 加载 `paper-quality-lessons.skill.md` + `reviewer-audit-checklist` §7

### 5. 🎯 战略上下文
**核心结论链**：
1. Function level: CLS ≈ CWM（TOST p=0.007, 5 seeds），TRAJ 等价 inconclusive（power ~0.3）
2. Repo level: CLS >> CWM（18-26pp gap），format collapse 是主因（53-74% unparseable）
3. 86.05% mis-training 实验是 format collapse 因果证据的最强支撑（CLS-format 训练的 CWM 模型 → 0% unparseable + 86.05% accuracy）
4. 14B 缩小所有 gap 至 1.07pp（3 seeds, single family Qwen3）

**易错点**：
- **ckpt-300 reeval 的 seq2048 数据绝不能与 Table 2 混用**——之前差点出这个错，Director 专门审查过
- Table 2 三个 seed 的 checkpoint 不同：s42 用 ckpt-400，s456/s123 用 ckpt-6633。这不是 bug，是各 seed 独立 early-stopping 选出的 best checkpoint
- val/test divergence：later checkpoint（ckpt-6100, val_loss ~0.52）test accuracy 更高，early checkpoint（ckpt-300/400, val_loss 0.286）test accuracy 更低。这说明 repo-level CWM 的 val loss 不是可靠的 checkpoint 选择信号
- `checkpoints_repo_cwm_8b_conda` 和 `checkpoints_backup_cwm_8b` 都是 s42 训练，前者是原始目录，后者是备份/重命名
