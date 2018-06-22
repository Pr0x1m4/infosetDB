import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from infoset.utils import graphene_utils
from infoset.db.db_orm import db_session, DeviceAgent as DeviceAgentModel
from datetime import datetime


class DeviceAgentAttribute:

    idx_deviceagent = graphene.ID(description="")
    idx_device = graphene.Float(description="")
    idx_agent = graphene.Float(description="")
    last_timestamp = graphene.Float(description="")
    enabled = graphene.Float(description="")
    ts_modified = graphene.DateTime(description="")
    ts_created = graphene.DateTime(description="")


class DeviceAgent(SQLAlchemyObjectType, DeviceAgentAttribute):
    class Meta:
        model = DeviceAgentModel
        interfaces = (relay.Node, )


class DeviceAgentInput(graphene.InputObjectType, DeviceAgentAttribute):
    """Arguments to create DeviceAgent."""
    pass


class CreateDeviceAgent(graphene.Mutation):
    """Mutation to create a DeviceAgent."""
    _deviceagent = graphene.Field(
        lambda: DeviceAgent, description="DeviceAgent created by this mutation.")

    class Arguments:
        input = DeviceAgentInput(required=True)

    def mutate(self, info, input):
        data = graphene_utils.input_to_dictionary(input)
        data['ts_created'] = datetime.utcnow()
        data['ts_modified'] = datetime.utcnow()

        _deviceagent = DeviceAgentModel(**data)
        db_session.add(_deviceagent)
        db_session.commit()

        return CreateDeviceAgent(_deviceagent=_deviceagent)


class UpdateDeviceAgentInput(graphene.InputObjectType, DeviceAgentAttribute):

    _deviceagent = graphene.ID(
        required=True, description="Unique identifier of the DeviceAgent")


class UpdateDeviceAgent(graphene.Mutation):
    _deviceagent = graphene.Field(
        lambda: DeviceAgent, description="DeviceAgent updated by this mutation.")

    class Arguments:
        input = UpdateDeviceAgentInput(required=True)

    def mutate(self, info, input):
        data = graphene_utils.input_to_dictionary(input)
        data['ts_modified'] = datetime.utcnow()
        _deviceagent = db_session.query(
            DeviceAgentModel).filter_by(id=data['id'])
        _deviceagent.update(data)
        db_session.commit()
        _deviceagent = db_session.query(
            DeviceAgentModel).filter_by(id=data['id']).first()

        return UpdateDeviceAgent(_deviceagent=_deviceagent)
