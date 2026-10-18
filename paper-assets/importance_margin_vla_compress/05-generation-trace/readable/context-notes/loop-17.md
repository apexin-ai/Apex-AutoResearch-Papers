# director / loop_17.md

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_17.md`
- **Structured JSON:** [`ee34b25fcb2bb24f4b9a.json`](../../sessions/ee/ee34b25fcb2bb24f4b9a.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 17
reason: max_messages
updated: '2026-05-26T18:59:34+00:00'
---

### 1. 🔴 硬约束 / 红线
- **硬截止 C002**: 所有实验必须在 **2026-05-28 12:00 UTC（北京时间 20:00）** 前完成，最后 12h 留给论文定稿
- **GPU 白名单**: 只能用 cqa1-33015 (4 GPU) + westd-27271 (2 GPU) + westd-38929 (4 GPU) + westd-41074 (4 GPU)，共 14 张
- **C001**: Spatial suite 对比禁止用 LoRA baseline (6.2%) 作基准，必须用 official baseline 或 full-FT
- **cqa1 部署**: submit_on_allocated 不支持（bare python 不在 PATH），必须走 tmux + `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`
- **ROADMAP GPU 表可能与实际漂移**，每次接手先 `get_project_status` + SSH 实查 nvidia-smi 校准

### 2. 🖥️ 基础设施快照
- **westd-38929** (4×RTX 4090): `/root/autodl-tmp/importance_margin_vla_compress`
- **westd-41074** (4×RTX 4090): 同上路径
- **westd-27271** (2 GPU 分配): 同上路径
- **cqa1-33015** (4×RTX 4090): 同上路径，conda base 环境
- 模型: OpenVLA finetuned 在 `/root/autodl-tmp/openvla-7b-finetuned-libero-10`（westd），π0.5 模型在 cqa1 本地
- HF cache: `/root/autodl-tmp/.hf_cache`（AutoDL 实例）
- 所有实验都在 tmux session 中运行，cron 追踪完成事件（11 个活跃 cron）
- 审稿 C 群 chat_id: `oc_83179cdc26b856fbbaf531d145edb3bd`

### 3. 📊 当前状态
**刚完成**：确认 cqa1 GPU 0/1 新部署实验已注册 registry（eval_pi05_l2norm_k07_long_seed42 + eval_pi05_attention_k07_long_seed42_v2），14/14 GPU 满载确认。

**里程碑**：Crossover table 16/16 ✅ | Abstract 已提交 ✅ | D237 position encoding sensitivity 确认 ✅ | Paper Agent D237 叙事升级完成 ✅ | Provenance 70/73

**RUNNING 实验（~14 个，分布在 4 台服务器）**：全部是 cliff curve 端点填充——OpenVLA 和 π0.5 两个模型在 Object/Long/Goal suites 上的中间 k 值（k=0.5/0.7/0.75/0.85）。ROADMAP 里有详细 GPU 表但可能与实际有偏差，建议接手后先校准。

**Paper Agent** 正在写作中，provenance 70/73 有 3 个 tier-3 gap 待补。

### 4. 📋 待办（条件触发式）
- 当前批次 cliff curve 实验陆续完成 → 收割结果填入 ROADMAP cliff curve 表 → 通知 Paper Agent 更新论文数据
- 所有 cliff curve 完成 → 整合最终 crossover + cliff 数据 → Paper Agent 最终定稿
- Provenance 3 个 tier-3 gap 补全 → 73/73 → 可提交 study
- GPU 空出来 → 立即部署待处理实验（eval_pi05_attention_k05_long_seed42_v3、eval_pi05_random_k07_long_seed42 等），不允许空卡
- 审稿 C 群回传审稿报告 → 按 review-report-action skill 处理（Holistic Pass + Action Matrix）
- **May 29**: 论文最终提交

### 5. 🎯 战略上下文
**核心发现**：VLA vision token 可压缩性取决于 scoring method × connector architecture × task complexity 的三维交互。关键证据链：
- **L2norm 完美单调递减**（压越多性能越差，可预测）
- **Random 出现 V-shape**（k=0.85 处灾难性下降，k=0.75 反弹）→ D237 归因于 position encoding sensitivity
- **Crossover 现象**：不同 suite 在不同 k 值处，最优方法会交叉——没有"一招鲜"

**论文定位**: CoRL 2026，analysis contribution（非 method contribution），强调"不同 regime 需要不同压缩策略"的 systematic finding。

**易错点**：
- ROADMAP GPU 表与实际经常漂移，不要信表上写的，SSH 实查
- cqa1 用 conda 不用 venv，westd 系列也是 conda
- Agent 有时 worker 部署成功但忘记注册 registry，每次确认部署后追问 registry 状态
- Random k=0.85 的 V-shape 是真实现象（已 cross-seed 验证），不是 bug，不要让 Agent 重查


---
