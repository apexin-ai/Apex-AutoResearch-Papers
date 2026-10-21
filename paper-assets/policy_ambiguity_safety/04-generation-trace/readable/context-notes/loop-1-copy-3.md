# reviewer / loop_1.md

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Context and loop notes

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `task_context/history/reviewer/loop_1.md`
- **Structured JSON:** [`36c5c890b7ae01fc88e5.json`](../../sessions/36/36c5c890b7ae01fc88e5.json)

## Before a recorded user message

1 recorded events

### Context note

_source line 1_

---
loop: 1
reason: max_wall_time
updated: '2026-05-21T02:06:12+00:00'
---

### 1. 🔴 硬约束 / 红线
- 本項目全 API 無 GPU，不存在 GPU 設備號約束
- 5 模型全走 OpenRouter 代理（47.94.22.126/v1），cross-judge 配對固定：GPT-4.1 判 GPT-5.4+DeepSeek，GPT-5.4 判 Claude+Qwen3+DeepSeek。**不可更改 judge 分配**——論文所有 within-judge 分析基於此配對
- C3 (layer effect) 已定性為 **inconclusive**（within-judge 不顯著 + Holm-Bonferroni 失敗）。不可在任何章節將其升級為 confirmed claim
- Incompleteness 的 49.2pp effect 是 **upper bound**（info addition confound）。論文中提及此數字時必須附帶 caveat
- 論文 EMNLP 2026 long paper：主文嚴格 8 頁，Limitations + References 不計入

### 2. 🖥️ 基础设施快照
- 服務器：localhost(ubuntu)，工作目錄 `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts`
- 論文源碼：`docs/paper/` 下，`main.tex` + `sections/*.tex` + `references.bib`
- 分析數據：`artifacts/full_study/analysis/` 下 19 個 JSON 文件（full_statistics, bootstrap_ci, mcnemar_matched, tost_sensitivity_5model, within_judge_c2, info_delta_analysis, realism_validation, severity_sensitivity, power_analysis, systematic_nocuity_5model 等）
- `per_clause_summary.csv`（186KB）在同目錄，每條 clause × model 的 violation rate
- 無 GPU / 無 wandb / 無 tmux / 無 cron。全部實驗已完成
- plan_009 標註材料：CSV + guidelines + calibration.py 已就緒，等人工標註者操作 Google Sheets

### 3. 📊 当前状态
**剛完成**：Director 的 Soundness 提升審查（4 問回覆）+ ROADMAP 更新審查 + variance decomposition 敘事一致性審查 + 系統性論文質量審查（4 問回覆）

**Registry 狀態**：
- plan_009: PREPARING（人工標註，標註者 2026-05-21 到位）
- 其餘 9 個實驗全部 DONE（mvp_001, diag_001, plan_002/002c/003a/003b/004/005/006）

**等待中**：
- C群二審反饋（Round 2 已提交 continue mode）
- plan_009 人工標註完成 → judge calibration 數據
- Director 決策：是否根據我的建議派 Agent 做加固分析（擴展 Error Analysis 到 5 模型、clause-level variance decomposition with interaction term）

### 4. 📋 待办
- C群二審反饋到達 → 按 §5 審查模式 B 逐項審查修改方案，重點關注 Soundness 評分變化
- plan_009 人工標註完成 → 核實 judge calibration 數據與論文 Limitations "Cross-judge asymmetry" 段一致性
- Paper Agent 提交新 round → 檢查：(a) realism FK amb_vs_original 選擇性報告是否修正，(b) Analysis §6.2 vs C3 張力是否加限定句，(c) Intro "three-tier" 是否加 incompleteness caveat
- 若 Agent 做了 clause-level variance decomposition with interaction → 核實 interaction variance 佔比是否與 C4 χ²=31.02 一致
- Error Analysis 擴展到 5 模型 → 核實 failure mode distribution 是否跨模型一致（當前 2 模型結論：5/6 types 同 dominant mode）

### 5. 🎯 战略上下文
**核心結論**：Policy ambiguity 普遍危險（+34.0pp），但 type × model interaction 決定嚴重程度。Incompleteness 是 universal blind spot（46-62%），auth_scope 是 canary type for safety training（12-64%）。C3 layer effect inconclusive。

**決策鏈**：D020 pivot Uniform→Differential Nocuity → D024 5-model analysis C3 downgrade → D025 C群審稿處理

**最容易判斷錯的事**：
1. **C3 和 Analysis §6.2 的關係**：C3 (violation rate 層效應) inconclusive ≠ §6.2 (failure mode 層機制) invalid。兩者用不同 evidence source，但審稿人會攻擊表面矛盾。§6.2 需要一句限定語連接 C3
2. **"Three-tier" 的脆弱性**：移除 incompleteness 後 omnibus p=0.079，三層退化為兩層。Abstract/Intro 的 "three-tier" 完全依賴有 confound 的 incompleteness。這不是 critical 但是最明顯的審稿人攻擊面
3. **Within-judge 是本論文命脈**：所有 cross-judge confound 的防禦都靠 within-judge 分析（Claude/Qwen3/DeepSeek 同 judge）。如果有人質疑 within-judge 分組的代表性，目前沒有額外防線——plan_009 人工標註是唯一補充
4. **Realism validation 段有選擇性報告**：amb_vs_original FK (p=0.006, d=0.29) 被省略，只報了 amb_vs_unamb FK (p=0.10)。我已 flag 為 warning，待修正
5. **ICC 有兩套數字別搞混**：reproducibility ICC (0.919, per-type 0.807-0.989) = 同模型重複跑穩定性；cross-model per-type ICC (0.29-0.49) = 不同模型對同一 clause 是否同意。前者在 Method+C3，後者在 variance decomposition


---
