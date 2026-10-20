"""
Testing modular functionalities along the task generation, task simulation, and task evaluation.
"""

from env.variables import domain_keys, domain_assistant_keys
from env.helpers import get_action_parameters, dfsprune_dep_pro, gather_action_default_dependencies,\
    dfsins_constr_links, dfsins_cl_cd_aid, dfsgather_invfunccalldirgraph,\
    bfsconvert_ifg_to_tree, bfsconvert_tree_to_ifg,\
    dfsgather_ifg_func
from env.generation import get_dep_perms,\
    dfsgather_dep_tree_vis, gather_ifg_graph_vis,\
    get_dep_task_str, get_inv_func_graph_str


"""testing methods for task generation"""

# dynamic additional variable assignment during constraint links
def test_constraint_link_dynamic_parameter_name():
    # using the bank domain's definitions for constraint links and etc
    domain_str = "bank"
    default_dependency_option = "full"
    dep = ("and",
        [
            ("single", "logged_in_user", {"username":"user1"}),
            ("single", "logged_in_user", {"username":"user2"}),
            ("single", "logged_in_user", {"username":"user3"}),
            ("single", "not logged_in_user", {"username":"user3"}),
            ("single", "not authenticated_admin_password", {"username":"user2"}),
        ]
    )
    # gathering information
    da = domain_assistant_keys[domain_str] # domain assistant
    aid = da.action_innate_dependencies
    ard = da.action_required_dependencies
    acd = da.action_customizable_dependencies
    cl = da.constraint_links
    cd = da.constraint_dependencies
    default_deps = gather_action_default_dependencies(ard, acd, cd, default_dependency_option) # adding constraint deps
    dss = domain_keys[domain_str+"_strict"]()
    ds = dss.evaluation_get_domain_system() # domain system
    action_parameters = get_action_parameters(ds, da)
    # operations
    dep_cl = dfsins_constr_links(dep, cl, default_deps, action_parameters)
    dep_cl_cd_aid = dfsins_cl_cd_aid(dep, cl, cd, aid, default_deps, action_parameters) # adding both constraint links and deps
    # printing out result for verification
    print("original dependency")
    print(dfsgather_dep_tree_vis(dep))
    print("dependency with constraint links")
    print(dfsgather_dep_tree_vis(dep_cl))
    print("dependency with constraint links, constraint dependencies, and action innate dependencies")
    print(dfsgather_dep_tree_vis(dep_cl_cd_aid))
    
# permutations of difficult dependencies
def test_task_permutations():
    # dependencies to test
    dep1 = ("and", [
        ("or", [
            ("and", [
                ("single", "a", None),
                ("single", "b", None)
            ]),
            ("and", [
                ("single", "not b", None),
                ("single", "not a", None)
            ])
        ]),
        ("single", "c", None)
    ]) # xor
    dep2 = (
        "chain",
        [
            ("single", "a", None),
            ("single", "b", None),
            ("single", "c", None),
        ]
    ) # chain negation is gate
    dep3 = ("and", [
        ("and", [
            ("or", [
                ("and", [
                    ("single", "test_type_is_drive", {"test_type": "test_type"}),
                    ("single", "knowledge_test_passed", {"username": "username"})
                ]),
                ("and", [
                    ("single", "not test_type_is_drive", {"test_type": "test_type"}),
                    ("single", "not knowledge_test_passed", {"username": "username"})
                ]),
            ]),
            ("single", "above_minimum_age", {"username": "username"})
        ]),
        ("single", "can_schedule", {"username": "username", "test_type": "test_type"}),
        ("single", "within_attempt_limit", {"username": "username", "test_type": "test_type"})
    ]) # complex dependency from dmv
    dep4 = ("chain", [
        ("chain", [
            ("single", "logged_in_user", {"username": "username"}),
            ("single", "internal_check_test_slot_available", {"test_type": "test_type", "schedule_time":"schedule_time"})
        ]),
        ("and", [
            ("and", [
                ("or", [
                    ("and", [
                        ("single", "test_type_is_drive", {"test_type": "test_type"}),
                        ("single", "knowledge_test_passed", {"username": "username"})
                    ]),
                    ("and", [
                        ("single", "not test_type_is_drive", {"test_type": "test_type"}),
                        ("single", "not knowledge_test_passed", {"username": "username"})
                    ]),
                ]),
                ("single", "above_minimum_age", {"username": "username"})
            ]),
            ("single", "can_schedule", {"username": "username", "test_type": "test_type"}),
            ("single", "within_attempt_limit", {"username": "username", "test_type": "test_type"})
        ])
    ]) # complex dependency from dmv
    deps = [dep1, dep2, dep3, dep4]
    # printing out for visual inspection
    for dep in deps:
        print("dependency to generate tasks for")
        print(dfsgather_dep_tree_vis(dep))
        tasks = get_dep_perms(dep, k=-1)
        print("resulting tasks")
        print(get_dep_task_str(tasks))
        
