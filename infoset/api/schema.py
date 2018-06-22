from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
from infoset.api.schema_datapoint import CreateDatapoint, UpdateDatapoint, Datapoint
from infoset.api.schema_device import CreateDevice, UpdateDevice, Device
from infoset.api.schema_deviceagent import CreateDeviceAgent, UpdateDeviceAgent, DeviceAgent
from infoset.api.schema_data import CreateData, UpdateData, Data
from infoset.api.schema_agentname import CreateAgentName, UpdateAgentName, AgentName
from infoset.api.schema_agent import CreateAgent, UpdateAgent, Agent


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    datapoint = graphene.relay.Node.Field(Datapoint)
    device =  graphene.relay.Node.Field(Device)
    deviceagent = graphene.relay.Node.Field(DeviceAgent)
    data = graphene.relay.Node.Field(Data)
    agent = graphene.relay.Node.Field(Agent)
    agentname = graphene.relay.Node.Field(AgentName)
    all_datapoints = SQLAlchemyConnectionField(Datapoint)
    all_devices = SQLAlchemyConnectionField(Device)
    all_deviceagents = SQLAlchemyConnectionField(DeviceAgent)
    all_data = SQLAlchemyConnectionField(Data)
    all_agentnames = SQLAlchemyConnectionField(AgentName)
    all_agents = SQLAlchemyConnectionField(Agent)

class Mutation(graphene.ObjectType):
    createDatapoint = CreateDatapoint.Field()
    updateDatapoint = UpdateDatapoint.Field()
    createData = CreateData.Field()
    updateData = UpdateData.Field()
    createDevice = CreateDevice.Field()
    updateDevice = UpdateDevice.Field()
    createDeviceAgent = CreateDeviceAgent.Field()
    updateDeviceAgent = UpdateDeviceAgent.Field()
    createAgentName = CreateAgentName.Field()
    updateAgentName = UpdateAgentName.Field()
    createAgent = CreateAgent.Field()
    updateAgent = UpdateAgent.Field()

schema = graphene.Schema(query=Query, mutation = Mutation)


