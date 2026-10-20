# 服务器故障诊断报告

**服务器**: seetacloud-westd-4x5090 (4× RTX 5090 32GB)
**诊断时间**: 2026-05-16 ~08:30 UTC

---

## 1. cls8b-s42-ckpt3600-seq2048-ablation

**结论: 实际已成功完成，非故障**

日志显示 9784/9784 样本全部处理完毕，结果已写入磁盘：
- `eval_repo_cls.json` + `eval_repo_cls_predictions.jsonl`
- 路径: `/root/autodl-tmp/eval_results/cls8b_s42_resume_ckpt3600_test_seq2048/`

**结果摘要**:
| 指标 | 值 |
|------|-----|
| Accuracy | 83.04% |
| F1 macro | 76.80% |
| F1 (fail) | 64.8% (P=73.9%, R=57.6%) |
| F1 (pass) | 88.8% (P=85.5%, R=92.5%) |
| Majority baseline | 73.0% |
| Gap vs majority | +10.1pp |
| Unparseable | 136/9784 (1.4%) |

Cron 标记为 failed 应属误判（可能进程退出后 sentinel 未被写入，或 W&B 未配置）。

---

## 2. repo-level-cwm-8b-conda-v5（CWM 8B 训练）

**根因: 进程被系统杀死（疑似 OOM 或平台强制回收）**

- PID 400279 已死亡
- 训练停在 step **6198/6633**（93.4%），日志无错误信息直接中断
- 最后几步速度骤降：12s/it → 18.2s/it，随后无输出
- 与 CWM eval (ckpt-400) 几乎同时被杀（eval 的 EXIT_CODE=137 确认 SIGKILL）
- 可能原因：训练在 checkpoint-6100 做 eval 时，eval 子进程与同时运行的 ckpt-400 eval 争抢 cuda:0 显存，触发系统级 OOM kill

**检查点状态**:
| Checkpoint | 时间 |
|------------|------|
| checkpoint-6100 | May 16 07:53 |
| checkpoint-6000 | May 16 07:13 |
| checkpoint-5900 | May 16 06:34 |
| checkpoint-5800 | May 16 05:54 |
| checkpoint-400 | May 14 16:32 |

**恢复计算**:
- 最新可用 checkpoint: **6100**
- 总目标: 6633 steps
- 剩余: **533 steps**
- 预估耗时: ~533 × 12s ≈ **1.8 小时**

---

## 3. cwm8b-ckpt400-test-eval

**根因: SIGKILL (EXIT_CODE=137)，系统级 OOM kill**

- PID 381618 已死亡
- 日志确认 `Killed` 信号，EXIT_CODE=137
- 处理到 **5280/9784** 样本（54.0%），running_acc=64.7%
- 部分结果文件: `results_incremental.jsonl`，**5280 行**，18.6 MB

**部分结果可用性**: 5280 条结果完整可用（incremental 写入模式），可用于初步分析或用 `--resume` 从断点续跑。

---

## GPU 当前状态

| GPU | 型号 | 显存使用 | 利用率 |
|-----|------|---------|--------|
| 0 | RTX 5090 | 0 / 32607 MiB | 0% |
| 1 | RTX 5090 | 0 / 32607 MiB | 0% |
| 2 | RTX 5090 | 0 / 32607 MiB | 0% |
| 3 | RTX 5090 | 0 / 32607 MiB | 0% |

**全部空闲。** 磁盘: /root/autodl-tmp 100GB 可用（61% 已用）。

---

## 恢复建议

### 优先级 1: CWM 8B v5 训练（恢复）
- 从 checkpoint-6100 resume，剩余 533 steps，约 1.8 小时
- **必须确保恢复时不要同时在 cuda:0 上跑 eval 任务**
- 建议先单独跑完训练，再跑 eval

### 优先级 2: CWM 8B ckpt-400 eval（重跑/续跑）
- 如果 eval 脚本支持 `--resume`，从 5280 条续跑，剩余 4504 样本
- 如果不支持 resume，用已有 5280 条部分结果做初步分析，训练完成后再完整跑 final checkpoint eval
- **不要与训练同时在同一 GPU 上运行**

### 优先级 3: CLS ablation
- 无需恢复，**结果已完整**。需要更新 registry 状态为 DONE(success)。

### 防护措施
- 训练和 eval 任务分配到不同 GPU，或错开时间执行
- eval 使用 `--batch_size 1 --max_new_tokens 1024` 时单卡峰值显存可能接近 32GB，与训练 eval 阶段冲突时极易 OOM
