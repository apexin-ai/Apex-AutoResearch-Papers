# Research conversation: <agent_context> ## memory.md 中已有的 Evidence Tax 数据 ### Evidence Tax (LLaMA) — D134 决策：用 fair comparison 报告 - RSFT 3-seed: — Part 2 of 2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-agent-context-memory-md-evidence-tax-evidence-tax-llama-d134-fair-comparison-r.md) · [Structured JSON](../../../sessions/cc/cc4fcef832710e327a50.json)

## Round 1

### Tool result

_source line 82 · 2026-05-21T03:37:54.500Z_

<details><summary>↩ Tool result · `toolu_01QsuxRhnvFQA8SNw9AsrKex`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"196 /root/autodl-tmp/freige/scripts/analysis/fair_evidence_tax.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1e674b5b-a688-470d-8be8-23f9c063f102",
  "isSidechain": false,
  "promptId": "9de4b2f0-56de-4de7-a2d6-d458631a94f6",
  "type": "user",
  "uuid": "7236b406-7f2c-419e-8765-f271195f0df6",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"196 /root/autodl-tmp/freige/scripts/analysis/fair_evidence_tax.py\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"196 /root/autodl-tmp/freige/scripts/analysis/fair_evidence_tax.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"
    }
  },
  "sourceToolAssistantUUID": "1e674b5b-a688-470d-8be8-23f9c063f102",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "8ac8f8ae-44c6-4626-8ebe-c70f91645eec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 83 · 2026-05-21T03:37:54.506Z_

```json
{
  "parentUuid": "7236b406-7f2c-419e-8765-f271195f0df6",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "157a86fd-9e19-40e8-b396-75bec6ab05ca",
  "timestamp": "2026-05-21T03:37:54.506Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "8ac8f8ae-44c6-4626-8ebe-c70f91645eec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 84 · 2026-05-21T03:39:46.204Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have everything I need. Let me also read the rest of the fair_evidence_tax.py to check if it supports @2048 input. Let me also check the RSFT with-evi @1024 results from the original eval dirs.

Actually, looking at the script header, fair_evidence_tax.py takes --with-evi and --no-evi prediction paths as input. It doesn't care about @1024 vs @2048 - it just reads predictions.json files. So it should work fine with @2048 data as long as you point it at the right predictions files.


I need to pull the RSFT with-evi @1024 metrics to complete the comparison table, and I'm tracking the four evaluation jobs currently running across the GPUs to see when they finish. Generating metrics table... I'm noticing something odd with the s43 results at 2048 tokens — the ignoring F1 score dropped dramatically to 0.3389, which seems counterintuitive given the increased context window. The truncation rate is still quite high at 36.4%, which explains the poor performance, but it's surprising that even doubling the token limit didn't substantially reduce truncation issues for this model.

In contrast, s44 shows a much more positive response to the 2048 limit, with F1 improving from 0.3326 to 0.4373 and truncation dropping from 41.7% to 25%. The fair tax script should work fine with the 2048 data since it just takes prediction paths regardless of token limits. I need to verify the RSFT with-evidence baseline numbers from the registry to make sure my comparisons are accurate.

Looking at the no-evidence RSFT scores at 1024 across the three models, they're all clustered around 0.55. Comparing against the with-evidence versions, the evidence tax is consistently negative across all three models, meaning evidence actually helps performance. The mean tax is around -1.14 percentage points with some variance between models.

For the 2048 measurements, I need both with and without evidence runs for all three models, but right now only the s42 with-evidence run at 2048 is in progress. The no-evidence baseline at 2048 hasn't started yet, and neither have the s43 or s44 runs. Since the requirement is to measure the evidence tax at matched 2048, I'll need to get those remaining runs queued up once the SFT work finishes.

Now I'm going to update memory.md carefully, preserving the existing 1024 evidence tax data while adding the new 2048 section. Generating results table...

I'm noticing some inconsistencies in the s44 results—the fair_tax value appears to have been computed with mismatched data versions, where the with-evidence metrics at @1024 got mixed in with the @2048 no-evidence data. Let me verify which configuration actually produced those numbers by checking the full_set results more carefully. matched@2048 results would need both sides at the same token budget, but these fair_tax files are actually mixing with-evi@1024 against no-evi@2048, which means they're intermediate results rather than the final comparison I need.

For s42 specifically, I can see the truly matched@2048 data: with-evi gives 0.5649 ign_f1 while no-evi gives 0.5210, which yields a raw tax of -4.39pp—and that matches exactly what's in the ROADMAP, confirming evidence actually helps performance here. Now I need to verify whether the fair tax calculation for this matched@2048 s42 comparison has already been computed.

Looking at the status table, s42 has both sides complete at @2048, but the fair_tax still needs to be recomputed since the current file was built using @1024 with-evi data. Meanwhile s43 and s44 are still running their with-evi@2048 evaluations.

Now I'm checking the RSFT results — s42 has with-evi@2048 running while no-evi@2048 is queued, and s43/s44 haven't started yet. For the 14B model, with-evi@2048 is currently running while the @1024 results are already in.

Looking at the truncation comparison for no-evi, I need to verify the @1024 baseline numbers since I mixed up the with-evi score with the no-evi one. I'm working through the tax calculation formula — if tax represents the difference between no-evidence and with-evidence scores, then for SFT s42 at 1024 tokens, a raw tax of -1.65pp means the no-evidence score would be 0.5384 - 0.0165 = 0.5219, confirming that evidence actually helps performance.

Now I need to verify whether the no-evidence results at 1024 tokens exist in my directory list, since I have references to eval_llama_sft_s42_no_evidence_std and several s43 variants that should be at that resolution.

Looking back at the fair_tax files, I realize the "2048" in the filename is misleading—it's actually marking the no-evidence@2048 results, not the matched@2048 data I'm trying to compile. The with-evidence values in those files are at 1024 tokens, so these aren't the final matched results I need.

The fair_evidence_tax.py script already handles both token lengths since it just reads from prediction files without caring about max_new_tokens, so no code changes are required. I have enough information to write up the summary now, though I'll note which results are still missing from the full picture.

Generating markdown table... Generating benchmark results table... Looking at the fair tax calculations, I see that mixing different token lengths (@1024 with-evi against @2048 no-evi) is skewing the results by several percentage points. The fair_evidence_tax.py script is already flexible enough to handle the @2048 data without modifications. I'm tracking what's still running—the SFT models with evidence at @2048 should finish in a few hours, then I can submit the remaining no-evi and RSFT jobs once GPU capacity opens up.

Once all the matched @2048 runs complete for each seed, I'll re-run the fair tax calculation to get clean comparisons, then update the memory file with the final results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "157a86fd-9e19-40e8-b396-75bec6ab05ca",
  "isSidechain": false,
  "requestId": "req_011CbF1v8NXiPMmD5u8Ggah3",
  "type": "assistant",
  "uuid": "f7fe7eeb-cda7-4c6f-9738-173f4d8a9ca3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "8ac8f8ae-44c6-4626-8ebe-c70f91645eec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLZ1w1jqTjRTnySjJZbmyE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2930,
      "cache_read_input_tokens": 51795,
      "output_tokens": 6282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6282,
          "cache_read_input_tokens": 51795,
          "cache_creation_input_tokens": 2930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2930
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 85 · 2026-05-21T03:39:50.601Z_

所有数据已收集。4 GPU 全在跑 with-evi@2048 eval：
- GPU 0: RSFT s42 with-evi@2048
- GPU 1: 14B RSFT with-evi@2048
- GPU 2: SFT s43 with-evi@2048
- GPU 3: SFT s44 with-evi@2048

现在编译汇总表并写入 memory.md。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7fe7eeb-cda7-4c6f-9738-173f4d8a9ca3",
  "isSidechain": false,
  "requestId": "req_011CbF1v8NXiPMmD5u8Ggah3",
  "type": "assistant",
  "uuid": "a456ba9b-5a90-43f4-866e-f624be80dcb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "8ac8f8ae-44c6-4626-8ebe-c70f91645eec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLZ1w1jqTjRTnySjJZbmyE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2930,
      "cache_read_input_tokens": 51795,
      "output_tokens": 6282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6282,
          "cache_read_input_tokens": 51795,
          "cache_creation_input_tokens": 2930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2930
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-21T03:39:50.758Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01RFR83fviWmJhoEJT2v47Lp`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a456ba9b-5a90-43f4-866e-f624be80dcb7",
  "isSidechain": false,
  "requestId": "req_011CbF1v8NXiPMmD5u8Ggah3",
  "type": "assistant",
  "uuid": "2adf4981-f27b-4638-8657-f757a7593359",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "8ac8f8ae-44c6-4626-8ebe-c70f91645eec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLZ1w1jqTjRTnySjJZbmyE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2930,
      "cache_read_input_tokens": 51795,
      "output_tokens": 6282,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6282,
          "cache_read_input_tokens": 51795,
          "cache_creation_input_tokens": 2930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2930
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-21T03:39:50.782Z_