# inverse function call graph construction
def test_ifcg_construction():
    # information gathering
    domain_str = "bank"
    da = domain_assistant_keys[domain_str]
    ard = da.action_required_dependencies
    acd = da.action_customizable_dependencies
    cl = da.constraint_links
    cp = da.constraint_processes
    dss = domain_keys[domain_str+"_strict"]()
    ds = dss.evaluation_get_domain_system()
    action_parameters = get_action_parameters(ds, da)
    action_user_goal = ("single", "transfer_funds", {key: key for key in action_parameters["transfer_funds"]})
    # dependency of the action
    dep = (
        "and",
        [
            ("and",[
                ("single", "internal_check_username_exist", {"username": "username"}),
                ("single", "internal_check_username_exist", {"username": "destination_username"})
            ]),
            ("and",[
                ("single", "logged_in_user", {"username": "username"}),
                ("single", "authenticated_admin_password", {"username": "username"}),
                ("single", "sufficient_account_balance", {'username': 'username', 'amount': 'amount'})
            ])
        ]
    )
    # operations
    dd = gather_action_default_dependencies(ard, acd, None, "full") # default action dependencies without the constraint dependencies, actions handled by cp
    ifg = dfsgather_invfunccalldirgraph(dep, cl, cp, dd, action_parameters, action_user_goal)
    # printing result for visual inspection
    print(get_inv_func_graph_str(ifg))

# correct tree pruning, pruned tree should be functionally the same, with the same tasks
def test_prune_tree():
    # dependencies to test if the parts that should be pruned are pruned
    dep1 = ("and", [
        ("chain", [
            ("single", "internal_check_username_exist", {'username': 'username'}),
            ("single", "login_user", {'username': 'username', 'identification': 'identification'})
        ]),
        ("chain", [
            ("chain", [
                ("single", "internal_check_username_exist", {'username': 'username'}),
                ("single", "login_user", {'username': 'username', 'identification': 'identification'})
            ]),
            ("single", "authenticate_admin_password", {'username': 'username', 'admin_password': '[REDACTED]'})
        ])
    ])
    dep2 = ("and", [
        ("chain", [
            ("single", "a", None),
            ("single", "b", None),
        ]),
        ("and", [
            ("gate", [
                ("single", "a", None),
                ("single", "b", None),
            ]),
            ("and", [
                ("single", "c", None),
                ("single", "d", None),
            ])
        ]),
        ("or", [
            ("and", [
                ("single", "a", None),
                ("single", "b", None),
            ]),
            ("and", [
                ("single", "not b", None),
                ("single", "not a", None),
            ])
        ]),
        ("single", "c", None),
    ])
    dep3 = ("and", [
        ("chain",[
            ("single", "a", None),
            ("single", "b", None),
        ]),
        ("or",[
            ("and",[
                ("single", "a", None),
                ("single", "b", None),
            ]),
            ("and",[
                ("single", "not b", None),
                ("single", "not a", None),
            ])
        ]),
    ])
    dep4 = ("and", [
        ("single", "a", None),
        ("single", "b", None),
        ("or", [
            ("single", "a", None),
            ("single", "c", None)
        ])
    ])
    dep5 = ("or", [
        ("single", "a", None),
        ("single", "b", None),
        ("and", [
            ("single", "a", None),
            ("single", "c", None)
        ])
    ])
    dep6 = ("and", [
        ("single", "a", None),
        ("single", "b", None),
        ("chain", [
            ("single", "a", None),
            ("single", "b", None)
        ])
    ])
    dep7 = ("and", [
        ("and", [
            ("single", "a", None),
            ("single", "b", None)
        ]),
        ("or", [
            ("single", "a", None),
            ("single", "b", None)
        ])
    ])
    dep8 = ("and", [
        ("single", "a", None),
        ("or", [
            ("single", "a", None),
            ("single", "b", None)
        ])
    ])
    deps = [dep1, dep2, dep3, dep4, dep5, dep6, dep7, dep8]
    # printing out results, smaller tree, same tasks
    k = -1 # though -1 is the same, noticable different with k=1
    for dep in deps:
        print("original dependency")
        print(dfsgather_dep_tree_vis(dep))
        tasks = get_dep_perms(dep, k)
        print(get_dep_task_str(tasks))
        print("pruned dependency")
        dep_pruned = dfsprune_dep_pro(dep)
        print(dfsgather_dep_tree_vis(dep_pruned))
        tasks_pruned = get_dep_perms(dep_pruned, k)
        print(get_dep_task_str(tasks_pruned))
        
