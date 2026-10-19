# ApexTune AIF360 trajectory: aif360-r2-gpt56sol-20260907

- Code version: `code-v1`
- Experiment round: `2`
- Search strategy: `unified-diff-no-local-hpo`
- Strategy meaning: Each successful LLM request produced one unified-diff structure and one full validation; campaign-local HPO was disabled.
- Model: `OpenAI/gpt-5.6-sol`
- Protocol: `diagnostic`; comparable=`false`; leaderboard eligible=`false`
- LLM structure requests: `211`
- Reserved requests without a durable terminal record: `0`
- Validated structures: `100`
- Generation-failed structures: `111`
- Full validation steps: `100`
- Default structure validations: `100`
- HPO variant validations: `0`
- Stall batch decisions / cooldown batches: `0` / `0`
- Restart draws: `{}`
- Pool parent draws / pooled steps: `0` / `0`
- Final normalized score: `0.2287421027577004`
- Final absolute AOD: `0.011120493106355073`
- Final accuracy: `0.6429215509467989`

`APEXTUNE_STRUCTURE_INDEX.jsonl` has one row for every logical LLM request, including failed generation requests. `APEXTUNE_VALIDATION_TRAJECTORY.jsonl` has one row for every full validation. Rows sharing an `apextune_structure_id` belong to the same LLM-proposed code structure; `variant_kind=hpo_variant` marks local parameter variants of that structure. On `code-v4` rows, `admission_kind` labels the archive outcome (new_cell / displaced_elite / pooled / rejected) and `pooled=true` marks near-best variants retained by the epsilon-band elite pool. Requests reserved before a process interruption but lacking a durable terminal record are retained with `status=missing` and are not counted as successful or failed generations.
