import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from infoset.utils import graphene_utils
from infoset.db.db_orm import SESSION, AgentName as AgentNameModel
from datetime import datetime


class AgentNameAttribute:

    idx_agentname = graphene.ID(description="")
    name = graphene.String(description="")
    enabled = graphene.Float(description="")
    ts_modified = graphene.DateTime(description="")
    ts_created = graphene.DateTime(description="")


class AgentName(SQLAlchemyObjectType, AgentNameAttribute):
    class Meta:
        model = AgentNameModel
        interfaces = (relay.Node, )


class AgentNameInput(graphene.InputObjectType, AgentNameAttribute):
    """Arguments to create AgentName."""
    pass


class CreateAgentName(graphene.Mutation):
    """Mutation to create a AgentName."""
    _agentname = graphene.Field(
        lambda: AgentName, description="AgentName created by this mutation.")

    class Arguments:
        input = AgentNameInput(required=True)

    def mutate(self, info, input):
        data = graphene_utils.input_to_dictionary(input)
        data['ts_created'] = datetime.utcnow()
        data['ts_modified'] = datetime.utcnow()

        _agentname = AgentNameModel(**data)
        SESSION.add(_agentname)
        SESSION.commit()

        return CreateAgentName(_agentname=_agentname)


class UpdateAgentNameInput(graphene.InputObjectType, AgentNameAttribute):

    _agentname = graphene.ID(
        required=True, description="Unique identifier of the AgentName")


class UpdateAgentName(graphene.Mutation):
    _agentname = graphene.Field(
        lambda: AgentName, description="AgentName updated by this mutation.")

    class Arguments:
        input = UpdateAgentNameInput(required=True)

    def mutate(self, info, input):
        data = graphene_utils.input_to_dictionary(input)
        data['ts_modified'] = datetime.utcnow()
        _agentname = SESSION.query(AgentNameModel).filter_by(id=data['id'])
        _agentname.update(data)
        SESSION.commit()
        _agentname = SESSION.query(
            AgentNameModel).filter_by(id=data['id']).first()

        return UpdateAgentName(_agentname=_agentname)