<details><summary>↩ Tool result · `toolu_01RFR83fviWmJhoEJT2v47Lp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# faith-evidence-ie Memory\\n\\n## 服务器架构（2026-05-20 更新）\\n\\n- **主服务器 westd-37389**: 4× RTX PRO 6000 Blackwell, 98GB VRAM/卡, 350GB 数据盘 (46% used, 190GB free)\\n  - SSH: `rtx5090-4x` (connect.westd.seetacloud.com:37389)\\n  - 环境: conda base, Python 3.12, PyTorch 2.8.0+cu128, transformers 5.8.1, flash-attn 2.8.3\\n- **数据源 bjb2-12179**: 全部 208G 数据完好，rsync 迁移主体完成，SFT adapter 补传中\\n  - SSH: `bjb2-12179` (connect.bjb2.seetacloud.com:12179)\\n- **废弃 bjb1-49673**: AutoDL 重启导致数据清空，已关停\\n\\n## GPU 分配教训（2026-05-20）\\n\\nLLaMA SFT 脚本里有 `export CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-0}}`，会覆盖 submit_training_job 注入的 CUDA_VISIBLE_DEVICES。**必须通过 `GPU=X` 环境变量传物理 GPU 编号**，不能依赖框架注入。\\n\\n## submit_training_job timeout 教训（2026-05-20 更新）\\n\\nLLaMA 8B no-evidence eval timeout 参考：\\n- **max_new_tokens=1024**: ~2h+，至少 14400s (4h)\\n- **max_new_tokens=2048 + 高截断 seed (s43)**: ~4.5h+，4h 仍不够（237/247, 96%，末段 ~70s/batch）。**至少 21600s (6h)**。s43 原 1024 版 truncation=38.4%，2048 版生成更长输出导致每 batch 耗时远超 s42/s44\\n\\n## LLaMA 完整统计（2026-05-20 更新）\\n\\n### SFT 3-seed\\n| Seed | ign_f1 | rel_f1 | edcr |\\n|------|--------|--------|------|\\n| s42 | 0.5384 | 0.5514 | — |\\n| s43 | 0.5142 | 0.5308 | 0.5866 |\\n| s44 | 0.4802 | 0.4902 | 0.6579 |\\n| **Mean** | **0.5109** | — | — |\\n| **Std** | **0.0238** | — | — |\\n\\ns44 异常低（较 s42 低 5.8pp），拉大了 SFT 方差。这恰好强化了 RSFT variance compression 的价值。\\n\\n### RSFT 3-seed (k=1)\\n| Seed | ign_f1 | rel_f1 | edcr |\\n|------|--------|--------|------|\\n| s42 | 0.5714 | 0.5839 | 0.5799 |\\n| s43 | 0.5662 | 0.5780 | 0.5783 |\\n| s44 | 0.5587 | 0.5706 | 0.5829 |\\n| **Mean** | **0.5654** | — | — |\\n| **Std** | **0.0052** | — | — |\\n\\n### 跨方法对比\\n- **SFT→RSFT Δ**: +5.45pp\\n- **方差压缩**: 4.58× (0.0238→0.0052)\\n- RSFT 在最弱 SFT seed (s44) 上仍显著提升：0.4802→0.5587 (+7.85pp)\\n\\n### Evidence Tax (LLaMA) — D134 决策：用 fair comparison 报告\\n\\n**RSFT 3-seed（完整）**：\\n- s42: no-evi 0.5526, with-evi 0.5714, tax=-1.88pp (evidence helps)\\n- s43: no-evi 0.5546, with-evi 0.5662, tax=-1.16pp (evidence helps)\\n- s44: no-evi 0.5550, with-evi 0.5587, tax=-0.37pp (evidence helps, 微弱)\\n- **Mean: -1.14pp ± 0.76pp**（3-seed 一致负向 = evidence 对 RSFT 有帮助）\\n- RSFT format compliance: 984/985 (99.9%)，fair comparison ≈ full set\\n\\n**SFT s44 no-evi 截断异常**：ign_f1=0.3326, truncation 41.7% (411/985)。正在跑 2048 版验证截断 vs 真实退化。\\n\\n**SFT（1024 版，已完成 2/3 seed）**：\\n- s42: raw tax=-1.65pp（不公平），**fair tax=+1.35pp**（evidence 有害）\\n- s44: raw tax=-14.76pp, **fair tax=-12.62pp**（evidence 极度有帮助，但截断率异常高）\\n- s43: 🔄 running\\n\\n**2048 版验证实验（进行中）**：\\n- eval_llama_sft_s42_no_evidence_2048 (cuda:3) — 方法论一致性\\n- eval_llama_sft_s44_no_evidence_2048 (cuda:2) — 截断伪影 vs 真实退化诊断\\n\\n**Reviewer control 需求**：如果 2048 版结果显著不同于 1024 → 需要 with-evi@2048 control（证明 with-evi 对 token limit 不敏感）。如果差异 <1pp → 不需要。\\n\\n## 🚨 Evidence Tax 方法论（D134 决策）\\n\\n**论文报告标准**：用 fair comparison（format-OK 子集），不修 parser。与 1.7B D083 方法论一致。\\n\\n**Fair comparison 脚本**：`/root/autodl-tmp/freige/scripts/analysis/fair_evidence_tax.py`，已用 s42 数据验证通过。\\n\\n**RSFT 压缩 evidence tax 方差**（Director insight）：SFT evidence tax swing 14pp（+1.35 到 -12.62），RSFT swing 1.5pp（-0.38 到 -1.88）。RSFT 不仅压缩 RE 方差，还让 evidence 的角色变得可预测。SFT 下 evidence 效果是 seed lottery，RSFT 下一致有帮助。\\n\\n## RSFT inference 架构（2026-05-20 确认）\\n\\nRSFT 是 nested LoRA：inference.py 先 merge SFT adapter 到 base model，再加载 RSFT adapter。**eval 时必须传 `--sft_adapter` 参数**，否则代码报错。\\n\\n## 14B Pipeline 状态（2026-05-20 更新）\\n\\n- Generation: r4 完成, 24216 candidates from 3027 docs\\n- **CED Scoring 完成** (plan017_14b_ced_scoring)：\\n  - 输出: `/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl` (3015 条, 9.1MB)\\n  - Selected F1=0.730, CED=0.690, Combined=0.768\\n  - vs 4B: F1 +5.4pp (0.676→0.730), CED +1.4pp (0.676→0.690)\\n  - 14B 候选质量显著优于 4B，验证 scaling 假设\\n- 下一步: RSFT training on 14B scored data\\n\\n## Qwen3-8B RSFT Evidence Tax 确认（2026-05-20）\\n\\n- no-evi ign_f1 = 0.5336, with-evi ign_f1 = 0.5414\\n- D127 tax = -0.78pp（evidence helps，微弱）\\n- 与 LLaMA RSFT (-1.14pp) 方向一致，跨家族均为负\\n\\n## Reviewer 发现（2026-05-20）\\n\\n- SFT evidence tax 方法论不一致：应该用同一模型加 `--no_evidence` flag，而非对比独立训练的 no-evidence 模型\\n- LLaMA eval configs 的 base_model 指向 Qwen3-4B（不影响结果，model_path 正确）\\n\\n## 竞品实验参考\\n\\n（待填充——首次进入新方向时从 literature_map 提取）\\n\", \"total_chars\": 4037, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2adf4981-f27b-4638-8657-f757a7593359",
  "isSidechain": false,
  "promptId": "9de4b2f0-56de-4de7-a2d6-d458631a94f6",
  "type": "user",
  "uuid": "1be298ee-fd6c-482d-8fb8-f963f3ddc48d",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\\\", \\\"content\\\": \\\"# faith-evidence-ie Memory\\\\n\\\\n## 服务器架构（2026-05-20 更新）\\\\n\\\\n- **主服务器 westd-37389**: 4× RTX PRO 6000 Blackwell, 98GB VRAM/卡, 350GB 数据盘 (46% used, 190GB free)\\\\n  - SSH: `rtx5090-4x` (connect.westd.seetacloud.com:37389)\\\\n  - 环境: conda base, Python 3.12, PyTorch 2.8.0+cu128, transformers 5.8.1, flash-attn 2.8.3\\\\n- **数据源 bjb2-12179**: 全部 208G 数据完好，rsync 迁移主体完成，SFT adapter 补传中\\\\n  - SSH: `bjb2-12179` (connect.bjb2.seetacloud.com:12179)\\\\n- **废弃 bjb1-49673**: AutoDL 重启导致数据清空，已关停\\\\n\\\\n## GPU 分配教训（2026-05-20）\\\\n\\\\nLLaMA SFT 脚本里有 `export CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-0}}`，会覆盖 submit_training_job 注入的 CUDA_VISIBLE_DEVICES。**必须通过 `GPU=X` 环境变量传物理 GPU 编号**，不能依赖框架注入。\\\\n\\\\n## submit_training_job timeout 教训（2026-05-20 更新）\\\\n\\\\nLLaMA 8B no-evidence eval timeout 参考：\\\\n- **max_new_tokens=1024**: ~2h+，至少 14400s (4h)\\\\n- **max_new_tokens=2048 + 高截断 seed (s43)**: ~4.5h+，4h 仍不够（237/247, 96%，末段 ~70s/batch）。**至少 21600s (6h)**。s43 原 1024 版 truncation=38.4%，2048 版生成更长输出导致每 batch 耗时远超 s42/s44\\\\n\\\\n## LLaMA 完整统计（2026-05-20 更新）\\\\n\\\\n### SFT 3-seed\\\\n| Seed | ign_f1 | rel_f1 | edcr |\\\\n|------|--------|--------|------|\\\\n| s42 | 0.5384 | 0.5514 | — |\\\\n| s43 | 0.5142 | 0.5308 | 0.5866 |\\\\n| s44 | 0.4802 | 0.4902 | 0.6579 |\\\\n| **Mean** | **0.5109** | — | — |\\\\n| **Std** | **0.0238** | — | — |\\\\n\\\\ns44 异常低（较 s42 低 5.8pp），拉大了 SFT 方差。这恰好强化了 RSFT variance compression 的价值。\\\\n\\\\n### RSFT 3-seed (k=1)\\\\n| Seed | ign_f1 | rel_f1 | edcr |\\\\n|------|--------|--------|------|\\\\n| s42 | 0.5714 | 0.5839 | 0.5799 |\\\\n| s43 | 0.5662 | 0.5780 | 0.5783 |\\\\n| s44 | 0.5587 | 0.5706 | 0.5829 |\\\\n| **Mean** | **0.5654** | — | — |\\\\n| **Std** | **0.0052** | — | — |\\\\n\\\\n### 跨方法对比\\\\n- **SFT→RSFT Δ**: +5.45pp\\\\n- **方差压缩**: 4.58× (0.0238→0.0052)\\\\n- RSFT 在最弱 SFT seed (s44) 上仍显著提升：0.4802→0.5587 (+7.85pp)\\\\n\\\\n### Evidence Tax (LLaMA) — D134 决策：用 fair comparison 报告\\\\n\\\\n**RSFT 3-seed（完整）**：\\\\n- s42: no-evi 0.5526, with-evi 0.5714, tax=-1.88pp (evidence helps)\\\\n- s43: no-evi 0.5546, with-evi 0.5662, tax=-1.16pp (evidence helps)\\\\n- s44: no-evi 0.5550, with-evi 0.5587, tax=-0.37pp (evidence helps, 微弱)\\\\n- **Mean: -1.14pp ± 0.76pp**（3-seed 一致负向 = evidence 对 RSFT 有帮助）\\\\n- RSFT format compliance: 984/985 (99.9%)，fair comparison ≈ full set\\\\n\\\\n**SFT s44 no-evi 截断异常**：ign_f1=0.3326, truncation 41.7% (411/985)。正在跑 2048 版验证截断 vs 真实退化。\\\\n\\\\n**SFT（1024 版，已完成 2/3 seed）**：\\\\n- s42: raw tax=-1.65pp（不公平），**fair tax=+1.35pp**（evidence 有害）\\\\n- s44: raw tax=-14.76pp, **fair tax=-12.62pp**（evidence 极度有帮助，但截断率异常高）\\\\n- s43: 🔄 running\\\\n\\\\n**2048 版验证实验（进行中）**：\\\\n- eval_llama_sft_s42_no_evidence_2048 (cuda:3) — 方法论一致性\\\\n- eval_llama_sft_s44_no_evidence_2048 (cuda:2) — 截断伪影 vs 真实退化诊断\\\\n\\\\n**Reviewer control 需求**：如果 2048 版结果显著不同于 1024 → 需要 with-evi@2048 control（证明 with-evi 对 token limit 不敏感）。如果差异 <1pp → 不需要。\\\\n\\\\n## 🚨 Evidence Tax 方法论（D134 决策）\\\\n\\\\n**论文报告标准**：用 fair comparison（format-OK 子集），不修 parser。与 1.7B D083 方法论一致。\\\\n\\\\n**Fair comparison 脚本**：`/root/autodl-tmp/freige/scripts/analysis/fair_evidence_tax.py`，已用 s42 数据验证通过。\\\\n\\\\n**RSFT 压缩 evidence tax 方差**（Director insight）：SFT evidence tax swing 14pp（+1.35 到 -12.62），RSFT swing 1.5pp（-0.38 到 -1.88）。RSFT 不仅压缩 RE 方差，还让 evidence 的角色变得可预测。SFT 下 evidence 效果是 seed lottery，RSFT 下一致有帮助。\\\\n\\\\n## RSFT inference 架构（2026-05-20 确认）\\\\n\\\\nRSFT 是 nested LoRA：inference.py 先 merge SFT adapter 到 base model，再加载 RSFT adapter。**eval 时必须传 `--sft_adapter` 参数**，否则代码报错。\\\\n\\\\n## 14B Pipeline 状态（2026-05-20 更新）\\\\n\\\\n- Generation: r4 完成, 24216 candidates from 3027 docs\\\\n- **CED Scoring 完成** (plan017_14b_ced_scoring)：\\\\n  - 输出: `/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl` (3015 条, 9.1MB)\\\\n  - Selected F1=0.730, CED=0.690, Combined=0.768\\\\n  - vs 4B: F1 +5.4pp (0.676→0.730), CED +1.4pp (0.676→0.690)\\\\n  - 14B 候选质量显著优于 4B，验证 scaling 假设\\\\n- 下一步: RSFT training on 14B scored data\\\\n\\\\n## Qwen3-8B RSFT Evidence Tax 确认（2026-05-20）\\\\n\\\\n- no-evi ign_f1 = 0.5336, with-evi ign_f1 = 0.5414\\\\n- D127 tax = -0.78pp（evidence helps，微弱）\\\\n- 与 LLaMA RSFT (-1.14pp) 方向一致，跨家族均为负\\\\n\\\\n## Reviewer 发现（2026-05-20）\\\\n\\\\n- SFT evidence tax 方法论不一致：应该用同一模型加 `--no_evidence` flag，而非对比独立训练的 no-evidence 模型\\\\n- LLaMA eval configs 的 base_model 指向 Qwen3-4B（不影响结果，model_path 正确）\\\\n\\\\n## 竞品实验参考\\\\n\\\\n（待填充——首次进入新方向时从 literature_map 提取）\\\\n\\\", \\\"total_chars\\\": 4037, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# faith-evidence-ie Memory\\n\\n## 服务器架构（2026-05-20 更新）\\n\\n- **主服务器 westd-37389**: 4× RTX PRO 6000 Blackwell, 98GB VRAM/卡, 350GB 数据盘 (46% used, 190GB free)\\n  - SSH: `rtx5090-4x` (connect.westd.seetacloud.com:37389)\\n  - 环境: conda base, Python 3.12, PyTorch 2.8.0+cu128, transformers 5.8.1, flash-attn 2.8.3\\n- **数据源 bjb2-12179**: 全部 208G 数据完好，rsync 迁移主体完成，SFT adapter 补传中\\n  - SSH: `bjb2-12179` (connect.bjb2.seetacloud.com:12179)\\n- **废弃 bjb1-49673**: AutoDL 重启导致数据清空，已关停\\n\\n## GPU 分配教训（2026-05-20）\\n\\nLLaMA SFT 脚本里有 `export CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-0}}`，会覆盖 submit_training_job 注入的 CUDA_VISIBLE_DEVICES。**必须通过 `GPU=X` 环境变量传物理 GPU 编号**，不能依赖框架注入。\\n\\n## submit_training_job timeout 教训（2026-05-20 更新）\\n\\nLLaMA 8B no-evidence eval timeout 参考：\\n- **max_new_tokens=1024**: ~2h+，至少 14400s (4h)\\n- **max_new_tokens=2048 + 高截断 seed (s43)**: ~4.5h+，4h 仍不够（237/247, 96%，末段 ~70s/batch）。**至少 21600s (6h)**。s43 原 1024 版 truncation=38.4%，2048 版生成更长输出导致每 batch 耗时远超 s42/s44\\n\\n## LLaMA 完整统计（2026-05-20 更新）\\n\\n### SFT 3-seed\\n| Seed | ign_f1 | rel_f1 | edcr |\\n|------|--------|--------|------|\\n| s42 | 0.5384 | 0.5514 | — |\\n| s43 | 0.5142 | 0.5308 | 0.5866 |\\n| s44 | 0.4802 | 0.4902 | 0.6579 |\\n| **Mean** | **0.5109** | — | — |\\n| **Std** | **0.0238** | — | — |\\n\\ns44 异常低（较 s42 低 5.8pp），拉大了 SFT 方差。这恰好强化了 RSFT variance compression 的价值。\\n\\n### RSFT 3-seed (k=1)\\n| Seed | ign_f1 | rel_f1 | edcr |\\n|------|--------|--------|------|\\n| s42 | 0.5714 | 0.5839 | 0.5799 |\\n| s43 | 0.5662 | 0.5780 | 0.5783 |\\n| s44 | 0.5587 | 0.5706 | 0.5829 |\\n| **Mean** | **0.5654** | — | — |\\n| **Std** | **0.0052** | — | — |\\n\\n### 跨方法对比\\n- **SFT→RSFT Δ**: +5.45pp\\n- **方差压缩**: 4.58× (0.0238→0.0052)\\n- RSFT 在最弱 SFT seed (s44) 上仍显著提升：0.4802→0.5587 (+7.85pp)\\n\\n### Evidence Tax (LLaMA) — D134 决策：用 fair comparison 报告\\n\\n**RSFT 3-seed（完整）**：\\n- s42: no-evi 0.5526, with-evi 0.5714, tax=-1.88pp (evidence helps)\\n- s43: no-evi 0.5546, with-evi 0.5662, tax=-1.16pp (evidence helps)\\n- s44: no-evi 0.5550, with-evi 0.5587, tax=-0.37pp (evidence helps, 微弱)\\n- **Mean: -1.14pp ± 0.76pp**（3-seed 一致负向 = evidence 对 RSFT 有帮助）\\n- RSFT format compliance: 984/985 (99.9%)，fair comparison ≈ full set\\n\\n**SFT s44 no-evi 截断异常**：ign_f1=0.3326, truncation 41.7% (411/985)。正在跑 2048 版验证截断 vs 真实退化。\\n\\n**SFT（1024 版，已完成 2/3 seed）**：\\n- s42: raw tax=-1.65pp（不公平），**fair tax=+1.35pp**（evidence 有害）\\n- s44: raw tax=-14.76pp, **fair tax=-12.62pp**（evidence 极度有帮助，但截断率异常高）\\n- s43: 🔄 running\\n\\n**2048 版验证实验（进行中）**：\\n- eval_llama_sft_s42_no_evidence_2048 (cuda:3) — 方法论一致性\\n- eval_llama_sft_s44_no_evidence_2048 (cuda:2) — 截断伪影 vs 真实退化诊断\\n\\n**Reviewer control 需求**：如果 2048 版结果显著不同于 1024 → 需要 with-evi@2048 control（证明 with-evi 对 token limit 不敏感）。如果差异 <1pp → 不需要。\\n\\n## 🚨 Evidence Tax 方法论（D134 决策）\\n\\n**论文报告标准**：用 fair comparison（format-OK 子集），不修 parser。与 1.7B D083 方法论一致。\\n\\n**Fair comparison 脚本**：`/root/autodl-tmp/freige/scripts/analysis/fair_evidence_tax.py`，已用 s42 数据验证通过。\\n\\n**RSFT 压缩 evidence tax 方差**（Director insight）：SFT evidence tax swing 14pp（+1.35 到 -12.62），RSFT swing 1.5pp（-0.38 到 -1.88）。RSFT 不仅压缩 RE 方差，还让 evidence 的角色变得可预测。SFT 下 evidence 效果是 seed lottery，RSFT 下一致有帮助。\\n\\n## RSFT inference 架构（2026-05-20 确认）\\n\\nRSFT 是 nested LoRA：inference.py 先 merge SFT adapter 到 base model，再加载 RSFT adapter。**eval 时必须传 `--sft_adapter` 参数**，否则代码报错。\\n\\n## 14B Pipeline 状态（2026-05-20 更新）\\n\\n- Generation: r4 完成, 24216 candidates from 3027 docs\\n- **CED Scoring 完成** (plan017_14b_ced_scoring)：\\n  - 输出: `/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl` (3015 条, 9.1MB)\\n  - Selected F1=0.730, CED=0.690, Combined=0.768\\n  - vs 4B: F1 +5.4pp (0.676→0.730), CED +1.4pp (0.676→0.690)\\n  - 14B 候选质量显著优于 4B，验证 scaling 假设\\n- 下一步: RSFT training on 14B scored data\\n\\n## Qwen3-8B RSFT Evidence Tax 确认（2026-05-20）\\n\\n- no-evi ign_f1 = 0.5336, with-evi ign_f1 = 0.5414\\n- D127 tax = -0.78pp（evidence helps，微弱）\\n- 与 LLaMA RSFT (-1.14pp) 方向一致，跨家族均为负\\n\\n## Reviewer 发现（2026-05-20）\\n\\n- SFT evidence tax 方法论不一致：应该用同一模型加 `--no_evidence` flag，而非对比独立训练的 no-evidence 模型\\n- LLaMA eval configs 的 base_model 指向 Qwen3-4B（不影响结果，model_path 正确）\\n\\n## 竞品实验参考\\n\\n（待填充——首次进入新方向时从 literature_map 提取）\\n\", \"total_chars\": 4037, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "2adf4981-f27b-4638-8657-f757a7593359",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "8ac8f8ae-44c6-4626-8ebe-c70f91645eec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 88_

```json
{
  "type": "last-prompt",
  "leafUuid": "1be298ee-fd6c-482d-8fb8-f963f3ddc48d",
  "sessionId": "8ac8f8ae-44c6-4626-8ebe-c70f91645eec"
}
```

---


### Runtime record

_source line 89_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile matched@2048 evidence tax data summary",
  "sessionId": "8ac8f8ae-44c6-4626-8ebe-c70f91645eec"
}
```

