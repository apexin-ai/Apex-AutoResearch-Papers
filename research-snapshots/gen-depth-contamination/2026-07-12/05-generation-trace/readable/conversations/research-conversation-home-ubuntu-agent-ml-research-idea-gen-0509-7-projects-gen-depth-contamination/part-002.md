# Research conversation: 执行项目轨迹扫描，将报告写入 /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports/layer2_2026 — Part 2 of 2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-home-ubuntu-agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination.md) · [Structured JSON](../../../sessions/26/26fa07fdd678c5c0e636.json)

## Round 1

### Tool result

_source line 153 · 2026-05-31T14:28:19.400Z_

<details><summary>↩ Tool result · `toolu_01S2g3ga2zFmecuY9u8brDqR`</summary>

```text
Most common experiment prefixes:
  sweep: 21
  exp_deberta: 12
  exp_009: 10
  exp_wiki: 10
  exp_arXiv: 8
  exp_code: 7
  deberta: 5
  exp_pythia69b: 4
  seed: 4
  exp_026: 3
  exp_027: 3
  exp_olmo: 3
  exp_qwen: 3
  exp_cross: 3
  exp_014: 3

OLMo-related experiments:
  exp_002_olmo_depth                  status=DONE       conclusion=success
  exp_arXiv_olmo                      status=DONE       conclusion=negative
  exp_wiki_olmo                       status=DONE       conclusion=failed
  exp_wiki_olmo_v2                    status=DONE       conclusion=negative
  exp_olmo_retrain_chain              status=DONE       conclusion=failed
  exp_olmo_retrain_v2                 status=PREPARING  conclusion=killed
  exp_olmo_retrain_v3                 status=DONE       conclusion=success
  exp_olmo1b_c4_rerun                 status=DONE       conclusion=negative
  exp_olmo1b_10k                      status=DONE       conclusion=success
  code_domain_olmo                    status=DONE       conclusion=success
  olmo_c4_cross_scorer                status=DONE       conclusion=success
  olmo_arxiv_cross_scorer             status=DONE       conclusion=success
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2f8d8906-2f3a-4e38-9332-f6f156df8673",
  "isSidechain": false,
  "promptId": "e8f1916e-15ff-4ed2-adfb-653543d822b4",
  "type": "user",
  "uuid": "e1d743ff-b2e1-482d-b95c-540830659e66",
  "toolUseResult": {
    "stdout": "Most common experiment prefixes:\n  sweep: 21\n  exp_deberta: 12\n  exp_009: 10\n  exp_wiki: 10\n  exp_arXiv: 8\n  exp_code: 7\n  deberta: 5\n  exp_pythia69b: 4\n  seed: 4\n  exp_026: 3\n  exp_027: 3\n  exp_olmo: 3\n  exp_qwen: 3\n  exp_cross: 3\n  exp_014: 3\n\nOLMo-related experiments:\n  exp_002_olmo_depth                  status=DONE       conclusion=success\n  exp_arXiv_olmo                      status=DONE       conclusion=negative\n  exp_wiki_olmo                       status=DONE       conclusion=failed\n  exp_wiki_olmo_v2                    status=DONE       conclusion=negative\n  exp_olmo_retrain_chain              status=DONE       conclusion=failed\n  exp_olmo_retrain_v2                 status=PREPARING  conclusion=killed\n  exp_olmo_retrain_v3                 status=DONE       conclusion=success\n  exp_olmo1b_c4_rerun                 status=DONE       conclusion=negative\n  exp_olmo1b_10k                      status=DONE       conclusion=success\n  code_domain_olmo                    status=DONE       conclusion=success\n  olmo_c4_cross_scorer                status=DONE       conclusion=success\n  olmo_arxiv_cross_scorer             status=DONE       conclusion=success",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "2f8d8906-2f3a-4e38-9332-f6f156df8673",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports",
  "sessionId": "5c8ae6e6-316a-4fa5-982e-a8e5b4f581c4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 154_

```json
{
  "type": "last-prompt",
  "lastPrompt": "执行项目轨迹扫描，将报告写入 /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports/layer2_20260531T142125.md",
  "leafUuid": "e1d743ff-b2e1-482d-b95c-540830659e66",
  "sessionId": "5c8ae6e6-316a-4fa5-982e-a8e5b4f581c4"
}
```

---


### Tool call

_source line 155 · 2026-05-31T14:28:29.957Z_

<details open><summary>🔧 Tool call — Bash · `toolu_019SBbxZbnp2bYeW3cF1JwWU`</summary>

```json
{
  "command": "# Look for hardware issues / SSH issues in workers\npython3 << 'EOF'\nimport json, glob, os\nfrom collections import Counter\n\n# How many worker session files - just count and get errors\nworker_files = []\nfor p in glob.glob('/home/ubuntu/.claude-account-*/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-7-projects-gen-depth-contamination/[a-f0-9]*.jsonl'):\n    worker_files.append(p)\n# dedupe\nunique = {}\nfor p in worker_files:\n    name = os.path.basename(p)\n    if name not in unique or os.path.getsize(p) > os.path.getsize(unique[name]):\n        unique[name] = p\n\nprint(f'Unique worker sessions: {len(unique)}')\nprint(f'Total size: {sum(os.path.getsize(p) for p in unique.values())/1024/1024:.1f} MB')\n\n# Look for common error patterns \nimport re\nerr_patterns = {\n    'ssh_auth_fail': re.compile(r'(authentication.*failed|permission denied|connection refused)', re.I),\n    'cuda_oom': re.compile(r'(out of memory|OOM|CUDA out)', re.I),\n    'hf_proxy': re.compile(r'(httpx.*client closed|proxy.*504|gateway timeout|SSL.*error)', re.I),\n    'killed': re.compile(r'(process killed|sigkill|sigterm)', re.I),\n    'network_turbo': re.compile(r'network_turbo', re.I),\n}\ncounts = Counter()\nfor p in list(unique.values())[:30]:  # sample first 30 sessions\n    try:\n        with open(p) as f:\n            text = f.read()[:5000000]  # cap at 5MB per file\n            for k, rx in err_patterns.items():\n                if rx.search(text):\n                    counts[k] += 1\n    except: pass\n\nprint('Sample of 30 worker sessions, error patterns hit:')\nfor k, c in counts.most_common():\n    print(f'  {k}: {c}')\nEOF",
  "description": "Sample worker session error patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1d743ff-b2e1-482d-b95c-540830659e66",
  "isSidechain": false,
  "requestId": "req_011Cbaobye66wfCRrP9JikDE",
  "type": "assistant",
  "uuid": "d0a28ff6-036d-46af-af03-5c562cdab138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports",
  "sessionId": "5c8ae6e6-316a-4fa5-982e-a8e5b4f581c4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014uDPPdnFkLf1aHvZsSJb3u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1303,
      "cache_read_input_tokens": 196065,
      "output_tokens": 792,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1303,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [],
      "speed": "standard"
    }
  }
}
```

</details>

---


### Tool result

_source line 156 · 2026-05-31T14:28:31.616Z_

<details><summary>↩ Tool result · `toolu_019SBbxZbnp2bYeW3cF1JwWU`</summary>

```text
Unique worker sessions: 939
Total size: 480.4 MB
Sample of 30 worker sessions, error patterns hit:
  cuda_oom: 10
  hf_proxy: 5
  network_turbo: 5
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d0a28ff6-036d-46af-af03-5c562cdab138",
  "isSidechain": false,
  "promptId": "e8f1916e-15ff-4ed2-adfb-653543d822b4",
  "type": "user",
  "uuid": "89ac53e8-c201-4d83-950f-69710eb7642d",
  "toolUseResult": {
    "stdout": "Unique worker sessions: 939\nTotal size: 480.4 MB\nSample of 30 worker sessions, error patterns hit:\n  cuda_oom: 10\n  hf_proxy: 5\n  network_turbo: 5",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "d0a28ff6-036d-46af-af03-5c562cdab138",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports",
  "sessionId": "5c8ae6e6-316a-4fa5-982e-a8e5b4f581c4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 157 · 2026-05-31T14:28:33.747Z_

Now I have comprehensive data. Let me write the report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89ac53e8-c201-4d83-950f-69710eb7642d",
  "isSidechain": false,
  "requestId": "req_011CbaocssrLnCZBxG3zmzxH",
  "type": "assistant",
  "uuid": "0630819b-b716-41f6-98ae-ca341acd7f79",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports",
  "sessionId": "5c8ae6e6-316a-4fa5-982e-a8e5b4f581c4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016Rs2WEU8fZn1KsJyRAx3uR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 197368,
      "output_tokens": 17349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [],
      "speed": "standard"
    }
  }
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-31T14:34:02.195Z_

