import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from infoset.db.db_orm import db_session, Datapoint as DatapointModel
from infoset.utils import graphene_utils
from datetime import datetime


class DatapointAttribute:
    idx_datapoint = graphene.ID(description="")
    idx_deviceagent = graphene.Float(description="")
    idx_department = graphene.Float(description="")
    idx_billcode = graphene.Float(description="")
    id_datapoint = graphene.Float(description="")
    agent_label = graphene.Float(description="")
    agent_source = graphene.Float(description="")
    enabled = graphene.Float(description="")
    billable = graphene.Float(description="")
    timefixed_value = graphene.Float(description="")
    base_type = graphene.Float(description="")
    last_timestamp = graphene.Float(description="")
    ts_modified = graphene.DateTime(description="")
    ts_created = graphene.DateTime(description="")


class Datapoint(SQLAlchemyObjectType, DatapointAttribute):
    class Meta:
        model = DatapointModel
        interfaces = (relay.Node, )


class DatapointInput(graphene.InputObjectType, DatapointAttribute):
    """Arguments to create datapoint."""
    pass


class CreateDatapoint(graphene.Mutation):
    """Mutation to create a datapoint."""
    _datapoint = graphene.Field(
        lambda: Datapoint, description="Datapoint created by this mutation.")

    class Arguments:
        input = DatapointInput(required=True)

    def mutate(self, info, input):
        data = graphene_utils.input_to_dictionary(input)
        data['ts_created'] = datetime.utcnow()
        _datapoint = DatapointModel(**data)
        db_session.add(_datapoint)
        db_session.commit()

        return CreateDatapoint(_datapoint=_datapoint)


class UpdateDatapointInput(graphene.InputObjectType, DatapointAttribute):

    id = graphene.ID(
        required=True, description="Unique identifier of the Datapoint")


class UpdateDatapoint(graphene.Mutation):
    _datapoint = graphene.Field(
        lambda: Datapoint, description="Datapoint updated by this mutation.")

    class Arguments:
        input = UpdateDatapointInput(required=True)

    def mutate(self, info, input):
        data = graphene_utils.input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        _datapoint = db_session.query(DatapointModel).filter_by(id=data['id'])
        _datapoint.update(data)
        db_session.commit()
        _datapoint = db_session.query(
            DatapointModel).filter_by(id=data['id']).first()

        return UpdateDatapoint(_datapoint=_datapoint)