---


### Assistant

_source line 90 · 2026-05-21T03:40:37.574Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full current memory.md. Let me compose the updated version with the new "@2048 Evidence Tax 数据编译" section added. I need to:

1. Keep all existing content
2. Add the new section
3. Update some stale sections (like "2048 版验证实验（进行中）" which are now completed)

Let me update the following:
- The "Evidence Tax (LLaMA)" section: update the SFT @1024 status (s43 was running, need to check) and the 2048 verification experiments (now completed)


- Add the new "Matched@2048 Evidence Tax 数据编译" section

Actually, I'll skip updating the @1024 data since I don't have the metrics readily available, and just focus on adding the new @2048 section as requested.

The task is specifically to add this new section, not rewrite the whole file, so I'll keep everything else intact and insert it after the Reviewer 发现 section, before 竞品实验参考.

I'm constructing the new section with the D137 decision about evidence tax calculations at matched token budgets and the LLaMA 8B SFT metrics at @2048.

Generating markdown table... Generating results table... 已有 fair_tax_*_2048.json 文件是用 with-evi@1024 + no-evi@2048 计算的，**不是** matched@2048。需要 with-evi@2048 完成后重新计算。

现在看着 LLaMA 8B 的 RSFT 结果，三个种子的 @2048 评估都在排队提交，其中 s42 with-evi 正在 GPU 0 上运行。@1024 的税收均值约 -1.14pp，格式合规率 99.9%，截断率在 18-19%，@2048 可能会有明显变化。