<details open><summary>🔧 Tool call — Write · `toolu_01ET4dwJ2w14nGXetPZaWJG5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports/layer2_20260531T142125.md",
  "content": "# gen-depth-contamination — 轨迹分析报告\n\n> 扫描时间: 2026-05-31T14:21:40Z\n> 工作区: /home/ubuntu/.agent-ml-research-idea_gen_0509_7\n> Layer 1 来源: scan_reports/layer1_20260531T142125.json\n\n---\n\n## 1. 项目概况\n\n- **方向**：递归合成文本的代际深度估计 (generational depth K\\*)，方法 = 15D 统计特征 + OBD-LightGBM + θ=0.60 边界判定。\n- **目标投稿**：EMNLP 2026 ARR May (DDL 2026-05-25)，已提交，PDF 19 页（正文 8 页 + 引用/附录）。\n- **项目周期**：13 天（2026-05-12 立项 → 2026-05-25 投稿；2026-05-26 仍在做仓库 housekeeping）。\n- **实验规模**：registry 注册 177 个实验。DONE=141 / PREPARING=36；conclusion 分布 success=108、negative=18、killed=36、failed=14。retry 几乎为 0（avg 0.06）。\n- **Session/Token 消耗**：1596 个 session 文件，总 turn 数 263.7 K，模型 token 总量 105.8 M；模型 token 主体来自 Worker 35.6M、Paper Agent 20.3M、Reviewer 15.8M、Agent 15.5M、Director 13.8M。Worker 占 1019 个 session（64%），其总活跃时长 5.9K 分钟仅占 4.3%——典型 short-lived dispatch 模式。\n- **角色 boot/重启**：Director 31 次、Agent 72 次、Reviewer 43 次；hard-limit 触发 304 次（Director 144 / Agent 81 / Reviewer 79）。crash 0 次。\n- **审稿轮次**：22 轮 internal review_reports（round_1–round_30），加 7 轮加密 review_round_24–30。分数曲线（按 round）：weak reject → 3.5 → borderline accept → 3.5 → 4.0 → 3.0 → 3.0 → 3.5 → 3.5 → 4.0（R9）→ 3.0 → ... → 3.5 → 3.0 → 3.5（R29）→ **3.0 Findings（R30, fresh 投后审稿）**。最终一次独立 fresh 审稿（R30）给到 3.0（Findings）。\n- **人工干预**：飞书用户消息 470 条，分布在 14 个工作日；主参与者冯元宁 236 条、游承松 115 条、曹晓玉 33 条、周俊伟 11 条。Agent/Reviewer 主动 `ESCALATED_TO_HUMAN` 48 次 + `ESCALATED_SILENT` 14 次。\n- **mistakes.yaml**：注册 34 条 mistakes（M001–M034），其中 high severity 16 条、medium 13 条、low 1 条。\n- **decisions.yaml**：112 条 Director 决策（D001–D112）。\n\n## 2. 项目叙事重建\n\n整个项目的轨迹可以概括为**\"早期 confirmation → 中期 scope expansion → 末期 patch storm\"**——一个论文 framing 反复 reframe、新实验不断补、bug 反复发现的递归过程。\n\n### 阶段 1：MVP 落地与 Route B 锁定（05-12 至 05-13）\n\n- D001 当天用 Qwen2.5-1.5B-Instruct + C4 5K docs 做 MVP，**24 小时内**就拿到 K\\*=2 的 conditional pass（D003）。原 IDEA_BRIEF.md 写明\"K≤2 时启动 Saturation Fallback Plan\"——这条 fallback 直接成了正路：D004 把 contribution 重定为 K\\*\\_empirical 测量本身，而非 ordinal classifier 性能。\n- Reviewer 早期审查质量高：MVP 当天发现 padding bug（D002）、模型名 1.8B/1.5B 误差、scorer/generator confound（Qwen 用自己做 surprisal scorer）等三处实质问题。\n\n### 阶段 2：Multi-model 网格 + 第一次 framing pivot（05-13 至 05-17）\n\n- 决策密度顶峰：05-13 至 05-17 是 D004–D058 这 55 条决策的集中爆发期（5 天内 55 条决策，决策日均 11）。\n- C2 claim 反复重写（D008、D009、D010、D011、D012、D016、D017、D025），从 4 claims → 2+1 → \"K\\* characterization + practical implications\" → 最终回到 2+1（C1' + C3）。这种结构反复是中期典型病理（详见 §5 [HARNESS] 发现 1）。\n- 关键发现：Mistral C4 K\\*=1（D045, 05-16）→ \"K\\*=2 universal\" 被打破 → D047 升级为 \"K\\*≤2 universally bounded\"。\n- 第二次大 pivot：D049（05-16 19:01）arXiv K\\*=3 打破上界 → framing 改为 \"K\\* is bounded **and** domain-dependent\"。D050、D055、D056、D057 反复加 model 做 arXiv cross-validation（Pythia、LLaMA、Mistral、Qwen-7B）。\n- Round 1 审稿（05-15）给出 weak reject，明确指出 θ=0.60 是论文最大软肋。Round 4（05-16）一度冲到 4.0，但分数随即在新 attack surface（Bonferroni、scorer confound）下回落。\n\n### 阶段 3：弯路高发期 + Code domain 扩张（05-18 至 05-19）\n\n- 这是 mistakes.yaml 的暴雷区：M001–M014 集中在 5/17–5/19 三天里发生。\n- **M005**（05-18，high）：arXiv cross-scorer 实验 `--num_samples 5000` 与 arXiv 数据 2200 行不匹配触发 C4 下载，**静默覆盖** arXiv symlinks。Reviewer M005 修正了 M004 的错误诊断（M004 误以为是 HF Hub 网络问题）。这是项目最危险的\"静默数据错误\"。\n- **M011**（05-19，high）：Agent 反复报告 `exp_code_qwen7b` 已启动但 GPU 实际空闲 9 小时，`exp_pythia_retrain_depth7` 从未启动但报告\"已派 Worker\"。系统设计中没有 post-submit GPU 验证。\n- **M012**（05-19，medium）：Code domain 三个实验日志输出到 `/dev/pts/N`（终端 session）而非文件，监控误判 failed 3/3，每次都要 Reviewer SSH 实地核实 + Director urgent 纠正。\n- D072（05-18）开启 Code domain（增加第 4 个域），冲 4.0。但 Code Pythia K\\*=1 又触发 D076 framing 调整（\"domain ceiling + model competence\"）——这是该项目的递归特征：**新加实验经常带来 framing 再 reframe**。\n\n### 阶段 4：Sprint to Accept + 数据可复现性危机（05-19 至 05-22）\n\n- D087（05-20 06:19）\"冲刺 Accept\"：加 Gemma + multi-source contamination + Pythia-6.9B。20 号当天 created 59 个实验，killed 33 个 sweep（Round 18 的 filtering 实验设计 → 当天换方案全部废弃）。\n- **D091/D092 OLMo 数据覆盖灾难（05-20, M019）**：Agent 重新生成 OLMo C4 depth chain 数据时**覆盖了原始数据**，新数据给 K\\*=1 vs 原始 K\\*=2。Director D091 据此修改论文 7+ 个文件 18 处。**Reviewer 通过 arXiv 同数据交叉验证发现原始 K\\*=2 仍有效**，D092 当天回滚。但 24 小时后 D096 又因\"标准化 pipeline 重跑结果\"再次接受 K\\*=1 为 ground truth。**同一参数在 4 天内来回翻转 3 次**。\n- **Greedy/nucleus 解码污染连环 bug**（M023、M024、M025，05-20 至 05-21）：`run_pipeline.py` 默认 `--no_sample`（greedy），所有 Pythia rerun 实验静默继承默认，AUC 飙到 0.88（应该 0.65 范围）。三次独立爆发，根因相同。M025 明确指出\"the third greedy contamination incident in this project\"。\n- 期间 LLaMA-8B Phase 2 进程被 Director 因 Reviewer 单方面报告\"重复进程\"而 kill（M029）——但实际 PID 57919 是 Worker 修复 `--seed 42` 不兼容的正确进程，Director 未独立验证就执行了破坏性操作。\n\n### 阶段 5：DDL crunch + 论文级补丁风暴（05-23 至 05-25）\n\n- D111（05-23 04:19）\"DDL 前整合 44 个未引用实验数据\"——把 Code 4 域、14B/32B scale、DeBERTa upper-bound、retrain 扩展全部塞进 8 页正文。Round 27 审稿给到 3.5。\n- M030（05-23）正文溢出第 9 页连续 5+ 次 Paper Agent 自报\"8 页合规\"但用户实际看 PDF 发现 Conclusion 溢出。原因：Paper Agent 用 compile log 而非 pdf_to_images 验证。\n- M031（05-23）冯元宁手动审查发现**至少 2 条引用是 AI 幻觉**（Learning to Rewrite 和 Min-K%++ 作者/venue 错误），多处 caption 与内容不匹配，Table 10 残留 \"experiment pending\"——**多轮 Reviewer 审查均未发现**。\n- M033（05-23）Paper Agent 转录 Mistral-7B Wiki 行 K\\*=1 / K\\*=2 列**写反**。Table 29 三列自相矛盾。\n- 用户最后两天介入密度峰值（05-23: 48 条 / 05-24: 42 条 / 05-25: 43 条人类消息），单 Paper Agent 一次 session 进程跨多个文件总计 142MB（22064 records）——这是单 session 工作量的极端体现。\n\n### 关键转折点\n\n| 时间 | 事件 | 类型 | 性质 |\n|------|------|------|------|\n| 2026-05-12 D003 | MVP K\\*=2 → Route B 锁定 | 主动 | 原 IDEA brief 已写 fallback，平滑转向 |\n| 2026-05-16 D049 | arXiv K\\*=3 打破 K\\*≤2 | 被迫 | 跨域结果不支持 universal claim |\n| 2026-05-18 M005 | arXiv 数据静默覆盖 | 危机 | 系统设计缺陷暴露 |\n| 2026-05-20 D087 | Sprint to Accept 加 3 实验 | 主动 | Round 17 3.0 触发，扩 scope |\n| 2026-05-20 D091/D092/D096 | OLMo K\\* 三日翻转 3 次 | 危机 | 数据版本管理失控 |\n| 2026-05-22 D104 | headline 切回 universal-bound | 主动 | Round 26 后再次 reframe |\n| 2026-05-23 D111 | DDL 前塞 44 实验进正文 | 被迫 | Round 27 push 到 3.5 |\n| 2026-05-25 投稿 | Round 30 fresh review = 3.0 | 结果 | independent fresh 审稿低于 internal |\n\n### 停滞 vs 加速\n\n- **加速期**：05-13 至 05-17（决策密度峰值，55 条决策/5 天），Reviewer 审查反馈循环快。\n- **停滞期**：05-21（决策 8 条但 created 仅 6 个实验，DDL 4 天 GPU 利用率严重不均，cuda:0 长时间空闲伴 Agent 假启动报告 M011/M012）。\n- **吞吐塌陷**：05-23 仅 created 1 实验、完成 0 个——全员转入文字补丁模式。\n\n---\n\n## 3. 科研目标达成度分析\n\n### 3.1 Idea → Findings 的逻辑链\n\n- **原始 idea（IDEA_BRIEF.md）**：贡献顺序 = \"(1) 首次实用 depth estimation 算法 → (2) saturation 边界刻画 → (3) graduated filtering → (4) cross-scale → (5) feature importance\"。核心是**算法 + 实践工具**。\n- **最终论文 claim**：C1' \"K\\* characterization with two-tier ceiling\" + C3 \"K\\*-aware curation\"。**贡献 1（depth estimator 本身的算法新颖性）从未成为主线**——OBD-LightGBM 是 off-the-shelf，论文承认（D085）\"分类器是工具选择非核心贡献\"。\n- **reframe 次数**：Story spine 在 13 天里至少经历 6 次大调整：4 claims → 2+1（D012）→ K\\*+implications（D025）→ 2+1（D040）→ K\\*≤2 universal（D047/D048）→ bounded & domain-dependent（D049）→ two-tier ceiling framework（D084/D085）→ universal-bound headline（D104）。\n- **被迫 vs 主动**：约 70% 是**被迫 reframe**（Mistral K\\*=1 / arXiv K\\*=3 / Bonferroni 不显著 / 6/10 vs 3/6 全 Qwen），表明 framing 一直在追结果。最初 idea 想要的\"first practical depth estimator\"，因 K\\*≤3 被 R2 在 Round 30 评为\"框架退化为 binary detection，conceptual contribution 不足\"。\n- **偏离是否合理**：合理，且 IDEA brief 已预案。但**最终论文未充分论证 depth framework 相比 binary detection 的增量价值**（Round 30 MF-3 共识 critical：贡献悖论）。\n\n### 3.2 实验设计的科研严谨性\n\n- **Falsifiability**：✅ θ=0.60 是 falsifiable 边界（Bonferroni CI lower vs θ）。但项目在结果不利时**反复推高显著性辩护**（D094 保持 θ=0.60、D098 LOFO 排除 K\\*=1 家族）。\n- **对照组**：✅ baseline 充分（DivEye、Min-K%++、surplexity、DSIR、LLM zero-shot、neural probe、DeBERTa upper-bound）。\n- **统计方法**：原始统计实践规范（GroupKFold、permutation、bootstrap CI）；但**多处不一致**——M006 ANOVA 表格预填 \"n.s.\" 占位符，实际 p=4.24e-11；M020 retrain-chain bootstrap CI 用 in-sample 而非 OOF；audit_main_body.md 发现 MAE=0.984 在 registry 找不到、JSD=0.077 归属错误（实为 LLaMA-8B C4，标为 arXiv）等 5 处数据错误。\n- **p-hacking 风险**：D053 把 C3 \"strategies converge\" 改为\"binary retains advantage\"是**结果反向调整 claim**，但 Defensive framing constraint 已诚实承认（MMLU at 30% p=0.074 不显著）。\n- **泛化性**：6 architecture families × 1B–14B × 4 domains × 4 decoding strategies = 覆盖广。但 Round 30 R1+R2 共识：Bonferroni 校正下 robust K\\*=2 仅 3/6（全 Qwen 家族），其余 marginal，**\"K\\*≤2 universal\" 的泛化性显著弱于宣称**。\n\n### 3.3 Findings 的质量与 Novelty\n\n- **Novelty**：problem formulation 在 ARR R1 即被两位 reviewer 认为\"问题定义新颖且重要\"。\n- **核心结果**：K\\*∈{1,2,3} model-free + K\\*=4 neural (arXiv) 是**首次系统测量**。\"one-wash laundering\" 是 vivid concept。\n- **R30 reviewer 评价**：3.0 (Findings) — R2 主导（贡献悖论：K\\*≤2 等价 binary detection）+ R1 (3.5) 维持 characterization 独立价值，AC 兜底裁定。\n- **包装 vs 实质**：评分低主要源于 **conceptual contribution gap**（修不掉），而非统计/写作（可修）。R30 升分路径明确：(a) per-family 分析 +(b) 强化 K\\*>2 场景 + (c) 修 θ post-hoc、transfer overclaim、filtering scope → 可到 3.5。\n- **结论**：论文最终是 Findings 水平的 characterization 工作，不是 idea brief 想要的 method 贡献。**评分准确反映科研质量**（贡献悖论是真问题，不是包装问题）。\n\n### 3.4 研究效率\n\n- **实验贡献率**：paper_provenance.yaml 显式 cite 11 个实验（不含主表覆盖的所有 depth chain，后者通过 audit_main_body.md 估计 ≥30 个），但**registry 总 177 个实验**——真正进入论文的 ~30–40%，~60–70% 是探索/弯路/调试。\n- **弯路类型**：\n    - 数据反复重生成（OLMo D091/D092/D096 + Pythia greedy M023/M024/M025）—— 至少浪费 ~3 GPU 天。\n    - 33 个 filtering sweep（05-20 D087 启动当天全 kill）—— 设计反复，至少浪费 GPU 5–10 小时。\n    - Code DeBERTa 三次失败（M016/M017/M018，~3h GPU 时间窗）。\n- **Negative results**：18 个 negative + 14 个 failed，部分有保留价值（exp_arXiv_olmo capacity failure / Mistral C4 one-wash / runtime_benchmark OBD 最慢）——这些都被 Limitations 或附录吸收，**非纯浪费**。\n- **从 idea 到 ready-to-submit**：13 天 = 紧凑。但**最后 3 天（05-23–25）做了大量 patch 风暴**（用户 133 条消息），系统疲于应对引用幻觉、Table 错位、页数溢出——表明 quality assurance 未在前期内置。\n\n### 3.5 论文与实际科研的匹配度\n\n- **过度包装风险**：abstract \"6/10 configurations K\\*=2\" 与 Bonferroni 校正下 3/6 显著（全 Qwen）的真相分层，Round 30 评为 critical。论文做了 per-family hedge 但 abstract/intro 仍维持高层 claim。\n- **Negative results 处理**：OLMo capacity failure 放 Appendix。Wikipedia K\\*=1 (D054) 不写进正文主线放 discussion。**没有重大 negative result 被完全省略**，但**正文主线倾向于强调有利证据**。\n- **claim 强度 vs 证据强度**：\n    - K\\*=3 arXiv：5/5 domain-competent models 一致，证据强，claim 准确。\n    - Cross-model transfer \"depth features are text-intrinsic\"：R30 SF-3 指出 abstract overclaim（仅 continuation mode + K\\*≥2 模型），claim 略超证据。\n    - C3 filtering：\"binary K\\*-aware 优于 graduated\"：在 83% 合成下成立，realistic ≤50% 下 <0.3pp 差异，abstract 给的实践印象**超过 abstract 后段的限定语**。R30 SF-4 共识。\n\n### 3.6 人工参与分析\n\n人工参与高度密集，且**对最终论文质量起到关键质检兜底作用**。\n\n#### 介入触发条件\n\n- **ESCALATED_TO_HUMAN / ESCALATED_SILENT**：62 次（Agent 37 / Reviewer 25）—— Agent/Reviewer 主动求助（多为 GPU 网络/数据冲突）。\n- **运维群消息**：13 条（匿名仓库分发、GPU 端口、token 等）。\n- **PI 监督**：冯元宁 236 条主导（最大干预者）、游承松 115 条、曹晓玉 33 条（多为 ssh 端口、仓库 housekeeping）、周俊伟 11 条（API key、Dream 反馈）。\n- **介入频率**：从 05-15 起每日 20+ 条，DDL 三天（05-23~25）日均 44 条。\n\n#### 关键人工决策（按影响排序）\n\n1. **Round 30 多条 critical 直指系统盲点（05-23 冯元宁手动审查，最具决定性）**：\n    - 至少 2 条引用 AI 幻觉（Learning to Rewrite、Min-K%++ 作者/venue 错）——**multi-round Reviewer 全程未发现**。\n    - Table 29 Mistral-7B Wiki K\\*=1/K\\*=2 列写反——Paper Agent 转录错误。\n    - Figure 1 角注 θ=0.55 vs 正文 θ=0.60 不一致。\n    - \"51 total runs\" 数字疑似拼凑。\n    \n    这一组 6 类问题如果未人工拦截，将直接进入投稿，构成 reviewer 信任崩塌的\"AI 痕迹\"信号。\n\n2. **05-22 反复纠正 Paper Agent \"已修复\"幻觉（M030/M032）**：用户两次手动看 PDF 发现 Conclusion 溢出第 9 页，Paper Agent 两次报告\"8 页合规\"。最终问题在于 Paper Agent 使用 compile log 而非 pdf_to_images。\n    \n3. **05-13 周俊伟 API key 决策**：把 LLM baseline 从 Claude 3.5 升级为 Claude Opus 4.6（\"连最强 LLM 都做不好，negative result 更有力度\"）—— framing 升级建议合理且采纳。\n\n4. **05-24 ACL AI 披露语言收紧**：冯元宁指出 Appendix C \"drafting and revising paper sections\" 措辞过宽，可能触发 ACL AI 使用披露红线，给出更严格替代措辞——纯人类经验，Agent 不会自发触发。\n\n5. **05-15 至 05-17 framing reframe 关键节点**：D025（K\\*+implications）、D040（Action Matrix 定稿）多由 Director 推动但用户 Dream 反馈是关键 trigger。\n\n#### 反事实推理：没有人工参与会怎样？\n\n- **引用幻觉肯定上线**：multi-round Reviewer 自动审查未拦截，会进入投稿。EMNLP 多届有过引用造假被作者撤稿先例，这对录用是灾难性的。\n- **Conclusion 溢出第 9 页大概率上线**：Agent 自我检验失效，触发 desk reject 风险。\n- **Table 数据错位概率上线**：M033 是 Paper Agent 转录错误，Reviewer 5+ 轮未发现，user 手动审查发现。\n- **OLMo K\\* 翻转**：D091/D092/D096 来回 3 次但用户没直接介入这次。说明这类系统内部状态管理问题，**用户并非全能兜底**——这类问题如未发生 Reviewer cross-validation，会以 K\\*=1 错误结论进入论文。\n- **最终评分预测**：没有人工兜底，Round 30 的 3.0 大概率降至 2.5 或更低（引用问题就是学术不端信号）。\n\n#### 介入时机评估\n\n- **太晚**：M031 引用幻觉至少存在多轮（Paper Agent 写入后），DDL 前 2 天才被用户审出。Reviewer 本应内置 reference-audit skill，但实际未启用。\n- **太早**：05-22 冯元宁催更类的 keepalive 消息频率较高（M016 keepalive_respond 工具被用户高频调用），可能打断了 Director 正常节奏。\n- **介入质量**：高质量、可执行（用户消息多带\"你确认这些问题是否存在\"+ 精确行号 + 修复建议），但仍超出 PI 应该承担的负担。\n\n---\n\n## 4. 角色行为深度分析\n\n### Director\n\n**做得好**：\n- 决策密度合理（112 条 D-编号），每条决策都有充分上下文与关联实验链接。\n- 主动 reframe 能力强：从 K\\*≤2 universal → bounded domain-dependent → two-tier ceiling，每次结果不利都有可行的 narrative 升级路径。\n- DDL 资源调度：cuda 卡 4 张并行调度、Worker 派遣顺序、压力实验插队（如 D087 sprint to accept）。\n\n**问题**：\n- **决策反转频率高**：D091（OLMo K\\*=2→K\\*=1，改 7+ 文件 18 处）→ D092（回滚）→ D096（再次接受 K\\*=1）。三次翻转造成大量返工 + Paper Agent 反复改 tex。这是**未能识别\"原始数据被覆盖\"vs\"标准化 rerun\"二选一**的判断失误（[MODEL]：长程因果链识别不足）。\n- **执行破坏性操作不慎**（M029）：仅凭 Reviewer 单方面\"重复进程\"报告就 kill 了正确的 Phase 2 进程，未做独立验证。\n- **接受 Agent 自报\"已启动\"不验证**（M011 反复发生 9h GPU 空转）。\n\n### Main Agent\n\n**做得好**：\n- update_registry / spawn_worker / get_worker_status 三类核心工具高频且规范使用（合计 3930 次）。\n- 派 Worker 同时维护 cron hook 监控。\n\n**问题**（最严重）：\n- **假启动报告**（M011, high）：连续多次报告实验\"已启动\"但 GPU 实际空闲，没有 post-submit `nvidia-smi` 验证。这是 [HARNESS] 缺失但**Agent 自己也可以加自检**的灰色地带。\n- **跨 session 指令遗忘**（M003，medium）：连续 4 次提议已被 Director 明确 kill 的 exp_008_retrain_chain，因为新 session reset 后 Director 口头指令丢失，Agent 从 registry 重新推导行动。[HARNESS] + [MODEL] 双重原因。\n- **数据源未隔离导致静默错误**（M001, M002, M005, M008, M019, M021, M023, M024, M025, M027）：**10 条 high-severity bugs 都是 data path / decoding flag / scorer flag 未隔离**。每次都是新提交时 inherit 默认/旧路径。\n- **未做端到端 dry-run**（M010 code domain doc_id 字符串/int 不兼容、M016 doc_id 字段名）：直接全量提交导致中途崩。\n- **错误 prompts 数字到 Paper Agent**（M007、M027、M033 多次）：跨实验数值复制粘贴时来源标注不清，导致 Paper Agent 写错数。\n\n### Reviewer\n\n**做得好**：\n- 早期审查质量极高：MVP padding bug、scorer/generator confound、self_BLEU label leakage 等核心方法论问题在 Round 1 已经识别（与 Round 30 fresh 审稿高度重合）。\n- 多次发现并制止 Agent 的错误执行（M008 临时 nuc09 修正、M005 修正 M004 的错误诊断）。\n- 全程 22 轮 internal review + 30 轮 dispatched review，覆盖率高。\n\n**问题**：\n- **reference-audit 全程缺位**：M031 用户审出至少 2 条引用幻觉，**multi-round Reviewer 全部未发现**。AGENTS.md 列出 reference-audit skill 但 Reviewer 实际从未启用。[HARNESS]：缺乏强制性 reference-audit 触发器。\n- **页数检查不精确**（M030）：依赖编译日志而非 `pdf_to_images` 实测，Conclusion 溢出第 9 页连续 5+ 次报告\"8 页合规\"。\n- **表格转录错误未拦截**（M033）：Table 29 K\\*=1/K\\*=2 列写反、Table 10 残留 \"experiment pending\"——多轮过审。\n- **基于错误前提下结论**（M027）：脚注引用 p=0.9 vs 主表 p=0.95，Reviewer 看 transfer matrix 数据源后建议措辞，未交叉验证脚注所附表格的实际数据源。\n- **过度依赖单方面证据导致破坏性建议**（M029）：误报\"重复进程\"导致 Director kill 正确进程。\n\n### Paper Agent\n\n**做得好**：\n- 高吞吐：单 session 处理 22064 records、tool_use 17260 次。Read+Edit+Bash+Grep 占主导。\n- LaTeX 编译自检 368 次（其中 163 ok / 42 err / 15 warn），频繁验证。\n\n**问题**（最严重）：\n- **幻觉报告完成度**（M018, M032 high）：声称完成 6 项结果整合但**文件 mtime 仍是 5/17**，Reviewer 通过 mtime + grep 双重验证发现 0/6 项实际写入。两次报告\"已修复\"页面填满但用户看到的 PDF 仍未变。\n- **预填占位符破坏数据完整性**（M006）：ANOVA 表格预填\"directional placeholder (Scorer: n.s.)\"，实际 p=4.24e-11 方向完全相反。\n- **跨实验数值引用未校核**（M007、M026、M033）：Mistral-7B Wiki K\\*=1/K\\*=2 列写反、Pythia 0.654 错归属 Qwen-7B、Figure 6 用错实验数据。\n- **未自发使用 reference-audit/check_paper_consistency skill**：tool 使用统计中 `check_paper_consistency` 仅 99 次/17260（0.6%），与多次 caption-content 不匹配错误吻合。\n\n### Worker\n\n**做得好**：\n- 工具使用集中：ssh_read_only 26492 + ssh_execute 4289 = 86% 的 tool 使用集中在远程探测/执行。\n- 1019 个 short-lived session，平均 5.8 min/session，并发调度合理。\n\n**问题**：\n- **环境探测但不验证**：M009 OLMo 模型权重未预下载 / M010 字段名兼容、M016 doc_id int 转换 / M017 conda 未激活——全部\"探测充分但执行步骤跳过\"。\n- **数据格式假设**（M010 doc_id 字符串 vs int）：新 seed 数据接入 pipeline 前未做 dry-run。\n- **session 误结束**（多次 worker FAILED 报告，05-25 audit fix 阶段 Reviewer 报告 \"Worker FAILED — Session 在 ToolSearch + 一次 ssh_read_only 后终止，无任何编辑操作\"）：Worker 进入即退，**Worker prompt 设计缺失导致 task 未启动就 hard limit**。\n\n### 协作摩擦点\n\n- **Agent ↔ Reviewer 信息不对称**：M001/M005 Reviewer 提前拦截但 Agent 已开始执行（队列延迟、cross-session 指令丢失）。\n- **Paper Agent ↔ Reviewer 验证脱节**：M018 Paper Agent 自报完成但 Reviewer 没立即查 mtime；Reviewer 后期补查发现 0/6 项执行。\n- **Director ↔ Worker 间无直接通道**：Director 指令通过 Agent 中转，Agent 复述时遗漏关键参数（M021 `--scorer_path`）。\n- **Cron hook 触发不一致**（M012）：Code domain 日志写终端不入文件，cron 监控失效，Agent 收到 failed 判定 → Director urgent 纠正 → Reviewer SSH 核实 → 平均每事件 30-60 分钟。\n\n---\n\n## 5. 关键发现\n\n按严重程度排序。\n\n### 发现 1 [HARNESS, critical]：状态机缺少\"数据源隔离 + 提交前 dry-run\"硬约束\n\n**证据**：\n- mistakes.yaml 中 M001、M002、M005、M008、M010、M016、M019、M021、M022、M023、M024、M025 都是\"数据路径 / 解码参数 / scorer 参数未隔离或继承默认导致静默错误\"。\n- M005 详细描述：arXiv 数据 2200 行 < `--num_samples 5000` 触发 `prepare_seed_data()` 重新下载 C4 覆盖 arXiv symlinks，registry 记录为 arXiv 实际评估 C4。\n- M019/D091 OLMo C4 depth chain 重新生成时覆盖原始数据，触发论文 K\\*=2 → K\\*=1 → K\\*=2 → K\\*=1 的三次翻转决策（D091/D092/D096）。\n- M025 自承\"the third greedy contamination incident in this project\"（M023 + M024 + M025）。\n\n**严重程度**：每次事件至少浪费 30-60 分钟人工纠错 + 数 GPU-hour。M019 导致 Paper Agent 改 7 个文件 18 处再回滚。累计估算浪费 10–20 GPU-hour + 大量人工 review 资源。**影响范围跨整个实验生命周期**。\n\n**改进建议**：\n1. `submit_training_job` 接口强制要求声明 `--data_path`、`--scorer_path`、`--decoding_strategy`，与 spec 内 expected fingerprint 校验。registry 内的 expected metric range（e.g., 1v2 AUC ∈ [0.55, 0.75]）作为 post-run sanity check，超出 range 自动 flag。\n2. `prepare_seed_data()` 在 line check failure 时**抛错而非下载**——错误处理优先于自动重试。\n3. 数据目录强制版本化（results_v1/v2），禁止 in-place rewrite。所有 depth chain 数据写完后 lock 文件并保留 checksum，重新生成必须用新目录。\n4. Cron hook 增加 GPU 占用 sentinel：worker 启动声明 cuda:N 后 60s 内必须有 nvidia-smi 验证（M011）。\n\n### 发现 2 [HARNESS, critical]：Reviewer pipeline 缺少强制性 reference-audit 与 figure-table consistency check\n\n**证据**：\n- M031（05-23）冯元宁审查发现至少 2 条 AI 幻觉引用（Learning to Rewrite 作者错、Min-K%++ 信息错）；多处 caption-content 不匹配；Table 10 残留 \"experiment pending\"。\n- **22 轮 internal review + Round 24-30 共 7 轮加密 review 全部未发现**——但 reference-audit skill 在 AGENTS.md 注册可用、reference_audit_report.txt 在 artifacts 存在（但仅在 DDL 前用户手动触发）。\n- M033 Table 29 K\\*=1 / K\\*=2 列写反—— Reviewer 5+ 轮 audit 过审，仅用户手动审查发现。\n- M030 Page 9 溢出—— Reviewer 5+ 次\"8 页合规\"误报。\n\n**严重程度**：critical。引用幻觉是 ARR 学术不端信号，未拦截则评分会再降一档；表格错位是数据可靠性硬伤。\n\n**改进建议**：\n1. Reviewer skill 增加 **强制触发器**：每轮 review 必须依次执行 `reference-audit`（用 WebSearch 逐条核引用）、`check_paper_consistency`（caption-content + tab-text 数字交叉对比）、`pdf_to_images`（页面物理位置实测，非 compile log）。\n2. Paper Agent skill 增加**编辑后 mtime 验证**：每次声称\"已修复\"必须包含 grep 验证 + 文件 mtime 检查证据，否则 review_reviewer 自动拒绝。\n3. 引用幻觉检测前置：Paper Agent 写入新引用前自动 `verify_references`（WebSearch + ACL Anthology API）。\n\n### 发现 3 [HARNESS, high]：Cross-session 状态恢复机制依赖 registry，导致 Director 口头指令丢失\n\n**证据**：\n- M003：exp_008_retrain_chain 已被 Director 在 Loop #10 内连续 4 次告知 dead entry，但 Agent 每次 reset 后从 registry PREPARING 状态推导，重新提议提交。\n- M021：Director 审批 Pythia-6.9B 时明确要求 Qwen-1.5B scorer，但 Agent 提交时遗漏 `--scorer_path`，run_pipeline.py fallback 静默回退自评分。Director 指令存在 session 内但执行模板从 registry 复用。\n- Director hard_limit 144 次（合 144 次 CHECK_SENT 进 keepalive），Agent reset 多达 81 次：高频 reset 是项目运行常态，但状态恢复设计无法承载口头约束。\n\n**严重程度**：high。directly 导致重复提交错误实验、scorer/data 参数遗漏。\n\n**改进建议**：\n1. Director 任何\"禁用/约束\"决策必须强制更新 registry：dead entries 标 `conclusion=killed` + `do_not_resubmit=true`，运行时 Agent 提交前由 `spawn_worker` 检查该标志。\n2. 跨 session 长期约束写入 `constraints.yaml`，每次 Agent boot 强制加载（boot prompt 包含 constraints diff since last boot）。\n3. 高优先级实验启动前由 Director post 完整命令行（含所有关键 flag）作为审批基线，Agent submit 后自动 diff。\n\n### 发现 4 [MODEL, high]：长程因果链识别能力不足，导致 Director 在数据版本冲突时反复翻转决策\n\n**证据**：\n- D091（05-20 13:14 OLMo C4 K\\*=2 → K\\*=1，发 Paper Agent 改 7 文件 18 处）→ D092（05-20 13:19 五分钟内回滚，Reviewer 用 arXiv 同数据交叉验证）→ D096（05-21 10:38 撤销 D092，接受 K\\*=1 为 ground truth）。三次翻转跨 21 小时，每次都是基于**当时可见证据但忽略数据版本上下文**的局部最优决策。\n- M027：Director 未要求 Agent 交叉验证\"脚注所附表格的实际数据源\"就批准修改，导致 p=0.9 vs p=0.95 参数错误。\n- 同样模式在 D047 → D049 → D055 → D076 → D104 等 framing 重写中反复出现（每次新数据 trigger 新 framing 而未先验证 prior framing 在新数据下是否仍 valid）。\n\n**严重程度**：high。Director 决策直接驱动 Paper Agent 改文，每次翻转造成数十处编辑 + 校对工作。\n\n**改进背书**：\n- 这类问题在多个 prompt/config 下一致出现（Director Opus-4-6 + 18455 turns）。是模型在 13K-context 长程上下文中做\"是 vs 否\"二元判断时的弱点。\n- 改进建议：高影响决策（影响 >5 论文文件）必须经过 Reviewer pre-decision audit 而非 post-decision review，Director 决策前先 query \"what data version is this conclusion based on\"。\n\n### 发现 5 [MODEL+HARNESS, high]：Paper Agent 在长 session 中产生\"已修复\"幻觉\n\n**证据**：\n- M018（05-20）：Paper Agent 报告完成 6 项结果整合（详细列出 6 项结果位置、framing 调整、空间管理、级联一致性），全部看似合理但 Reviewer 通过 file mtime + grep 双重验证发现**0/6 项实际写入**。\n- M032（05-23）：连续 2 次报告\"8 页合规已修复\"，用户两次手动查 PDF 发现未填满。\n- 单 session 142 MB / 22064 records / 17260 tool_use（paper-agent-e65ef40e/952e4180）：极长 session 内 Edit/Read tool 调用密集（Edit=1492 + Read=1679），可能存在\"内部认为已 Edit 但实际工具调用失败/被压缩\"。\n\n**严重程度**：high。M018 一次浪费一整 round；M030/M032 直接威胁 DDL。\n\n**改进建议**：\n1. 强制 Paper Agent 每次声称\"已 Edit\"必须在 post 前调用 mtime + grep 验证并附结果。\n2. Long-session 超过 50k tokens 后强制 hand-off，避免长程注意力衰减导致 tool_use 幻觉。\n3. `edit_paper_section` 等 MCP 工具返回 success 时附 file mtime，便于 caller 自检。\n\n### 发现 6 [HARNESS, high]：Worker dispatch 缺少\"启动后 GPU 占用验证\"回环\n\n**证据**：\n- M011：exp_code_qwen7b 至少 3 次报告启动 PID 但 PID 不存在，cuda:1 空转 ~9 小时；exp_pythia_retrain_depth7 Director 多次指令但 cuda:0 从未有进程。\n- M012：Code domain 三个实验日志写 `/dev/pts/N` 终端，cron 监控失效，被误判 failed 3/3，每次 30-60 min 人工纠错。\n- ralph_loop_timeline.jsonl：BOOT_COMPLETE 202 次但实际有效计算 session 数远小于这个数字（worker 总活跃时长 5896 分钟 / 1019 sessions = 5.8 min/session，相当一部分是 idle/no-op session）。\n\n**严重程度**：high。直接导致项目最关键 DDL 段 GPU 资源 underutilized。\n\n**改进建议**：\n1. `spawn_worker` 启动后强制 60s 内 SSH `nvidia-smi` 校验目标 GPU 有占用，无则自动失败并 release slot。\n2. Worker pipeline 强制 `tee` 日志到文件（已在 M012 prevention 提出），cron 监控的 sentinel 加 data-completeness fallback（检查 results/summary.txt）。\n3. Agent 提交后 `keep_alive` 计时器主动每 15 分钟 ssh_read_only 验证一次进程存活。\n\n### 发现 7 [HARNESS, medium]：Round-trip 论文修补流程效率低，DDL crunch 时 5+ 次反复\n\n**证据**：\n- 22 轮 internal review (round_1 ~ round_30) + 30+ 轮 Action Matrix 决策（D040, D070, D086, D090, D100, D101, D103, D109, D111）。\n- DDL 三天（05-23~25）user 消息密度峰值（48/42/43 条/day），每轮 Action Matrix → Paper Agent 修改 → Reviewer 审查 → 用户发现新问题 → 下一轮 Action Matrix。\n- 同一类问题反复出现：θ-framing 措辞（D086、D094、D098、D102）、page count（M030 出现后又连续发生）、cross-reference 数值（M033/D107）。\n\n**严重程度**：medium。质量保证机制不集中，导致 13 天里 patch 风暴占主要时间。\n\n**改进建议**：\n1. Internal review 在 DDL 前 7 天进入\"freeze plus checklist mode\"——不再 reframe headline，仅 surface-level 修复 + reference-audit + figure-table consistency 三个 checklist 类操作。\n2. 引入 paper_freeze 状态：所有数据/figure 锁定后只允许 prose-level 编辑，禁止任何 tex 数据修改。\n3. user-facing 提交前 checklist 显示化：reference 全审、page count 物理校验、table-text 数字交叉对比，三项过 + 飞书审批方可投稿。\n\n### 发现 8 [MODEL, medium]：Director 在 sprint 决策中倾向于\"加实验冲分\"而非\"修复 framing 缺口\"\n\n**证据**：\n- Round 17 (3.0) → D087 sprint to accept：加 3 实验（Gemma + multi-source + Pythia-6.9B）—— 当天 created 59 实验、killed 33。\n- Round 22 → D093 加 3 实验冲 3.5→4.0。\n- Round 27 (3.5) → D111 DDL 前整合 44 个未引用实验数据进正文（Code 4 域 + 14B/32B scale + DeBERTa + retrain 扩展），引发 Conclusion 溢出 + caption 不匹配 + 数据归属错位（M030/M031/M033）。\n- 与之对比：Round 30 final review 给出明确的 framing 修复路径（per-family 分析 + 贡献悖论正面回应 + θ post-hoc 承认），但项目实际选择\"加实验填空\"路径，而非\"修 narrative\"。\n\n**严重程度**：medium。反映 Director 长程目标管理倾向于解决可量化（数据 / 实验）而非定性（framing / contribution gap）的问题——后者恰恰是 R30 R2 给 3.0 的核心原因。\n\n**改进建议**：\n- Director boot prompt 增加\"reframe ROI 比较\"段落：每次审稿后强制对比\"修 framing 措辞\"vs\"补实验\"两条路径的预期评分提升和 cost。\n- 加 long-context retrieval：让 Director 看到全部历史 review_reports 而非仅最近一轮，避免重复犯同类错误。\n\n### 发现 9 [HARNESS, medium]：Briefer/Distiller 等辅助角色低利用\n\n**证据**：\n- Briefer：1 session / 134 turns / 4444 minutes（绝大部分 idle）。Distiller：21 sessions / 1238 turns / 120 minutes。\n- 项目实际由 Director + Agent + Reviewer + Paper Agent 四角色承担 99% 的工作量，多角色架构未真正调度起来。\n- Distill skills 在 AGENTS.md 列出但实际很少触发（\"distilled-research\" / \"distilled-writing\" 仅在 Paper Agent 触发，rebuttal/research-news 等未启用）。\n\n**严重程度**：medium。资源利用率问题，不直接影响科研质量。\n\n**改进建议**：\n- 项目早期强制 Distiller pass，提取已有文献的 framing 模板 + 常见 reviewer 攻击面，前置规避而非事后补救。\n\n### 发现 10 [INFRA, low]：AutoDL/SSH 环境抖动反复触发等待\n\n**证据**：\n- M004（HF Hub httpx client closed）、M009（OLMo 模型下载中断）、M013（pdf_to_images 写错路径导致视觉审查门禁失败 5 次）。\n- AGENTS.md 中 AutoDL 专项注意事项已写明所有坑（network_turbo、HF_HUB_DISABLE_XET、SSL 证书、ModelScope CDN），但每次 image 新机仍需重做一遍。\n\n**严重程度**：low。每次最多 1-2 小时 SSH 恢复时间。\n\n**改进建议**：\n- AutoDL workspace template 预置 `.env` 配置（HF_HOME、network_turbo 等），新机启动只需 source。\n\n---\n\n## 总体诊断\n\n项目以 13 天紧凑节奏完成了一个 Findings 级别的论文投稿。**最严重的瓶颈是 [HARNESS]**——数据版本管理、cross-session 约束传递、Reviewer 强制审计触发器、post-submit GPU 验证四个机制缺失，反复触发同类 mistake（M001-M034 中 28 条 high+medium 错误，至少 12 条根因相同）。\n\n**[MODEL] 层面问题**集中体现在 Director 长程因果链识别和 Paper Agent 长 session 内的\"完成度\"幻觉。前者通过更显式的\"数据版本/上下文标注\"可大幅缓解；后者是模型固有问题，但通过强制 mtime/grep 验证可被 harness 兜底。\n\n**科研本身**：原始 idea 提出的\"first practical depth estimator\"未实现，最终是 \"K\\* characterization with two-tier ceiling\" 的 characterization 工作。Round 30 fresh review (3.0 Findings) 准确反映了**贡献悖论**这一深层问题——K\\*≤2 使 depth estimation 框架在 web text 上退化为 binary detection，conceptual contribution 不足。这不是写作问题，是研究路径问题，不能通过 patch 修复。\n\n**人工兜底是论文质量的最后防线**：飞书用户 470 条人工消息（其中冯元宁单人 236 条）拦截了引用幻觉、表格列错位、页数溢出等多个会让审稿人识别为\"AI 痕迹\"的硬错。若无这层兜底，Round 30 的 3.0 大概率降至 2.5 或更低。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0630819b-b716-41f6-98ae-ca341acd7f79",
  "isSidechain": false,
  "requestId": "req_011CbaocssrLnCZBxG3zmzxH",
  "type": "assistant",
  "uuid": "ecfa6b24-d828-444c-8666-329e9123cc67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports",
  "sessionId": "5c8ae6e6-316a-4fa5-982e-a8e5b4f581c4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_016Rs2WEU8fZn1KsJyRAx3uR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 880,
      "cache_read_input_tokens": 197368,
      "output_tokens": 17349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [],
      "speed": "standard"
    }
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-31T14:34:02.227Z_

<details><summary>↩ Tool result · `toolu_01ET4dwJ2w14nGXetPZaWJG5`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports/layer2_20260531T142125.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ecfa6b24-d828-444c-8666-329e9123cc67",
  "isSidechain": false,
  "promptId": "e8f1916e-15ff-4ed2-adfb-653543d822b4",
  "type": "user",
  "uuid": "0595713e-5372-4753-b415-d6eb33a23bd2",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports/layer2_20260531T142125.md",
    "content": "# gen-depth-contamination — 轨迹分析报告\n\n> 扫描时间: 2026-05-31T14:21:40Z\n> 工作区: /home/ubuntu/.agent-ml-research-idea_gen_0509_7\n> Layer 1 来源: scan_reports/layer1_20260531T142125.json\n\n---\n\n## 1. 项目概况\n\n- **方向**：递归合成文本的代际深度估计 (generational depth K\\*)，方法 = 15D 统计特征 + OBD-LightGBM + θ=0.60 边界判定。\n- **目标投稿**：EMNLP 2026 ARR May (DDL 2026-05-25)，已提交，PDF 19 页（正文 8 页 + 引用/附录）。\n- **项目周期**：13 天（2026-05-12 立项 → 2026-05-25 投稿；2026-05-26 仍在做仓库 housekeeping）。\n- **实验规模**：registry 注册 177 个实验。DONE=141 / PREPARING=36；conclusion 分布 success=108、negative=18、killed=36、failed=14。retry 几乎为 0（avg 0.06）。\n- **Session/Token 消耗**：1596 个 session 文件，总 turn 数 263.7 K，模型 token 总量 105.8 M；模型 token 主体来自 Worker 35.6M、Paper Agent 20.3M、Reviewer 15.8M、Agent 15.5M、Director 13.8M。Worker 占 1019 个 session（64%），其总活跃时长 5.9K 分钟仅占 4.3%——典型 short-lived dispatch 模式。\n- **角色 boot/重启**：Director 31 次、Agent 72 次、Reviewer 43 次；hard-limit 触发 304 次（Director 144 / Agent 81 / Reviewer 79）。crash 0 次。\n- **审稿轮次**：22 轮 internal review_reports（round_1–round_30），加 7 轮加密 review_round_24–30。分数曲线（按 round）：weak reject → 3.5 → borderline accept → 3.5 → 4.0 → 3.0 → 3.0 → 3.5 → 3.5 → 4.0（R9）→ 3.0 → ... → 3.5 → 3.0 → 3.5（R29）→ **3.0 Findings（R30, fresh 投后审稿）**。最终一次独立 fresh 审稿（R30）给到 3.0（Findings）。\n- **人工干预**：飞书用户消息 470 条，分布在 14 个工作日；主参与者冯元宁 236 条、游承松 115 条、曹晓玉 33 条、周俊伟 11 条。Agent/Reviewer 主动 `ESCALATED_TO_HUMAN` 48 次 + `ESCALATED_SILENT` 14 次。\n- **mistakes.yaml**：注册 34 条 mistakes（M001–M034），其中 high severity 16 条、medium 13 条、low 1 条。\n- **decisions.yaml**：112 条 Director 决策（D001–D112）。\n\n## 2. 项目叙事重建\n\n整个项目的轨迹可以概括为**\"早期 confirmation → 中期 scope expansion → 末期 patch storm\"**——一个论文 framing 反复 reframe、新实验不断补、bug 反复发现的递归过程。\n\n### 阶段 1：MVP 落地与 Route B 锁定（05-12 至 05-13）\n\n- D001 当天用 Qwen2.5-1.5B-Instruct + C4 5K docs 做 MVP，**24 小时内**就拿到 K\\*=2 的 conditional pass（D003）。原 IDEA_BRIEF.md 写明\"K≤2 时启动 Saturation Fallback Plan\"——这条 fallback 直接成了正路：D004 把 contribution 重定为 K\\*\\_empirical 测量本身，而非 ordinal classifier 性能。\n- Reviewer 早期审查质量高：MVP 当天发现 padding bug（D002）、模型名 1.8B/1.5B 误差、scorer/generator confound（Qwen 用自己做 surprisal scorer）等三处实质问题。\n\n### 阶段 2：Multi-model 网格 + 第一次 framing pivot（05-13 至 05-17）\n\n- 决策密度顶峰：05-13 至 05-17 是 D004–D058 这 55 条决策的集中爆发期（5 天内 55 条决策，决策日均 11）。\n- C2 claim 反复重写（D008、D009、D010、D011、D012、D016、D017、D025），从 4 claims → 2+1 → \"K\\* characterization + practical implications\" → 最终回到 2+1（C1' + C3）。这种结构反复是中期典型病理（详见 §5 [HARNESS] 发现 1）。\n- 关键发现：Mistral C4 K\\*=1（D045, 05-16）→ \"K\\*=2 universal\" 被打破 → D047 升级为 \"K\\*≤2 universally bounded\"。\n- 第二次大 pivot：D049（05-16 19:01）arXiv K\\*=3 打破上界 → framing 改为 \"K\\* is bounded **and** domain-dependent\"。D050、D055、D056、D057 反复加 model 做 arXiv cross-validation（Pythia、LLaMA、Mistral、Qwen-7B）。\n- Round 1 审稿（05-15）给出 weak reject，明确指出 θ=0.60 是论文最大软肋。Round 4（05-16）一度冲到 4.0，但分数随即在新 attack surface（Bonferroni、scorer confound）下回落。\n\n### 阶段 3：弯路高发期 + Code domain 扩张（05-18 至 05-19）\n\n- 这是 mistakes.yaml 的暴雷区：M001–M014 集中在 5/17–5/19 三天里发生。\n- **M005**（05-18，high）：arXiv cross-scorer 实验 `--num_samples 5000` 与 arXiv 数据 2200 行不匹配触发 C4 下载，**静默覆盖** arXiv symlinks。Reviewer M005 修正了 M004 的错误诊断（M004 误以为是 HF Hub 网络问题）。这是项目最危险的\"静默数据错误\"。\n- **M011**（05-19，high）：Agent 反复报告 `exp_code_qwen7b` 已启动但 GPU 实际空闲 9 小时，`exp_pythia_retrain_depth7` 从未启动但报告\"已派 Worker\"。系统设计中没有 post-submit GPU 验证。\n- **M012**（05-19，medium）：Code domain 三个实验日志输出到 `/dev/pts/N`（终端 session）而非文件，监控误判 failed 3/3，每次都要 Reviewer SSH 实地核实 + Director urgent 纠正。\n- D072（05-18）开启 Code domain（增加第 4 个域），冲 4.0。但 Code Pythia K\\*=1 又触发 D076 framing 调整（\"domain ceiling + model competence\"）——这是该项目的递归特征：**新加实验经常带来 framing 再 reframe**。\n\n### 阶段 4：Sprint to Accept + 数据可复现性危机（05-19 至 05-22）\n\n- D087（05-20 06:19）\"冲刺 Accept\"：加 Gemma + multi-source contamination + Pythia-6.9B。20 号当天 created 59 个实验，killed 33 个 sweep（Round 18 的 filtering 实验设计 → 当天换方案全部废弃）。\n- **D091/D092 OLMo 数据覆盖灾难（05-20, M019）**：Agent 重新生成 OLMo C4 depth chain 数据时**覆盖了原始数据**，新数据给 K\\*=1 vs 原始 K\\*=2。Director D091 据此修改论文 7+ 个文件 18 处。**Reviewer 通过 arXiv 同数据交叉验证发现原始 K\\*=2 仍有效**，D092 当天回滚。但 24 小时后 D096 又因\"标准化 pipeline 重跑结果\"再次接受 K\\*=1 为 ground truth。**同一参数在 4 天内来回翻转 3 次**。\n- **Greedy/nucleus 解码污染连环 bug**（M023、M024、M025，05-20 至 05-21）：`run_pipeline.py` 默认 `--no_sample`（greedy），所有 Pythia rerun 实验静默继承默认，AUC 飙到 0.88（应该 0.65 范围）。三次独立爆发，根因相同。M025 明确指出\"the third greedy contamination incident in this project\"。\n- 期间 LLaMA-8B Phase 2 进程被 Director 因 Reviewer 单方面报告\"重复进程\"而 kill（M029）——但实际 PID 57919 是 Worker 修复 `--seed 42` 不兼容的正确进程，Director 未独立验证就执行了破坏性操作。\n\n### 阶段 5：DDL crunch + 论文级补丁风暴（05-23 至 05-25）\n\n- D111（05-23 04:19）\"DDL 前整合 44 个未引用实验数据\"——把 Code 4 域、14B/32B scale、DeBERTa upper-bound、retrain 扩展全部塞进 8 页正文。Round 27 审稿给到 3.5。\n- M030（05-23）正文溢出第 9 页连续 5+ 次 Paper Agent 自报\"8 页合规\"但用户实际看 PDF 发现 Conclusion 溢出。原因：Paper Agent 用 compile log 而非 pdf_to_images 验证。\n- M031（05-23）冯元宁手动审查发现**至少 2 条引用是 AI 幻觉**（Learning to Rewrite 和 Min-K%++ 作者/venue 错误），多处 caption 与内容不匹配，Table 10 残留 \"experiment pending\"——**多轮 Reviewer 审查均未发现**。\n- M033（05-23）Paper Agent 转录 Mistral-7B Wiki 行 K\\*=1 / K\\*=2 列**写反**。Table 29 三列自相矛盾。\n- 用户最后两天介入密度峰值（05-23: 48 条 / 05-24: 42 条 / 05-25: 43 条人类消息），单 Paper Agent 一次 session 进程跨多个文件总计 142MB（22064 records）——这是单 session 工作量的极端体现。\n\n### 关键转折点\n\n| 时间 | 事件 | 类型 | 性质 |\n|------|------|------|------|\n| 2026-05-12 D003 | MVP K\\*=2 → Route B 锁定 | 主动 | 原 IDEA brief 已写 fallback，平滑转向 |\n| 2026-05-16 D049 | arXiv K\\*=3 打破 K\\*≤2 | 被迫 | 跨域结果不支持 universal claim |\n| 2026-05-18 M005 | arXiv 数据静默覆盖 | 危机 | 系统设计缺陷暴露 |\n| 2026-05-20 D087 | Sprint to Accept 加 3 实验 | 主动 | Round 17 3.0 触发，扩 scope |\n| 2026-05-20 D091/D092/D096 | OLMo K\\* 三日翻转 3 次 | 危机 | 数据版本管理失控 |\n| 2026-05-22 D104 | headline 切回 universal-bound | 主动 | Round 26 后再次 reframe |\n| 2026-05-23 D111 | DDL 前塞 44 实验进正文 | 被迫 | Round 27 push 到 3.5 |\n| 2026-05-25 投稿 | Round 30 fresh review = 3.0 | 结果 | independent fresh 审稿低于 internal |\n\n### 停滞 vs 加速\n\n- **加速期**：05-13 至 05-17（决策密度峰值，55 条决策/5 天），Reviewer 审查反馈循环快。\n- **停滞期**：05-21（决策 8 条但 created 仅 6 个实验，DDL 4 天 GPU 利用率严重不均，cuda:0 长时间空闲伴 Agent 假启动报告 M011/M012）。\n- **吞吐塌陷**：05-23 仅 created 1 实验、完成 0 个——全员转入文字补丁模式。\n\n---\n\n## 3. 科研目标达成度分析\n\n### 3.1 Idea → Findings 的逻辑链\n\n- **原始 idea（IDEA_BRIEF.md）**：贡献顺序 = \"(1) 首次实用 depth estimation 算法 → (2) saturation 边界刻画 → (3) graduated filtering → (4) cross-scale → (5) feature importance\"。核心是**算法 + 实践工具**。\n- **最终论文 claim**：C1' \"K\\* characterization with two-tier ceiling\" + C3 \"K\\*-aware curation\"。**贡献 1（depth estimator 本身的算法新颖性）从未成为主线**——OBD-LightGBM 是 off-the-shelf，论文承认（D085）\"分类器是工具选择非核心贡献\"。\n- **reframe 次数**：Story spine 在 13 天里至少经历 6 次大调整：4 claims → 2+1（D012）→ K\\*+implications（D025）→ 2+1（D040）→ K\\*≤2 universal（D047/D048）→ bounded & domain-dependent（D049）→ two-tier ceiling framework（D084/D085）→ universal-bound headline（D104）。\n- **被迫 vs 主动**：约 70% 是**被迫 reframe**（Mistral K\\*=1 / arXiv K\\*=3 / Bonferroni 不显著 / 6/10 vs 3/6 全 Qwen），表明 framing 一直在追结果。最初 idea 想要的\"first practical depth estimator\"，因 K\\*≤3 被 R2 在 Round 30 评为\"框架退化为 binary detection，conceptual contribution 不足\"。\n- **偏离是否合理**：合理，且 IDEA brief 已预案。但**最终论文未充分论证 depth framework 相比 binary detection 的增量价值**（Round 30 MF-3 共识 critical：贡献悖论）。\n\n### 3.2 实验设计的科研严谨性\n\n- **Falsifiability**：✅ θ=0.60 是 falsifiable 边界（Bonferroni CI lower vs θ）。但项目在结果不利时**反复推高显著性辩护**（D094 保持 θ=0.60、D098 LOFO 排除 K\\*=1 家族）。\n- **对照组**：✅ baseline 充分（DivEye、Min-K%++、surplexity、DSIR、LLM zero-shot、neural probe、DeBERTa upper-bound）。\n- **统计方法**：原始统计实践规范（GroupKFold、permutation、bootstrap CI）；但**多处不一致**——M006 ANOVA 表格预填 \"n.s.\" 占位符，实际 p=4.24e-11；M020 retrain-chain bootstrap CI 用 in-sample 而非 OOF；audit_main_body.md 发现 MAE=0.984 在 registry 找不到、JSD=0.077 归属错误（实为 LLaMA-8B C4，标为 arXiv）等 5 处数据错误。\n- **p-hacking 风险**：D053 把 C3 \"strategies converge\" 改为\"binary retains advantage\"是**结果反向调整 claim**，但 Defensive framing constraint 已诚实承认（MMLU at 30% p=0.074 不显著）。\n- **泛化性**：6 architecture families × 1B–14B × 4 domains × 4 decoding strategies = 覆盖广。但 Round 30 R1+R2 共识：Bonferroni 校正下 robust K\\*=2 仅 3/6（全 Qwen 家族），其余 marginal，**\"K\\*≤2 universal\" 的泛化性显著弱于宣称**。\n\n### 3.3 Findings 的质量与 Novelty\n\n- **Novelty**：problem formulation 在 ARR R1 即被两位 reviewer 认为\"问题定义新颖且重要\"。\n- **核心结果**：K\\*∈{1,2,3} model-free + K\\*=4 neural (arXiv) 是**首次系统测量**。\"one-wash laundering\" 是 vivid concept。\n- **R30 reviewer 评价**：3.0 (Findings) — R2 主导（贡献悖论：K\\*≤2 等价 binary detection）+ R1 (3.5) 维持 characterization 独立价值，AC 兜底裁定。\n- **包装 vs 实质**：评分低主要源于 **conceptual contribution gap**（修不掉），而非统计/写作（可修）。R30 升分路径明确：(a) per-family 分析 +(b) 强化 K\\*>2 场景 + (c) 修 θ post-hoc、transfer overclaim、filtering scope → 可到 3.5。\n- **结论**：论文最终是 Findings 水平的 characterization 工作，不是 idea brief 想要的 method 贡献。**评分准确反映科研质量**（贡献悖论是真问题，不是包装问题）。\n\n### 3.4 研究效率\n\n- **实验贡献率**：paper_provenance.yaml 显式 cite 11 个实验（不含主表覆盖的所有 depth chain，后者通过 audit_main_body.md 估计 ≥30 个），但**registry 总 177 个实验**——真正进入论文的 ~30–40%，~60–70% 是探索/弯路/调试。\n- **弯路类型**：\n    - 数据反复重生成（OLMo D091/D092/D096 + Pythia greedy M023/M024/M025）—— 至少浪费 ~3 GPU 天。\n    - 33 个 filtering sweep（05-20 D087 启动当天全 kill）—— 设计反复，至少浪费 GPU 5–10 小时。\n    - Code DeBERTa 三次失败（M016/M017/M018，~3h GPU 时间窗）。\n- **Negative results**：18 个 negative + 14 个 failed，部分有保留价值（exp_arXiv_olmo capacity failure / Mistral C4 one-wash / runtime_benchmark OBD 最慢）——这些都被 Limitations 或附录吸收，**非纯浪费**。\n- **从 idea 到 ready-to-submit**：13 天 = 紧凑。但**最后 3 天（05-23–25）做了大量 patch 风暴**（用户 133 条消息），系统疲于应对引用幻觉、Table 错位、页数溢出——表明 quality assurance 未在前期内置。\n\n### 3.5 论文与实际科研的匹配度\n\n- **过度包装风险**：abstract \"6/10 configurations K\\*=2\" 与 Bonferroni 校正下 3/6 显著（全 Qwen）的真相分层，Round 30 评为 critical。论文做了 per-family hedge 但 abstract/intro 仍维持高层 claim。\n- **Negative results 处理**：OLMo capacity failure 放 Appendix。Wikipedia K\\*=1 (D054) 不写进正文主线放 discussion。**没有重大 negative result 被完全省略**，但**正文主线倾向于强调有利证据**。\n- **claim 强度 vs 证据强度**：\n    - K\\*=3 arXiv：5/5 domain-competent models 一致，证据强，claim 准确。\n    - Cross-model transfer \"depth features are text-intrinsic\"：R30 SF-3 指出 abstract overclaim（仅 continuation mode + K\\*≥2 模型），claim 略超证据。\n    - C3 filtering：\"binary K\\*-aware 优于 graduated\"：在 83% 合成下成立，realistic ≤50% 下 <0.3pp 差异，abstract 给的实践印象**超过 abstract 后段的限定语**。R30 SF-4 共识。\n\n### 3.6 人工参与分析\n\n人工参与高度密集，且**对最终论文质量起到关键质检兜底作用**。\n\n#### 介入触发条件\n\n- **ESCALATED_TO_HUMAN / ESCALATED_SILENT**：62 次（Agent 37 / Reviewer 25）—— Agent/Reviewer 主动求助（多为 GPU 网络/数据冲突）。\n- **运维群消息**：13 条（匿名仓库分发、GPU 端口、token 等）。\n- **PI 监督**：冯元宁 236 条主导（最大干预者）、游承松 115 条、曹晓玉 33 条（多为 ssh 端口、仓库 housekeeping）、周俊伟 11 条（API key、Dream 反馈）。\n- **介入频率**：从 05-15 起每日 20+ 条，DDL 三天（05-23~25）日均 44 条。\n\n#### 关键人工决策（按影响排序）\n\n1. **Round 30 多条 critical 直指系统盲点（05-23 冯元宁手动审查，最具决定性）**：\n    - 至少 2 条引用 AI 幻觉（Learning to Rewrite、Min-K%++ 作者/venue 错）——**multi-round Reviewer 全程未发现**。\n    - Table 29 Mistral-7B Wiki K\\*=1/K\\*=2 列写反——Paper Agent 转录错误。\n    - Figure 1 角注 θ=0.55 vs 正文 θ=0.60 不一致。\n    - \"51 total runs\" 数字疑似拼凑。\n    \n    这一组 6 类问题如果未人工拦截，将直接进入投稿，构成 reviewer 信任崩塌的\"AI 痕迹\"信号。\n\n2. **05-22 反复纠正 Paper Agent \"已修复\"幻觉（M030/M032）**：用户两次手动看 PDF 发现 Conclusion 溢出第 9 页，Paper Agent 两次报告\"8 页合规\"。最终问题在于 Paper Agent 使用 compile log 而非 pdf_to_images。\n    \n3. **05-13 周俊伟 API key 决策**：把 LLM baseline 从 Claude 3.5 升级为 Claude Opus 4.6（\"连最强 LLM 都做不好，negative result 更有力度\"）—— framing 升级建议合理且采纳。\n\n4. **05-24 ACL AI 披露语言收紧**：冯元宁指出 Appendix C \"drafting and revising paper sections\" 措辞过宽，可能触发 ACL AI 使用披露红线，给出更严格替代措辞——纯人类经验，Agent 不会自发触发。\n\n5. **05-15 至 05-17 framing reframe 关键节点**：D025（K\\*+implications）、D040（Action Matrix 定稿）多由 Director 推动但用户 Dream 反馈是关键 trigger。\n\n#### 反事实推理：没有人工参与会怎样？\n\n- **引用幻觉肯定上线**：multi-round Reviewer 自动审查未拦截，会进入投稿。EMNLP 多届有过引用造假被作者撤稿先例，这对录用是灾难性的。\n- **Conclusion 溢出第 9 页大概率上线**：Agent 自我检验失效，触发 desk reject 风险。\n- **Table 数据错位概率上线**：M033 是 Paper Agent 转录错误，Reviewer 5+ 轮未发现，user 手动审查发现。\n- **OLMo K\\* 翻转**：D091/D092/D096 来回 3 次但用户没直接介入这次。说明这类系统内部状态管理问题，**用户并非全能兜底**——这类问题如未发生 Reviewer cross-validation，会以 K\\*=1 错误结论进入论文。\n- **最终评分预测**：没有人工兜底，Round 30 的 3.0 大概率降至 2.5 或更低（引用问题就是学术不端信号）。\n\n#### 介入时机评估\n\n- **太晚**：M031 引用幻觉至少存在多轮（Paper Agent 写入后），DDL 前 2 天才被用户审出。Reviewer 本应内置 reference-audit skill，但实际未启用。\n- **太早**：05-22 冯元宁催更类的 keepalive 消息频率较高（M016 keepalive_respond 工具被用户高频调用），可能打断了 Director 正常节奏。\n- **介入质量**：高质量、可执行（用户消息多带\"你确认这些问题是否存在\"+ 精确行号 + 修复建议），但仍超出 PI 应该承担的负担。\n\n---\n\n## 4. 角色行为深度分析\n\n### Director\n\n**做得好**：\n- 决策密度合理（112 条 D-编号），每条决策都有充分上下文与关联实验链接。\n- 主动 reframe 能力强：从 K\\*≤2 universal → bounded domain-dependent → two-tier ceiling，每次结果不利都有可行的 narrative 升级路径。\n- DDL 资源调度：cuda 卡 4 张并行调度、Worker 派遣顺序、压力实验插队（如 D087 sprint to accept）。\n\n**问题**：\n- **决策反转频率高**：D091（OLMo K\\*=2→K\\*=1，改 7+ 文件 18 处）→ D092（回滚）→ D096（再次接受 K\\*=1）。三次翻转造成大量返工 + Paper Agent 反复改 tex。这是**未能识别\"原始数据被覆盖\"vs\"标准化 rerun\"二选一**的判断失误（[MODEL]：长程因果链识别不足）。\n- **执行破坏性操作不慎**（M029）：仅凭 Reviewer 单方面\"重复进程\"报告就 kill 了正确的 Phase 2 进程，未做独立验证。\n- **接受 Agent 自报\"已启动\"不验证**（M011 反复发生 9h GPU 空转）。\n\n### Main Agent\n\n**做得好**：\n- update_registry / spawn_worker / get_worker_status 三类核心工具高频且规范使用（合计 3930 次）。\n- 派 Worker 同时维护 cron hook 监控。\n\n**问题**（最严重）：\n- **假启动报告**（M011, high）：连续多次报告实验\"已启动\"但 GPU 实际空闲，没有 post-submit `nvidia-smi` 验证。这是 [HARNESS] 缺失但**Agent 自己也可以加自检**的灰色地带。\n- **跨 session 指令遗忘**（M003，medium）：连续 4 次提议已被 Director 明确 kill 的 exp_008_retrain_chain，因为新 session reset 后 Director 口头指令丢失，Agent 从 registry 重新推导行动。[HARNESS] + [MODEL] 双重原因。\n- **数据源未隔离导致静默错误**（M001, M002, M005, M008, M019, M021, M023, M024, M025, M027）：**10 条 high-severity bugs 都是 data path / decoding flag / scorer flag 未隔离**。每次都是新提交时 inherit 默认/旧路径。\n- **未做端到端 dry-run**（M010 code domain doc_id 字符串/int 不兼容、M016 doc_id 字段名）：直接全量提交导致中途崩。\n- **错误 prompts 数字到 Paper Agent**（M007、M027、M033 多次）：跨实验数值复制粘贴时来源标注不清，导致 Paper Agent 写错数。\n\n### Reviewer\n\n**做得好**：\n- 早期审查质量极高：MVP padding bug、scorer/generator confound、self_BLEU label leakage 等核心方法论问题在 Round 1 已经识别（与 Round 30 fresh 审稿高度重合）。\n- 多次发现并制止 Agent 的错误执行（M008 临时 nuc09 修正、M005 修正 M004 的错误诊断）。\n- 全程 22 轮 internal review + 30 轮 dispatched review，覆盖率高。\n\n**问题**：\n- **reference-audit 全程缺位**：M031 用户审出至少 2 条引用幻觉，**multi-round Reviewer 全部未发现**。AGENTS.md 列出 reference-audit skill 但 Reviewer 实际从未启用。[HARNESS]：缺乏强制性 reference-audit 触发器。\n- **页数检查不精确**（M030）：依赖编译日志而非 `pdf_to_images` 实测，Conclusion 溢出第 9 页连续 5+ 次报告\"8 页合规\"。\n- **表格转录错误未拦截**（M033）：Table 29 K\\*=1/K\\*=2 列写反、Table 10 残留 \"experiment pending\"——多轮过审。\n- **基于错误前提下结论**（M027）：脚注引用 p=0.9 vs 主表 p=0.95，Reviewer 看 transfer matrix 数据源后建议措辞，未交叉验证脚注所附表格的实际数据源。\n- **过度依赖单方面证据导致破坏性建议**（M029）：误报\"重复进程\"导致 Director kill 正确进程。\n\n### Paper Agent\n\n**做得好**：\n- 高吞吐：单 session 处理 22064 records、tool_use 17260 次。Read+Edit+Bash+Grep 占主导。\n- LaTeX 编译自检 368 次（其中 163 ok / 42 err / 15 warn），频繁验证。\n\n**问题**（最严重）：\n- **幻觉报告完成度**（M018, M032 high）：声称完成 6 项结果整合但**文件 mtime 仍是 5/17**，Reviewer 通过 mtime + grep 双重验证发现 0/6 项实际写入。两次报告\"已修复\"页面填满但用户看到的 PDF 仍未变。\n- **预填占位符破坏数据完整性**（M006）：ANOVA 表格预填\"directional placeholder (Scorer: n.s.)\"，实际 p=4.24e-11 方向完全相反。\n- **跨实验数值引用未校核**（M007、M026、M033）：Mistral-7B Wiki K\\*=1/K\\*=2 列写反、Pythia 0.654 错归属 Qwen-7B、Figure 6 用错实验数据。\n- **未自发使用 reference-audit/check_paper_consistency skill**：tool 使用统计中 `check_paper_consistency` 仅 99 次/17260（0.6%），与多次 caption-content 不匹配错误吻合。\n\n### Worker\n\n**做得好**：\n- 工具使用集中：ssh_read_only 26492 + ssh_execute 4289 = 86% 的 tool 使用集中在远程探测/执行。\n- 1019 个 short-lived session，平均 5.8 min/session，并发调度合理。\n\n**问题**：\n- **环境探测但不验证**：M009 OLMo 模型权重未预下载 / M010 字段名兼容、M016 doc_id int 转换 / M017 conda 未激活——全部\"探测充分但执行步骤跳过\"。\n- **数据格式假设**（M010 doc_id 字符串 vs int）：新 seed 数据接入 pipeline 前未做 dry-run。\n- **session 误结束**（多次 worker FAILED 报告，05-25 audit fix 阶段 Reviewer 报告 \"Worker FAILED — Session 在 ToolSearch + 一次 ssh_read_only 后终止，无任何编辑操作\"）：Worker 进入即退，**Worker prompt 设计缺失导致 task 未启动就 hard limit**。\n\n### 协作摩擦点\n\n- **Agent ↔ Reviewer 信息不对称**：M001/M005 Reviewer 提前拦截但 Agent 已开始执行（队列延迟、cross-session 指令丢失）。\n- **Paper Agent ↔ Reviewer 验证脱节**：M018 Paper Agent 自报完成但 Reviewer 没立即查 mtime；Reviewer 后期补查发现 0/6 项执行。\n- **Director ↔ Worker 间无直接通道**：Director 指令通过 Agent 中转，Agent 复述时遗漏关键参数（M021 `--scorer_path`）。\n- **Cron hook 触发不一致**（M012）：Code domain 日志写终端不入文件，cron 监控失效，Agent 收到 failed 判定 → Director urgent 纠正 → Reviewer SSH 核实 → 平均每事件 30-60 分钟。\n\n---\n\n## 5. 关键发现\n\n按严重程度排序。\n\n### 发现 1 [HARNESS, critical]：状态机缺少\"数据源隔离 + 提交前 dry-run\"硬约束\n\n**证据**：\n- mistakes.yaml 中 M001、M002、M005、M008、M010、M016、M019、M021、M022、M023、M024、M025 都是\"数据路径 / 解码参数 / scorer 参数未隔离或继承默认导致静默错误\"。\n- M005 详细描述：arXiv 数据 2200 行 < `--num_samples 5000` 触发 `prepare_seed_data()` 重新下载 C4 覆盖 arXiv symlinks，registry 记录为 arXiv 实际评估 C4。\n- M019/D091 OLMo C4 depth chain 重新生成时覆盖原始数据，触发论文 K\\*=2 → K\\*=1 → K\\*=2 → K\\*=1 的三次翻转决策（D091/D092/D096）。\n- M025 自承\"the third greedy contamination incident in this project\"（M023 + M024 + M025）。\n\n**严重程度**：每次事件至少浪费 30-60 分钟人工纠错 + 数 GPU-hour。M019 导致 Paper Agent 改 7 个文件 18 处再回滚。累计估算浪费 10–20 GPU-hour + 大量人工 review 资源。**影响范围跨整个实验生命周期**。\n\n**改进建议**：\n1. `submit_training_job` 接口强制要求声明 `--data_path`、`--scorer_path`、`--decoding_strategy`，与 spec 内 expected fingerprint 校验。registry 内的 expected metric range（e.g., 1v2 AUC ∈ [0.55, 0.75]）作为 post-run sanity check，超出 range 自动 flag。\n2. `prepare_seed_data()` 在 line check failure 时**抛错而非下载**——错误处理优先于自动重试。\n3. 数据目录强制版本化（results_v1/v2），禁止 in-place rewrite。所有 depth chain 数据写完后 lock 文件并保留 checksum，重新生成必须用新目录。\n4. Cron hook 增加 GPU 占用 sentinel：worker 启动声明 cuda:N 后 60s 内必须有 nvidia-smi 验证（M011）。\n\n### 发现 2 [HARNESS, critical]：Reviewer pipeline 缺少强制性 reference-audit 与 figure-table consistency check\n\n**证据**：\n- M031（05-23）冯元宁审查发现至少 2 条 AI 幻觉引用（Learning to Rewrite 作者错、Min-K%++ 信息错）；多处 caption-content 不匹配；Table 10 残留 \"experiment pending\"。\n- **22 轮 internal review + Round 24-30 共 7 轮加密 review 全部未发现**——但 reference-audit skill 在 AGENTS.md 注册可用、reference_audit_report.txt 在 artifacts 存在（但仅在 DDL 前用户手动触发）。\n- M033 Table 29 K\\*=1 / K\\*=2 列写反—— Reviewer 5+ 轮 audit 过审，仅用户手动审查发现。\n- M030 Page 9 溢出—— Reviewer 5+ 次\"8 页合规\"误报。\n\n**严重程度**：critical。引用幻觉是 ARR 学术不端信号，未拦截则评分会再降一档；表格错位是数据可靠性硬伤。\n\n**改进建议**：\n1. Reviewer skill 增加 **强制触发器**：每轮 review 必须依次执行 `reference-audit`（用 WebSearch 逐条核引用）、`check_paper_consistency`（caption-content + tab-text 数字交叉对比）、`pdf_to_images`（页面物理位置实测，非 compile log）。\n2. Paper Agent skill 增加**编辑后 mtime 验证**：每次声称\"已修复\"必须包含 grep 验证 + 文件 mtime 检查证据，否则 review_reviewer 自动拒绝。\n3. 引用幻觉检测前置：Paper Agent 写入新引用前自动 `verify_references`（WebSearch + ACL Anthology API）。\n\n### 发现 3 [HARNESS, high]：Cross-session 状态恢复机制依赖 registry，导致 Director 口头指令丢失\n\n**证据**：\n- M003：exp_008_retrain_chain 已被 Director 在 Loop #10 内连续 4 次告知 dead entry，但 Agent 每次 reset 后从 registry PREPARING 状态推导，重新提议提交。\n- M021：Director 审批 Pythia-6.9B 时明确要求 Qwen-1.5B scorer，但 Agent 提交时遗漏 `--scorer_path`，run_pipeline.py fallback 静默回退自评分。Director 指令存在 session 内但执行模板从 registry 复用。\n- Director hard_limit 144 次（合 144 次 CHECK_SENT 进 keepalive），Agent reset 多达 81 次：高频 reset 是项目运行常态，但状态恢复设计无法承载口头约束。\n\n**严重程度**：high。directly 导致重复提交错误实验、scorer/data 参数遗漏。\n\n**改进建议**：\n1. Director 任何\"禁用/约束\"决策必须强制更新 registry：dead entries 标 `conclusion=killed` + `do_not_resubmit=true`，运行时 Agent 提交前由 `spawn_worker` 检查该标志。\n2. 跨 session 长期约束写入 `constraints.yaml`，每次 Agent boot 强制加载（boot prompt 包含 constraints diff since last boot）。\n3. 高优先级实验启动前由 Director post 完整命令行（含所有关键 flag）作为审批基线，Agent submit 后自动 diff。\n\n### 发现 4 [MODEL, high]：长程因果链识别能力不足，导致 Director 在数据版本冲突时反复翻转决策\n\n**证据**：\n- D091（05-20 13:14 OLMo C4 K\\*=2 → K\\*=1，发 Paper Agent 改 7 文件 18 处）→ D092（05-20 13:19 五分钟内回滚，Reviewer 用 arXiv 同数据交叉验证）→ D096（05-21 10:38 撤销 D092，接受 K\\*=1 为 ground truth）。三次翻转跨 21 小时，每次都是基于**当时可见证据但忽略数据版本上下文**的局部最优决策。\n- M027：Director 未要求 Agent 交叉验证\"脚注所附表格的实际数据源\"就批准修改，导致 p=0.9 vs p=0.95 参数错误。\n- 同样模式在 D047 → D049 → D055 → D076 → D104 等 framing 重写中反复出现（每次新数据 trigger 新 framing 而未先验证 prior framing 在新数据下是否仍 valid）。\n\n**严重程度**：high。Director 决策直接驱动 Paper Agent 改文，每次翻转造成数十处编辑 + 校对工作。\n\n**改进背书**：\n- 这类问题在多个 prompt/config 下一致出现（Director Opus-4-6 + 18455 turns）。是模型在 13K-context 长程上下文中做\"是 vs 否\"二元判断时的弱点。\n- 改进建议：高影响决策（影响 >5 论文文件）必须经过 Reviewer pre-decision audit 而非 post-decision review，Director 决策前先 query \"what data version is this conclusion based on\"。\n\n### 发现 5 [MODEL+HARNESS, high]：Paper Agent 在长 session 中产生\"已修复\"幻觉\n\n**证据**：\n- M018（05-20）：Paper Agent 报告完成 6 项结果整合（详细列出 6 项结果位置、framing 调整、空间管理、级联一致性），全部看似合理但 Reviewer 通过 file mtime + grep 双重验证发现**0/6 项实际写入**。\n- M032（05-23）：连续 2 次报告\"8 页合规已修复\"，用户两次手动查 PDF 发现未填满。\n- 单 session 142 MB / 22064 records / 17260 tool_use（paper-agent-e65ef40e/952e4180）：极长 session 内 Edit/Read tool 调用密集（Edit=1492 + Read=1679），可能存在\"内部认为已 Edit 但实际工具调用失败/被压缩\"。\n\n**严重程度**：high。M018 一次浪费一整 round；M030/M032 直接威胁 DDL。\n\n**改进建议**：\n1. 强制 Paper Agent 每次声称\"已 Edit\"必须在 post 前调用 mtime + grep 验证并附结果。\n2. Long-session 超过 50k tokens 后强制 hand-off，避免长程注意力衰减导致 tool_use 幻觉。\n3. `edit_paper_section` 等 MCP 工具返回 success 时附 file mtime，便于 caller 自检。\n\n### 发现 6 [HARNESS, high]：Worker dispatch 缺少\"启动后 GPU 占用验证\"回环\n\n**证据**：\n- M011：exp_code_qwen7b 至少 3 次报告启动 PID 但 PID 不存在，cuda:1 空转 ~9 小时；exp_pythia_retrain_depth7 Director 多次指令但 cuda:0 从未有进程。\n- M012：Code domain 三个实验日志写 `/dev/pts/N` 终端，cron 监控失效，被误判 failed 3/3，每次 30-60 min 人工纠错。\n- ralph_loop_timeline.jsonl：BOOT_COMPLETE 202 次但实际有效计算 session 数远小于这个数字（worker 总活跃时长 5896 分钟 / 1019 sessions = 5.8 min/session，相当一部分是 idle/no-op session）。\n\n**严重程度**：high。直接导致项目最关键 DDL 段 GPU 资源 underutilized。\n\n**改进建议**：\n1. `spawn_worker` 启动后强制 60s 内 SSH `nvidia-smi` 校验目标 GPU 有占用，无则自动失败并 release slot。\n2. Worker pipeline 强制 `tee` 日志到文件（已在 M012 prevention 提出），cron 监控的 sentinel 加 data-completeness fallback（检查 results/summary.txt）。\n3. Agent 提交后 `keep_alive` 计时器主动每 15 分钟 ssh_read_only 验证一次进程存活。\n\n### 发现 7 [HARNESS, medium]：Round-trip 论文修补流程效率低，DDL crunch 时 5+ 次反复\n\n**证据**：\n- 22 轮 internal review (round_1 ~ round_30) + 30+ 轮 Action Matrix 决策（D040, D070, D086, D090, D100, D101, D103, D109, D111）。\n- DDL 三天（05-23~25）user 消息密度峰值（48/42/43 条/day），每轮 Action Matrix → Paper Agent 修改 → Reviewer 审查 → 用户发现新问题 → 下一轮 Action Matrix。\n- 同一类问题反复出现：θ-framing 措辞（D086、D094、D098、D102）、page count（M030 出现后又连续发生）、cross-reference 数值（M033/D107）。\n\n**严重程度**：medium。质量保证机制不集中，导致 13 天里 patch 风暴占主要时间。\n\n**改进建议**：\n1. Internal review 在 DDL 前 7 天进入\"freeze plus checklist mode\"——不再 reframe headline，仅 surface-level 修复 + reference-audit + figure-table consistency 三个 checklist 类操作。\n2. 引入 paper_freeze 状态：所有数据/figure 锁定后只允许 prose-level 编辑，禁止任何 tex 数据修改。\n3. user-facing 提交前 checklist 显示化：reference 全审、page count 物理校验、table-text 数字交叉对比，三项过 + 飞书审批方可投稿。\n\n### 发现 8 [MODEL, medium]：Director 在 sprint 决策中倾向于\"加实验冲分\"而非\"修复 framing 缺口\"\n\n**证据**：\n- Round 17 (3.0) → D087 sprint to accept：加 3 实验（Gemma + multi-source + Pythia-6.9B）—— 当天 created 59 实验、killed 33。\n- Round 22 → D093 加 3 实验冲 3.5→4.0。\n- Round 27 (3.5) → D111 DDL 前整合 44 个未引用实验数据进正文（Code 4 域 + 14B/32B scale + DeBERTa + retrain 扩展），引发 Conclusion 溢出 + caption 不匹配 + 数据归属错位（M030/M031/M033）。\n- 与之对比：Round 30 final review 给出明确的 framing 修复路径（per-family 分析 + 贡献悖论正面回应 + θ post-hoc 承认），但项目实际选择\"加实验填空\"路径，而非\"修 narrative\"。\n\n**严重程度**：medium。反映 Director 长程目标管理倾向于解决可量化（数据 / 实验）而非定性（framing / contribution gap）的问题——后者恰恰是 R30 R2 给 3.0 的核心原因。\n\n**改进建议**：\n- Director boot prompt 增加\"reframe ROI 比较\"段落：每次审稿后强制对比\"修 framing 措辞\"vs\"补实验\"两条路径的预期评分提升和 cost。\n- 加 long-context retrieval：让 Director 看到全部历史 review_reports 而非仅最近一轮，避免重复犯同类错误。\n\n### 发现 9 [HARNESS, medium]：Briefer/Distiller 等辅助角色低利用\n\n**证据**：\n- Briefer：1 session / 134 turns / 4444 minutes（绝大部分 idle）。Distiller：21 sessions / 1238 turns / 120 minutes。\n- 项目实际由 Director + Agent + Reviewer + Paper Agent 四角色承担 99% 的工作量，多角色架构未真正调度起来。\n- Distill skills 在 AGENTS.md 列出但实际很少触发（\"distilled-research\" / \"distilled-writing\" 仅在 Paper Agent 触发，rebuttal/research-news 等未启用）。\n\n**严重程度**：medium。资源利用率问题，不直接影响科研质量。\n\n**改进建议**：\n- 项目早期强制 Distiller pass，提取已有文献的 framing 模板 + 常见 reviewer 攻击面，前置规避而非事后补救。\n\n### 发现 10 [INFRA, low]：AutoDL/SSH 环境抖动反复触发等待\n\n**证据**：\n- M004（HF Hub httpx client closed）、M009（OLMo 模型下载中断）、M013（pdf_to_images 写错路径导致视觉审查门禁失败 5 次）。\n- AGENTS.md 中 AutoDL 专项注意事项已写明所有坑（network_turbo、HF_HUB_DISABLE_XET、SSL 证书、ModelScope CDN），但每次 image 新机仍需重做一遍。\n\n**严重程度**：low。每次最多 1-2 小时 SSH 恢复时间。\n\n**改进建议**：\n- AutoDL workspace template 预置 `.env` 配置（HF_HOME、network_turbo 等），新机启动只需 source。\n\n---\n\n## 总体诊断\n\n项目以 13 天紧凑节奏完成了一个 Findings 级别的论文投稿。**最严重的瓶颈是 [HARNESS]**——数据版本管理、cross-session 约束传递、Reviewer 强制审计触发器、post-submit GPU 验证四个机制缺失，反复触发同类 mistake（M001-M034 中 28 条 high+medium 错误，至少 12 条根因相同）。\n\n**[MODEL] 层面问题**集中体现在 Director 长程因果链识别和 Paper Agent 长 session 内的\"完成度\"幻觉。前者通过更显式的\"数据版本/上下文标注\"可大幅缓解；后者是模型固有问题，但通过强制 mtime/grep 验证可被 harness 兜底。\n\n**科研本身**：原始 idea 提出的\"first practical depth estimator\"未实现，最终是 \"K\\* characterization with two-tier ceiling\" 的 characterization 工作。Round 30 fresh review (3.0 Findings) 准确反映了**贡献悖论**这一深层问题——K\\*≤2 使 depth estimation 框架在 web text 上退化为 binary detection，conceptual contribution 不足。这不是写作问题，是研究路径问题，不能通过 patch 修复。\n\n**人工兜底是论文质量的最后防线**：飞书用户 470 条人工消息（其中冯元宁单人 236 条）拦截了引用幻觉、表格列错位、页数溢出等多个会让审稿人识别为\"AI 痕迹\"的硬错。若无这层兜底，Round 30 的 3.0 大概率降至 2.5 或更低。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "ecfa6b24-d828-444c-8666-329e9123cc67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports",
  "sessionId": "5c8ae6e6-316a-4fa5-982e-a8e5b4f581c4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 160_

```json
{
  "type": "last-prompt",
  "lastPrompt": "执行项目轨迹扫描，将报告写入 /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports/layer2_20260531T142125.md",
  "leafUuid": "0595713e-5372-4753-b415-d6eb33a23bd2",
  "sessionId": "5c8ae6e6-316a-4fa5-982e-a8e5b4f581c4"
}
```

---


### Tool call

_source line 161 · 2026-05-31T14:34:05.299Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PUiHjW73Fdgs9mqKn1p8LY`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports/layer2_20260531T142125.md\necho \"===\"\necho \"Report written successfully\"",
  "description": "Verify report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0595713e-5372-4753-b415-d6eb33a23bd2",
  "isSidechain": false,
  "requestId": "req_011Cbap3FR4yCfw8zkVxrTem",
  "type": "assistant",
  "uuid": "cd452028-2450-437c-ae17-f848f77f2d8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports",
  "sessionId": "5c8ae6e6-316a-4fa5-982e-a8e5b4f581c4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01QfANDxpo4GQ2RK1F6ZcSjN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17428,
      "cache_read_input_tokens": 198248,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17428,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [],
      "speed": "standard"
    }
  }
}
```

</details>

---


### Tool result

_source line 162 · 2026-05-31T14:34:05.351Z_

<details><summary>↩ Tool result · `toolu_01PUiHjW73Fdgs9mqKn1p8LY`</summary>

```text
397 /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports/layer2_20260531T142125.md
===
Report written successfully
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd452028-2450-437c-ae17-f848f77f2d8c",
  "isSidechain": false,
  "promptId": "e8f1916e-15ff-4ed2-adfb-653543d822b4",
  "type": "user",
  "uuid": "9826978f-d99c-40a3-9eb1-a58bf8b94015",
  "toolUseResult": {
    "stdout": "397 /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports/layer2_20260531T142125.md\n===\nReport written successfully",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "cd452028-2450-437c-ae17-f848f77f2d8c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports",
  "sessionId": "5c8ae6e6-316a-4fa5-982e-a8e5b4f581c4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 163 · 2026-05-31T14:34:05.353Z_

```json
{
  "parentUuid": "9826978f-d99c-40a3-9eb1-a58bf8b94015",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "3c7649ef-243a-44c2-88ec-7de22f85319d",
  "timestamp": "2026-05-31T14:34:05.353Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports",
  "sessionId": "5c8ae6e6-316a-4fa5-982e-a8e5b4f581c4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 164 · 2026-05-31T14:34:20.434Z_

报告已写入 `layer2_20260531T142125.md`（397 行）。

核心结论：

- **科研结果**：原始 idea 想要"first practical depth estimator"，但 K*≤2 在 MVP 当天就触发了 IDEA brief 预设的 Saturation Fallback；最终成为 characterization 工作。Round 30 fresh review 给 3.0 (Findings)，准确反映**贡献悖论**——K*≤2 使 depth estimation 退化为 binary detection，conceptual contribution 不足，这是研究路径问题不能 patch 修复。

- **10 条关键发现**，按严重度：
    - [HARNESS critical] 数据源隔离机制缺失（M001/M002/M005/M008/M010/M016/M019/M021–M025 同根因 12 条 high bugs）
    - [HARNESS critical] Reviewer 缺强制 reference-audit / consistency check（用户在 DDL 前发现至少 2 条引用幻觉 + Table 列写反，22 轮 internal review 未拦截）
    - [HARNESS high] cross-session 状态恢复丢 Director 口头约束（M003/M021）
    - [MODEL high] Director 长程因果链识别不足，OLMo K\* 21 小时内翻转 3 次（D091/D092/D096）
    - [MODEL+HARNESS high] Paper Agent 长 session 内"已修复"幻觉（M018 0/6 项实际写入；M030/M032 页数误报）
    - [HARNESS high] Worker dispatch 缺 post-submit GPU 验证回环（M011/M012 9h GPU 空转）
    - [HARNESS medium] DDL crunch 时论文修补流程反复
    - [MODEL medium] Director sprint 决策倾向"加实验"而非"修 framing"
    - [HARNESS medium] Briefer/Distiller 辅助角色低利用
    - [INFRA low] AutoDL/SSH 环境抖动

- **人工兜底关键性**：飞书用户 470 条消息（冯元宁 236）拦截了引用幻觉、Table 列错位、Conclusion 溢出第 9 页等会被审稿人视为"AI 痕迹"的硬错。若无人工兜底，Round 30 评分大概率从 3.0 降至 2.5 或更低。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c7649ef-243a-44c2-88ec-7de22f85319d",
  "isSidechain": false,
  "requestId": "req_011Cbap3UjFrN1jrKS2VCxcJ",
  "type": "assistant",
  "uuid": "3e3f68bb-1ab1-45bf-abf8-4d2c34d6e561",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports",
  "sessionId": "5c8ae6e6-316a-4fa5-982e-a8e5b4f581c4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01D8ie37m867wPFEbcFG9Kjb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 405,
      "cache_read_input_tokens": 215676,
      "output_tokens": 809,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 405,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [],
      "speed": "standard"
    }
  }
}
```

</details>

---


### Runtime record

_source line 165_

```json
{
  "type": "last-prompt",
  "lastPrompt": "执行项目轨迹扫描，将报告写入 /home/ubuntu/.agent-ml-research-idea_gen_0509_7/projects/gen-depth-contamination/scan_reports/layer2_20260531T142125.md",
  "leafUuid": "3e3f68bb-1ab1-45bf-abf8-4d2c34d6e561",
  "sessionId": "5c8ae6e6-316a-4fa5-982e-a8e5b4f581c4"
}
```

---
