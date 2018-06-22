import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from infoset.utils import graphene_utils
from infoset.db.db_orm import db_session, Data as DataModel
from datetime import datetime


class DataAttribute:
    idx_datapoint = graphene.ID(description="")
    timestamp = graphene.Float(description="")
    value = graphene.Int(description="")


class Data(SQLAlchemyObjectType, DataAttribute):
    class Meta:
        model = DataModel
        interfaces = (relay.Node, )


class DataInput(graphene.InputObjectType, DataAttribute):
    """Arguments to create data."""
    pass


class CreateData(graphene.Mutation):
    """Mutation to create a data."""
    _data = graphene.Field(
        lambda: Data, description="Data created by this mutation.")

    class Arguments:
        input = DataInput(required=True)

    def mutate(self, info, input):
        data = graphene_utils.input_to_dictionary(input)
        _data = DataModel(**data)
        db_session.add(_data)
        db_session.commit()

        return CreateData(_data=_data)


class UpdateDataInput(graphene.InputObjectType, DataAttribute):

    id = graphene.ID(
        required=True, description="Unique identifier of the Data")


class UpdateData(graphene.Mutation):
    _data = graphene.Field(
        lambda: Data, description="Data updated by this mutation.")

    class Arguments:
        input = UpdateDataInput(required=True)

    def mutate(self, info, input):
        data = graphene_utils.input_to_dictionary(input)
        _data = db_session.query(DataModel).filter_by(id=data['id'])
        _data.update(data)
        db_session.commit()
        _data = db_session.query(DataModel).filter_by(id=data['id']).first()

        return UpdateData(_data=_data)