Qwen3-14B 这边 with-evi 配置也在 GPU 1 上运行中，no-evi 的 @2048 结果还在等待提交，两个配置的 @1024 截断率都在 10.7-10.8% 左右。 Looking at the GPU usage, the SFT evaluations with evidence at 2048 tokens are progressing well—s42 took about 2.9 hours and s43/s44 have been running for roughly 2.5 hours, so they should wrap up in another 1-2 hours. The RSFT and 14B models just started about 15 minutes ago and are expected to take around 3 hours each. For the queue, I can immediately compute the fair_tax matched results for SFT s42 since both datasets are ready, and then move on to the RSFT s42 no-evidence run once that's queued.

The remaining tasks—RSFT s43/s44 and the 14B model—are all waiting for GPU availability, and the fair_tax calculations for s43/s44 depend on their with-evidence runs finishing first. I've also verified that the fair_evidence_tax script handles both evidence and no-evidence prediction paths and works transparently with the 2048 token data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1be298ee-fd6c-482d-8fb8-f963f3ddc48d",
  "isSidechain": false,
  "requestId": "req_011CbF24hejkLrvoxvmHvjBy",
  "type": "assistant",
  "uuid": "b308b256-7901-44e1-85e2-e14c36a156d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "8ac8f8ae-44c6-4626-8ebe-c70f91645eec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015naNAkSxb3Pmh11ANpWFCE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8889,
      "cache_read_input_tokens": 54725,
      "output_tokens": 6455,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8889,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6455,
          "cache_read_input_tokens": 54725,
          "cache_creation_input_tokens": 8889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8889
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 91 · 2026-05-21T03:40:38.032Z_

