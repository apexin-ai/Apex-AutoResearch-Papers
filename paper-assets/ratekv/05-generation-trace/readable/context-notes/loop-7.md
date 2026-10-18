# agent / loop_7.md

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/agent/loop_7.md`
- **Structured JSON:** [`5ef349eb3c50eb04f412.json`](../../sessions/5e/5ef349eb3c50eb04f412.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 7
reason: idle_timeout
updated: '2026-05-15T00:49:53+00:00'
---

### 1. 🔴 硬约束 / 红线
- GPU 白名单：仅 `cuda:0` 和 `cuda:1`（westd-37397），不得使用其他设备
- 所有 eval 必须用 **bf16**，禁止 fp16（Llama/Qwen overflow 事故已验证）
- Profile 文件加载时必须验证 concentration 值（hires ~0.61, lowres ~0.42），防止文件名歧义导致数据混用
- 论文 PPL 数据统一用 hires_mckp_reeval pipeline 数字，不引用 exp_e 的绝对 PPL
- Claim 2 限定 "moderate-to-aggressive compression (≥4x)"，2x 下 MCKP 不如 uniform
- ssh_execute 有 30 秒硬超时，长操作必须 tmux 脚本 + 轮询

### 2. 🖥️ 基础设施快照
- 服务器：**westd-37397**，2× RTX PRO 6000 96GB
- 工作目录：`/root/ratekv`，account: root
- Python：`/root/miniconda3/bin/python`（conda base 环境，不是 venv）
- 环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- HF cache：`/root/autodl-tmp/.hf_cache`（需显式 `HF_HOME` 设置）
- 活跃进程：
  - `mistral_c4_hires_crossdataset`：PID 273407, tmux session, cuda:1, RUNNING
  - `gemma2_hires_bf16_2bitonly`：状态 ANALYZING（进程应已结束，等分析）
- Cron：reconcile 返回 0，**无活跃 cron 监控**——mistral_c4 和 gemma2 可能没有 cron 看守，需要手动检查

### 3. 📊 当前状态
Registry 总计 72 个实验：65 DONE (34 success / 15 negative / 8 killed / 8 failed), 5 PREPARING (均已 killed/superseded), 1 ANALYZING, 1 RUNNING。**无活跃 Worker**。

**正在进行**：
- `mistral_c4_hires_crossdataset`：RUNNING on cuda:1，Mistral C4 cross-dataset 验证（hires）
- `gemma2_hires_bf16_2bitonly`：ANALYZING，Gemma-2 hires 2-bit profiling 已完成执行，需要提取结果

**等待中**：
- P0 patches：Director 尚未决策 Qwen concentration 用 0.61（单值）还是 0.59-0.66（range）
- Group C 审稿报告尚未回传
- Scatter 图 concentration 值校验未完成（可能用了 standard 而非 hires 数据）
- Heatmap 重生成状态不明（report.md 提到 Worker 运行中，但无活跃 Worker）

### 4. 📋 待办（条件触发式）
- **gemma2_hires_bf16_2bitonly 分析完成** → spawn Worker 提取 log 中的 concentration + top-5% delta，更新 registry metrics，写入 5-model evidence table。预期 concentration ≈ 0.23（与 standard 一致，确认 Flat/FAIL）
- **mistral_c4_hires_crossdataset 完成** → 提取 C4 vs WT2 allocation agreement（预期 >96%），更新 Table 相关数据，验证跨模型 cross-dataset 一致性
- **两个 hires 实验都完成** → 所有 5 模型 hires 数据齐全，去掉 Table 3 的 ‡ 标注，论文数据冻结
- **Director 决策 0.61 vs range** → 全文替换 concentration 值，执行 P0 patches
- **Group C 审稿报告到达** → 按 rebuttal skill 处理
- **无 cron 监控** → 立即检查 mistral_c4 进程是否存活，必要时手动 spawn Worker 查状态

### 5. 🎯 战略上下文
**核心结论**：cardinality constraint 是 100% 的方法贡献（greedy+constraint = MCKP+constraint, delta=0.0000）。heterogeneity 的 distribution shape（spike vs spread）决定 non-uniform 是否值得——GQA ratio 不是可靠 proxy（Yi-1.5 GQA 8:1 但 FAIL 反证）。

**5-model verdict**：Qwen PASS, Yi-1.5 FAIL, Llama ≈Uniform, Mistral FAIL, Gemma-2 FAIL。论文 narrative = architecture-dependent heterogeneity analysis + cardinality constraint as universal mechanism。

**易踩的坑**：
- Yi-1.5 hires concentration=0.71 是 false positive（单 outlier L4H3 spike，不是 spread）。Claim 3 的 0.50 阈值只在 standard profiling 下 5/5 准确，hires 下 4/5。D050 决定升级诊断为 concentration + shape 双条件
- `qwen_float32_profiles.json` 中 "float32" 指精度不是分辨率，实际是 lowres 数据
- 5 个 PREPARING 实验都是历史遗留（killed/superseded），不要尝试恢复
- 距 ARR deadline 仅 ~10 天（May 25），数据冻结后重心转论文 polish

**决策链关键节点**：D048 Claim 3 PASS → D049 GQA proxy 不可靠 → D050 concentration+shape 双条件 → D051 Qwen 全文统一 0.61


---
