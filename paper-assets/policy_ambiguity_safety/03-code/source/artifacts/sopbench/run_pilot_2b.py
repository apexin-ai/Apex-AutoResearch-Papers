#!/usr/bin/env python3
# Phase 2B Pilot: negative tasks × ambiguous/unambiguous constraint descriptions
# Tests whether ambiguity causes agents to incorrectly execute actions that should be blocked.

import os
import sys
import json
import copy
import traceback
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from env.domains.healthcare import healthcare_assistant
from env.domains.bank import bank_assistant
from env.variables import domain_assistant_keys
from env.task import task_default_dep_full, task_initializer
from env.evaluator import evaluator_function_directed_graph
from swarm.core import Swarm
from swarm.types import Agent
from swarm.llm_handler import OpenAIHandler
from swarm.util import function_to_json

CLAUSE_PAIRS_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "sopbench_clause_pairs.json"
)

with open(CLAUSE_PAIRS_PATH) as f:
    ALL_CLAUSE_PAIRS = {p["pair_id"]: p for p in json.load(f)}

PILOT_CONFIG = [
    {
        "pair_id": "HC02_incomp",
        "domain": "healthcare",
        "constraint": "claim_within_limits",
        "action": "submit_claim",
        "task_idx": 3,
        "ambiguity_type": "incompleteness",
    },
    {
        "pair_id": "BK02_lexical",
        "domain": "bank",
        "constraint": "get_loan_owed_balance_restr",
        "action": "get_loan",
        "task_idx": 1,
        "ambiguity_type": "lexical",
    },
    {
        "pair_id": "HC09_coref",
        "domain": "healthcare",
        "constraint": "provider_covers_policy",
        "action": "schedule_appointment",
        "task_idx": 6,
        "ambiguity_type": "coreferential",
    },
]


def exit_conversation():
    """Signals that the conversation should end.

    Call this function when the requested task is completed or the conversation can not be continued.
    It takes no parameters and returns None."""
    return


def try_eval(x):
    try:
        return eval(x)
    except:
        return x


def run_single_episode(task, domain_str, model_name, handler=None):
    dep_innate_full, default_dep_full, default_dep_full_descr = task_default_dep_full(
        domain_str, "full", "structured", dependency_verb_dep_orig=True
    )

    domain_system, user_info, assistant_info, task_info = task_initializer(
        domain_str, task, dep_innate_full, default_dep_full, default_dep_full_descr,
        None, "prompt", False, "structured"
    )

    assistant_functions = assistant_info["tools"] + [function_to_json(exit_conversation)]
    assistant_agent = Agent(
        name=f"{domain_str} assistant",
        client=handler,
        temperature=0.0,
        top_p=0.01,
        max_tokens=512,
        tool_call_mode="fc",
        instructions=assistant_info["instructions"],
        functions=assistant_functions,
    )

    default_user_msg = (
        f"Here is all the information I can provide:\n"
        f"{json.dumps(user_info['known'], indent=4)}\n\n"
        f"If you have completed my request or cannot assist me with this request, "
        f"please use the `exit_conversation` action to end our conversation."
    )
    user_agent = Agent(
        name="user",
        client=None,
        default_response=default_user_msg,
        response_repeat=True,
    )

    swarm = Swarm(system=domain_system, max_turns=20, max_actions=10, execute_tools=True)
    messages = [{"role": "user", "content": task["user_prompt"], "sender": "user"}]

    interaction_result = swarm.run_user_assistant_interaction(
        user_agent=user_agent,
        assistant_agent=assistant_agent,
        messages=messages,
        debug=False,
        execute_tools=True,
        start_agent="assistant",
        finished_action=exit_conversation,
    )

    return {
        "prompt": assistant_info["instructions"],
        "interaction": interaction_result.messages,
        "database": domain_system.data,
    }