Now I'll compose the updated memory.md with the new section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b308b256-7901-44e1-85e2-e14c36a156d0",
  "isSidechain": false,
  "requestId": "req_011CbF24hejkLrvoxvmHvjBy",
  "type": "assistant",
  "uuid": "19b0f36a-f714-4785-b329-75f01516ffba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "8ac8f8ae-44c6-4626-8ebe-c70f91645eec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015naNAkSxb3Pmh11ANpWFCE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8889,
      "cache_read_input_tokens": 54725,
      "output_tokens": 6455,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8889,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6455,
          "cache_read_input_tokens": 54725,
          "cache_creation_input_tokens": 8889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8889
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-21T03:41:39.615Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_019DLginr396VYPYWthqNBDh`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "memory.md",
  "content": "# faith-evidence-ie Memory\n\n## 服务器架构（2026-05-20 更新）\n\n- **主服务器 westd-37389**: 4× RTX PRO 6000 Blackwell, 98GB VRAM/卡, 350GB 数据盘 (46% used, 190GB free)\n  - SSH: `rtx5090-4x` (connect.westd.seetacloud.com:37389)\n  - 环境: conda base, Python 3.12, PyTorch 2.8.0+cu128, transformers 5.8.1, flash-attn 2.8.3\n- **数据源 bjb2-12179**: 全部 208G 数据完好，rsync 迁移主体完成，SFT adapter 补传中\n  - SSH: `bjb2-12179` (connect.bjb2.seetacloud.com:12179)\n- **废弃 bjb1-49673**: AutoDL 重启导致数据清空，已关停\n\n## GPU 分配教训（2026-05-20）\n\nLLaMA SFT 脚本里有 `export CUDA_VISIBLE_DEVICES=${GPU:-${CUDA_VISIBLE_DEVICES:-0}}`，会覆盖 submit_training_job 注入的 CUDA_VISIBLE_DEVICES。**必须通过 `GPU=X` 环境变量传物理 GPU 编号**，不能依赖框架注入。\n\n## submit_training_job timeout 教训（2026-05-20 更新）\n\nLLaMA 8B no-evidence eval timeout 参考：\n- **max_new_tokens=1024**: ~2h+，至少 14400s (4h)\n- **max_new_tokens=2048 + 高截断 seed (s43)**: ~4.5h+，4h 仍不够（237/247, 96%，末段 ~70s/batch）。**至少 21600s (6h)**。s43 原 1024 版 truncation=38.4%，2048 版生成更长输出导致每 batch 耗时远超 s42/s44\n\n## LLaMA 完整统计（2026-05-20 更新）\n\n### SFT 3-seed\n| Seed | ign_f1 | rel_f1 | edcr |\n|------|--------|--------|------|\n| s42 | 0.5384 | 0.5514 | — |\n| s43 | 0.5142 | 0.5308 | 0.5866 |\n| s44 | 0.4802 | 0.4902 | 0.6579 |\n| **Mean** | **0.5109** | — | — |\n| **Std** | **0.0238** | — | — |\n\ns44 异常低（较 s42 低 5.8pp），拉大了 SFT 方差。这恰好强化了 RSFT variance compression 的价值。\n\n### RSFT 3-seed (k=1)\n| Seed | ign_f1 | rel_f1 | edcr |\n|------|--------|--------|------|\n| s42 | 0.5714 | 0.5839 | 0.5799 |\n| s43 | 0.5662 | 0.5780 | 0.5783 |\n| s44 | 0.5587 | 0.5706 | 0.5829 |\n| **Mean** | **0.5654** | — | — |\n| **Std** | **0.0052** | — | — |\n\n### 跨方法对比\n- **SFT→RSFT Δ**: +5.45pp\n- **方差压缩**: 4.58× (0.0238→0.0052)\n- RSFT 在最弱 SFT seed (s44) 上仍显著提升：0.4802→0.5587 (+7.85pp)\n\n### Evidence Tax (LLaMA) — D134 决策：用 fair comparison 报告\n\n**RSFT 3-seed（完整，@1024）**：\n- s42: no-evi 0.5526, with-evi 0.5714, tax=-1.88pp (evidence helps)\n- s43: no-evi 0.5546, with-evi 0.5662, tax=-1.16pp (evidence helps)\n- s44: no-evi 0.5550, with-evi 0.5587, tax=-0.37pp (evidence helps, 微弱)\n- **Mean: -1.14pp ± 0.76pp**（3-seed 一致负向 = evidence 对 RSFT 有帮助）\n- RSFT format compliance: 984/985 (99.9%)，fair comparison ≈ full set\n\n**SFT（@1024，已完成 2/3 seed）**：\n- s42: raw tax=-1.65pp（不公平），**fair tax=+1.35pp**（evidence 有害）\n- s44: raw tax=-14.76pp, **fair tax=-12.62pp**（evidence 极度有帮助，但截断率异常高）\n\n## 🚨 Evidence Tax 方法论（D134/D137 决策）\n\n**论文报告标准**：用 fair comparison（format-OK 子集），不修 parser。与 1.7B D083 方法论一致。\n\n**D137 追加**：所有 evidence tax 必须在 matched token budget (max_new_tokens=2048) 下计算，@1024 受截断伪影影响。\n\n**Fair comparison 脚本**：`/root/autodl-tmp/freige/scripts/analysis/fair_evidence_tax.py`，接受 `--with-evi` 和 `--no-evi` predictions.json 路径，对 max_new_tokens 透明，已支持 @2048 数据输入，**无需修改**。\n\n**RSFT 压缩 evidence tax 方差**（Director insight）：SFT evidence tax swing 14pp（+1.35 到 -12.62），RSFT swing 1.5pp（-0.38 到 -1.88）。RSFT 不仅压缩 RE 方差，还让 evidence 的角色变得可预测。SFT 下 evidence 效果是 seed lottery，RSFT 下一致有帮助。\n\n## Matched@2048 Evidence Tax 数据编译（2026-05-21）\n\n### LLaMA 8B SFT — @2048 原始指标\n\n| Seed | Config | ign_f1 | truncated | format_ok | status |\n|------|--------|--------|-----------|-----------|--------|\n| s42 | no-evi@2048 | 0.5210 | 201 (20.4%) | 874 (88.7%) | ✅ |\n| s42 | with-evi@2048 | 0.5649 | 147 (14.9%) | 976 (99.1%) | ✅ |\n| s43 | no-evi@2048 | 0.3389 | 359 (36.4%) | 834 (84.7%) | ✅ |\n| s43 | with-evi@2048 | — | — | — | 🔄 running (GPU 2) |\n| s44 | no-evi@2048 | 0.4373 | 246 (25.0%) | 977 (99.2%) | ✅ |\n| s44 | with-evi@2048 | — | — | — | 🔄 running (GPU 3) |\n\n**SFT s42 matched@2048 raw tax**: 0.5210 - 0.5649 = **-4.39pp**（evidence helps，比 @1024 raw tax -1.65pp 幅度大 2.7 倍）\n\n⚠️ s43 no-evi@2048 ign_f1=0.3389 极低，truncation 仍 36.4% 即使 2048 tokens——该 seed 输出极度冗长。\n\n### LLaMA 8B SFT — Matched@2048 Evidence Tax 汇总\n\n| Seed | with-evi@2048 ign_f1 | no-evi@2048 ign_f1 | matched tax (pp) | fair tax (pp) | status |\n|------|----------------------|---------------------|------------------|---------------|--------|\n| s42 | 0.5649 | 0.5210 | -4.39 | 待计算 | ✅ 两侧齐备 |\n| s43 | 🔄 running | 0.3389 | — | — | with-evi 待完成 |\n| s44 | 🔄 running | 0.4373 | — | — | with-evi 待完成 |\n\n⚠️ 已有 `fair_tax_*_2048.json` 文件是用 with-evi@1024 + no-evi@2048 计算的（s42: +1.20pp, s44: -4.18pp），**不是 matched@2048**。需 with-evi@2048 完成后用 fair_evidence_tax.py 重算。\n\n### LLaMA 8B RSFT — @2048\n\n| Seed | Config | @1024 ign_f1 | @2048 ign_f1 | status |\n|------|--------|-------------|-------------|--------|\n| s42 | with-evi | 0.5714 | 🔄 running (GPU 0) | — |\n| s42 | no-evi | 0.5526 | 待提交 | — |\n| s43 | with-evi | 0.5662 | 待提交 | — |\n| s43 | no-evi | 0.5546 | 待提交 | — |\n| s44 | with-evi | 0.5587 | 待提交 | — |\n| s44 | no-evi | 0.5550 | 待提交 | — |\n\nRSFT @1024 tax mean=-1.14pp±0.76pp，format compliance 99.9%（fair≈full）。@1024 截断率 18-19%，@2048 预期降低。\n\n### Qwen3-14B RSFT — @2048\n\n| Config | @1024 ign_f1 | @1024 truncated | @2048 ign_f1 | status |\n|--------|-------------|-----------------|-------------|--------|\n| with-evi | 0.5886 | 105 (10.7%) | 🔄 running (GPU 1) | — |\n| no-evi | 0.5432 | 106 (10.8%) | 待提交 | — |\n\n14B @1024 raw tax: 0.5432 - 0.5886 = **-4.54pp**（evidence helps，幅度最大）\n\n### GPU 占用快照（2026-05-21 ~11:00 UTC）\n\n| GPU | PID | Task | Started |\n|-----|-----|------|---------|\n| 0 | 70711 | RSFT s42 with-evi@2048 | 10:47 |\n| 1 | 70393 | 14B RSFT with-evi@2048 | 10:46 |\n| 2 | 64396 | SFT s43 with-evi@2048 | 08:46 |\n| 3 | 64024 | SFT s44 with-evi@2048 | 08:45 |\n\nSFT with-evi@2048 参考耗时：s42 用了 2.9h (10492s)。s43/s44 已跑 ~2.5h，预计再 1-2h 完成。RSFT/14B 刚启动 ~15min，预计 ~2-3h。\n\n### 待执行任务队列（按优先级）\n\n1. ✅ **SFT s42 matched@2048 fair tax** — 两侧数据齐备，可立即运行 fair_evidence_tax.py\n2. 等 GPU 空闲后提交：RSFT s42 no-evi@2048\n3. 等 GPU 空闲后提交：RSFT s43 with-evi@2048 + no-evi@2048\n4. 等 GPU 空闲后提交：RSFT s44 with-evi@2048 + no-evi@2048\n5. 等 GPU 空闲后提交：14B no-evi@2048\n6. SFT s43/s44 fair tax matched@2048 — 等 with-evi@2048 完成后计算\n7. RSFT 3-seed matched@2048 fair tax — 等全部 6 个 eval 完成后计算\n8. 14B matched@2048 tax — 等 with-evi@2048 + no-evi@2048 都完成\n\n## RSFT inference 架构（2026-05-20 确认）\n\nRSFT 是 nested LoRA：inference.py 先 merge SFT adapter 到 base model，再加载 RSFT adapter。**eval 时必须传 `--sft_adapter` 参数**，否则代码报错。\n\n## 14B Pipeline 状态（2026-05-21 更新）\n\n- Generation: r4 完成, 24216 candidates from 3027 docs\n- **CED Scoring 完成** (plan017_14b_ced_scoring)：\n  - 输出: `/root/autodl-tmp/rsft_scored_14b/rsft_train.jsonl` (3015 条, 9.1MB)\n  - Selected F1=0.730, CED=0.690, Combined=0.768\n  - vs 4B: F1 +5.4pp (0.676→0.730), CED +1.4pp (0.676→0.690)\n- **RSFT Training 完成**，eval @1024 done（with-evi ign_f1=0.5886, no-evi ign_f1=0.5432）\n- 当前：with-evi@2048 eval 运行中\n\n## Qwen3-8B RSFT Evidence Tax 确认（2026-05-20）\n\n- no-evi ign_f1 = 0.5336, with-evi ign_f1 = 0.5414\n- D127 tax = -0.78pp（evidence helps，微弱）\n- 与 LLaMA RSFT (-1.14pp) 方向一致，跨家族均为负\n\n## Reviewer 发现（2026-05-20）\n\n- SFT evidence tax 方法论不一致：应该用同一模型加 `--no_evidence` flag，而非对比独立训练的 no-evidence 模型\n- LLaMA eval configs 的 base_model 指向 Qwen3-4B（不影响结果，model_path 正确）\n\n## 竞品实验参考\n\n（待填充——首次进入新方向时从 literature_map 提取）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19b0f36a-f714-4785-b329-75f01516ffba",
  "isSidechain": false,
  "requestId": "req_011CbF24hejkLrvoxvmHvjBy",
  "type": "assistant",
  "uuid": "5a171c7c-f85a-4f69-9894-b209f40d4b98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "8ac8f8ae-44c6-4626-8ebe-c70f91645eec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015naNAkSxb3Pmh11ANpWFCE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8889,
      "cache_read_input_tokens": 54725,
      "output_tokens": 6455,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8889,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6455,
          "cache_read_input_tokens": 54725,
          "cache_creation_input_tokens": 8889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8889
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-21T03:41:39.640Z_

<details><summary>↩ Tool result · `toolu_019DLginr396VYPYWthqNBDh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a171c7c-f85a-4f69-9894-b209f40d4b98",
  "isSidechain": false,
  "promptId": "9de4b2f0-56de-4de7-a2d6-d458631a94f6",
  "type": "user",
  "uuid": "49ef0d92-4bb1-433e-8295-4dfe4b024e99",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "5a171c7c-f85a-4f69-9894-b209f40d4b98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "8ac8f8ae-44c6-4626-8ebe-c70f91645eec",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 94 · 2026-05-21T03:41:48.741Z_

