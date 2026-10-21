from openai.types.chat import ChatCompletionMessage
from openai.types.chat.chat_completion_message_tool_call import (
    ChatCompletionMessageToolCall,
    Function,
)
from typing import List, Callable, Union, Optional, Literal
from swarm.llm_handler import OpenAIHandler
# Third-party imports
from pydantic import BaseModel

AgentFunction = Callable[[], Union[str, "Agent", dict]]


class Agent(BaseModel):
    model_config = {"arbitrary_types_allowed": True}
    
    name: str = "Agent"
    client: Union[OpenAIHandler, None] = None
    instructions: str = "You are a helpful agent."
    system: Optional[BaseModel] = None
    functions: List[Union[Callable, dict]] = []
    parallel_tool_calls: bool = False
    tool_call_mode: Literal["fc", "react", "act-only", "react-v"] = "fc"
    temperature: float = 1.0
    top_p: float = 1.0
    max_tokens: int = 512
    default_response: Optional[str] = None
    response_repeat: bool = True


class Response(BaseModel):
    messages: List = []
    agent: Optional[Agent] = None
    context_variables: dict = {}


class Result(BaseModel):
    """
    Encapsulates the possible return values for an agent function.

    Attributes:
        value (str): The result value as a string.
        agent (Agent): The agent instance, if applicable.
        context_variables (dict): A dictionary of context variables.
    """

    value: str = ""
    agent: Optional[Agent] = None
    context_variables: dict = {}