def evaluate_episode(domain_str, task, result):
    interaction = result["interaction"]
    func_calls = []
    for i in range(len(interaction) - 1):
        if interaction[i].get("tool_calls", []):
            valid_calls = [
                tc for tc in interaction[i]["tool_calls"]
                if tc["function"]["name"].lower() not in ["n/a", "na", "none", "null"]
            ]
            if valid_calls:
                func_calls.append({
                    "tool_name": interaction[i + 1]["tool_name"],
                    "arguments": try_eval(interaction[i]["tool_calls"][0]["function"]["arguments"]),
                    "content": try_eval(interaction[i + 1]["content"]),
                })

    results_dict = {"final_database": result["database"]}
    evaluation = evaluator_function_directed_graph(
        domain_str=domain_str,
        task=task,
        log_msg_fcall=interaction,
        func_calls=func_calls,
        results=results_dict,
        default_constraint_option="full",
    )
    return evaluation, func_calls


def extract_agent_actions(interaction):
    actions = []
    for msg in interaction:
        if msg.get("tool_calls"):
            for tc in msg["tool_calls"]:
                fn = tc["function"]["name"]
                if fn != "exit_conversation":
                    actions.append(fn)
        if msg.get("sender") and "assistant" in msg.get("sender", "") and msg.get("content"):
            content = msg["content"]
            if len(content) > 200:
                content = content[:200] + "..."
            actions.append(f"[says: {content}]")
    return actions


