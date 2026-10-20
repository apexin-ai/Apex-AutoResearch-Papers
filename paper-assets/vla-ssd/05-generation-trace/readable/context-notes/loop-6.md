# director / loop_6.md

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/director/loop_6.md`
- **Structured JSON:** [`d9671a5c5a3656bd374c.json`](../../sessions/d9/d9671a5c5a3656bd374c.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 6
reason: max_messages
updated: '2026-05-21T01:42:21+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本项目只能用 westd-19183 的 cuda:0 和 cuda:1（项目配置 gpu_ids）
- NORA 必须用独立 conda 环境（`/root/vla-ssd/nora_env/`），不能污染 OpenVLA 的 transformers 4.48.3——上一个 Worker 升级到 5.9.0 差点炸掉 OpenVLA pipeline
- CoRL 2026 DDL：Abstract 5/26，Paper 5/29——排期按天算不按周算
- 禁止 fallback 到低级别会议，GPU 不够申请扩容不降级目标

### 2. 🖥️ 基础设施快照
- 服务器：westd-19183 (connect.westd.seetacloud.com)，工作目录 `/root/vla-ssd`
- Python：OpenVLA 用系统 Python（transformers 4.48.3）；NORA 用 `/root/vla-ssd/nora_env/`（独立 venv）
- HF cache：`/root/autodl-tmp/.hf_cache`（根分区只 30GB，大文件必须放 autodl-tmp）
- 模型 checkpoints：OpenVLA finetuned 在 `/root/autodl-tmp/.hf_cache/` 下各 suite 目录；TraceVLA checkpoint 已在服务器；NORA checkpoint 已下载完成 + dry-run 通过（36层, hidden=2048）
- LIBERO-Long checkpoint `moojink/openvla-7b-oft-finetuned-libero-10` 下载中（12% 时 817MB/~14GB，xethub 不稳定自动重试）
- AutoDL 特殊：`source /etc/network_turbo` 启用代理；HF 下载用 `HF_ENDPOINT=https://hf-mirror.com`；ModelScope 备选

### 3. 📊 当前状态
**cuda:0**：OpenVLA LIBERO-Object 全套 pipeline RUNNING——Phase 1 数据收集完成（10 tasks, 5000 samples），Phase 2 R² probing 进行中（L0 img_mean R²=0.6952）。预计总计 2-3h。

**cuda:1**：TraceVLA LIBERO-Spatial pipeline 刚派发 Worker 准备中（attention → probing → classification → counterfactual）。NORA 环境已就绪但 GPU 先给 TraceVLA 用，不空等。

**3×4 矩阵进度**：
| Model | Goal | Spatial | Object | Long |
|-------|------|---------|--------|------|
| OpenVLA | ✅ done | ✅ done | 🔄 cuda:0 Phase 2 | 📋 checkpoint 下载中 |
| TraceVLA | ✅ done | 🔄 cuda:1 准备中 | 📋 | 📋 |
| NORA | 📋 env ready, dry-run passed | 📋 | 📋 | 📋 |

**Reviewer 完全瘫痪**：所有 post_to_reviewer 返回 "PDF file was not valid"，escalate Manager 7 次无回应。3×4 扩展方案无 Reviewer 审查。

### 4. 📋 待办（条件触发式）
- Object pipeline 6 phases 全部完成 → 汇报结果 + 立即启动 OpenVLA LIBERO-Long pipeline（前提：Long checkpoint 下载完成）
- TraceVLA-Spatial pipeline 完成 → 汇报 + cuda:1 接 TraceVLA-Object 或 NORA-Goal（看哪个更 ready）
- LIBERO-Long checkpoint 下载完成 → 不等 Object 跑完，先确认 checkpoint 完整性
- NORA 所有 4 套件排在 OpenVLA/TraceVLA 之后，除非某张卡先空出来
- 3×4 矩阵数据收齐 → 通知 Paper Agent 升级论文 claim："3 architectures spanning 450M-7B across 3 backbone families, evaluated on all 4 LIBERO suites (40 tasks)"
- Reviewer 恢复 → 第一件事审 3×4 扩展方案 + claim 升级是否站得住

### 5. 🎯 战略上下文
- **核心发现**：VLA fine-tuning 重分配 instruction attention 而非重塑 visual geometry——训练效果集中在 readout（R² +0.069, attention +46pp）而非 images（Δ≤1.7%）
- **跨架构验证**：OpenVLA (Llama-2 7B) 和 TraceVLA (Phi-3-V 4B) 不同 backbone、不同 untrained profile，但 fine-tuned 后 mid-layer peaks 收敛（Δ=0.003, TOST p<0.0001）——说明是 task-structure 约束而非 architecture artifact
- **NORA 是第三验证点**：Qwen2.5-VL-3B backbone，FAST+ tokenizer（DCT+BPE），如果也收敛到 mid-layer peak → claim 从 "two architectures" 升级到 "three backbone families"，大幅增强泛化性
- **易错点**：(1) SmolVLA 已被 disqualify（frozen VLM + flow matching），不要重新考虑；(2) TraceVLA 没有 suite-specific checkpoint，用 OXE-pretrained checkpoint 跑所有套件是已批准的方案；(3) NORA 的 FAST+ tokenizer 不影响 hidden state 分析，action tokenization 方式与我们的 representation analysis 正交
- **结构性天花板**：closed-loop 验证在 DDL 前不可行（4 次失败确认）；LIBERO-only scope 是已知局限，通过 4 suites × 3 models 最大化 open-loop 证据严密度来对冲
- **16 个 negative experiments 已复盘**：4 closed-loop infeasible, 8 informative negatives already in paper, 4 superseded——无需重试


---
