# Project coordination (archived snapshot) — Part 2 of 2

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../coordination-coordination-20260513-235202.md) · [Structured JSON](../../../sessions/b6/b68f7499123697aa005d.json)

## Round 32

### Assistant

_source line 602 · 2026-05-13T23:52:02.100817+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- GPU 白名单：westd-37397 的 cuda:0 和 cuda:1（2× RTX PRO 6000 Blackwell 96GB）
- submit_training_job 命令必须 `bash -c "..."` 包裹（tmux 用 sh 执行，source/conda activate 会 127）
- tmux 非交互 shell 不加载 .bashrc，每条命令前必须 `source /etc/network_turbo && export HF_ENDPOINT=https://hf-mirror.com && export HF_HOME=/root/autodl-tmp/.hf_cache && export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt && export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`
- transformers 4.57.6 的 Qwen2 模型 `use_cache=False` 时必须传 `cache_position=torch.arange(seq_len, device=device)`，否则 IndexError
- Eviction 路径已被 3 个实验彻底 falsify——不要再尝试任何 eviction 相关实验

### 2. 🖥️ 基础设施快照
- 服务器：westd-37397，工作目录 `/root/ratekv/`
- Python：`/root/miniconda3/bin/python`（conda base，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
- Python 3.12.3, PyTorch 2.10.0+cu128, CUDA 12.8 (Driver 595.58, CUDA Version 13.2)
- 7B 模型：`/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B`（路径含 `___` 但 7B 能正常加载）
- 1.5B 模型：`/root/autodl-tmp/models/Qwen2.5-1.5B`（干净路径，之前 ModelScope `___` 路径会 HFValidationError）
- Calibration 数据：`/root/ratekv/calibration_data.json`（20 条，每条 ≥1000 tokens，WikiText-103 拼接）
- 活跃进程：**无**（两卡空闲 0% util）。Worker `worker_infra_read-expb-results_20260513T235027` 正在读日志

### 3. 📊 当前状态
**正在等待 Worker 回调**：`worker_infra_read-expb-results` 正在拉取 Exp B（go/no-go 决策实验）的完整结果日志。Exp B Worker 已完成代码编写 + 1.5B smoke test + 7B 完整实验，产出了 `full_bitwidth_results.json` 和多个 log 文件，但 Worker 只返回了文件列表未贴数据。

Registry 状态：
- `exp_b_hires_quant` PREPARING — go/no-go 决策实验（PPL-guided quant-only MCKP, {2,4,8,16}-bit action space）。Worker 已跑完，结果待读取
- 所有其他实验 DONE：mvp_001-004 (failed/negative), sanity_001-004 (failed/success), p0_1_ppl_fast (negative), p0_2_cliff_1.5B/7B (success), exp_a_targeted_hybrid (negative)

### 4. 📋 待办
- `worker_infra_read-expb-results` 回调到达 → 读完整结果 → 更新 `exp_b_hires_quant` registry → 向 Director 汇报完整 PPL 对比表 + Pass/Fail 判定
- 如果 Exp B **PASS**（non-uniform MCKP PPL < uniform 4-bit 15.45 by ≥0.5）→ 项目继续，进入 research 阶段，写 paper_framing.md + experiment_plan.yaml
- 如果 Exp B **FAIL**（≈ uniform）→ 项目需 Director 决策是否 archive
- 如果 Worker 回调数据不完整 → 再派 Worker 读 `/root/ratekv/full_bitwidth.log` + `budget_matched.log` + `manual_test.log`
- Exp B 结果出来后 → 更新 memory.md 记录最终结论

### 5. 🎯 战略上下文
**项目在 go/no-go 决策点**。核心假设经历了三次 pivot：
1. MSE distortion → falsified（MSE-guided PPL 比 uniform 差 70×）
2. PPL distortion + eviction → falsified（eviction compounding effect + Layer 0 无法承受任何 eviction）
3. PPL-guided per-head bit-width allocation（{2,4,8,16}-bit, quant-only）→ **结果待读取**

**关键洞察**（已确认的事实）：
- Per-head quantization sensitivity 高度不均匀：Layer 0 heads 2-bit 导致 +32% PPL (7B)，大部分 L1-L27 heads 2-bit 仅 0-2%
- 4-bit 和 8-bit 对所有 head 安全（zero cliff）
- Quant-only MCKP 之前 = uniform 是因为 action space 只有 {4-bit}（tautology），不是因为 non-uniform 没价值
- Exp B 的 {2,4,8,16}-bit action space 是第一次真正测试 non-uniform quantization

**易错点**：
- 不要混淆 "quant-only MCKP = uniform" 的历史结果（tautology）和 Exp B 的结果（真正的 non-uniform 测试）
- calibration PPL delta 和 full WikiText-2 eval PPL 之间可能存在 gap（eviction 已踩过这个坑，quantization 是否也有此问题待观察）
- Exp B Worker 产出了多个 log 文件（full_bitwidth.log, manual_test.log, budget_matched.log），需要全部读取才能完整判断
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_16f4cc04d259f364091fe7b4addd7912"
}
```

</details>

---
