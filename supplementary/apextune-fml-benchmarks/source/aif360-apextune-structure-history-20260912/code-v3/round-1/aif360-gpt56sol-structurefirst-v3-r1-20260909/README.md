# ApexTune AIF360 trajectory: aif360-gpt56sol-structurefirst-v3-r1-20260909

- Code version: `code-v3`
- Experiment round: `1`
- Search strategy: `structure-first-up-to-three-defaults`
- Strategy meaning: Each mutation batch explored up to three independent LLM-authored structure defaults before allowing at most one HPO follow-up; the run completed the full 100-step validation budget.
- Model: `OpenAI/gpt-5.6-sol`
- Protocol: `diagnostic`; comparable=`false`; leaderboard eligible=`false`
- LLM structure requests: `130`
- Reserved requests without a durable terminal record: `9`
- Validated structures: `98`
- Generation-failed structures: `23`
- Full validation steps: `100`
- Default structure validations: `98`
- HPO variant validations: `2`
- Stall batch decisions / cooldown batches: `0` / `0`
- Restart draws: `{}`
- Pool parent draws / pooled steps: `0` / `0`
- Final normalized score: `0.18698138041007062`
- Final absolute AOD: `0.05288121545398486`
- Final accuracy: `0.6348061316501352`

`APEXTUNE_STRUCTURE_INDEX.jsonl` has one row for every logical LLM request, including failed generation requests. `APEXTUNE_VALIDATION_TRAJECTORY.jsonl` has one row for every full validation. Rows sharing an `apextune_structure_id` belong to the same LLM-proposed code structure; `variant_kind=hpo_variant` marks local parameter variants of that structure. On `code-v4` rows, `admission_kind` labels the archive outcome (new_cell / displaced_elite / pooled / rejected) and `pooled=true` marks near-best variants retained by the epsilon-band elite pool. Requests reserved before a process interruption but lacking a durable terminal record are retained with `status=missing` and are not counted as successful or failed generations.
