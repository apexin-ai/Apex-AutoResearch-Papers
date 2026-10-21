# Project coordination (archived snapshot) — Part 5 of 5

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Conversation logs

[← Part 4](part-004.md) · [Transcript overview](../coordination-coordination-20260517-110205.md) · [Structured JSON](../../../sessions/db/dbf326303797256f083e.json)

## Round 125

### Assistant

_source line 2497 · 2026-05-17T11:02:05.214219+00:00_

&lt;handoff>
### 1. 🔴 硬约束 / 红线
- cqa1-38874 只分配了 cuda:0，westd-24295 的 GPU 不在本项目 gpu_ids 白名单中（70B 实验是特批）
- NER batch-level BCS-F1 是 NULL (r≈0.004, n=450)，r=+0.50/+0.58 已确认为虚假相关（type frequency confound），论文中已全部删除/修正，绝对不能恢复
- n=69 TOST (interaction=0.47pp, p=0.003) 使用 BCS-controlled 数据（Exp 2），不能用 d051 random batches (n=525) 扩展——数据设计不匹配，SE 爆炸
- Few-NERD full schema = 66 types（不是 64），FewRel count levels 包含 count_40
- MAVEN count curve 数据来自 exp004_maven_bcs（不在 d051 中），Reviewer 查 d051 找不到是正常的

### 2. 🖥️ 基础设施快照
- **cqa1-38874**: 本地分析用，cuda:0 空闲，工作目录 `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/`
- **westd-24295**: 2×GPU，vLLM serving LLaMA-3.1-70B-Instruct-FP8，模型路径 `/root/autodl-tmp/models/llama-3.1-70b-instruct-fp8/`，代码 `/root/schema-dag-extraction/`
- **活跃进程**: westd tmux `exp3_70b` 运行 `scripts/run_d051_count_curves_llama70b.py --dataset fewnerd --seed 42 --model_path /root/autodl-tmp/models/llama-3.1-70b-instruct-fp8`，6 count levels × 25 batches，预计 ~50min（约 11:15 UTC 完成）
- **论文**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex`，21 pages, body=8 pages
- **httpx 注意**: westd 上 pip install datasets 升级了 httpx，所有后续脚本必须用本地模型路径 + HF_HUB_OFFLINE=1

### 3. 📊 当前状态
**刚完成**: D054 Round 11 全部 6 个 Phase 的文本修改 + 数据一致性修复 + Q3/Q5 分析整合 + NER r=+0.50/+0.58 虚假相关修正。Q3 n=525 扩展分析完成但结论是数据设计不匹配，不可用。

**Registry**: `exp_llama70b_cross_model` RUNNING（westd，Exp 1/2 done，Exp 3 running）

**等待中**:
- 70B Exp 3 (Few-NERD count curves) 完成回调 — 无 cron 监控，需要手动检查或 Director 通知
- Director 对 Q3 n=525 分析结论的确认（建议不报告，保留原 n=69 TOST）

### 4. 📋 待办
- 70B Exp 3 完成 → 读取结果 → 一次性写入所有 70B 结果到论文（§4 或 Appendix "Cross-Model Validation"：Exp 1 Dim1 count curves, Exp 2 Dim2 delta=+10.94pp, Exp 3 NER count curves）→ 这是最后一个 major 写入任务
- 70B 全部完成 → update_registry conclusion + metrics + checkpoint_path/log_path → 汇报 Director → 准备 Round 12
- Director 确认 Q3 n=525 不报告 → 无需改论文（logit sensitivity 已在 appendix，基于原 n=69 数据）
- 如 Director 要求 Q3 更大 power → 正确做法是在更多 count levels 上做 BCS-controlled 实验（非 random batches）

### 5. 🎯 战略上下文
- **Deadline**: ARR May 25 (D053)，约 18h 剩余，论文 body 已 8 pages
- **Title 已改**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
- **核心叙事**: 两维降解（count→recall, confusability→type confusion），bounded association in RE, coupled in NER。Dim2 是 RE-specific at batch level（NER batch-level BCS 是 null）
- **易错点 1**: 不要混淆 n=69 TOST（BCS-controlled, Exp 2）和 n=525（d051 count curves, Exp 1）——数据设计完全不同，不可简单扩展
- **易错点 2**: MAVEN count curve 数据在 exp004_maven_bcs（不是 d051），Reviewer 可能再问
- **易错点 3**: paper_framing.md 已更新 "bounded association" + "LLaMA-3.1-70B-Instruct (FP8)"，但 Evidence Hierarchy 中一些旧数据（如 FewRel Δ=-31.2pp）来自早期实验，与当前论文报告的数字可能有差异
- **Q5 防线**: FewRel 完全 balanced，BCS unique R²=0.259 (partial R²=0.467 controlling composition, p<0.001)——审稿人问"BCS 是否只是 composition proxy"时的关键证据
&lt;/handoff>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_04544c3b7bc497e1d098ba47fb56a6c2"
}
```

</details>

---
