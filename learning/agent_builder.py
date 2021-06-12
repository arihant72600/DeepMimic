import json
import numpy as np
from learning.ppo_agent import PPOAgent
from learning.amp_agent import AMPAgent

AGENT_TYPE_KEY = "AgentType"

def build_agent(world, id, file):
    agent = None
    agent_name = 'none'
    with open(file) as data_file:    
        json_data = json.load(data_file)
        
        assert AGENT_TYPE_KEY in json_data
        agent_type = json_data[AGENT_TYPE_KEY]
        
        if (agent_type == PPOAgent.NAME):
            agent = PPOAgent(world, id, json_data)
            agent_name = 'PPO'
        elif (agent_type == AMPAgent.NAME):
            agent = AMPAgent(world, id, json_data)
            agent_name = 'AMP'
        else:
            assert False, 'Unsupported agent type: ' + agent_type
        
        print('////////////////////////\n////////////////////////\n')
        print(agent_name)
        print('\n////////////////////////\n////////////////////////\n')

    return agent