import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from infoset.utils import graphene_utils
from infoset.db.db_orm import SESSION, Agent as AgentModel
from datetime import datetime


class AgentAttribute:

    idx_agent = graphene.ID(description="")
    idx_agentname = graphene.Float(description="")
    id_agent = graphene.String(description="")
    enabled = graphene.Float(description="")
    ts_modified = graphene.DateTime(description="")
    ts_created = graphene.DateTime(description="")


class Agent(SQLAlchemyObjectType, AgentAttribute):
    class Meta:
        model = AgentModel
        interfaces = (relay.Node, )


class AgentInput(graphene.InputObjectType, AgentAttribute):
    """Arguments to create Agent."""
    pass


class CreateAgent(graphene.Mutation):
    """Mutation to create a Agent."""
    _agent = graphene.Field(
        lambda: Agent, description="Agent created by this mutation.")

    class Arguments:
        input = AgentInput(required=True)

    def mutate(self, info, input):
        data = graphene_utils.input_to_dictionary(input)
        data['ts_created'] = datetime.utcnow()
        data['ts_modified'] = datetime.utcnow()

        _agent = AgentModel(**data)
        SESSION.add(_agent)
        SESSION.commit()

        return CreateAgent(_agent=_agent)


class UpdateAgentInput(graphene.InputObjectType, AgentAttribute):

    _agent = graphene.ID(
        required=True, description="Unique identifier of the Agent")


class UpdateAgent(graphene.Mutation):
    _agent = graphene.Field(
        lambda: Agent, description="Agent updated by this mutation.")

    class Arguments:
        input = UpdateAgentInput(required=True)

    def mutate(self, info, input):
        data = graphene_utils.input_to_dictionary(input)
        data['ts_modified'] = datetime.utcnow()
        _agent = SESSION.query(AgentModel).filter_by(id=data['id'])
        _agent.update(data)
        SESSION.commit()
        _agent = SESSION.query(AgentModel).filter_by(id=data['id']).first()

        return UpdateAgent(_agent=_agent)