# representing the inverse function call graph as a tree
def test_ifg_visualization():
    domain_str = "bank"
    ds = domain_keys[domain_str]()
    da = domain_assistant_keys[domain_str]
    action = "transfer_funds"
    default_dependency_option = "full"
    # testing gathering the inverse function graph and the graph visualization
    inv_func_graph = dfsgather_ifg_func(ds, da, action, default_dependency_option, False)
    print(get_inv_func_graph_str(inv_func_graph))
    inv_func_graph1 = {
        "nodes": [
            ("x", None),
            "and",
            "or",
            ("a", None),
            "or",
            ("b", None),
            ("c", None),
            ("d", None)
        ],
        "connections": [
            (0, 1),
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 5),
            (2, 6),
            (3, 5),
            (4, 6),
            (4, 7),
            (1, 5),
        ]
    }
    inv_func_graph2 = {
        "nodes": [
            ("x", None),
            "and",
            "or",
            "or",
            ("a", None),
            ("b", None),
            ("c", None),
            "and",
            ("d", None),
        ],
        "connections": [
            (0, 1),
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 4),
            (2, 5),
            (3, 5),
            (3, 6),
            (1, 7),
            (7, 8)
        ]
    }
    print(gather_ifg_graph_vis(inv_func_graph1, False))
    print(gather_ifg_graph_vis(inv_func_graph2, True))
    # testing to see if converting back and forth from graph to tree will affect the fundamental graph (it shouldn't)
    print(gather_ifg_graph_vis(inv_func_graph, True))
    print(dfsgather_dep_tree_vis(bfsconvert_ifg_to_tree(inv_func_graph)))
    print(gather_ifg_graph_vis(bfsconvert_tree_to_ifg(bfsconvert_ifg_to_tree(inv_func_graph), inv_func_graph["nodes"][0]), True))
    # testing converting a dependency into a inverse function graph
    ard = da.action_required_dependencies
    acd = da.action_customizable_dependencies
    cd = da.constraint_dependencies
    cl = da.constraint_links
    dd = gather_action_default_dependencies(ard, acd, cd, default_dependency_option)
    action_parameters = get_action_parameters(ds, da)
    dependency = dfsins_constr_links(dd["transfer_funds"], cl, dd, action_parameters)
    print(dfsgather_dep_tree_vis(dependency))
    print(gather_ifg_graph_vis(bfsconvert_tree_to_ifg(dependency, ("transfer_funds", {ele:ele for ele in action_parameters["transfer_funds"]}))))
    print(get_inv_func_graph_str(bfsconvert_tree_to_ifg(dependency)))
    print(gather_ifg_graph_vis(bfsconvert_tree_to_ifg(dependency)))
    inv_func_graph3 = {
        "nodes": [("x", None)],
        "connections": []
    }
    print(gather_ifg_graph_vis(inv_func_graph3))


"""main testing method"""

def testing():
    # task generation tests
    test_constraint_link_dynamic_parameter_name()
    test_task_permutations()
    test_ifcg_construction()
    test_prune_tree()
    test_ifg_visualization()