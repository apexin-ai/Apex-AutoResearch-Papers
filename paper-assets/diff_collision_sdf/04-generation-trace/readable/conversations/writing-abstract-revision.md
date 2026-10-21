# writing abstract revision

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_writing_abstract_revision_20260527T071518.jsonl`
- **Structured JSON:** [`b9d5bfbce5af64668bab.json`](../../sessions/b9/b9d5bfbce5af64668bab.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-27T07:19:26.464090+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-27T07:19:26.464453+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T07:19:26.464658+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "diff_collision_sdf",
  "file": "paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "diff_collision_sdf",
    "file": "paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T07:19:26.464928+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/paper_framing.md\", \"content\": \"# ColliForce-VLA Paper Framing\\n\\n> 维护者: Director | 最后更新: 2026-05-27 01:15 UTC | D035: Scenario B 双 seed 确认，Core Insight 修正 | Post-MVP research phase\\n\\n## Core Insight\\n\\nVLA safety 评估存在系统性缺陷：collision avoidance rate (CAR) 被 action collapse 和几何路径安全严重污染，导致 \\\"安全\\\" 指标虚高。我们通过大规模实证分析（90+ 实验, 6000+ episodes）揭示这一系统性缺陷，提出 EE displacement-filtered CAR 作为修正指标，并证明碰撞避免能力隐式来自 collision-free demonstration data，而非显式几何监督——SDF auxiliary loss 在全测试范围 λ∈[0.005, 0.1] 完全冗余，binding constraint 是 EE-only 的结构性不匹配。\\n\\n## Working Title\\n\\n\\\"Rethinking VLA Safety Evaluation: When 98% of Collision Avoidance is an Illusion\\\"\\n\\n> 聚焦评估方法论贡献（影响面广、scope-proof），SDF 作为验证工具而非主贡献\\n\\n## Target Venue\\n\\n**Primary**: CoRL 2026 Main / ICRA 2027 (用户明确要求主会)\\n**定位**: Diagnostic/evaluation methodology paper with positive method contribution\\n**Fit**: Robotics safety track — \\\"VLA safety metrics are fundamentally broken\\\" 对社区有直接影响\\n\\n## Core Claims (D028 重组: 4→3 claims)\\n\\n### Claim 1: CAR Metric Contaminated by Fake Safety (Primary — 证据强度 ★★★★★)\\n\\nStandard CAR metric is systematically contaminated by two distinct mechanisms: (a) action collapse producing frozen robots falsely counted as \\\"safe\\\", and (b) geometric path safety where capable robots happen to avoid obstacles without any avoidance behavior. \\\"Collision-free\\\" ≠ \\\"collision-avoiding.\\\"\\n\\n**Primary evidence — Action collapse (fake safety)**:\\n- 800 episodes A1 per-episode analysis: CAR=91.5%, but 99.6% of safe episodes show obstacle displacement < 0.1mm (~5nm median) — robot is frozen\\n- TSR=0% 独立确认 action collapse\\n- 术语修正 (D023): fake safety 判定以 TSR=0% + obstacle displacement < 0.1mm 双证据链为主\\n\\n**Supporting evidence — Capability-safety anti-correlation (原 Claim 2)**:\\n- Pi0.5 3-seed eval: TSR=74.7±1.5%, CAR=26.8±1.6% — 更强模型完成更多任务
…[truncated 9749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-27T07:19:26.465098+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "diff_collision_sdf",
  "filters": "{'status': 'DONE'}",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "diff_collision_sdf",
    "filters": "{'status': 'DONE'}",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-27T07:19:26.465548+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_stepwise_s0_l1_24k_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-27T06:00:33.591Z\", \"updated_at\": \"2026-05-27T06:59:23.825Z\", \"hypothesis\": \"Re-eval 24K with correct --pi05 flag. Original eval_stepwise_s0_l1_24k produced frozen=29.5% artifact due to missing --pi05. 26K v2 with --pi05 showed frozen=0%. This re-eval verifies whether 24K frozen was also an artifact. Expected: frozen=0%, CAR ≈ 54-56% (baseline range).\", \"parent\": \"eval_stepwise_s0_l1_24k\", \"conclusion\": \"negative\", \"metrics\": {\"CAR\": 52.5, \"dfCAR\": 52.5, \"frozen_rate\": 0, \"TSR\": 50.5, \"per_task_CAR\": {\"orange_juice\": 54, \"chocolate_pudding\": 72, \"milk\": 64, \"bbq_sauce\": 20}, \"per_task_TSR\": {\"orange_juice\": 30, \"chocolate_pudding\": 78, \"milk\": 30, \"bbq_sauce\": 64}, \"per_task_frozen\": {\"orange_juice\": 0, \"chocolate_pudding\": 0, \"milk\": 0, \"bbq_sauce\": 0}}}, \"eval_stepwise_s0_l1_24k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-27T03:55:41.168Z\", \"updated_at\": \"2026-05-27T05:58:26.176Z\", \"hypothesis\": \"Step-wise eval of λ=0.1 seed0 at 24K steps on safelibero_object. Continuing the learning curve: 16K(CAR=55.5)→20K(CAR=55)→22K(CAR=60.5)→24K(?). Tests whether CAR continues to improve with more training or plateaus/degrades.\", \"parent\": \"eval_stepwise_s0_l1_22k\", \"metrics\": {\"INVALID\": true, \"invalidation_reason\": \"Missing --pi05 flag caused architecture mismatch (Pi0 instead of Pi0.5), producing 29.5% frozen episodes as artifact. All metrics from this eval are unreliable. See eval_stepwise_s0_l1_24k_v2 for corrected results.\", \"original_CAR\": 55.5, \"original_frozen_rate\": 29.5, \"original_dfCAR\": 36.9}, \"conclusion\": \"failed\"}, \"eval_stepwise_s0_l1_26k_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-27T05:32:59.417Z\", \"updated_at\": \"2026-05-27T05:55:50.151Z\", \"hypothesis\": \"The 24K frozen episodes (29.5%) were caused by miss
…[truncated 15092 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T07:19:26.465755+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/abstract*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/abstract*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T07:19:26.465892+00:00_

artifacts/drafts/abstract.tex
artifacts/_project/paper/abstract_v2.tex
artifacts/drafts/abstract_v2.tex
.venv/lib/python3.14/site-packages/pip/_vendor/resolvelib/resolvers/abstract.py
.venv/lib/python3.14/site-packages/pip/_vendor/resolvelib/resolvers/__pycache__/abstract.cpython-314.pyc
docs/paper/abstract.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-27T07:19:26.466018+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**/*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T07:19:26.466157+00:00_

artifacts/_project/paper/method_draft.md
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/method.tex
docs/paper/_archive/method.tex
artifacts/_project/paper/related_work.tex
docs/paper/_archive/experiments.tex
docs/paper/_archive/conclusion_DEPRECATED.tex
artifacts/_project/paper/analysis_claim1.tex
artifacts/_project/paper/analysis_claim2.tex
artifacts/_project/paper/analysis_claim3.tex
artifacts/_project/paper/experimental_framework.tex
artifacts/_project/paper/introduction_v2.tex
artifacts/_project/paper/abstract_v2.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/related_work_v2.tex
docs/paper/archive/analysis_claim4.tex
docs/paper/_pdf_images/main_p1.png
docs/paper/_pdf_images/main_p2.png
docs/paper/_pdf_images/main_p3.png
docs/paper/_pdf_images/main_p4.png
docs/paper/_pdf_images/main_p5.png
docs/paper/_pdf_images/main_p6.png
docs/paper/_pdf_images/main_p7.png
docs/paper/_pdf_images/main_p8.png
docs/paper/_pdf_images/main_p9.png
docs/paper/_pdf_images/main_p10.png
docs/paper/_pdf_images/main_p11.png
docs/paper/_pdf_images/main_p12.png
docs/paper/_pdf_images/main_p13.png
docs/paper/_pdf_images/main_p14.png
artifacts/_project/paper/section5_5_method_boundaries.md
paper/section5_5_method_boundaries.md
docs/paper/experimental_framework.tex
docs/paper/archive/analysis_claim3.tex
docs/paper/archive/analysis_claim1.tex
docs/paper/archive/analysis_claim2.tex
artifacts/_project/paper/paper_draft.pdf
docs/paper/references.bib
docs/paper/related_work.tex
docs/paper/corl_2026.sty
docs/paper/corlabbrvnat.bst
docs/paper/main.tex
docs/paper/contingency_claim3.tex
docs/paper/method.tex
docs/paper/claim1.tex
docs/paper/claim2.tex
artifacts/_project/paper/abc_scenario_patches.md
docs/paper/introduction.tex
docs/paper/discussion.tex
docs/paper/main.blg
docs/paper/main.bbl
docs/paper/main.aux
docs/paper/main.out
docs/paper/main.fls
docs/paper/main.log
docs/paper/main.pdf
docs/paper/main.fdb_latexmk
docs/paper/appendix.tex
docs/paper/claim3.tex
…[truncated 24 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T07:19:26.466338+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T07:19:26.466518+00:00_

1	\begin{abstract}
2	Vision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are systematically contaminated by action collapse.
3	On SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\% CAR while 99.6\% of its safe episodes exhibit end-effector displacement below 0.1\,mm---the robot is frozen, not safe.
4	We present displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes, as a corrective metric; the bimodal displacement distribution makes it robust across a $[2, 200]$\,mm threshold range.
5	Our analysis further reveals that end-effector-only Signed Distance Field (SDF) supervision is neither necessary nor structurally sufficient for collision avoidance.
6	It is counterproductive at inference time: three ground-truth oracle variants all reduce CAR below unrefined baselines, as SDF gradients repelling the end-effector drive arm links into obstacles.
7	It is redundant during training: LoRA-only fine-tuning raises CAR from 28.5\% to 54.5\%$\,\pm\,$2.83, matching SDF-augmented training at $\lambda{=}0.005$ (54.5\%$\,\pm\,$2.29) and $\lambda{=}0.01$ (56.33\%$\,\pm\,$1.61) \placeholder{$\lambda{=}0.1$ 30K three-seed results pending}.
8	Per-task avoidance patterns remain identical across all conditions, indicating that collision avoidance arises from collision-free demonstration data rather than geometric supervision.
9	Displacement filtering is necessary for meaningful VLA safety evaluation; EE-only geometric supervision can be neither credited with nor expected to deliver collision avoidance.
10	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-27T07:19:26.466668+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "diff_collision_sdf",
  "filters": "{'status': 'DONE'}",
  "limit": "20",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "diff_collision_sdf",
    "filters": "{'status': 'DONE'}",
    "limit": "20",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T07:19:26.467262+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_stepwise_s0_l1_24k_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-27T06:00:33.591Z\", \"updated_at\": \"2026-05-27T06:59:23.825Z\", \"hypothesis\": \"Re-eval 24K with correct --pi05 flag. Original eval_stepwise_s0_l1_24k produced frozen=29.5% artifact due to missing --pi05. 26K v2 with --pi05 showed frozen=0%. This re-eval verifies whether 24K frozen was also an artifact. Expected: frozen=0%, CAR ≈ 54-56% (baseline range).\", \"parent\": \"eval_stepwise_s0_l1_24k\", \"spec\": {\"command\": \"python scripts/eval_safelibero.py --checkpoint /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l1/24000 --config_name pi05_libero --model_type lora_baseline --pi05 --suite safelibero_object --safety_level II --n_episodes 50 --seed 7 --gpu 0\", \"server\": \"westd-35807\", \"gpu\": [\"cuda:0\"], \"pid\": \"669037\", \"log_path\": \"/tmp/eval_24k_v2.log\", \"data_path\": \"safelibero_object\", \"data_count\": 200, \"model_name\": \"pi05_a1_sdf_object_pudding_seed0_l1_24k\", \"seed\": 7, \"checkpoint_source\": \"/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l1/24000\", \"eval_data\": \"safelibero_object_safety_II\"}, \"reproduce\": {\"finished_at\": \"2026-05-27T06:41:52.105Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-27T06:41:50.686Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-27T06:41:55.098533+00:00\"}]}, \"metrics\": {\"CAR\": 52.5, \"dfCAR\": 52.5, \"frozen_rate\": 0, \"TSR\": 50.5, \"per_task_CAR\": {\"orange_juice\": 54, \"chocolate_pudding\": 72, \"milk\": 64, \"bbq_sauce\": 20}, \"per_task_TSR\": {\"orange_juice\": 30, \"chocolate_pudding\": 78, \"milk\": 30, \"bbq_sauce\": 64}, \"per_task_frozen\": {\"orange_juice\": 0, \"chocolate_pud
…[truncated 31253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T07:19:26.467513+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "diff_collision_sdf",
  "filters": "{'status': 'DONE'}",
  "limit": "40",
  "fields": "['metrics', 'conclusion', 'hypothesis', 'notes']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "diff_collision_sdf",
    "filters": "{'status': 'DONE'}",
    "limit": "40",
    "fields": "['metrics', 'conclusion', 'hypothesis', 'notes']"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-27T07:19:26.468051+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_stepwise_s0_l1_24k_v2\": {\"hypothesis\": \"Re-eval 24K with correct --pi05 flag. Original eval_stepwise_s0_l1_24k produced frozen=29.5% artifact due to missing --pi05. 26K v2 with --pi05 showed frozen=0%. This re-eval verifies whether 24K frozen was also an artifact. Expected: frozen=0%, CAR ≈ 54-56% (baseline range).\", \"conclusion\": \"negative\", \"metrics\": {\"CAR\": 52.5, \"dfCAR\": 52.5, \"frozen_rate\": 0, \"TSR\": 50.5, \"per_task_CAR\": {\"orange_juice\": 54, \"chocolate_pudding\": 72, \"milk\": 64, \"bbq_sauce\": 20}, \"per_task_TSR\": {\"orange_juice\": 30, \"chocolate_pudding\": 78, \"milk\": 30, \"bbq_sauce\": 64}, \"per_task_frozen\": {\"orange_juice\": 0, \"chocolate_pudding\": 0, \"milk\": 0, \"bbq_sauce\": 0}}}, \"eval_stepwise_s0_l1_24k\": {\"hypothesis\": \"Step-wise eval of λ=0.1 seed0 at 24K steps on safelibero_object. Continuing the learning curve: 16K(CAR=55.5)→20K(CAR=55)→22K(CAR=60.5)→24K(?). Tests whether CAR continues to improve with more training or plateaus/degrades.\", \"metrics\": {\"INVALID\": true, \"invalidation_reason\": \"Missing --pi05 flag caused architecture mismatch (Pi0 instead of Pi0.5), producing 29.5% frozen episodes as artifact. All metrics from this eval are unreliable. See eval_stepwise_s0_l1_24k_v2 for corrected results.\", \"original_CAR\": 55.5, \"original_frozen_rate\": 29.5, \"original_dfCAR\": 36.9}, \"conclusion\": \"failed\"}, \"eval_stepwise_s0_l1_26k_v2\": {\"hypothesis\": \"The 24K frozen episodes (29.5%) were caused by missing --pi05 flag in eval, not by SDF training degradation. Re-running 26K eval with --pi05 should eliminate frozen episodes and reveal true collision avoidance performance close to LoRA baseline (dfCAR ~54.5%).\", \"metrics\": {\"TSR\": 0.53, \"CAR\": 0.535, \"dfCAR\": 0.535, \"frozen_rate\": 0, \"frozen_episodes\": 0, \"total_episodes\": 200, \"per_task\": {\"orange_juice\": {\"TSR\": 0.32, \"CAR\": 0.46, \"dfCAR\": 0.46
…[truncated 28163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-27T07:19:26.468332+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
  "old_string": "yet we show these metrics are systematically contaminated by action collapse.",
  "new_string": "yet we show these metrics are contaminated by action collapse."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
    "old_string": "yet we show these metrics are systematically contaminated by action collapse.",
    "new_string": "yet we show these metrics are contaminated by action collapse."
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T07:19:26.468511+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-27T07:19:26.468641+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
  "old_string": "three ground-truth oracle variants all reduce CAR below unrefined baselines",
  "new_string": "three ground-truth oracle variants all reduce dfCAR below unrefined baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
    "old_string": "three ground-truth oracle variants all reduce CAR below unrefined baselines",
    "new_string": "three ground-truth oracle variants all reduce dfCAR below unrefined baselines"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T07:19:26.468777+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-27T07:19:26.468896+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
  "old_string": "LoRA-only fine-tuning raises CAR from",
  "new_string": "LoRA-only fine-tuning raises dfCAR from"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex",
    "old_string": "LoRA-only fine-tuning raises CAR from",
    "new_string": "LoRA-only fine-tuning raises dfCAR from"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-27T07:19:26.469028+00:00_

The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-27T07:19:26.469162+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-27T07:19:26.469293+00:00_

1	\begin{abstract}
2	Vision-Language-Action (VLA) models report high Collision Avoidance Rates (CAR) on safety benchmarks, yet we show these metrics are contaminated by action collapse.
3	On SafeLIBERO, an SDF-augmented Pi0 achieves 91.5\% CAR while 99.6\% of its safe episodes exhibit end-effector displacement below 0.1\,mm---the robot is frozen, not safe.
4	We present displacement-filtered CAR (dfCAR), which excludes sub-threshold episodes, as a corrective metric; the bimodal displacement distribution makes it robust across a $[2, 200]$\,mm threshold range.
5	Our analysis further reveals that end-effector-only Signed Distance Field (SDF) supervision is neither necessary nor structurally sufficient for collision avoidance.
6	It is counterproductive at inference time: three ground-truth oracle variants all reduce dfCAR below unrefined baselines, as SDF gradients repelling the end-effector drive arm links into obstacles.
7	It is redundant during training: LoRA-only fine-tuning raises dfCAR from 28.5\% to 54.5\%$\,\pm\,$2.83, matching SDF-augmented training at $\lambda{=}0.005$ (54.5\%$\,\pm\,$2.29) and $\lambda{=}0.01$ (56.33\%$\,\pm\,$1.61) \placeholder{$\lambda{=}0.1$ 30K three-seed results pending}.
8	Per-task avoidance patterns remain identical across all conditions, indicating that collision avoidance arises from collision-free demonstration data rather than geometric supervision.
9	Displacement filtering is necessary for meaningful VLA safety evaluation; EE-only geometric supervision can be neither credited with nor expected to deliver collision avoidance.
10	\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_writing_abstract_revision_20260527T071518",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-27T07:19:26.469502+00:00_

三处修改已完成：

1. **L2**: "systematically contaminated" → "contaminated" — 去掉过度声称
2. **28.5% 保留** — Registry `eval_pi05_baseline_reeval_disp` 确认 Pi0.5 baseline CAR=28.5%（fixed eval script, 200 episodes），是正确值
3. **dfCAR 术语统一** — L6、L7 的 "CAR" 改为 "dfCAR"。引入 dfCAR 后（L4）全部使用 dfCAR；L2-3 保留 "CAR" 因为那里讨论的是被污染的原始指标。所有报告数值的模型 frozen=0%，dfCAR=CAR，数值无变化，术语一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_writing_abstract_revision_20260527T071518"
}
```

</details>

---