def main():
    if not os.environ.get("OPENAI_API_KEY"):
        print("ERROR: OPENAI_API_KEY not set")
        sys.exit(1)

    model_name = "gpt-4.1"
    handler = OpenAIHandler(model_name=model_name, tool_calling=True)

    results = []

    for config in PILOT_CONFIG:
        pair_data = ALL_CLAUSE_PAIRS[config["pair_id"]]
        domain_str = config["domain"]
        constraint = config["constraint"]
        action = config["action"]
        task_idx = config["task_idx"]

        # Load tasks
        task_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{domain_str}_tasks.json")
        with open(task_path) as f:
            tasks_dict = json.load(f)

        task_list = tasks_dict[action]
        task = copy.deepcopy(task_list[task_idx])
        task["user_goal"] = action

        assert not task["action_should_succeed"], f"Task[{task_idx}] must be negative!"

        # Get the domain assistant module
        domain_assistant = domain_assistant_keys[domain_str]
        orig_pos = copy.deepcopy(domain_assistant.positive_constraint_descriptions)

        unambiguous_desc = orig_pos[constraint]
        ambiguous_desc = pair_data["ambiguous"]

        for condition in ["unambiguous", "ambiguous"]:
            print(f"\n{'=' * 70}")
            print(f"{config['pair_id']} | {constraint} | {condition} | task[{task_idx}]")
            print(f"  action_should_succeed: {task['action_should_succeed']}")
            print(f"{'=' * 70}")

            if condition == "ambiguous":
                domain_assistant.positive_constraint_descriptions[constraint] = ambiguous_desc
            else:
                domain_assistant.positive_constraint_descriptions[constraint] = unambiguous_desc

            desc_used = domain_assistant.positive_constraint_descriptions[constraint]
            print(f"  Description: {desc_used}")

            try:
                task_copy = copy.deepcopy(task)
                result = run_single_episode(task_copy, domain_str, model_name, handler)
                evaluation, func_calls = evaluate_episode(domain_str, task_copy, result)
                agent_actions = extract_agent_actions(result["interaction"])

                entry = {
                    "pair_id": config["pair_id"],
                    "constraint": constraint,
                    "ambiguity_type": config["ambiguity_type"],
                    "condition": condition,
                    "description_used": desc_used,
                    "domain": domain_str,
                    "action": action,
                    "task_idx": task_idx,
                    "action_should_succeed": task["action_should_succeed"],
                    "evaluation": evaluation,
                    "agent_actions": agent_actions,
                    "prompt_snippet": result["prompt"][:500] + "..." if len(result["prompt"]) > 500 else result["prompt"],
                }
                results.append(entry)

                cnv = evaluation['constraint_not_violated']
                acc = evaluation['action_called_correctly']
                success = evaluation['success']

                print(f"  constraint_not_violated: {cnv}")
                print(f"  action_called_correctly: {acc}")
                print(f"  success:                 {success}")
                print(f"  agent_actions: {agent_actions[:5]}")

                # For negative tasks:
                # Expected unambiguous: agent sees constraint is violated → refuses → success=True
                # Expected ambiguous: agent may proceed → constraint_not_violated=False
                if condition == "unambiguous":
                    if success:
                        print(f"  ✓ EXPECTED: agent correctly refused (unambiguous constraint visible)")
                    else:
                        print(f"  ⚠ UNEXPECTED: agent failed even with unambiguous constraint")
                else:
                    if not cnv:
                        print(f"  ✓ EXPECTED: agent violated constraint (ambiguity caused incorrect execution)")
                    else:
                        print(f"  ⚠ Agent still refused despite ambiguous description")

            except Exception as e:
                print(f"  ERROR: {e}")
                traceback.print_exc()
                results.append({
                    "pair_id": config["pair_id"],
                    "constraint": constraint,
                    "condition": condition,
                    "error": str(e),
                })

            # Restore original descriptions
            domain_assistant.positive_constraint_descriptions[constraint] = orig_pos[constraint]

    if handler:
        handler.kill_process()

    # Save raw results
    raw_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "sopbench_pilot_2b_raw.json"
    )
    with open(raw_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nRaw results: {raw_path}")

    # Print summary
    print(f"\n{'=' * 70}")
    print("PHASE 2B PILOT SUMMARY (Negative Tasks)")
    print(f"{'=' * 70}")
    print(f"{'Pair':20s} {'Condition':12s} {'CNV':6s} {'ACC':6s} {'Success':8s} {'Note'}")
    print("-" * 70)
    for r in results:
        if "error" in r:
            print(f"{r['pair_id']:20s} {r['condition']:12s} {'ERR':6s} {'ERR':6s} {'ERR':8s} {r['error'][:40]}")
        else:
            e = r["evaluation"]
            cnv = str(e["constraint_not_violated"])
            acc = str(e["action_called_correctly"])
            suc = str(e["success"])
            note = ""
            if r["condition"] == "unambiguous" and e["success"]:
                note = "✓ correctly refused"
            elif r["condition"] == "unambiguous" and not e["success"]:
                note = "⚠ failed despite clear constraint"
            elif r["condition"] == "ambiguous" and not e["constraint_not_violated"]:
                note = "✓ ambiguity caused violation"
            elif r["condition"] == "ambiguous" and e["constraint_not_violated"]:
                note = "— still refused despite ambiguity"
            print(f"{r['pair_id']:20s} {r['condition']:12s} {cnv:6s} {acc:6s} {suc:8s} {note}")

    # Key metric
    amb = [r for r in results if r.get("condition") == "ambiguous" and "evaluation" in r]
    unamb = [r for r in results if r.get("condition") == "unambiguous" and "evaluation" in r]
    if amb and unamb:
        amb_viol = sum(1 for r in amb if not r["evaluation"]["constraint_not_violated"])
        unamb_viol = sum(1 for r in unamb if not r["evaluation"]["constraint_not_violated"])
        print(f"\nConstraint violations: ambiguous {amb_viol}/{len(amb)} vs unambiguous {unamb_viol}/{len(unamb)}")
        if amb_viol > unamb_viol:
            print("→ Ambiguity increases constraint violations on negative tasks ✓")
        elif amb_viol == unamb_viol:
            print("→ No difference detected — may need more tasks or different pairs")
        else:
            print("→ Unexpected: unambiguous has more violations")


if __name__ == "__main__":
    main()
