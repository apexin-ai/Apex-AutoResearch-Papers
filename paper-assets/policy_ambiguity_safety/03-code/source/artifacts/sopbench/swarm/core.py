# Standard library imports
import copy
import json
from collections import defaultdict
from typing import List, Callable, Union, Any, Optional
from colorama import Fore, Style
# Package/library imports
from openai import OpenAI

# Local imports
from .util import function_to_json, debug_print, model_dump_json, construct_chatcompletion
from .types import (
    Agent,
    AgentFunction,
    ChatCompletionMessage,
    ChatCompletionMessageToolCall,
    Function,
    Response,
    Result,
)

__CTX_VARS_NAME__ = "context_variables"


class Swarm:
    def __init__(self, system: Any, max_turns=20, max_actions=10, execute_tools: bool = True):
        self.system = system
        self.max_turns = max_turns
        self.max_actions = max_actions
        self.execute_tools = execute_tools
        
    def get_chat_completion(
        self,
        agent: Agent,
        history: List,
        debug: bool=False,
    ) -> ChatCompletionMessage:

        # Add color printing for input()
        if agent.name == "human":
            huamn_input = input(f"{Fore.CYAN}[Human] {Style.RESET_ALL}")
            return construct_chatcompletion(role=agent.name, 
                                            content=huamn_input)
        
        # use default response if there is one provided and no client is provided
        if agent.default_response and agent.response_repeat:
            return construct_chatcompletion(role=agent.name, 
                                            content=agent.default_response)
        elif agent.default_response and not agent.response_repeat:
            # Use this default response only once at the begining of the history
            # Check if the default response is already in the history, if so, do not repeat it
            default_response_found = False
            for message in history:
                if message["content"] == agent.default_response:
                    default_response_found = True
                    break
            # Only repeat the default response if it is not already in the history
            if not default_response_found:
                return construct_chatcompletion(role=agent.name, 
                                                content=agent.default_response)
            
        tools = []
        for f in agent.functions:
            if callable(f):
                tools.append(function_to_json(f))
            elif isinstance(f, dict):
                tools.append(f)
            else:
                raise ValueError(f"Invalid function type: {type(f)}")

        messages = [{"role": "system", "content": agent.instructions}] + history
        debug_print(debug, "Getting chat completion for input:", messages)

        create_params = {
            "messages": messages,
            "temperature": agent.temperature,
            "top_p": agent.top_p,
            "max_tokens": agent.max_tokens,
        }
        if tools:
            create_params["tools"] = tools
            create_params["parallel_tool_calls"] = agent.parallel_tool_calls
        
        # use chat mode by default, only if using openai o-series models
        model_name = agent.client.model_name_huggingface
        mode = "chat"
        for _ in ["o1", "o3", "o4"]:
            if _ in model_name:
                mode = "reasoning"
                break
            
        return agent.client.inference(
            create_params, debug, mode=mode, tool_call_mode=agent.tool_call_mode)["completion"]

    def handle_function_result(self, result, debug) -> Result:
        match result:
            case Result() as result:
                return result

            case Agent() as agent:
                return Result(
                    value=json.dumps({"assistant": agent.name}),
                    agent=agent,
                )
            case _:
                try:
                    return Result(value=str(result))
                except Exception as e:
                    error_message = f"Failed to cast response to string: {result}. Make sure agent functions return a string or Result object. Error: {str(e)}"
                    debug_print(debug, error_message)
                    raise TypeError(error_message)

    def handle_tool_calls(
        self,
        tool_calls: List[ChatCompletionMessageToolCall],
        functions: List[AgentFunction],
        context_variables: dict,
        debug: bool,
    ) -> Response:
        
        # Build mapping of function names to their implementations
        # For callable functions, use the function name as key
        # For JSON schema functions, get the implementation from the system object
        function_map = {}
        for f in functions:
            if callable(f):
                function_map[f.__name__] = f
            elif isinstance(f, dict):
                # For JSON schema functions, get callable from system
                if hasattr(self.system, f["function"]["name"]):
                    function_map[f["function"]["name"]] = getattr(self.system, f["function"]["name"])
                
        partial_response = Response(
            messages=[], agent=None, context_variables={})

        for tool_call in tool_calls:
            name = tool_call.function.name
            # handle missing tool case, skip to next tool
            if name not in function_map:
                debug_print(debug, f"Tool {name} not found in function map.")
                partial_response.messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "tool_name": name,
                        "content": f"Error: Tool {name} not found.",
                    }
                )
                continue
            try:
                args = json.loads(tool_call.function.arguments)
            except Exception as e:
                print(f"Error parsing tool call arguments: {tool_call.function.arguments}")
                raise e
            debug_print(
                debug, f"Processing tool call: {name} with arguments {args}")

            # pass context_variables to agent functions
            # if __CTX_VARS_NAME__ in func.__code__.co_varnames:
            #     args[__CTX_VARS_NAME__] = context_variables
            
            # Actually run the function call
            func = function_map[name]
            try:
                raw_result = func(**args)
                # the first element indicates the success of the function call, and the second element is the result
                if isinstance(raw_result, tuple):
                    raw_result = raw_result[1]
            except Exception as e:
                # Contain the error type and error message
                raw_result = f"{e.__class__.__name__}: {str(e)}"

            result: Result = self.handle_function_result(raw_result, debug)
            partial_response.messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "tool_name": name,
                    "content": result.value,
                }
            )
            partial_response.context_variables.update(result.context_variables)
            if result.agent:
                partial_response.agent = result.agent

        return partial_response

    def update_active_agent(self, history: List, agents: List[Agent], active_agent_idx: int) -> None:
        # switch the active agent
        active_agent = agents[active_agent_idx]
        
        agent_history = []
        # switch the history roles, always identify myself as assistant
        if active_agent_idx == 0: # user agent, reverse the message roles
            for message in history:
                new_message = copy.deepcopy(message)
                if message["role"] == "tool":
                    continue
                elif message["sender"] == active_agent.name:
                    new_message = {
                        "role": "assistant",
                        "content": message["content"],
                        "sender": message["sender"]
                    }
                    agent_history.append(new_message)
                else: # assistant agent
                    if message["content"]:
                        new_message = {
                            "role": "user",
                            "content": message["content"],
                            "sender": message["sender"]
                        }
                        agent_history.append(new_message)
        
        else: # assistant agent
            for message in history:
                new_message = copy.deepcopy(message)
                if message["role"] == "tool":
                    pass
                elif message["sender"] == active_agent.name:
                    new_message["role"] = "assistant"
                else: # user agent
                    new_message["role"] = "user"
                agent_history.append(new_message)
                        
        return active_agent, agent_history
            
    def run_user_assistant_interaction(
        self,
        user_agent: Agent,
        assistant_agent: Agent,
        messages: List,
        start_agent: str,
        finished_action: Callable,
        debug: bool = False,
        max_turns: int = 20,
        max_actions: int = 10,
        context_variables: dict = {},
        execute_tools: bool = True,
    ) -> Response:
        
        max_turns = min(max_turns, self.max_turns)
        max_actions = min(max_actions, self.max_actions)
        # the whole history of the conversation
        history = copy.deepcopy(messages)
        actions = []
        
        # each agent has its own history (both playing assistant)
        agents = [user_agent, assistant_agent]
        
        # starts the conversation
        active_agent_idx = 0 if start_agent == "user" else 1 # user: 0, assistant: 1
        active_agent = agents[active_agent_idx]
        active_agent_history = copy.deepcopy(history)
        
        # update the active agent's history
        active_agent, active_agent_history = self.update_active_agent(history, agents, active_agent_idx)
        
        # run the conversation until max_turns or until the active agent is None
        while len(history) < max_turns and len(actions) < max_actions and active_agent:

            print("Active agent:", active_agent.name, f"({active_agent.client.model_name_huggingface if active_agent.client else 'None'})")            
            # get completion with current history
            completion = self.get_chat_completion(
                agent=active_agent,
                history=active_agent_history,
                debug=debug,
            )

            message = completion.choices[0].message
            debug_print(debug, "Received completion:", message)
            
            # Convert the message to a dictionary
            if hasattr(message, "to_dict"):
                message_dict = message.to_dict()
            elif hasattr(message, "model_dump_json"):
                message_dict = json.loads(message.model_dump_json())
            elif isinstance(message, dict):
                message_dict = message
            else:
                message_dict_raw = model_dump_json(message)
                message_dict = json.loads(message_dict_raw)
            
            # Add the sender to the message
            message_dict["sender"] = active_agent.name
            history.append(message_dict)

            # Check if there is valid tool call
            if message.tool_calls:
                for tool_call in message.tool_calls:
                    if tool_call.function.name.lower() in ["none", "n/a"]:
                        message.tool_calls = None
                        break
            
            if not message.tool_calls or not execute_tools:
                debug_print(debug, "Ending turn... Switching to", agents[abs(1 - active_agent_idx)].name)
                # switch to the other agent and update history
                # remember that both agents are assistant role during inference
                # switch the active agent index
                active_agent_idx = abs(1 - active_agent_idx)
                active_agent, active_agent_history = self.update_active_agent(history, agents, active_agent_idx)
                continue
            
            # if the finishsed action in within the message.tool_calls, exit the conversation
            def check_finished_action(tool_calls, finished_action):
                for tool_call in tool_calls:
                    if tool_call.function.name == finished_action.__name__:
                        return True
                return False
                
            if check_finished_action(message.tool_calls, finished_action):
                active_agent = None
                break
            
            # add the tool calls to the actions
            actions.extend(message.tool_calls)
            
            # handle function calls, updating context_variables, and switching agents
            partial_response = self.handle_tool_calls(
                message.tool_calls, active_agent.functions, context_variables, debug
            )
            debug_print(debug, "Tool call response:", partial_response)
            # add the tool call response to the history, and the active agent's history
            history.extend(partial_response.messages)
            # update the active agent's history but do not switch agents
            active_agent, active_agent_history = self.update_active_agent(history, agents, active_agent_idx)
            
            # update the environment, change active agent (usually when there are multiple assistant agents)
            if partial_response.agent:
                active_agent = partial_response.agent

        return Response(
            messages=history,
            agent=active_agent,
        )