汇总完成。关键发现：

**已齐备的 matched@2048 数据：**
- SFT s42: with-evi=0.5649, no-evi=0.5210, **raw tax=-4.39pp**（evidence helps，幅度是 @1024 的 2.7 倍）

**4 个 with-evi@2048 eval 正在跑（4 GPU 全占）：**
- SFT s43 (GPU 2, 已跑 ~2.5h), s44 (GPU 3, 已跑 ~2.5h) — 预计再 1-2h
- RSFT s42 (GPU 0, 刚启动) — 预计 ~2-3h
- 14B RSFT (GPU 1, 刚启动) — 预计 ~2-3h

**可立即执行：** SFT s42 的 fair_evidence_tax.py，两侧 @2048 predictions 都已就绪。

**待后续提交（需等 GPU 空闲）：** RSFT s42 no-evi@2048, RSFT s43/s44 双侧@2048, 14B no-evi@2048 — 共 7 个 eval job。

**fair_evidence_tax.py** 对 max_new_tokens 透明，无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "49ef0d92-4bb1-433e-8295-4dfe4b024e99",
  "isSidechain": false,
  "requestId": "req_011CbF2CiwMZKS6N2SHym9pM",
  "type": "assistant",
  "uuid": "4b69ff80-c9d7-4e1e-8410-659637513118",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "8ac8f8ae-44c6-4626-8ebe-c70f91645eec",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bpp3BvXQc3A7xHgnZQ9DiJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6533,
      "cache_read_input_tokens": 63614,
      "output_tokens": 370,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6533,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 370,
          "cache_read_input_tokens": 63614,
          "cache_creation_input_tokens": 6533,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6533
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 95_

```json
{
  "type": "last-prompt",
  "leafUuid": "4b69ff80-c9d7-4e1e-8410-659637513118",
  "sessionId": "8ac8f8ae-44c6-4626-8ebe-c70f91645eec"
}
```

---


### Runtime record

_source line 96_

```json
{
  "type": "ai-title",
  "aiTitle": "Compile matched@2048 evidence tax data summary",
  "sessionId": "8ac8f8ae-44c6-4626-8ebe-c70f91645eec"
}
```

---
