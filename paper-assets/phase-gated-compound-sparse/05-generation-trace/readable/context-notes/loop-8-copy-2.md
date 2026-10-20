# agent / loop_8.md

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_8.md`
- **Structured JSON:** [`77915d0f916fc324adfb.json`](../../sessions/77/77915d0f916fc324adfb.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 8
reason: idle_timeout
updated: '2026-05-14T21:43:09+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-22162 cuda:0,1,2,3 共 4 张，不得用其他设备
- c2_n500_deepseek 占 cuda:0+1，c2_qw_n500 占 cuda:2+3，在这两个实验完成前不得抢占
- II 主指标已从 mean 切换为 median + median bootstrap CI（D054），所有新分析必须用 median
- Qwen s015 CI 跨零是预注册的 nuanced finding（D037/D038），不是 bug，不要试图"修复"
- DeepSeek magnitude ~4× Qwen 是 model-dependent onset threshold，禁止直接比较绝对值，只比较趋势（ρ=1.0）
- 论文已全文完成，数字一致性审查已通过，修改任何 table/figure 必须用 bf16 canonical 数据

### 2. 🖥️ 基础设施快照
- 服务器：westd-22162，工作目录 /root/autodl-tmp/pacs/
- Python：/root/miniconda3/bin/python（conda base 环境，不是 venv）
- 激活命令：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- 模型路径：未在 memory.md 中记录，需 SSH 确认（/root/autodl-tmp/ 下）
- 日志目录：/root/autodl-tmp/pacs/logs/
- c3_llama 分析产出：/root/autodl-tmp/pacs/analysis_output/c3_llama_{results,cohens_d,report}.*
- 活跃进程：
  - c2_n500_deepseek: cuda:0+1, PID 未明确记录（cron 用 pid=c2_n500_gpu0 标识），RUNNING
  - c2_qw_n500: cuda:2+3, PID 131864/132002 (tmux), RUNNING
- 活跃 cron：c2_n500_deepseek + c2_qw_n500 两个监控 cron

### 3. 📊 当前状态
**刚做完**：收到 c5b_pilot 失败 cron 回调，已派 Worker `worker_diagnose_c5b_pilot_20260514T182945` SSH 诊断。日志文件 /root/autodl-tmp/pacs/logs/c5b_pilot.log 不存在（进程可能启动即崩溃）。Worker 正在查找实际日志、tmux 残留、dmesg OOM 记录等。

**Registry 状态**：
- c2_n500_deepseek — RUNNING，DeepSeek 8 conditions n=500，cuda:0+1，预估 ~18h
- c2_qw_n500 — RUNNING，Qwen 8 conditions n=500，cuda:2+3，PID 131864/132002
- c5b_pilot — DONE(failed)，"process dead 5× with no sentinel/W&B"
- 其他 80 实验全部 DONE

**等待中**：
- Worker `worker_diagnose_c5b_pilot_20260514T182945` 回调 → 需要更新 registry notes + 汇报 Director
- c2_n500_deepseek cron 回调（完成或失败）
- c2_qw_n500 cron 回调（完成或失败）
- c2_qw_n500 有历史数据完整性风险：重复进程（PID 132389/132392 已死）运行期间 s015 的 ~8→~93 问题可能有交叉写入，完成后需验证 profiling_results.json 时间戳单调性和问题数=500

### 4. 📋 待办（条件触发式）
- Worker diagnose_c5b_pilot 回调 → 读诊断 JSON → update_registry notes 写入 root_cause → 判断是否可自动修复（infrastructure 类可重试一次，resource/hyperparameter 类汇报 Director）→ main_agent_post_to_director 汇报失败原因和建议
- c2_n500_deepseek cron 完成 → spawn worker 分析结果 → 更新论文 tables（用 median + bootstrap CI）→ 检查 Qwen s015 预注册条件 → 汇报 Director
- c2_qw_n500 cron 完成 → 先验证数据完整性（重复进程交叉写入风险）→ spawn worker 分析 → 更新论文 → 汇报 Director
- C2 双实验全部完成 → 合并 DeepSeek+Qwen n=500 结果 → 更新论文 §4/§5 tables + figures → 提交 Group C full review
- c5b_pilot 若诊断为 infrastructure 可修复 → 在 C2 占满 GPU 期间暂缓，C2 释放 GPU 后重新提交
- 截稿 2026-05-25（距今 11 天），C2 完成后剩余时间全部用于论文 polish + review 迭代

### 5. 🎯 战略上下文
- 核心发现：importance-based pruning 的 compound interaction severity 随 sparsity 单调递增，random masking 全 FAIL。跨模型趋势一致（Cohen's d ρ=1.0, gradient permutation p=0.043）
- C1(compound effect exists)/C2(statistical power)/C3(cross-architecture)/C5(mitigation)/C6(dose-response) 已 confirmed，C4(entropy-collapse) 降为 §6 supporting（D045/D046）
- 论文全文已完成并可编译，当前是"补充实验冲刺"阶段——C2 n=500 提升统计功效是最后的关键实验
- c5b_pilot（C5b mitigation pilot）失败不阻塞投稿——C5 已有其他实验支撑，pilot 是锦上添花
- **易踩的坑**：
  - 不要用 Cohen's d independent 版本，论文统一用 paired d_z（D048/D050 两次教训）
  - 不要直接比较 DeepSeek vs Qwen 绝对 II 值，只比较趋势方向和单调性
  - c2_qw_n500 完成后必须验证数据完整性（重复进程历史问题）
  - LLaMA s015 CI 不跨零（优于 Qwen s015），是论文叙事亮点，别漏掉


---
